import copy
import warnings
import itertools
from typing import List, Tuple, Dict
from core.tree_node import ProcessTreeNode

TraceList = List[Tuple[ProcessTreeNode, int, str]]
PartitionedState = Dict[str, TraceList]

class ProcessTreeAnalyzer:
    def __init__(self, max_traces_per_node: int = 10000):
        self.max_traces = max_traces_per_node
        self._truncation_warned = False
        self.nested_blocks_registry: Dict[str, ProcessTreeNode] = {}
        self._block_counter: int = 0
        self.added_tau_count: int = 0 # <--- NEW: Track injected taus
    
    def _is_tau_node(self, node: ProcessTreeNode) -> bool:
        if node.operator == 'LEAF':
            name_str = str(node.name).lower()
            return name_str in {"τ", "tau", "empty_tau", "none"}
        return False

    def _has_tau_leaf(self, node: ProcessTreeNode) -> bool:
        if self._is_tau_node(node): return True
        return any(self._has_tau_leaf(c) for c in node.children)

    def compute_frequencies(self, node: ProcessTreeNode, global_n: int = None) -> int:
        bottom_up_freq = self._compute_bottom_up(node)

        # `global_n` represents the model's own declared root capacity (Section 3.2:
        # "this total trace volume N is... provided as standard metadata accompanying
        # the published model") — it is supplied once, not re-derived from the log on
        # every call. The bottom-up pass's only documented role (Section 4.5.1,
        # "Filtered Data and Frequency Preservation") is to let the later top-down
        # pass detect a *deficit* against that declared capacity and compensate with a
        # silent-node injection — it must never be allowed to override the declared
        # capacity just because it computes something larger. This matters for trees
        # whose root is itself a LOOP with a silent ("tau") redo branch: redo leaves no
        # trace in the log, so bottom-up token-throughput math cannot distinguish "N
        # cases" from "N cases entered multiple times via untracked repetition" — only
        # the model's declared root capacity can resolve that ambiguity correctly.
        root_freq = global_n if global_n is not None else bottom_up_freq

        self._push_top_down(node, root_freq)
        return node.frequency

    def _compute_bottom_up(self, node: ProcessTreeNode) -> int:
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
        # Anchor frequency
        node.frequency = incoming_tokens
        if not node.children: return

        # Structural mutation leap: Wrap deficient children to absorb excess tokens dynamically
        # Structural mutation leap: Wrap deficient children to absorb excess tokens dynamically
        def safe_push(parent: ProcessTreeNode, child_idx: int, tokens: int):
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

                self.added_tau_count += 1 # <--- NEW: Count the mutation
                
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
                # BUG FIX (surplus): a real child's own bottom-up frequency can exceed
                # the actual top-down budget (e.g. a LOOP whose redo boundary is silent,
                # so its do-activity's raw occurrence count overstates the true case
                # count). Scale every real child proportionally down to fit the budget
                # instead of trusting each child's native (possibly inflated) frequency --
                # mirrors the deficit-side wrapping safe_push already does below.
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
                    # BUG FIX (deficit): do_child's own bottom-up frequency undercounts
                    # the case budget (e.g. its content is rare/filtered in the log).
                    # Lift it via safe_push's tau-wrap instead of trusting its native
                    # value, so the missing cases get an honest placeholder rather than
                    # silently vanishing.
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
        self._truncation_warned = False
        self.nested_blocks_registry.clear()
        self._block_counter = 0
        self.added_tau_count = 0 # <--- NEW: Reset on new run
        # Caches the block name assigned to a given opaque PAR/LOOP node (by identity).
        # The zero-redo branch below re-traverses the same `do` child node that the
        # internal-traces loop already visits, so without this cache that single
        # logical block would be minted twice under two different IDs.
        self._block_id_cache: Dict[int, str] = {}
        final_state = self._analyze_recursive(node, local_N)
        # Exposed for exposure-metric calculations (e.g. auto_verifier_v2's Tree
        # Exposure metric): unlike "all", the "full" bucket never mixes in
        # Prefix/Suffix fragments of an already-counted Full chain, so summing its
        # frequencies gives a non-redundant partition of `local_N` instead of a
        # massively double-counted total.
        self.last_root_full = final_state["full"]
        # Full state (Full/Prefix/Suffix/All) exposed for the fractional exposure
        # variants (Max/Avg/Mean, see fractional_exposure.py), which need Prefix/Suffix
        # to credit cases the binary Tree Exposure metric (last_root_full alone) discards.
        self.last_root_state = final_state
        return final_state["all"]

    def _check_truncation(self, current_length: int):
        if current_length >= self.max_traces and not self._truncation_warned:
            warnings.warn(f"State space combinatorial explosion intercepted. Truncating permutations at {self.max_traces} max traces to prevent OOM crash.")
            self._truncation_warned = True

    def _analyze_recursive(self, node: ProcessTreeNode, local_N: int) -> PartitionedState:
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
            # Determine each child's guaranteed share of the requested local_N via
            # the same Overlap Formula already used for SEQ cross-multiplication
            # below (Section 3.2.2): child_n = max(0, child.frequency + local_N -
            # node.frequency). These normally agree with the children's own stored
            # frequencies (every standard top-down call passes local_N ==
            # node.frequency, for which this formula reduces to child_n ==
            # child.frequency exactly) -- but the LOOP zero-redo path intentionally
            # recurses into a do-child with a smaller local_N (zero_redo_freq) to
            # isolate just the never-redone cases.
            #
            # An earlier version of this fix used proportional scaling
            # (child_n = child.frequency * local_N/node.frequency) instead. That
            # correctly capped the total at local_N (fixing test_11_nesting.csv's
            # >100% bug), but it does so by assuming the smaller cohort's internal
            # choice is distributed in the same proportion as the whole population
            # -- a statistical assumption, not a derived guarantee, which is exactly
            # what this thesis is built to avoid claiming. It produced confident-
            # looking but unjustified fractional "predicted frequencies" (e.g.
            # 28/11 = 2.545...) for patterns whose true overlap-based guaranteed
            # minimum was actually 0. The overlap formula gives the real minimum --
            # often 0 when the cohort is too small or the split too even to pin
            # down, sometimes a genuine nonzero integer when the math supports one
            # -- instead of a plausible-sounding guess.
            own_freq = node.frequency
            if own_freq > 0:
                l_n = max(0.0, node.children[0].frequency + local_N - own_freq)
                r_n = max(0.0, node.children[1].frequency + local_N - own_freq)
            else:
                l_n = r_n = 0.0
            l_state = self._analyze_recursive(node.children[0], l_n)
            r_state = self._analyze_recursive(node.children[1], r_n)

            # A branch that resolves to nothing observable -- a silent (tau) leaf,
            # or any sub-tree that dissolves to one -- still represents real cases
            # that took this path. The LEAF rule above correctly returns a fully
            # empty state for a tau leaf (it contributes no events), but plain
            # concatenation below has no way to represent "N cases took this branch
            # and produced nothing": the branch's frequency would simply vanish from
            # every bucket. Confirmed on XOR(tau:9, D:1), N=10: the Full bucket
            # reported only D's 1 case, with the 9 tau-cases nowhere to be found
            # (see output/BUG_tau_xor_dissolution.md). Inject a zero-length
            # placeholder entry carrying that branch's frequency so it survives the
            # union below, the same way a real leaf would -- it has no content, but
            # its case count must still be counted by whatever consumes this bucket.
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

            # The overlap formula's two child shares can legitimately sum to less
            # than local_N: that gap is the volume genuinely too ambiguous to assign
            # to either specific branch (this is the honest counterpart to the old
            # proportional scaling's overstatement -- it admits "don't know" instead
            # of guessing). That volume must not simply vanish (the same class of
            # bug already found and fixed for tau dissolution), but it also cannot
            # be claimed as a Strict Trace for either branch. Represent it the same
            # way PAR/LOOP already represent irreducible uncertainty: as a registered,
            # opaque [nested XOR_k] block, so every existing structural check
            # (is_globally_strict, pattern_length, the auditor's block_alphabets/
            # block_patterns) handles it automatically with no further special-casing.
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
            # Same overlap-formula local_N adjustment as XOR above, for the same
            # reason: the LOOP zero-redo path can recurse into a SEQ do-child with a
            # local_N smaller than node.frequency. Unlike XOR, SEQ's two children
            # represent the SAME case population passing through sequentially (not a
            # split into disjoint groups), so under the normal invariant
            # (children[i].frequency == node.frequency for both) this reduces to
            # child_n == local_N exactly for both children -- no remainder is ever
            # possible here, since there is no "which child did it go to" question to
            # leave ambiguous.
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
                    # Recursively resolve the DO subtree instead of deep-copying it raw.
                    # A raw copy can still contain an internal XOR (a real choice), which
                    # would then be mislabeled "ST" (deterministic) even though the rendered
                    # pattern shows a "[A | B]" choice — leaving the trace open to
                    # interpretation. Recursing splits any such XOR into separate,
                    # genuinely deterministic alternative traces.
                    do_state = self._analyze_recursive(do_node, zero_redo_freq)

                    for t_node, t_freq, t_type in do_state["full"]:
                        final_node = t_node
                        # --- Force sequence formatting for the Zero-Redo trace ---
                        # To distinguish a zero-redo loop execution from a raw atomic event,
                        # we wrap it in a Sequence operator. This guarantees the formatter
                        # outputs ⟨C⟩ instead of just C.
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
        """Recursively counts unique activities and structural operators."""
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