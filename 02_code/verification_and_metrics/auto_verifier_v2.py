import pm4py as pm_lib
import pandas as pd
import itertools
from pathlib import Path
from typing import Dict, List, Tuple, Set
import re

from core.data_assimilation import DataAssimilation
from core.analyzer import ProcessTreeAnalyzer
from visualization.formatters import get_flat_representation
from visualization.visualizer import ProcessTreeVisualizer
from fractional_exposure import (
    expected_length_max, expected_length_avg, fractional_exposure, absolute_exposure_volume,
    classify_full_bucket, fragment_strict_exposure, local_strict_exposure, is_globally_strict,
)

class LogTraceVerifier:
    """
    Audits a mined process tree against the raw event log that produced it.

    For a given log, mines and assimilates the tree via the Deterministic Engine,
    enumerates the forced traces, and checks each predicted pattern against the
    real cases -- classifying every pattern as Verified, Discrepancy, Ghost, or
    Skipped -- while accumulating the exposure/coverage KPIs. Results are
    written as a Markdown audit report.

    Args:
        allow_interleaving: If ``True``, project each case onto a pattern's own
            alphabet before matching, so unrelated interleaved activities do not
            break an otherwise-present pattern.
        ignore_par_order: If ``True``, treat PAR-internal patterns as unordered
            (multiset) co-occurrences rather than requiring a fixed order.
        compute_fitness_precision: If ``False``, skip PM4Py's token-based
            fitness/precision replay (the slowest step); the values are read back
            from an existing report instead.

    Attributes:
        analyzer: The :class:`ProcessTreeAnalyzer` used for assimilation/analysis.
        tau_names: Names treated as silent (tau) leaves.
    """
    def __init__(self, allow_interleaving: bool = True, ignore_par_order: bool = True, compute_fitness_precision: bool = True):
        self.analyzer = ProcessTreeAnalyzer(max_traces_per_node=10000)
        self.tau_names = {"τ", "tau", "empty_tau", "none"}

        self.allow_interleaving = allow_interleaving
        self.ignore_par_order = ignore_par_order
        self.compute_fitness_precision = compute_fitness_precision

    def _load_raw_log(self, file_path: str) -> Dict[str, List[str]]:
        """
        Load the raw ordered activity sequence for every case in a log.

        Reads CSV via pandas or XES-family logs natively (kept as a PM4Py log
        object rather than a DataFrame), then groups events into per-case
        activity lists, tolerating non-standard case/activity column names.

        Args:
            file_path: Path to the event log (CSV or XES-family).

        Returns:
            A mapping of case id to its ordered list of activity names.

        Raises:
            ValueError: If the file extension is unsupported.
        """
        path_obj = Path(file_path)
        raw_cases = {}

        if path_obj.suffix.lower() == '.csv':
            data = pd.read_csv(file_path, sep=None, engine='python')
        elif path_obj.suffix.lower() in ['.xes', '.xml', '.mxml', '.gz']:
            # Read natively and keep the PM4Py log object (do not convert to a DataFrame)
            data = pm_lib.read_xes(file_path)
        else:
            raise ValueError(f"Unsupported file extension: {path_obj.suffix}")

        if isinstance(data, pd.DataFrame):
            case_candidates = ['case:concept:name', 'case id', 'case_id', 'case', 'id']
            case_col = next((c for cand in case_candidates for c in data.columns if c.lower() == cand), data.columns[0])

            act_candidates = ['concept:name', 'activity', 'task', 'event', 'action']
            act_col = next((c for cand in act_candidates for c in data.columns if c.lower() == cand), None)
            
            if act_col is None:
                act_col = data.columns[1] if len(data.columns) > 1 else data.columns[0]

            for case_id, group in data.groupby(case_col):
                raw_cases[str(case_id)] = [str(act).strip() for act in group[act_col].tolist()]
        else:
            for trace in data:
                case_id = trace.attributes.get('concept:name', 'Unknown_Case')
                raw_cases[str(case_id)] = [str(event['concept:name']).strip() for event in trace]

        return raw_cases

    def _get_model_alphabet(self, node) -> Set[str]:
        """
        Collect the set of real (non-tau) activity names in a subtree.

        Unlike :meth:`_get_leaves`, this does not exclude ``[nested ...]``
        placeholder names, so it reflects every directly-named activity.

        Args:
            node: The subtree root to scan.

        Returns:
            The set of non-tau leaf names found.
        """
        if node.operator == 'LEAF':
            name = str(node.name).strip()
            if name.lower() not in self.tau_names:
                return {name}
            return set()

        alphabet = set()
        for child in node.children:
            alphabet.update(self._get_model_alphabet(child))
        return alphabet

    def _compute_block_alphabets(self, registry: dict) -> Dict[str, Set[str]]:
        """
        Map each registered nested block to the set of real leaves it contains.

        Args:
            registry: The engine's ``nested_blocks_registry`` (block id -> subtree).

        Returns:
            A mapping of ``"[nested X]"`` token to its leaf-activity alphabet.
        """
        alphabets = {}
        for block_id, node in registry.items():
            alphabets[f"[{block_id}]"] = self._get_leaves(node)
        return alphabets

    def _compute_block_patterns(self, registry: dict) -> Dict[str, List[List[str]]]:
        """Precomputes each nested block's own valid sub-patterns (one instance's worth),
        so the fragment scanner can recognize a single execution of the block instead of
        greedily swallowing an entire alphabet-matching run as one match -- the latter
        silently collapses N>1 real repetitions (e.g. from an outer Loop redoing the same
        block several times back-to-back, with nothing but a silent tau between them) into
        a single counted occurrence, undercounting by exactly the outer Loop's redo count."""
        patterns = {}
        for block_id, node in registry.items():
            patterns[f"[{block_id}]"] = self._generate_valid_patterns(node)
        return patterns

    def _match_pattern_at(self, pattern: List[str], log_trace: List[str], idx: int,
                           block_alphabets: Dict[str, Set[str]], block_patterns: Dict[str, List[List[str]]]) -> "int | None":
        """Tries to consume exactly one instance of `pattern` starting at `idx`. Nested
        tokens within `pattern` are resolved recursively via their own one-instance match
        (not a flat greedy alphabet run), so a sequence like <D, [nested PAR_4], E> only
        ever consumes one PAR_4 instance, leaving subsequent repeats of the whole sequence
        to be picked up as separate matches by the caller. Returns the index just past the
        consumed instance, or None if `pattern` cannot be matched at `idx`."""
        for token in pattern:
            if idx >= len(log_trace):
                return None
            if token.startswith("[nested"):
                new_idx = self._match_one_block_instance(token, log_trace, idx, block_alphabets, block_patterns)
                if new_idx is None:
                    return None
                idx = new_idx
            else:
                if log_trace[idx] != token:
                    return None
                idx += 1
        return idx

    def _match_one_block_instance(self, token: str, log_trace: List[str], idx: int,
                                   block_alphabets: Dict[str, Set[str]], block_patterns: Dict[str, List[List[str]]]) -> "int | None":
        """Consumes exactly one execution of the opaque block `token`, preferring the
        longest of its own valid sub-patterns that matches at `idx`. Falls back to the
        original flat-alphabet greedy absorption when the block's patterns were marked
        COMPLEX (too many permutations to enumerate) or are unavailable, since a single
        bounded fallback is safer than no match at all in that case."""
        sub_patterns = block_patterns.get(token)
        if sub_patterns and sub_patterns != [["COMPLEX"]]:
            best_end = None
            for sub_pattern in sub_patterns:
                end = self._match_pattern_at(sub_pattern, log_trace, idx, block_alphabets, block_patterns)
                if end is not None and (best_end is None or end > best_end):
                    best_end = end
            if best_end is not None:
                return best_end
        # Fallback: flat-alphabet greedy absorption (only place this approximation remains)
        allowed_alphabet = block_alphabets.get(token, set())
        new_idx = idx
        while new_idx < len(log_trace) and log_trace[new_idx] in allowed_alphabet:
            new_idx += 1
        return new_idx if new_idx > idx else None

    def _get_leaves(self, node) -> Set[str]:
        """
        Collect the real, directly-named leaf activities of a subtree.

        Excludes both tau leaves and ``[nested ...]`` placeholder leaves, so the
        result is the block's own concrete alphabet.

        Args:
            node: The subtree root to scan.

        Returns:
            The set of concrete leaf-activity names.
        """
        if node.operator == 'LEAF':
            name = str(node.name).strip()
            if name.lower() in self.tau_names or "nested" in name:
                return set()
            return {name}
        leaves = set()
        for child in node.children:
            leaves.update(self._get_leaves(child))
        return leaves

    def _interleave_sequences(self, sequences: List[List[str]]) -> List[List[str]]:
        """
        Enumerate every order-preserving interleaving of several sequences.

        Each input sequence keeps its own internal order, but the sequences are
        merged in all possible ways (used to model unordered PAR execution).
        Duplicate interleavings are collapsed.

        Args:
            sequences: The sequences to interleave.

        Returns:
            A list of the distinct interleaved sequences.
        """
        active_seqs = [s for s in sequences if s]
        if not active_seqs: return [[]]
        if len(active_seqs) == 1: return [active_seqs[0]]

        result = []
        for i in range(len(active_seqs)):
            first_elem = active_seqs[i][0]
            remaining_seqs = [s[:] for s in active_seqs]
            remaining_seqs[i] = remaining_seqs[i][1:]
            for tail in self._interleave_sequences(remaining_seqs):
                result.append([first_elem] + tail)
                
        return [list(x) for x in set(tuple(x) for x in result)]

    def _generate_valid_patterns(self, node) -> List[List[str]]:
        """
        Enumerate the valid token sequences a subtree can produce.

        Recursively expands operators into their possible orderings: SEQ
        concatenates, XOR unions, PAR interleaves, and LOOP unrolls up to its redo
        frequency. ``[nested ...]`` placeholders are kept as single tokens. To
        bound cost, any expansion exceeding the internal permutation caps collapses
        to the sentinel ``[["COMPLEX"]]`` (the Atomic Fallback).

        Args:
            node: The subtree root to enumerate.

        Returns:
            A list of token-sequence patterns, or ``[["COMPLEX"]]`` if the pattern
            space is too large to enumerate.
        """
        MAX_PERMS = 1000
        if node.operator == 'LEAF':
            name = str(node.name).strip()
            if name.lower() in self.tau_names: return [[]]
            if name.startswith("[nested"): return [[name]]
            return [[name]]

        # Gracefully handle artificially wrapped single-child operators
        if not node.children:
            return [[]]
        if len(node.children) == 1:
            return self._generate_valid_patterns(node.children[0])

        if node.operator == 'SEQ':
            left_opts = self._generate_valid_patterns(node.children[0])
            right_opts = self._generate_valid_patterns(node.children[1])
            if left_opts == [["COMPLEX"]] or right_opts == [["COMPLEX"]]: return [["COMPLEX"]]
            res = [l + r for l in left_opts for r in right_opts]
            return res if len(res) <= MAX_PERMS else [["COMPLEX"]]

        if node.operator == 'PAR':
            child_opts = [self._generate_valid_patterns(c) for c in node.children]
            if any(opt == [["COMPLEX"]] for opt in child_opts): return [["COMPLEX"]]
            combinations = list(itertools.product(*child_opts))
            if len(combinations) > 50: return [["COMPLEX"]]
            all_interleavings = []
            for combo in combinations:
                all_interleavings.extend(self._interleave_sequences(list(combo)))
                if len(all_interleavings) > MAX_PERMS: return [["COMPLEX"]]
            return [list(x) for x in set(tuple(x) for x in all_interleavings)]

        if node.operator == 'XOR':
            left_opts = self._generate_valid_patterns(node.children[0])
            right_opts = self._generate_valid_patterns(node.children[1])
            if left_opts == [["COMPLEX"]] or right_opts == [["COMPLEX"]]: return [["COMPLEX"]]
            res = [list(x) for x in set(tuple(x) for x in left_opts + right_opts)]
            return res if len(res) <= MAX_PERMS else [["COMPLEX"]]

        if node.operator == 'LOOP':
            do_opts = self._generate_valid_patterns(node.children[0])
            redo_opts = self._generate_valid_patterns(node.children[1])
            if do_opts == [["COMPLEX"]] or redo_opts == [["COMPLEX"]]: return [["COMPLEX"]]
            
            redo_freq = getattr(node.children[1], 'frequency', 0)
            max_unrolls = redo_freq if redo_freq > 0 else 0
            res = []
            
            current_paths = do_opts[:]
            res.extend(current_paths)
            
            for _ in range(max_unrolls):
                next_paths = [path + r + d for path in current_paths for r in redo_opts for d in do_opts]
                res.extend(next_paths)
                current_paths = next_paths
                if len(res) > 1000:
                    return [["COMPLEX"]]
                
            res = [list(x) for x in set(tuple(x) for x in res)]
            return res if len(res) <= MAX_PERMS else [["COMPLEX"]]


    @staticmethod
    def _mark_covered(coverage_masks, index_map, case_id: str, positions: range, tier: int) -> None:
        """Marks the given filtered-trace `positions` as covered at `tier`, translating
        them back to their original (pre-alphabet-filtering) indices via `index_map`, so
        coverage masks stay aligned to the canonical case trace regardless of which
        interleaving-projected view a given pattern happened to be matched against.
        Tiers are 1 (strictest: ST-only) .. 3 (broadest: Total) -- a position keeps the
        LOWEST tier it ever qualifies for, never the highest, so a position already
        explained by a strict ST pattern doesn't get reclassified as merely "Total"
        just because a broader AS-tagged macro pattern also happens to cover it."""
        if coverage_masks is None:
            return
        mask = coverage_masks.get(case_id)
        idxs = index_map.get(case_id) if index_map else None
        if mask is None:
            return
        for pos in positions:
            orig = idxs[pos] if idxs is not None else pos
            if orig < len(mask) and (mask[orig] == 0 or tier < mask[orig]):
                mask[orig] = tier

    def _count_fragment_matches(self, valid_permutations: List[List[str]], target_cases: Dict[str, List[str]], is_unordered_par: bool, block_alphabets: Dict[str, Set[str]], block_patterns: Dict[str, List[List[str]]] = None,
                                 coverage_masks=None, index_map=None, tier: int = 0) -> Tuple[int, int]:
        """Greedily scans and counts all sub-sequence occurrences without requiring full trace consumption."""
        if not valid_permutations or valid_permutations == [["COMPLEX"]]: 
            return 0, 0
            
        match_count = 0
        observed_variations = set()
        
        valid_perms_set = {tuple(p) for p in valid_permutations if p}
        if not valid_perms_set:
            return len(target_cases), 1 
            
        for case_id, log_trace in target_cases.items():
            if is_unordered_par:
                from collections import Counter
                trace_counts = Counter(log_trace)
                for perm in valid_perms_set:
                    req_counts = Counter()
                    
                    # Unpack nested block alphabets so we can count them
                    for token in perm:
                        if token.startswith("[nested"):
                            allowed_alphabet = block_alphabets.get(token, set())
                            for act in allowed_alphabet:
                                req_counts[act] += 1
                        else:
                            req_counts[token] += 1
                            
                    possible_matches = min((trace_counts[act] // count for act, count in req_counts.items() if count > 0), default=0)
                    if possible_matches > 0:
                        match_count += possible_matches
                        observed_variations.add(perm)
                        if coverage_masks is not None:
                            mask = coverage_masks.get(case_id)
                            idxs = index_map.get(case_id) if index_map else None
                            if mask is not None:
                                positions_by_act: Dict[str, List[int]] = {}
                                for filt_pos, act in enumerate(log_trace):
                                    orig = idxs[filt_pos] if idxs is not None else filt_pos
                                    if orig < len(mask) and mask[orig] < tier:
                                        positions_by_act.setdefault(act, []).append(orig)
                                for act, count in req_counts.items():
                                    need = count * possible_matches
                                    for orig in positions_by_act.get(act, [])[:need]:
                                        if mask[orig] < tier:
                                            mask[orig] = tier
                        for act, count in req_counts.items():
                            trace_counts[act] -= count * possible_matches
            else:
                for perm in valid_perms_set:
                    if len(perm) == 0: continue
                    i = 0
                    while i < len(log_trace):
                        log_idx = i
                        gen_idx = 0
                        match_failed = False
                        
                        while gen_idx < len(perm) and log_idx < len(log_trace):
                            token = perm[gen_idx]
                            if token.startswith("[nested"):
                                new_log_idx = self._match_one_block_instance(
                                    token, log_trace, log_idx, block_alphabets, block_patterns or {}
                                )
                                if new_log_idx is not None and new_log_idx > log_idx:
                                    log_idx = new_log_idx
                                    gen_idx += 1
                                else:
                                    match_failed = True
                                    break
                            else:
                                if log_trace[log_idx] == token:
                                    log_idx += 1
                                    gen_idx += 1
                                else:
                                    match_failed = True
                                    break
                                    
                        # Complete internal pattern found
                        if not match_failed and gen_idx == len(perm):
                            match_count += 1
                            observed_variations.add(perm)
                            self._mark_covered(coverage_masks, index_map, case_id, range(i, log_idx), tier)
                            i = log_idx # Jump forward, preventing overlapping matches
                        else:
                            i += 1

        return match_count, len(observed_variations)

    # The hierarchical matcher, used for macro / end-to-end traces.
    def _count_hierarchical_matches(self, valid_permutations: List[List[str]], clean_cases: Dict[str, List[str]], block_alphabets: Dict[str, Set[str]],
                                     coverage_masks=None, index_map=None, tier: int = 0) -> Tuple[int, int]:
        """
        Count cases matched end-to-end by any of the given macro patterns.

        A case counts once if some pattern consumes its entire (cleaned) trace
        exactly (see :meth:`_is_hierarchical_match`); matched positions are marked
        in the coverage masks at ``tier``.

        Args:
            valid_permutations: Candidate full-trace token patterns.
            clean_cases: Case id -> alphabet-filtered activity list.
            block_alphabets: ``[nested X]`` token -> its allowed alphabet.
            coverage_masks: Optional per-case tier masks to update.
            index_map: Optional filtered->original index mapping per case.
            tier: Coverage tier to record for matched positions.

        Returns:
            A ``(match_count, distinct_patterns_observed)`` tuple.
        """
        if not valid_permutations or valid_permutations == [["COMPLEX"]]:
            return 0, 0

        match_count = 0
        observed_variations = set()
        valid_perms_set = {tuple(p) for p in valid_permutations if p}

        for case_id, log_trace in clean_cases.items():
            for perm in valid_perms_set:
                if self._is_hierarchical_match(list(perm), log_trace, block_alphabets):
                    match_count += 1
                    observed_variations.add(perm)
                    # A hierarchical match requires consuming the ENTIRE trace exactly
                    # (the macro consumer), so the whole filtered view --
                    # i.e. every position this pattern's alphabet projection retained --
                    # is what gets credited as covered, not just part of it.
                    self._mark_covered(coverage_masks, index_map, case_id, range(len(log_trace)), tier)
                    break
        return match_count, len(observed_variations)

    def _is_hierarchical_match(self, expected_tokens: List[str], log_trace: List[str], block_alphabets: Dict[str, Set[str]]) -> bool:
        """
        Check whether a token pattern consumes an entire case trace exactly.

        Walks ``expected_tokens`` against ``log_trace``: a plain token must match
        the next activity, while a ``[nested X]`` token greedily consumes a run of
        activities from its block alphabet. Succeeds only if both the pattern and
        the trace are fully consumed.

        Args:
            expected_tokens: The macro pattern to match.
            log_trace: The case's (cleaned) activity list.
            block_alphabets: ``[nested X]`` token -> its allowed alphabet.

        Returns:
            ``True`` if the pattern matches the whole trace exactly.
        """
        log_idx = 0
        gen_idx = 0
        while gen_idx < len(expected_tokens) and log_idx < len(log_trace):
            token = expected_tokens[gen_idx]
            if token.startswith("[nested"):
                allowed_alphabet = block_alphabets.get(token, set())
                consumed_something = False
                while log_idx < len(log_trace) and log_trace[log_idx] in allowed_alphabet:
                    log_idx += 1
                    consumed_something = True
                if consumed_something: gen_idx += 1
                else: return False 
            else:
                if log_trace[log_idx] == token:
                    log_idx += 1
                    gen_idx += 1
                else: return False
        return gen_idx == len(expected_tokens) and log_idx == len(log_trace)

    def verify_and_report(self, input_file: str, output_md_path: str, noise_threshold: float = 0.0):
        """
        Audit one log against its mined tree and write a Markdown report.

        Mines the original PM4Py tree, assimilates it into the Deterministic
        Engine's binary form, enumerates the forced traces, and checks each
        auditable pattern against the raw cases -- tallying Verified / Discrepancy
        / Ghost / Skipped outcomes and computing the tree-exposure, data-exposure,
        and data-coverage KPIs -- then writes an overview table, per-pattern audit
        table, and nested-block reference to ``output_md_path`` (with diagrams).

        Args:
            input_file: Path to the event log to audit.
            output_md_path: Path of the Markdown audit report to write.
            noise_threshold: Inductive-miner noise threshold used when mining.

        Returns:
            None. The report and its images are written to disk.
        """
        print(f"[*] Starting Audit for: {input_file} (Noise: {noise_threshold})")
        raw_cases = self._load_raw_log(input_file)
        total_cases = len(raw_cases)

        md_path_obj = Path(output_md_path)
        img_dir = md_path_obj.parent / "images"
        img_dir.mkdir(parents=True, exist_ok=True)
        
        orig_img_filename = f"orig_tree_{md_path_obj.stem}.png"
        orig_img_path = img_dir / orig_img_filename
        
        original_tree_str, orig_img_saved = self._print_original_pm4py_tree(input_file, noise_threshold, orig_img_path)
        
        if orig_img_saved:
            orig_img_markdown = f"![Original PM4Py Tree](images/{orig_img_filename})\n"
        else:
            orig_img_markdown = "*⚠️ Failed to generate original PM4Py tree diagram.*\n"

        root_tree = DataAssimilation.assimilate_from_file(
            input_file, self.analyzer, noise_threshold=noise_threshold,
            compute_metrics=self.compute_fitness_precision,
        )
        engine_traces = self.analyzer.analyze_forced_traces(root_tree, root_tree.frequency)

        extracted_registry = self.analyzer.nested_blocks_registry.copy()
        block_alphabets = self._compute_block_alphabets(extracted_registry)
        block_patterns = self._compute_block_patterns(extracted_registry)

        custom_img_filename = f"custom_tree_{md_path_obj.stem}"
        custom_img_path_base = img_dir / custom_img_filename
        
        try:
            visualizer = ProcessTreeVisualizer(root_tree, show_frequencies=True)
            visualizer.render(filename=str(custom_img_path_base), format='png', view=False)
            custom_img_markdown = f"![Assimilated Master Tree](images/{custom_img_filename}.png)\n"
        except Exception as e:
            custom_img_markdown = f"*⚠️ Failed to generate custom tree diagram: {e}*\n"

        fitness_raw = getattr(root_tree, 'pm4py_fitness', 'N/A')
        if isinstance(fitness_raw, dict): fitness_val = fitness_raw.get('average_trace_fitness', fitness_raw.get('log_fitness', fitness_raw))
        else: fitness_val = fitness_raw
        precision_val = getattr(root_tree, 'pm4py_precision', 'N/A')

        model_alphabet = self._get_model_alphabet(root_tree)
        clean_cases = {cid: [a for a in acts if a in model_alphabet] for cid, acts in raw_cases.items()}
        coverage_total_events = sum(len(acts) for acts in clean_cases.values())
        coverage_masks = {cid: [0] * len(acts) for cid, acts in clean_cases.items()}
        auditable_traces = [t for t in engine_traces if t[2].startswith("ST") or t[2].startswith("AS")]

        # --- 1. Gather pre-verification Statistics ---
        stats = self.analyzer.get_tree_stats(root_tree)
        binarization_ops = getattr(root_tree, 'binarization_additions', 'N/A')

        nested_loops = sum(1 for n in extracted_registry.values() if n.operator == 'LOOP')
        nested_pars = sum(1 for n in extracted_registry.values() if n.operator == 'PAR')
        total_patterns_found = len(auditable_traces)

        root_n = root_tree.frequency
        bucket_classification = classify_full_bucket(getattr(self.analyzer, 'last_root_full', []), extracted_registry)
        st_volume = bucket_classification["st_volume"]
        as_resolved_volume = bucket_classification["as_resolved_volume"]
        as_resolved_par_volume = bucket_classification["as_resolved_par_volume"]
        as_resolved_loop_volume = bucket_classification["as_resolved_loop_volume"]
        as_opaque_volume = bucket_classification["as_opaque_volume"]
        total_forced_volume = st_volume + as_resolved_volume + as_opaque_volume

        tree_exposure_pct = (st_volume / root_n * 100) if root_n > 0 else 0.0
        total_forced_volume_pct = (total_forced_volume / root_n * 100) if root_n > 0 else 0.0
        as_resolved_pct = (as_resolved_volume / root_n * 100) if root_n > 0 else 0.0

        as_resolved_par_pct = (as_resolved_par_volume / root_n * 100) if root_n > 0 else 0.0
        as_resolved_loop_pct = (as_resolved_loop_volume / root_n * 100) if root_n > 0 else 0.0
        as_opaque_pct = (as_opaque_volume / root_n * 100) if root_n > 0 else 0.0


        last_root_state = getattr(self.analyzer, 'last_root_state', None)
        if last_root_state is not None and root_n > 0:
            max_len = expected_length_max(root_tree, extracted_registry)
            avg_len = expected_length_avg(root_tree, extracted_registry)
            max_result = fractional_exposure(root_tree, last_root_state, extracted_registry, max_len, include_residual=True)
            avg_result = fractional_exposure(root_tree, last_root_state, extracted_registry, avg_len, include_residual=True)
            mean_result = absolute_exposure_volume(root_tree, last_root_state, extracted_registry)
            max_exposure_pct = max_result["fractional_pct"]
            avg_exposure_pct = avg_result["fractional_pct"]
            mean_events_per_case = mean_result["events_per_case"]

            fragment_strict_pct = fragment_strict_exposure(root_tree, last_root_state, extracted_registry, avg_len)["fragment_strict_pct"]

            fragment_strict_min2_pct = fragment_strict_exposure(root_tree, last_root_state, extracted_registry, avg_len, min_length=2.0)["fragment_strict_pct"]

            local_strict_pct = local_strict_exposure(root_tree, last_root_state, extracted_registry, avg_len, min_length=0.0)["local_strict_pct"]
            local_strict_min2_pct = local_strict_exposure(root_tree, last_root_state, extracted_registry, avg_len, min_length=2.0)["local_strict_pct"]
        else:
            max_exposure_pct = avg_exposure_pct = mean_events_per_case = 0.0
            fragment_strict_pct = fragment_strict_min2_pct = 0.0
            local_strict_pct = local_strict_min2_pct = 0.0
            max_len = avg_len = 0.0

        # Initialize the base document structure (we will insert the table later)
        md_lines = [
            f"# Process Engine Audit Report\n",
            "## Original PM4Py Tree\n", orig_img_markdown, f"\n```text\n{original_tree_str}\n```\n",
            "## Assimilated Master Tree\n", custom_img_markdown, "\n",
            "## Trace Verification\n",
            "| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |",
            "| :--- | :--- | :--- | :--- | :--- | :--- |"
        ]
        # ---------------------------------------------------

        verified_perfect, discrepancies, ghost_traces, skipped_traces = 0, 0, 0, 0
        verified_rows, discrepancy_rows, ghost_rows, skipped_rows = [], [], [], []
        seen_patterns = set()


        total_expected_volume = 0
        total_confirmed_volume = 0

        total_expected_st = 0
        total_confirmed_st = 0
        total_expected_st_par = 0
        total_confirmed_st_par = 0

        for node, engine_freq, t_type in auditable_traces:
            valid_permutations = self._generate_valid_patterns(node)
            md_trace = get_flat_representation(node).replace('|', '&#124;')

            # Classify the trace's structural context (block-internal vs macro, PAR handling).
            is_internal = "(in " in t_type
            is_par_internal = "(in PAR" in t_type and self.ignore_par_order
            tagged_in_par = "(in PAR" in t_type
            node_is_strict = is_globally_strict(node)

            # Internal loops repeat per trace, so never cap their target frequency. Macro traces stay capped.
            expected_freq = engine_freq if is_internal else min(engine_freq, total_cases)

            signature = (md_trace, expected_freq)
            if signature in seen_patterns: continue
            seen_patterns.add(signature)
            
            if valid_permutations == [["COMPLEX"]]:
                skipped_rows.append(f"| `[{t_type}]` | `{md_trace}` | ⚠️ OVER 1,000 | {expected_freq} | - | ⏩ **SKIPPED** |")
                skipped_traces += 1
                continue

            if valid_permutations == [[]]:
                total_patterns_found -= 1
                continue

            if self.allow_interleaving:
                local_alphabet = self._get_model_alphabet(node)
                for token in valid_permutations[0]:
                    if token.startswith("[nested"):
                        local_alphabet.update(block_alphabets.get(token, set()))

                if not local_alphabet:
                    target_cases = clean_cases
                    index_map = {cid: list(range(len(acts))) for cid, acts in clean_cases.items()}
                else:
                    target_cases, index_map = {}, {}
                    for cid, acts in clean_cases.items():
                        filtered, idxs = [], []
                        for orig_idx, a in enumerate(acts):
                            if a in local_alphabet:
                                filtered.append(a)
                                idxs.append(orig_idx)
                        target_cases[cid] = filtered
                        index_map[cid] = idxs
            else:
                target_cases = clean_cases
                index_map = {cid: list(range(len(acts))) for cid, acts in clean_cases.items()}


            if node_is_strict and not is_internal:
                coverage_tier = 1
            elif node_is_strict and tagged_in_par:
                coverage_tier = 2
            else:
                coverage_tier = 3
            temp_coverage = {cid: [0] * len(acts) for cid, acts in clean_cases.items()}

            # Route to the matching consumer based on whether the trace is block-internal.
            if is_internal:
                # Use the sliding fragment scanner
                actual_count, observed_vars = self._count_fragment_matches(
                    valid_permutations, target_cases, is_par_internal, block_alphabets, block_patterns,
                    coverage_masks=temp_coverage, index_map=index_map, tier=coverage_tier
                )
            else:
                # Use the strict Macro-trace end-to-end consumer
                actual_count, observed_vars = self._count_hierarchical_matches(
                    valid_permutations, target_cases, block_alphabets,
                    coverage_masks=temp_coverage, index_map=index_map, tier=coverage_tier
                )

            var_str = f"({observed_vars} permutations)" if observed_vars > 1 else "Exact Token Match"

            # --- EXPOSED VS. HIDDEN: METRIC 2 accumulation ---
            # Confirmed volume is capped at expected_freq so that surplus matches beyond
            # the guaranteed minimum don't inflate the confirmation rate.
            total_expected_volume += expected_freq
            total_confirmed_volume += min(actual_count, expected_freq)

            if node_is_strict and not is_internal:
                total_expected_st += expected_freq
                total_confirmed_st += min(actual_count, expected_freq)
            if node_is_strict and (not is_internal or tagged_in_par):
                total_expected_st_par += expected_freq
                total_confirmed_st_par += min(actual_count, expected_freq)

            # Evaluate as a minimum bound, not an exact match
            if actual_count == 0:
                status = "❌ **GHOST PATTERN**"
                ghost_traces += 1
                ghost_rows.append(f"| `[{t_type}]` | `{md_trace}` | {var_str} | $\\ge$ {expected_freq} | **{actual_count}** | {status} |")

            # If the log meets or exceeds the guaranteed minimum, the mathematical proof is Verified
            elif actual_count >= expected_freq:
                status = "✅ **VERIFIED**"
                verified_perfect += 1
                verified_rows.append(f"| `[{t_type}]` | `{md_trace}` | {var_str} | $\\ge$ {expected_freq} | **{actual_count}** | {status} |")
                # --- METRIC 3 commit: only a fully VERIFIED pattern's matched positions
                # are allowed to count as "proven" coverage -- a Discrepancy/Ghost pattern's
                # incidental partial matches are discarded entirely, never merged in.
                for cid, tiers in temp_coverage.items():
                    dest = coverage_masks[cid]
                    for idx, t in enumerate(tiers):
                        if t > 0 and (dest[idx] == 0 or t < dest[idx]):
                            dest[idx] = t

            # If it is greater than 0 but less than the expected minimum, the math failed.
            else:
                status = "⚠️ **DISCREPANCY**"
                discrepancies += 1
                discrepancy_rows.append(f"| `[{t_type}]` | `{md_trace}` | {var_str} | $\\ge$ {expected_freq} | **{actual_count}** | {status} |")

        # --- EXPOSED VS. HIDDEN: METRIC 2 final ratio ---
        data_exposure_pct = (total_confirmed_volume / total_expected_volume * 100) if total_expected_volume > 0 else 0.0
        data_exposure_st_pct = (total_confirmed_st / total_expected_st * 100) if total_expected_st > 0 else 0.0
        data_exposure_st_par_pct = (total_confirmed_st_par / total_expected_st_par * 100) if total_expected_st_par > 0 else 0.0

        # --- METRIC 3 final ratios (Data Coverage: the recall-side counterpart to Data
        # Exposure's precision-side question) ---
        coverage_st_count = sum(1 for tiers in coverage_masks.values() for t in tiers if t == 1)
        coverage_st_par_count = sum(1 for tiers in coverage_masks.values() for t in tiers if t in (1, 2))
        coverage_total_count = sum(1 for tiers in coverage_masks.values() for t in tiers if t >= 1)
        data_coverage_st_pct = (coverage_st_count / coverage_total_events * 100) if coverage_total_events > 0 else 0.0
        data_coverage_st_par_pct = (coverage_st_par_count / coverage_total_events * 100) if coverage_total_events > 0 else 0.0
        data_coverage_total_pct = (coverage_total_count / coverage_total_events * 100) if coverage_total_events > 0 else 0.0

        md_lines.extend(verified_rows + discrepancy_rows + ghost_rows + skipped_rows)
        md_lines.append("\n## Audit Summary")
        md_lines.append(f"- **Perfect Pattern Verifications:** {verified_perfect}")
        md_lines.append(f"- **Frequency Discrepancies:** {discrepancies}")
        md_lines.append(f"- **Ghost Patterns (Fatal):** {ghost_traces}")
        md_lines.append(f"- **Skipped (Complexity > 1000):** {skipped_traces}")
        md_lines.append(f"- **Tree Exposure (Strict, End-to-End % of N):** {tree_exposure_pct:.2f}%")
        md_lines.append(f"- **Tree Exposure (Strict, Fragment-Level % of N):** {fragment_strict_pct:.2f}%")
        md_lines.append(f"- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** {fragment_strict_min2_pct:.2f}%")
        md_lines.append(f"- **Tree Exposure (Local-Strict % of N):** {local_strict_pct:.2f}% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*")
        md_lines.append(f"- **Tree Exposure (Local-Strict, >=2 activities, % of N):** {local_strict_min2_pct:.2f}%")
        md_lines.append(f"- **Total Forced Volume (incl. unresolved AS, % of N):** {total_forced_volume_pct:.2f}%")
        md_lines.append(f"- **AS-Resolved Volume (% of N):** {as_resolved_pct:.2f}%")
        md_lines.append(f"- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** {as_resolved_par_pct:.2f}%")
        md_lines.append(f"- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** {as_resolved_loop_pct:.2f}%")
        md_lines.append(f"- **AS-Opaque Volume (% of N):** {as_opaque_pct:.2f}%")
        md_lines.append(f"- **Data Exposure (Confirmed % of Claimed Volume):** {data_exposure_pct:.2f}%")
        md_lines.append(f"- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** {data_exposure_st_pct:.2f}%")
        md_lines.append(f"- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** {data_exposure_st_par_pct:.2f}%")
        md_lines.append(f"- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** {data_coverage_st_pct:.2f}%")
        md_lines.append(f"- **Data Coverage, ST + ST-in-PAR (% of real log explained):** {data_coverage_st_par_pct:.2f}%")
        md_lines.append(f"- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** {data_coverage_total_pct:.2f}%")
        md_lines.append(f"- **Max Fractional Exposure (Worst-Case Normalized):** {max_exposure_pct:.2f}% (expected length: {max_len:.2f} events)")
        md_lines.append(f"- **Avg Fractional Exposure (Typical-Case Normalized):** {avg_exposure_pct:.2f}% (expected length: {avg_len:.2f} events)")
        md_lines.append(f"- **Mean Absolute Exposure Volume:** {mean_events_per_case:.2f} events/case")

        if extracted_registry:
            md_lines.append("\n---\n")
            md_lines.append("## Nested Structures Reference")
            md_lines.append("The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n")
            
            for block_id, original_node in extracted_registry.items():
                # Note: block_id is already formatted like "nested PAR_1"
                md_lines.append(f"### `[{block_id}]`")
                
                # Fetch the flat representation to show what's inside
                flat_rep = get_flat_representation(original_node)
                md_lines.append(f"- **Internal Structure:** `{flat_rep}`")
                md_lines.append(f"- **Block Frequency:** {original_node.frequency}\n")

                # --- CALCULATE LOOP MAX LENGTH ---
                if original_node.operator == 'LOOP':
                    # Safe fetch of REDO frequency
                    redo_freq = getattr(original_node.children[1], 'frequency', 0) if len(original_node.children) > 1 else 0
                    max_steps = (redo_freq * 2) + 1
                    md_lines.append(f"- **Max Loop Iterations:** `{redo_freq}`")
                    md_lines.append(f"- **Max Sub-Sequence Length:** `{max_steps}` steps (if one case consumes all iterations)\n")
                else:
                    md_lines.append("\n") # Formatting spacer
                
                # Generate a localized micro-diagram specifically for this nested block
                try:
                    # Clean the ID for safe file paths (e.g. "nested_PAR_1")
                    safe_id = block_id.replace(" ", "_")
                    ref_img_filename = f"nested_ref_{md_path_obj.stem}_{safe_id}"
                    ref_img_path_base = img_dir / ref_img_filename
                    
                    # Render the localized diagram
                    ref_visualizer = ProcessTreeVisualizer(original_node, show_frequencies=True)
                    ref_visualizer.render(str(ref_img_path_base), format='png', view=False)
                    
                    # Relative link to the images folder
                    ref_md_link = f"images/{ref_img_filename}.png"
                    md_lines.append(f"![{block_id} Internal Diagram]({ref_md_link})\n")
                except Exception as e:
                    md_lines.append(f"*⚠️ Failed to generate internal diagram: {e}*\n")
        
        # --- 2. Build the Overview Table and insert it right after the main Title ---
        overview_table = [
            "## Dataset & Audit Overview",
            "| Metric | Value |",
            "| :--- | :--- |",
            f"| **Dataset Name** | `{Path(input_file).name}` |",
            f"| **Noise Threshold** | `{noise_threshold}` |",
            f"| **Fitness** | `{fitness_val}` |",
            f"| **Precision** | `{precision_val}` |",
            f"| **Total Cases in Log** | `{total_cases}` |",
            f"| **Unique Activities** | `{stats['num_activities']}` |",
            f"| **XOR Operators** | `{stats['XOR']}` |",
            f"| **LOOP Operators** | `{stats['LOOP']}` |",
            f"| **SEQ Operators** | `{stats['SEQ']}` |",
            f"| **PAR Operators** | `{stats['PAR']}` |",
            f"| **Binarization Additions** | `{binarization_ops}` |",
            f"| **Tau Operators Added** | `{getattr(self.analyzer, 'added_tau_count', 0)}` |",
            f"| **Total Found Patterns** | `{total_patterns_found}` |",
            f"| **Verified Patterns** | `{verified_perfect}` |",
            f"| **Discrepancy Patterns** | `{discrepancies}` |",
            f"| **Ghost Patterns** | `{ghost_traces}` |",
            f"| **Nested LOOPs** | `{nested_loops}` |",
            f"| **Nested PARs** | `{nested_pars}` |",
            f"| **Tree Exposure (Strict, End-to-End % of N)** | `{tree_exposure_pct:.2f}%` |",
            f"| **Tree Exposure (Strict, Fragment-Level % of N)** | `{fragment_strict_pct:.2f}%` |",
            f"| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `{fragment_strict_min2_pct:.2f}%` |",
            f"| **Tree Exposure (Local-Strict % of N)** | `{local_strict_pct:.2f}%` |",
            f"| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `{local_strict_min2_pct:.2f}%` |",
            f"| **Total Forced Volume (incl. unresolved AS, % of N)** | `{total_forced_volume_pct:.2f}%` |",
            f"| **AS-Resolved Volume (% of N)** | `{as_resolved_pct:.2f}%` |",
            f"| **AS-Resolved Volume, PAR-only (% of N)** | `{as_resolved_par_pct:.2f}%` |",
            f"| **AS-Resolved Volume, LOOP-only (% of N)** | `{as_resolved_loop_pct:.2f}%` |",
            f"| **AS-Opaque Volume (% of N)** | `{as_opaque_pct:.2f}%` |",
            f"| **Data Exposure (Confirmed % of Claimed Volume)** | `{data_exposure_pct:.2f}%` |",
            f"| **Data Exposure, ST-only (% confirmed)** | `{data_exposure_st_pct:.2f}%` |",
            f"| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `{data_exposure_st_par_pct:.2f}%` |",
            f"| **Data Coverage, ST-only (% of real log)** | `{data_coverage_st_pct:.2f}%` |",
            f"| **Data Coverage, ST + ST-in-PAR (% of real log)** | `{data_coverage_st_par_pct:.2f}%` |",
            f"| **Data Coverage, Total (% of real log)** | `{data_coverage_total_pct:.2f}%` |",
            f"| **Max Fractional Exposure (Worst-Case Normalized)** | `{max_exposure_pct:.2f}%` |",
            f"| **Avg Fractional Exposure (Typical-Case Normalized)** | `{avg_exposure_pct:.2f}%` |",
            f"| **Mean Absolute Exposure Volume (events/case)** | `{mean_events_per_case:.2f}` |\n",
            "---\n"
        ]
        
        # Insert the overview table at index 1 (right below "# Process Engine Audit Report")
        md_lines = md_lines[:1] + overview_table + md_lines[1:]

        # Finally, write the complete report to the Markdown file
        with open(output_md_path, "w", encoding="utf-8") as f:
            f.write("\n".join(md_lines))

    def verify_batch(self, target_path: str, report_dir: str, noise_threshold: float = 0.0):
        """
        Audit every supported log at a path, one report per file.

        Accepts a single log file or a directory (scanned non-recursively for
        recognized extensions), and calls :meth:`verify_and_report` for each,
        writing ``audit_<stem>__noise<level>.md`` into ``report_dir``. A failure on
        one file is caught and logged so the batch continues.

        Args:
            target_path: A log file or directory of logs to audit.
            report_dir: Directory where the per-file reports are written.
            noise_threshold: Inductive-miner noise threshold used when mining.

        Returns:
            None. Reports are written to ``report_dir``.
        """
        path_obj = Path(target_path)
        report_out_dir = Path(report_dir)
        report_out_dir.mkdir(parents=True, exist_ok=True)

        files_to_process = []
        if path_obj.is_file():
            files_to_process.append(path_obj)
        elif path_obj.is_dir():
            for f in path_obj.iterdir():
                if f.is_file() and f.suffix.lower() in {'.csv', '.xes', '.xml', '.mxml', '.gz'}:
                    files_to_process.append(f)

        for i, file_path in enumerate(files_to_process, 1):
            try:
                out_path = report_out_dir / f"audit_{file_path.stem}__noise{noise_threshold}.md"
                self.verify_and_report(str(file_path), str(out_path), noise_threshold=noise_threshold)
            except Exception as e:
                print(f" FAILED to audit {file_path.name}: {e}")

    def _print_original_pm4py_tree(self, file_path: str, noise_threshold: float, img_out_path: Path) -> Tuple[str, bool]:
        """Mines, prints, and visually saves the pure pm4py process tree directly from the file."""
        print(f"\n[*] Mining original PM4Py Process Tree for {Path(file_path).name} (Noise: {noise_threshold})...")
        try:
            path_obj = Path(file_path)
            
            # Load and format the log for PM4Py
            if path_obj.suffix.lower() == '.csv':
                df = pd.read_csv(file_path, sep=None, engine='python')
                case_col = next((c for cand in ['case:concept:name', 'case id', 'case_id', 'case', 'id'] for c in df.columns if c.lower() == cand), df.columns[0])
                act_col = next((c for cand in ['concept:name', 'activity', 'task', 'event', 'action'] for c in df.columns if c.lower() == cand), df.columns[1] if len(df.columns) > 1 else df.columns[0])
                time_col = next((c for cand in ['time:timestamp', 'timestamp', 'time', 'date'] for c in df.columns if c.lower() == cand), None)
                
                if time_col:
                    df[time_col] = pd.to_datetime(df[time_col])
                    log = pm_lib.format_dataframe(df, case_id=case_col, activity_key=act_col, timestamp_key=time_col)
                else:
                    log = pm_lib.format_dataframe(df, case_id=case_col, activity_key=act_col)
            else:
                df = DataAssimilation._prepare_log_dataframe(file_path)
                df['concept:name'] = df['concept:name'].astype('category')
                log = pm_lib.format_dataframe(
                    df,
                    case_id='case:concept:name',
                    activity_key='concept:name',
                    timestamp_key='time:timestamp'
                )

            # Mine the tree purely using pm4py
            tree = pm_lib.discover_process_tree_inductive(log, noise_threshold=noise_threshold)
            tree_str = str(tree)
            
            # Print to console
            print("-" * 50)
            print("ORIGINAL PM4PY PROCESS TREE:")
            print(tree_str)
            print("-" * 50 + "\n")
            
            # Save the image using PM4Py
            try:
                pm_lib.save_vis_process_tree(tree, str(img_out_path))
                img_saved = True
            except Exception as e_img:
                print(f"[!] Warning: Failed to save PM4Py tree image: {e_img}")
                img_saved = False
                
            return tree_str, img_saved
            
        except Exception as e:
            print(f"[!] Warning: Failed to mine/print original PM4Py tree: {e}")
            return f"Failed to mine original tree: {e}", False

def prepare_for_verifier(input_file, output_file):
    """
    Normalize a raw CSV log into a verifier-safe, XES-style CSV.

    Renames the ``Case ID`` / ``Activity`` / ``Timestamp`` columns to their
    canonical ``concept:name`` forms, coerces case ids to strings, parses
    timestamps, sorts chronologically per case, and breaks identical-timestamp
    ties by adding cumulative milliseconds so event order is stable.

    Args:
        input_file: Path to the raw CSV log.
        output_file: Path of the cleaned CSV to write.

    Returns:
        None. The cleaned CSV is written to ``output_file``.
    """
    print("Loading data...")
    df = pd.read_csv(input_file)
    
    # 1. Rename columns to standard XES format
    print("Renaming columns...")
    df = df.rename(columns={
        'Case ID': 'case:concept:name',
        'Activity': 'concept:name',
        'Timestamp': 'time:timestamp'
    })
    
    # Ensure Case IDs are strings (verifiers hate mixed types)
    df['case:concept:name'] = df['case:concept:name'].astype(str)
    
    # 2. Convert timestamps to proper datetime objects
    print("Parsing timestamps...")
    df['time:timestamp'] = pd.to_datetime(df['time:timestamp'])
    
    # 3. Sort by Case ID, then by Timestamp to ensure logical flow
    print("Sorting data chronologically...")
    df = df.sort_values(by=['case:concept:name', 'time:timestamp'])
    
    # 4. Break timestamp ties by adding cumulative milliseconds
    print("Breaking identical timestamp ties...")
    df['time:timestamp'] = df['time:timestamp'] + pd.to_timedelta(df.groupby('case:concept:name').cumcount(), unit='ms')
    
    # 5. Save to a new CSV (verifiers usually prefer comma separator)
    print("Saving verifier-safe file...")
    df.to_csv(output_file, index=False)
    print(f"Done! Safe file created: {output_file}")

if __name__ == "__main__":

    verifier = LogTraceVerifier()

    #bpic2021_subfolders = ["Training Logs", "Test Logs", "Ground Truth Logs"]
    noise_levels = [0.0, 0.1, 0.2, 0.4, 0.5, 0.6, 0.8, 1.0]

    for noise in noise_levels:
        output_dir = f"output/BPIC2017_Verification/noise_{noise}"
        print(f"\n{'='*70}\n[BATCH] @ noise={noise} -> {output_dir}\n{'='*70}")
        try:
            verifier.verify_batch("data/BPIC2017", output_dir, noise_threshold=noise)
        except Exception as e:
            print(f"[!] FAILED: @ noise={noise}: {e}")

    #for subfolder in bpic2021_subfolders:
    #    input_dir = f"data/BPIC2021/{subfolder}"
    #    safe_name = subfolder.replace(" ", "_")
#
    #    for noise in noise_levels:
    #        output_dir = f"output/BPIC2021_Verification/{safe_name}/noise_{noise}"
    #        print(f"\n{'='*70}\n[BATCH] {subfolder} @ noise={noise} -> {output_dir}\n{'='*70}")
    #        try:
    #            verifier.verify_batch(input_dir, output_dir, noise_threshold=noise)
    #        except Exception as e:
    #            print(f"[!] FAILED: {subfolder} @ noise={noise}: {e}")

    #print("\nAll BPIC2021 batches complete.")