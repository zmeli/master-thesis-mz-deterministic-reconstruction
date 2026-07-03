import copy
import warnings
import itertools
from typing import List, Tuple, Dict
from core.tree_node import ProcessTreeNode

TraceList = List[Tuple[ProcessTreeNode, int, str]]
PartitionedState = Dict[str, TraceList]

class ProcessTreeAnalyzer:
    """
    Frequency-aware analyzer for binary process trees.

    Provides two capabilities over a :class:`ProcessTreeNode`:

    * Frequency reconciliation (:meth:`compute_frequencies`), which computes
      consistent node frequencies bottom-up and then redistributes an incoming
      token count top-down, injecting silent (tau) skip branches where a child
      cannot account for all of its parent's traffic.
    * Forced-trace enumeration (:meth:`analyze_forced_traces`), which unfolds the
      tree into the set of activity traces it can produce, abstracting opaque
      constructs (PAR/LOOP) into atomic summary blocks and capping the state
      space to avoid combinatorial explosion.

    Args:
        max_traces_per_node: Upper bound on the number of traces retained per
            node during enumeration. Guards against out-of-memory crashes caused
            by combinatorial blow-up.

    Attributes:
        max_traces: The configured per-node trace cap.
        nested_blocks_registry: Maps generated block identifiers (e.g.
            ``"nested PAR_1"``) to deep copies of the subtrees they abstract.
        added_tau_count: Number of silent (tau) branches injected during the
            most recent analysis.
    """
    def __init__(self, max_traces_per_node: int = 10000):
        self.max_traces = max_traces_per_node
        self._truncation_warned = False
        self.nested_blocks_registry: Dict[str, ProcessTreeNode] = {}
        self._block_counter: int = 0
        self.added_tau_count: int = 0 # Track injected taus

    def _is_tau_node(self, node: ProcessTreeNode) -> bool:
        """Return ``True`` if ``node`` is a silent (tau) leaf, else ``False``."""
        if node.operator == 'LEAF':
            name_str = str(node.name).lower()
            return name_str in {"τ", "tau", "empty_tau", "none"}
        return False

    def _has_tau_leaf(self, node: ProcessTreeNode) -> bool:
        """Return ``True`` if ``node`` or any of its descendants is a tau leaf."""
        if self._is_tau_node(node): return True
        return any(self._has_tau_leaf(c) for c in node.children)

    def compute_frequencies(self, node: ProcessTreeNode, global_n: int = None) -> int:
        """
        Reconcile node frequencies across the tree and return the root frequency.

        Runs a bottom-up pass to derive each node's frequency from its children,
        then a top-down pass that redistributes the root token count, mutating
        the tree in place (e.g. wrapping children in XOR/tau blocks where needed).

        Args:
            node: Root of the process tree to reconcile (modified in place).
            global_n: Explicit root frequency to enforce. If ``None``, the value
                derived by the bottom-up pass is used instead.

        Returns:
            The final frequency assigned to ``node``.
        """
        bottom_up_freq = self._compute_bottom_up(node)

        root_freq = global_n if global_n is not None else bottom_up_freq

        self._push_top_down(node, root_freq)
        return node.frequency

    def _compute_bottom_up(self, node: ProcessTreeNode) -> int:
        """
        Derive and store each node's frequency from its children, bottom-up.

        Applies operator-specific aggregation rules: XOR sums its branches, LOOP
        subtracts REDO from DO (warning and falling back to 0 on the anomalous
        REDO >= DO case), and SEQ/PAR take the maximum of their non-loop children.

        Returns:
            The frequency computed for ``node``.
        """
        if not node.children: return node.frequency
        
        child_freqs = [self._compute_bottom_up(c) for c in node.children]
        
        if node.operator == 'XOR':
            node.frequency = sum(child_freqs)
        elif node.operator == 'LOOP':
            do_freq, redo_freq = child_freqs[0], child_freqs[1]
            if redo_freq >= do_freq and not (do_freq == 0 and redo_freq == 0):
                warnings.warn("Logical anomaly in LOOP: REDO >= DO. Falling back to 0.")
                node.frequency = 0
            else:
                node.frequency = do_freq - redo_freq
        elif node.operator in ('SEQ', 'PAR'):
            non_loop_freqs = [c.frequency for c in node.children if c.operator != 'LOOP']
            if non_loop_freqs:
                node.frequency = max(non_loop_freqs)
            else:
                node.frequency = max(child_freqs)
            
        return node.frequency

    def _push_top_down(self, node: ProcessTreeNode, incoming_tokens: int):
        """
        Distribute ``incoming_tokens`` from ``node`` down to its children.

        Anchors ``node``'s frequency to the incoming count and recurses,
        routing tokens per operator semantics (SEQ/PAR forward the full count to
        each child; XOR splits proportionally; LOOP accounts for redo traffic).
        Where a child cannot absorb its share, it is wrapped in an XOR/tau block
        so the surplus is captured by an explicit silent skip.

        Args:
            node: Subtree root receiving the tokens (modified in place).
            incoming_tokens: Token count flowing into ``node``.
        """
        # Anchor frequency
        node.frequency = incoming_tokens
        if not node.children: return

        def safe_push(parent: ProcessTreeNode, child_idx: int, tokens: int):
            """Push ``tokens`` into one child, inserting a tau skip on shortfall."""
            child = parent.children[child_idx]
            tokens = max(0, round(tokens))
            if child.frequency < tokens:
                diff = tokens - child.frequency
                
                # 1. If the child is already a pure tau node, just let it absorb the tokens directly
                if self._is_tau_node(child):
                    child.frequency = tokens
                    return
                
                # 2. If the child is ALREADY an XOR block containing a tau fallback
                if child.operator == 'XOR':
                    tau_children = [c for c in child.children if self._is_tau_node(c)]
                    if tau_children:
                        # Inflate the existing XOR and its tau child! Do not wrap it again.
                        child.frequency = tokens
                        tau_children[0].frequency += diff
                        self._push_top_down(child, tokens)
                        return

                # 3. Otherwise (SEQ, PAR, LOOP, or strict LEAF), it needs a new wrapper
                tau_node = ProcessTreeNode("LEAF", "τ", frequency=diff)
                xor_node = ProcessTreeNode("XOR", frequency=tokens)
                
                # Note: This relies on your ProcessTreeNode supporting binary children
                xor_node.add_child(child)
                xor_node.add_child(tau_node)

                self.added_tau_count += 1 # Count the mutation
                
                parent.children[child_idx] = xor_node
                self._push_top_down(xor_node, tokens)
            else:
                self._push_top_down(child, tokens)
                
        if node.operator in ('SEQ', 'PAR'):
            for i in range(len(node.children)):
                safe_push(node, i, incoming_tokens)
                
        elif node.operator == 'XOR':
            real_children = [c for c in node.children if not self._is_tau_node(c)]
            tau_children = [c for c in node.children if self._is_tau_node(c)]
            
            sum_real = sum(c.frequency for c in real_children)

            if sum_real > incoming_tokens and real_children:

                for i, c in enumerate(node.children):
                    if not self._is_tau_node(c):
                        share = incoming_tokens * (c.frequency / sum_real)
                        safe_push(node, i, share)
                for i, t in enumerate(node.children):
                    if self._is_tau_node(t):
                        safe_push(node, i, 0)
                return

            remainder = max(0, incoming_tokens - sum_real)

            if tau_children:
                for i, c in enumerate(node.children):
                    if not self._is_tau_node(c):
                        safe_push(node, i, c.frequency)
                tau_split = remainder // len(tau_children)
                for i, t in enumerate(node.children):
                    if self._is_tau_node(t):
                        safe_push(node, i, tau_split)
            elif remainder > 0:
                tau_hiders = [c for c in real_children if self._has_tau_leaf(c)]
                if tau_hiders:
                    extra = remainder // len(tau_hiders)
                    for i, c in enumerate(node.children):
                        if c in tau_hiders: 
                            safe_push(node, i, c.frequency + extra)
                        else: 
                            safe_push(node, i, c.frequency)
                else:
                    extra = remainder // len(real_children)
                    for i, c in enumerate(node.children):
                        safe_push(node, i, c.frequency + extra)
            else:
                for i, c in enumerate(node.children):
                    safe_push(node, i, c.frequency)
                    
        elif node.operator == 'LOOP':
            do_child, redo_child = node.children[0], node.children[1]
            
            if self._has_tau_leaf(redo_child) and redo_child.frequency == 0:
                if do_child.frequency < incoming_tokens:

                    safe_push(node, 0, incoming_tokens)
                    safe_push(node, 1, 0)
                else:
                    actual_redos = do_child.frequency - incoming_tokens
                    safe_push(node, 0, do_child.frequency)
                    safe_push(node, 1, actual_redos)
            elif self._has_tau_leaf(do_child) and do_child.frequency == 0:
                actual_do = incoming_tokens + redo_child.frequency
                safe_push(node, 0, actual_do)
                safe_push(node, 1, redo_child.frequency)
            else:
                total_do_traffic = incoming_tokens + redo_child.frequency
                safe_push(node, 0, total_do_traffic)
                safe_push(node, 1, redo_child.frequency)

    def analyze_forced_traces(self, node: ProcessTreeNode, local_N: int) -> TraceList:
        """
        Unfold the tree into the set of traces it is forced to produce.

        Resets the analyzer's per-run state, runs the recursive enumeration, and
        caches the root's partitioned state on ``self`` (``last_root_state`` and
        ``last_root_full``) for downstream inspection.

        Args:
            node: Root of the process tree to enumerate.
            local_N: Token count (trace multiplicity) entering the root.

        Returns:
            The list of ``(subtree, frequency, tag)`` trace tuples for the tree.
        """
        self._truncation_warned = False
        self.nested_blocks_registry.clear()
        self._block_counter = 0
        self.added_tau_count = 0 
        self._block_id_cache: Dict[int, str] = {}
        final_state = self._analyze_recursive(node, local_N)
        self.last_root_full = final_state["full"]
        self.last_root_state = final_state
        return final_state["all"]

    def _check_truncation(self, current_length: int):
        """Emit a one-time warning when the trace cap is reached."""
        if current_length >= self.max_traces and not self._truncation_warned:
            warnings.warn(f"State space combinatorial explosion intercepted. Truncating permutations at {self.max_traces} max traces to prevent OOM crash.")
            self._truncation_warned = True

    def _analyze_recursive(self, node: ProcessTreeNode, local_N: int) -> PartitionedState:
        """
        Recursively enumerate the traces of ``node`` under ``local_N`` tokens.

        Returns a partitioned state with four buckets — ``"all"``, ``"full"``,
        ``"prefix"``, and ``"suffix"`` — each a list of ``(subtree, frequency,
        tag)`` tuples. The buckets track, respectively, every fragment, complete
        traces, traces that may start a run, and traces that may end one, so that
        SEQ can correctly stitch children together. Behaviour by operator:

        * LEAF: base case; tau leaves dissolve to the empty state.
        * XOR: splits tokens between the two branches, adding a tau placeholder
          for an empty branch and an ambiguous nested-block leaf for any
          unresolved remainder.
        * SEQ: cross-multiplies left and right traces, absorbing skipped branches.
        * PAR/LOOP: treated as opaque atomic blocks summarized by a registered
          nested-block leaf, with LOOP additionally splitting the strict
          zero-redo path from the encapsulated redo path.

        All buckets are capped at ``self.max_traces`` to bound the state space.
        """
        state = {"all": [], "full": [], "prefix": [], "suffix": []}
        if local_N <= 0: return state

        # RULE 1: LEAF - Base case. 
        if node.operator == 'LEAF':
            if self._is_tau_node(node): return state # Dissolve taus completely
            leaf_block = (copy.deepcopy(node), local_N, "ST")
            state["all"].append(leaf_block)
            state["full"].append(leaf_block)
            state["prefix"].append(leaf_block)
            state["suffix"].append(leaf_block)
            return state

        # RULE 2: XOR - Strict Bifurcation.
        if node.operator == 'XOR':

            own_freq = node.frequency
            if own_freq > 0:
                l_n = max(0.0, node.children[0].frequency + local_N - own_freq)
                r_n = max(0.0, node.children[1].frequency + local_N - own_freq)
            else:
                l_n = r_n = 0.0
            l_state = self._analyze_recursive(node.children[0], l_n)
            r_state = self._analyze_recursive(node.children[1], r_n)

            if not l_state["all"] and l_n > 0:
                placeholder = (ProcessTreeNode("LEAF", "τ", frequency=l_n), l_n, "ST")
                l_state = {"all": [placeholder], "full": [placeholder], "prefix": [placeholder], "suffix": [placeholder]}
                self.added_tau_count += 1
            if not r_state["all"] and r_n > 0:
                placeholder = (ProcessTreeNode("LEAF", "τ", frequency=r_n), r_n, "ST")
                r_state = {"all": [placeholder], "full": [placeholder], "prefix": [placeholder], "suffix": [placeholder]}
                self.added_tau_count += 1

            state["all"] = list(itertools.islice(l_state["all"] + r_state["all"], self.max_traces))
            state["full"] = list(itertools.islice(l_state["full"] + r_state["full"], self.max_traces))
            state["prefix"] = list(itertools.islice(l_state["prefix"] + r_state["prefix"], self.max_traces))
            state["suffix"] = list(itertools.islice(l_state["suffix"] + r_state["suffix"], self.max_traces))

            remainder = local_N - (l_n + r_n)
            if remainder > 1e-9:
                cached_name = self._block_id_cache.get(id(node))
                if cached_name is not None:
                    block_name = cached_name
                else:
                    self._block_counter += 1
                    block_name = f"XOR_{self._block_counter}"
                    self._block_id_cache[id(node)] = block_name
                block_id = f"nested {block_name}"
                self.nested_blocks_registry.setdefault(block_id, copy.deepcopy(node))
                ambiguous_leaf = ProcessTreeNode("LEAF", f"[{block_id}]", remainder)
                ambiguous_block = (ambiguous_leaf, remainder, "AS")
                state["all"].append(ambiguous_block)
                state["full"].append(ambiguous_block)
                state["prefix"].append(ambiguous_block)
                state["suffix"].append(ambiguous_block)

            self._check_truncation(len(state["all"]))
            return state

        # RULE 3: SEQ - Strict Linear Connection.
        elif node.operator == 'SEQ':

            own_freq = node.frequency
            if own_freq > 0:
                l_n = max(0.0, node.children[0].frequency + local_N - own_freq)
                r_n = max(0.0, node.children[1].frequency + local_N - own_freq)
            else:
                l_n = r_n = 0.0
            l_state = self._analyze_recursive(node.children[0], l_n)
            r_state = self._analyze_recursive(node.children[1], r_n)
            
            # Tau absorption: If a branch was a pure 'skip', instantly connect to the remaining branch.
            if not l_state["all"]: return r_state
            if not r_state["all"]: return l_state
            
            state["all"] = list(itertools.islice(l_state["all"] + r_state["all"], self.max_traces))
            
            def lazy_cross_multiply(left_list, right_list, target_bucket):
                """Lazily join overlapping left/right traces into SEQ pairs.

                Yields into ``target_bucket`` (and ``state["all"]``) only where the
                left and right token counts overlap, stopping once the cap is hit.
                """
                def generator():
                    for (l_node, l_f, l_t), (r_node, r_f, r_t) in itertools.product(left_list, right_list):
                        overlap = (l_f + r_f) - local_N
                        if overlap > 0:
                            new_seq = ProcessTreeNode("SEQ")
                            new_seq.add_child(copy.deepcopy(l_node))
                            new_seq.add_child(copy.deepcopy(r_node))
                            yield (new_seq, overlap, "ST")
                
                safe_traces = list(itertools.islice(generator(), self.max_traces - len(target_bucket)))
                target_bucket.extend(safe_traces)
                state["all"].extend(safe_traces)

            lazy_cross_multiply(l_state["full"], r_state["full"], state["full"])
            lazy_cross_multiply(l_state["full"], r_state["prefix"], state["prefix"])
            lazy_cross_multiply(l_state["suffix"], r_state["full"], state["suffix"])

            state["prefix"].extend(itertools.islice(l_state["prefix"], self.max_traces - len(state["prefix"])))
            state["suffix"].extend(itertools.islice(r_state["suffix"], self.max_traces - len(state["suffix"])))
            
            self._check_truncation(len(state["all"]))
            return state

        # RULE 4: PAR & LOOP - Opaque Atomic Blocks & Zero-Redo Extraction
        elif node.operator in ('PAR', 'LOOP'):
            
            # 1. Determine if this block will be abstracted and generate its ID early
            has_complex_child = any(c.operator != 'LEAF' for c in node.children)
            is_opaque = (node.operator in ('PAR', 'LOOP') or has_complex_child)
            
            if is_opaque:
                cached_name = self._block_id_cache.get(id(node))
                if cached_name is not None:
                    block_name = cached_name
                else:
                    self._block_counter += 1
                    # Creates a unified name like "PAR_1" or "LOOP_2"
                    block_name = f"{node.operator}_{self._block_counter}"
                    self._block_id_cache[id(node)] = block_name
                context_tag = f" (in {block_name})"
                block_id = f"nested {block_name}"
            else:
                # Fallback for simple flat structures that don't get a unique ID
                context_tag = f" (in {node.operator})"
                
            # 2. Harvest the internal traces using the synchronized context tag
            internal_traces = []
            for child in node.children:
                c_state = self._analyze_recursive(child, child.frequency)
                
                # Apply the specific tag (e.g., " (in PAR_1)") to the traces
                for t_node, t_freq, t_type in c_state["all"]:
                    # Prevent stacking tags if deeply nested
                    if "(in " not in t_type:
                        internal_traces.append((t_node, t_freq, t_type + context_tag))
                    else:
                        internal_traces.append((t_node, t_freq, t_type))
                
            # 3. Package the complex node itself
            if node.operator == 'LOOP':
                if is_opaque:
                    self.nested_blocks_registry[block_id] = copy.deepcopy(node)
                
                # --- THE ZERO-REDO MATH ---
                # Calculate the exact frequencies for the two mutually exclusive paths
                do_node = node.children[0]
                redo_freq = node.children[1].frequency if len(node.children) > 1 else 0
                
                zero_redo_freq = max(0, local_N - redo_freq)
                complex_freq = 1 if redo_freq > 0 else 0
                
                # Path A: The Zero-Redo Branch (Strict DO execution)
                if zero_redo_freq > 0:

                    do_state = self._analyze_recursive(do_node, zero_redo_freq)

                    for t_node, t_freq, t_type in do_state["full"]:
                        final_node = t_node

                        if final_node.operator != 'SEQ':
                            seq_wrapper = ProcessTreeNode("SEQ", frequency=t_freq)
                            seq_wrapper.add_child(final_node)
                            final_node = seq_wrapper

                        zero_redo_block = (final_node, t_freq, t_type)
                        state["full"].append(zero_redo_block)
                        state["prefix"].append(zero_redo_block)
                        state["suffix"].append(zero_redo_block)
                        state["all"].append(zero_redo_block)
                
                # Path B: The Complex Redo Branch (Encapsulated)
                if complex_freq > 0:
                    if is_opaque:
                        summary_leaf = ProcessTreeNode("LEAF", f"[{block_id}]", complex_freq)
                        redo_block = (summary_leaf, complex_freq, "AS")
                    else:
                        flat_node = ProcessTreeNode(node.operator, frequency=complex_freq)
                        for c in node.children:
                            flat_node.add_child(copy.deepcopy(c))
                        redo_block = (flat_node, complex_freq, "AS")
                        
                    state["full"].append(redo_block)
                    state["prefix"].append(redo_block)
                    state["suffix"].append(redo_block)
                    state["all"].append(redo_block)

            elif node.operator == 'PAR':
                if is_opaque:
                    summary_leaf = ProcessTreeNode("LEAF", f"[{block_id}]", local_N)
                    atomic_block = (summary_leaf, local_N, "AS")
                    self.nested_blocks_registry[block_id] = copy.deepcopy(node)
                else:
                    flat_node = ProcessTreeNode(node.operator, frequency=local_N)
                    for c in node.children:
                        flat_node.add_child(copy.deepcopy(c))
                    atomic_block = (flat_node, local_N, "AS")
                
                state["full"].append(atomic_block)
                state["prefix"].append(atomic_block)
                state["suffix"].append(atomic_block)
                state["all"].append(atomic_block)
            
            # 4. Compile the state
            state["all"] = list(itertools.islice(internal_traces + state["all"], self.max_traces))
            
            return state
        
    @staticmethod
    def get_tree_stats(node: ProcessTreeNode) -> dict:
        """
        Count the unique activities and structural operators in a tree.

        Walks the tree recursively, collecting distinct non-tau leaf names and
        tallying each operator type (XOR/LOOP/SEQ/PAR).

        Args:
            node: Root of the process tree to inspect.

        Returns:
            A dict with the set of ``'activities'``, an operator count per type
            (``'XOR'``, ``'LOOP'``, ``'SEQ'``, ``'PAR'``), and ``'num_activities'``
            giving the number of distinct activities.
        """
        stats = {'activities': set(), 'XOR': 0, 'LOOP': 0, 'SEQ': 0, 'PAR': 0}
        def walk(n):
            if n.operator == 'LEAF':
                name_str = str(n.name).lower()
                if name_str not in {"τ", "tau", "empty_tau", "none"}:
                    stats['activities'].add(str(n.name))
            elif n.operator in ['XOR', 'LOOP', 'SEQ', 'PAR']:
                stats[n.operator] += 1
            for c in n.children:
                walk(c)
        walk(node)
        stats['num_activities'] = len(stats['activities'])
        return stats