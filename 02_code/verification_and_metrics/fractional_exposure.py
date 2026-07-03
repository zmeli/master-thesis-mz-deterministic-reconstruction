"""
Fractional (partial-credit) companion to the binary Tree Exposure metric.

Tree Exposure only credits a case if the engine pins down a single, root-spanning Full
pattern for it. Any case that only gets a Prefix, a Suffix, or an Activity Set that the
engine can't stitch end-to-end (e.g. because it sits inside a degenerate root LOOP, as in
pdc2021_0000004 -- see the hand sanity-check) scores exactly 0, even if 90% of its activity
content is actually known. This script credits *how much* of each case's expected length is
pinned down, instead of all-or-nothing.

Three variants:

  - Max  : denominator = baseline structural length (every loop treated as one do-pass,
           no repeats) + the single LARGEST individual loop's own max-iteration extra
           length found anywhere in the tree, added once.
           Earlier attempt multiplied every nested loop's (1+max_iterations) factor
           together recursively, which blew up to absurd lengths (1935 "events" for a
           ~1000-case log) because a loop's redo budget is a one-time global total, not
           a per-outer-iteration allowance -- nesting two loops doesn't mean both maxes
           are simultaneously achievable. Taking only the single biggest contributor
           avoids that double-spending of the same global budget.
  - Avg  : every loop's iterations smoothed across its entire local population
           (avg_iterations = f(redo)/local_N). Recursion-safe: avg_iterations is always
           a small fraction (<=1 typically), so nested (1+avg_iterations) factors don't
           compound explosively the way (1+max_iterations) did.
  - Mean : NOT a percentage. Reports the average number of concrete, real (non-tau)
           events known per case, in absolute terms. An earlier version of this variant
           (Full bucket only, no residual credit) turned out to be numerically identical
           to TreeExposure_existing in every sampled file -- confirmed empirically -- so
           it carried no new information. This redefinition answers a genuinely
           different question than Max/Avg's relative percentages: those tell you what
           FRACTION of a (worst-case / typical) case is known, which hides the fact that
           an 80%-relative-exposure file with 5 expected events per case leaks far less
           actual content than a 40%-relative-exposure file with 50 expected events per
           case (4 known events vs. 20). Mean answers "how many real activities does an
           attacker actually learn per case, on average" -- directly comparable across
           files regardless of their structural complexity, and maps onto the
           privacy-impact framing more directly than a relative percentage.
           Bonus: needs no loop-iteration-length assumption at all (no expected_length_max
           /avg call), since it only sums the actual realized length of fragments the
           engine already found -- so it's immune to the loop-length-estimation ambiguity
           that affects Max and Avg.

Both the numerator and denominator expand opaque "[nested PAR_n]"/"[nested LOOP_n]"
placeholder leaves via the engine's own nested_blocks_registry -- without this, every
abstracted block (which can represent dozens of activities) counts as length 1, which
silently reproduces the same blind spot Tree Exposure already has.

Reuses the live engine (core/analyzer.py, core/data_assimilation.py) on the *same* input
files already used to produce the BPIC2021_Verification reports, rather than re-parsing
rendered markdown -- the per-node frequencies needed for exact length math aren't fully
serialized into the markdown text.
"""
import sys
import re
from pathlib import Path
import csv

sys.path.insert(0, str(Path(__file__).parent))
from core.tree_node import ProcessTreeNode
from core.data_assimilation import DataAssimilation
from core.analyzer import ProcessTreeAnalyzer

TRAINING_DIR = Path("data/BPIC2021/Training Logs")
NESTED_NAME_RE = re.compile(r"^\[nested (.+)\]$")


def is_tau(node: ProcessTreeNode) -> bool:
    return node.operator == 'LEAF' and str(node.name).lower() in {"τ", "tau", "empty_tau", "none"}


def resolve_nested(node: ProcessTreeNode, registry: dict) -> ProcessTreeNode:
    """If `node` is an opaque '[nested X_n]' placeholder leaf, swap in its real
    sub-tree from the registry. Leaves real nodes untouched."""
    if node.operator == 'LEAF':
        m = NESTED_NAME_RE.match(str(node.name))
        if m and f"nested {m.group(1)}" in registry:
            return registry[f"nested {m.group(1)}"]
    return node


def baseline_length(node: ProcessTreeNode, registry: dict) -> float:
    """Structural length treating every LOOP as a single do-pass (no repeats),
    expanding opaque nested-block placeholders via the registry."""
    node = resolve_nested(node, registry)
    if node.operator == 'LEAF':
        return 0.0 if is_tau(node) else 1.0
    if node.operator in ('SEQ', 'PAR'):
        return sum(baseline_length(c, registry) for c in node.children)
    if node.operator == 'XOR':
        f0 = node.children[0].frequency
        f1 = node.children[1].frequency
        total = f0 + f1
        if total <= 0:
            return 0.0
        return (f0 * baseline_length(node.children[0], registry) +
                f1 * baseline_length(node.children[1], registry)) / total
    if node.operator == 'LOOP':
        return baseline_length(node.children[0], registry)
    return 0.0


def best_loop_extra(node: ProcessTreeNode, registry: dict) -> float:
    """Largest single loop's own max-iteration extra length found anywhere in this
    subtree (do_len*max_iter + redo_len*max_iter for that one loop, using baseline
    -- i.e. non-compounded -- lengths for its do/redo children)."""
    node = resolve_nested(node, registry)
    if node.operator == 'LEAF':
        return 0.0

    best = 0.0
    for c in node.children:
        best = max(best, best_loop_extra(c, registry))

    if node.operator == 'LOOP' and node.frequency > 0:
        do_node = node.children[0]
        redo_freq = node.children[1].frequency if len(node.children) > 1 else 0
        do_len = baseline_length(do_node, registry)
        redo_len = baseline_length(node.children[1], registry) if len(node.children) > 1 else 0.0
        own_extra = do_len * redo_freq + redo_len * redo_freq
        best = max(best, own_extra)

    return best


def expected_length_max(root_tree: ProcessTreeNode, registry: dict) -> float:
    return baseline_length(root_tree, registry) + best_loop_extra(root_tree, registry)


def expected_length_avg(node: ProcessTreeNode, registry: dict) -> float:
    node = resolve_nested(node, registry)
    if node.operator == 'LEAF':
        return 0.0 if is_tau(node) else 1.0
    if node.operator in ('SEQ', 'PAR'):
        return sum(expected_length_avg(c, registry) for c in node.children)
    if node.operator == 'XOR':
        f0 = node.children[0].frequency
        f1 = node.children[1].frequency
        total = f0 + f1
        if total <= 0:
            return 0.0
        return (f0 * expected_length_avg(node.children[0], registry) +
                f1 * expected_length_avg(node.children[1], registry)) / total
    if node.operator == 'LOOP':
        do_node = node.children[0]
        if node.frequency <= 0:
            return 0.0
        redo_freq = node.children[1].frequency if len(node.children) > 1 else 0
        do_len = expected_length_avg(do_node, registry)
        redo_len = expected_length_avg(node.children[1], registry) if len(node.children) > 1 else 0.0
        avg_iter = redo_freq / node.frequency
        return do_len * (1 + avg_iter) + redo_len * avg_iter
    return 0.0


def expected_length_avg_additive(node: ProcessTreeNode, registry: dict) -> float:
    """Avg-mode length, fixed against multiplicative compounding across many nested
    loops within a single fragment.

    Bug found in practice: plain expected_length_avg() multiplies each LOOP's own
    (1+avg_iter) factor into its parent's, recursively. avg_iter values are typically
    small fractions, so this was assumed safe (Section's earlier reasoning) -- but a
    handful of files with 15-20 LOOP nodes nested within a single resolved fragment
    still blew up (e.g. 1.3^20 ~= 190x), producing Mean_events_per_case outliers in the
    thousands on otherwise unremarkable files.

    Fix: baseline structural length (every loop as one do-pass, no repeats) PLUS the
    ADDITIVE sum of every individual loop's own average-iteration extra (using
    baseline -- non-compounded -- lengths for that loop's own do/redo children). This
    mirrors the Max-mode single-deepest-loop fix's avoidance of multiplicative nesting,
    but sums every loop's typical contribution instead of keeping only the single
    biggest one, since "average" should reflect every loop's typical behavior along the
    path, not just the most extreme one.
    """
    return baseline_length(node, registry) + _sum_avg_loop_extras(node, registry)


def _sum_avg_loop_extras(node: ProcessTreeNode, registry: dict) -> float:
    node = resolve_nested(node, registry)
    if node.operator == 'LEAF':
        return 0.0
    if node.operator == 'LOOP' and node.frequency <= 0:

        return 0.0
    total = sum(_sum_avg_loop_extras(c, registry) for c in node.children)
    if node.operator == 'LOOP':
        do_node = node.children[0]
        redo_freq = node.children[1].frequency if len(node.children) > 1 else 0
        do_len = baseline_length(do_node, registry)
        redo_len = baseline_length(node.children[1], registry) if len(node.children) > 1 else 0.0
        avg_iter = redo_freq / node.frequency
        total += do_len * avg_iter + redo_len * avg_iter
    return total


def pattern_length(node: ProcessTreeNode, registry: dict) -> float:
    """Number of real (non-tau) leaf events represented by an already-extracted
    ST/AS fragment, expanding opaque nested-block placeholders via the registry
    (using the additive, non-compounding avg-mode length for any loop found inside
    an expanded block -- see expected_length_avg_additive -- since this is describing
    a concrete, already-realized occurrence rather than a worst-case bound, and must
    stay immune to the multiplicative-nesting blowup that affects naive avg-mode)."""
    node = resolve_nested(node, registry)
    if node.operator == 'LEAF':
        return 0.0 if is_tau(node) else 1.0
    if node.operator == 'LOOP':
        return expected_length_avg_additive(node, registry)
    if node.operator == 'XOR':

        f0 = node.children[0].frequency
        f1 = node.children[1].frequency
        total = f0 + f1
        if total <= 0:
            return 0.0
        return (f0 * pattern_length(node.children[0], registry) +
                f1 * pattern_length(node.children[1], registry)) / total
    return sum(pattern_length(c, registry) for c in node.children)


def has_real_content(node: ProcessTreeNode, registry: dict) -> bool:
    """False iff `node` reduces entirely to tau (no real, observable activity
    anywhere in it) -- e.g. the placeholder LEAF "tau" the engine's XOR rule
    injects so a silent branch's case volume survives bookkeeping (see
    BUG_tau_xor_dissolution.md), or any chain that dissolves to nothing else.
    Such a fragment conveys zero reconstructable content -- an attacker learns
    nothing from "this case took a branch that produced no event" -- so it must
    not earn credit in any exposure-style KPI (Tree Exposure, Data Exposure,
    Max/Avg/Mean), even though the engine is correct to track its case volume
    internally for frequency conservation."""
    return pattern_length(node, registry) > 0


def signature(node: ProcessTreeNode, freq: int) -> str:
    return f"{node.get_atomic_representation()}|{freq}"


def extract_nested_refs(node: ProcessTreeNode) -> set:
    """Recursively collects every '[nested X]' placeholder leaf name found anywhere
    in `node`'s subtree. Pure structural check -- doesn't trust `ttype`, since the
    SEQ rule's lazy_cross_multiply() hardcodes merged chains to "ST" even when one of
    the stitched components is itself an opaque AS block (confirmed in practice:
    test_20_loopDouble's only full-bucket entry is tagged "ST" despite containing
    "[nested PAR_1]"). An entry with any non-empty result here cannot be claimed as
    globally order-known, regardless of its ttype tag."""
    if node.operator == 'LEAF':
        m = NESTED_NAME_RE.match(str(node.name))
        return {f"nested {m.group(1)}"} if m else set()
    out = set()
    for c in node.children:
        out |= extract_nested_refs(c)
    return out


def is_globally_strict(node: ProcessTreeNode) -> bool:
    """True iff `node` contains zero embedded '[nested ...]' placeholders anywhere --
    i.e. its entire order, start to finish, is genuinely known, not just locally
    known within some branch."""
    return len(extract_nested_refs(node)) == 0


def is_block_internally_resolved(block_node: ProcessTreeNode, registry: dict) -> bool:
    """Checks whether an opaque PAR/LOOP block's own content is itself fully
    order-determined, independent of the cross-branch/redo-count ambiguity that made
    the engine treat the block as opaque in the first place.

    PAR: resolved iff every branch, analyzed in isolation, produces a `full` bucket
    that is 100% ST-tagged with zero further nested opacity of its own.
    LOOP: same check, applied only to the 'do' child (index 0) -- the redo child's
    count is the genuine, irreducible ambiguity for a LOOP, not part of this check.
    """
    def child_is_fully_resolved(child: ProcessTreeNode) -> bool:
        if child.frequency <= 0:
            return True
        sub_analyzer = ProcessTreeAnalyzer()
        sub_analyzer.analyze_forced_traces(child, child.frequency)
        full = sub_analyzer.last_root_state["full"]
        all_st = len(full) > 0 and all(ttype.startswith("ST") for _, _, ttype in full)
        return all_st and len(sub_analyzer.nested_blocks_registry) == 0

    if block_node.operator == 'PAR':
        return all(child_is_fully_resolved(c) for c in block_node.children)
    if block_node.operator == 'LOOP':
        return child_is_fully_resolved(block_node.children[0])
    return False


def classify_full_bucket(full_bucket, registry: dict) -> dict:
    """Splits a `full`-bucket's total frequency into three tiers:

      - st_volume: entries with zero embedded opacity (is_globally_strict) -- the
        new, strict Tree Exposure (End-to-End) numerator.
      - as_resolved_volume: entries that reference nested block(s), but every
        referenced block independently resolves (is_block_internally_resolved).
        Further split into as_resolved_par_volume / as_resolved_loop_volume by the
        referenced block(s)' operator -- a resolved PAR's open question is "which
        interleaving order" (an unordered co-occurrence guarantee), structurally
        different from a resolved LOOP's open question ("how many redo iterations",
        a count, not an ordering). An entry referencing a mix of PAR and LOOP blocks
        counts toward neither sub-bucket (rare in practice; weakest-link resolution
        still puts its frequency in as_resolved_volume overall).
      - as_opaque_volume: entries referencing at least one block that does not
        resolve (weakest-link rule: one opaque island disqualifies the whole entry).

    Entries that reduce entirely to tau (`has_real_content` is False -- e.g. the
    placeholder the engine's XOR rule injects so a silent branch's case volume
    survives bookkeeping, see BUG_tau_xor_dissolution.md) are excluded from all
    three buckets: "this case took a branch that produced no event" is not
    reconstructable content, so it earns no credit toward exposure of any kind.
    Consequently st_volume + as_resolved_volume + as_opaque_volume can be
    strictly less than sum(freq for full_bucket) whenever tau-only volume exists
    -- the gap is exactly that excluded tau volume, not a bug.
    """
    st_volume = 0.0
    as_resolved_volume = 0.0
    as_resolved_par_volume = 0.0
    as_resolved_loop_volume = 0.0
    as_opaque_volume = 0.0

    for node, freq, _ in full_bucket:
        if not has_real_content(node, registry):
            continue
        if is_globally_strict(node):
            st_volume += freq
            continue
        refs = extract_nested_refs(node)
        blocks = [registry[r] for r in refs if r in registry]
        if blocks and all(is_block_internally_resolved(b, registry) for b in blocks):
            as_resolved_volume += freq
            block_ops = {b.operator for b in blocks}
            if block_ops == {'PAR'}:
                as_resolved_par_volume += freq
            elif block_ops == {'LOOP'}:
                as_resolved_loop_volume += freq
        else:
            as_opaque_volume += freq

    return {
        "st_volume": st_volume,
        "as_resolved_volume": as_resolved_volume,
        "as_resolved_par_volume": as_resolved_par_volume,
        "as_resolved_loop_volume": as_resolved_loop_volume,
        "as_opaque_volume": as_opaque_volume,
    }


def absolute_exposure_volume(root_tree, final_state, registry) -> dict:
    """
    Mean variant, redefined (the original "Full bucket only" definition degenerated
    into being numerically identical to TreeExposure_existing in every sampled file --
    confirmed empirically, so it carried no new information).

    This reports the average number of concrete, real (non-tau) events known per case,
    in ABSOLUTE terms -- not a percentage of any estimated expected case length. Max and
    Avg both answer "what FRACTION of a (worst-case / typical) case is known," which
    hides a real distinction: a file with 80% relative exposure but only 5 expected
    events per case leaks far less actual content than one with 40% relative exposure
    and 50 expected events per case (4 known events vs. 20). This answers the
    complementary question directly: how many real activities does an attacker actually
    learn per case, on average -- the number that maps onto the privacy-impact
    framing more directly than a relative percentage does.

    A side benefit: unlike Max/Avg, this needs no loop-iteration-length assumption at
    all (no expected_length_max/avg call) -- it only sums the actual realized length of
    fragments the engine already found, so it's immune to the loop-length-estimation
    ambiguity that affects the other two variants.

    Full-bucket entries with zero real content (pure tau, e.g. the silent-branch
    placeholder from BUG_tau_xor_dissolution.md) are excluded from `full_freq_total`
    rather than counted as "fully resolved" -- they fall back into the residual
    population below, the same as any other case the engine doesn't fully resolve,
    so they get a fair shot at Prefix/Suffix credit instead of being silently
    written off as 0-event "known" cases.
    """
    root_n = root_tree.frequency
    if root_n <= 0:
        return {"events_per_case": 0.0}

    full = [(n, f, t) for n, f, t in final_state["full"] if has_real_content(n, registry)]
    full_signatures = {signature(n, f) for n, f, _ in full}
    full_freq_total = sum(f for _, f, _ in full)
    volume = sum(f * pattern_length(n, registry) for n, f, _ in full)

    residual = max(0, root_n - full_freq_total)
    if residual > 0:
        def residual_volume(bucket):
            total_freq, total_events = 0.0, 0.0
            for n, f, _ in bucket:
                if signature(n, f) in full_signatures:
                    continue
                if not has_real_content(n, registry):
                    continue
                total_freq += f
                total_events += f * pattern_length(n, registry)
            return total_freq, total_events

        prefix_freq, prefix_events = residual_volume(final_state["prefix"])
        suffix_freq, suffix_events = residual_volume(final_state["suffix"])
        chosen_freq, chosen_events = (prefix_freq, prefix_events) if prefix_events >= suffix_events else (suffix_freq, suffix_events)
        if chosen_freq > residual and chosen_freq > 0:
            chosen_events *= residual / chosen_freq  # don't credit more residual cases than actually exist
        volume += chosen_events

    return {"events_per_case": volume / root_n}


def fractional_exposure(root_tree, final_state, registry, expected_len: float, include_residual: bool) -> dict:
    """
    Aggregate-level approximation (documented limitation: case identity isn't tracked by
    the engine, so this credits coverage in aggregate rather than per individual case):

      1. Every Full-bucket entry contributes its full freq, UNCONDITIONALLY (a case in
         Full is 100% known by definition -- this term alone reproduces the existing
         Tree Exposure numerator exactly, so the fractional score can never fall below
         it). Pattern length is irrelevant here: a fully-resolved case that happens to
         be longer than the population's average expected length is still fully known,
         not "more than 100% known" -- there is nothing to ratio against.
      2. If include_residual: for the remaining (N - full_freq_total) cases, take
         whichever of the remaining (non-full-duplicate) Prefix/Suffix entries
         contributes the larger total length-ratio credit (freq * length/expected_len,
         capped at 1.0 per unit), as the best-known fragment representative of that
         residual population. This is where genuine *partial* credit applies, since
         these cases are NOT fully resolved and a length/expected_len ratio is the
         only thing being estimated. (Mean variant skips this -- Full chains only.)
      3. Total is capped at root_n so the result can never exceed 100%.

      4. A Full-bucket entry with zero real content (pure tau -- see
         BUG_tau_xor_dissolution.md) does not qualify for the unconditional
         Full-bucket credit in step 1: "this case took a branch that produced
         no event" is not known case content, so it falls back into the
         residual population and is only credited (if at all) via a genuine
         Prefix/Suffix fragment, same as any other unresolved case.
    """
    root_n = root_tree.frequency
    if root_n <= 0 or expected_len <= 0:
        return {"fractional_pct": 0.0, "expected_len": expected_len}

    full = [(n, f, t) for n, f, t in final_state["full"] if has_real_content(n, registry)]
    full_signatures = {signature(n, f) for n, f, _ in full}
    full_freq_total = sum(f for _, f, _ in full)
    numerator = full_freq_total

    if include_residual:
        residual = max(0, root_n - full_freq_total)
        if residual > 0:
            def residual_credit(bucket):
                total = 0.0
                for n, f, _ in bucket:
                    if signature(n, f) in full_signatures:
                        continue
                    if not has_real_content(n, registry):
                        continue
                    ratio = min(pattern_length(n, registry) / expected_len, 1.0)
                    total += f * ratio
                return total

            numerator += min(max(residual_credit(final_state["prefix"]), residual_credit(final_state["suffix"])), residual)

    numerator = min(numerator, root_n)
    pct = (numerator / root_n) * 100
    return {"fractional_pct": pct, "expected_len": expected_len}


def fragment_strict_exposure(root_tree, final_state, registry, expected_len: float, min_length: float = 0.0) -> dict:
    """
    Tree Exposure (Fragment-Level Strict): generalizes the strict, zero-opacity
    standard down to the fragment level, the same way fractional_exposure() (Max/Avg)
    generalizes Tree Exposure's binary Full-or-nothing into partial credit -- except
    every candidate fragment here must itself be globally strict (is_globally_strict),
    so nothing AS-tagged or opacity-containing is ever eligible, regardless of length.

    Candidates are pulled ONLY from `full`, `prefix`, `suffix` -- the root-level
    partition. `all`'s internally-tagged "(in PAR_x)"/"(in LOOP_x)" sub-fragments are
    deliberately excluded, even when individually deterministic (e.g. the lone forced
    `A` leaf inside a PAR branch): being "in a PAR" means the fragment's position is
    only known relative to its own branch, not globally, so it does not qualify as
    something we can say will appear in a specific, fully knowable position -- only
    fragments outside any opaque PAR/LOOP wrapper qualify, whether they span the whole
    case or just part of it. (An earlier version of this function credited `all`'s
    internal fragments too; removed because it let fragment-level credit saturate to
    100% even on cases with zero End-to-End exposure, which overstated what the metric
    was supposed to mean.)

    `min_length` filters out fragments shorter than that many real activities -- a
    length-1 fragment (a lone leaf) has no internal order to demonstrate, so crediting
    it overstates a "fixed order" claim. Pass min_length=2.0 for the "at least 2
    activities long, genuinely order-fixed" variant; min_length=0.0 (default) credits
    every globally-strict fragment with at least one real activity (pure tau never
    qualifies, regardless of min_length -- see `qualifies()` below).
    """
    root_n = root_tree.frequency
    if root_n <= 0 or expected_len <= 0:
        return {"fragment_strict_pct": 0.0}

    def qualifies(n):
        # max(min_length, 1.0): pure tau (pattern_length == 0) never qualifies
        # regardless of min_length -- "no real content" is a structural floor,
        # not a configurable threshold (see has_real_content's docstring).
        return is_globally_strict(n) and pattern_length(n, registry) >= max(min_length, 1.0)

    strict_full = [(n, f, t) for n, f, t in final_state["full"] if qualifies(n)]
    full_signatures = {signature(n, f) for n, f, _ in strict_full}
    full_freq_total = sum(f for _, f, _ in strict_full)
    numerator = full_freq_total

    residual = max(0, root_n - full_freq_total)
    if residual > 0:
        def residual_credit(bucket):
            total = 0.0
            for n, f, _ in bucket:
                if not qualifies(n):
                    continue
                if signature(n, f) in full_signatures:
                    continue
                ratio = min(pattern_length(n, registry) / expected_len, 1.0)
                total += f * ratio
            return total

        candidates = [
            residual_credit(final_state["prefix"]),
            residual_credit(final_state["suffix"]),
        ]
        numerator += min(max(candidates), residual)

    numerator = min(numerator, root_n)
    return {"fragment_strict_pct": (numerator / root_n) * 100}


def local_strict_exposure(root_tree, final_state, registry, expected_len: float, min_length: float = 0.0) -> dict:
    """
    Tree Exposure (Local-Strict): generalizes Fragment-Level one step further by also
    crediting individually globally-strict sub-fragments found *inside* an opaque
    PAR/LOOP block -- the "(in PAR_x)"/"(in LOOP_x)" tagged entries that `all` already
    carries but that `fragment_strict_exposure` deliberately ignores, since their
    position is only known relative to their own branch, not globally.

    `min_length` filters out fragments shorter than that many real activities --
    a length-1 fragment (a lone leaf) has no internal order to demonstrate, so
    crediting it overstates what the metric is meant to mean. Pass min_length=2.0
    for the "at least 2 activities long" variant; min_length=0.0 (default) credits
    every qualifying fragment with at least one real activity (pure tau never
    qualifies, regardless of min_length).

    WARNING (must ship with the number): this is deliberately more permissive than
    Fragment-Level and can read close to 100% even on a case that is 0% End-to-End
    and entirely AS-Opaque -- a deterministic sub-chain inside an unresolved PAR/LOOP
    branch still counts here. An earlier version of fragment_strict_exposure credited
    this same internal content and was pulled back out specifically because it let
    Fragment-Level saturate to 100% on such cases, overstating what was actually
    order-known (see fragment_strict_exposure's docstring). That credit is restored
    here as its own explicitly-labeled, separately-reported KPI instead -- it answers
    "how much of this case's content sits in some deterministic chain, local or
    global", not "how much of this case's order is known".
    """
    root_n = root_tree.frequency
    if root_n <= 0 or expected_len <= 0:
        return {"local_strict_pct": 0.0}

    def qualifies(n):

        return is_globally_strict(n) and pattern_length(n, registry) >= max(min_length, 1.0)

    strict_full = [(n, f, t) for n, f, t in final_state["full"] if qualifies(n)]
    full_signatures = {signature(n, f) for n, f, _ in strict_full}
    full_freq_total = sum(f for _, f, _ in strict_full)
    numerator = full_freq_total

    residual = max(0, root_n - full_freq_total)
    if residual > 0:
        def residual_credit(bucket):
            total = 0.0
            for n, f, _ in bucket:
                if not qualifies(n):
                    continue
                if signature(n, f) in full_signatures:
                    continue
                ratio = min(pattern_length(n, registry) / expected_len, 1.0)
                total += f * ratio
            return total

        candidates = [
            residual_credit(final_state["prefix"]),
            residual_credit(final_state["suffix"]),
        ]
        numerator += min(max(candidates), residual)


    seen_internal = set()
    internal_credit = 0.0
    for n, f, t in final_state.get("all", []):
        if "(in " not in t:
            continue
        if not qualifies(n):
            continue
        sig = signature(n, f)
        if sig in seen_internal:
            continue
        seen_internal.add(sig)
        ratio = min(pattern_length(n, registry) / expected_len, 1.0)
        internal_credit += f * ratio
    numerator += internal_credit

    numerator = min(numerator, root_n)
    return {"local_strict_pct": (numerator / root_n) * 100}


def analyze_file(file_path: Path, noise_threshold: float = 0.0) -> dict:
    analyzer = ProcessTreeAnalyzer(max_traces_per_node=10000)
    root_tree = DataAssimilation.assimilate_from_file(str(file_path), analyzer, noise_threshold=noise_threshold)
    analyzer.nested_blocks_registry.clear()
    analyzer._block_counter = 0
    analyzer._block_id_cache = {}
    final_state = analyzer._analyze_recursive(root_tree, root_tree.frequency)
    registry = analyzer.nested_blocks_registry

    root_n = root_tree.frequency
    tree_exposure = (sum(f for _, f, _ in final_state["full"]) / root_n * 100) if root_n > 0 else 0.0

    max_len = expected_length_max(root_tree, registry)
    avg_len = expected_length_avg(root_tree, registry)

    return {
        "file": file_path.name,
        "N": root_n,
        "TreeExposure_existing": tree_exposure,
        **{f"Max_{k}": v for k, v in fractional_exposure(root_tree, final_state, registry, max_len, include_residual=True).items()},
        **{f"Avg_{k}": v for k, v in fractional_exposure(root_tree, final_state, registry, avg_len, include_residual=True).items()},
        **{f"Mean_{k}": v for k, v in absolute_exposure_volume(root_tree, final_state, registry).items()},
    }


def main():
    files = sorted(TRAINING_DIR.glob("*.xes"))
    if not files:
        print(f"No input files found under {TRAINING_DIR}")
        return

    rows = []
    for f in files:
        try:
            rows.append(analyze_file(f))
        except Exception as e:
            print(f"[!] FAILED on {f.name}: {e}")

    out_csv = Path("output/BPIC2021_Verification/fractional_exposure.csv")
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["file", "N", "TreeExposure_existing",
                  "Max_fractional_pct", "Max_expected_len",
                  "Avg_fractional_pct", "Avg_expected_len",
                  "Mean_events_per_case"]
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    print(f"Analyzed {len(rows)} files. Wrote {out_csv}")
    for r in rows:
        print(f"  {r['file']}: Tree={r['TreeExposure_existing']:.2f}%  "
              f"Max={r['Max_fractional_pct']:.2f}%  Avg={r['Avg_fractional_pct']:.2f}%  "
              f"Mean={r['Mean_events_per_case']:.2f} events/case")


if __name__ == "__main__":
    main()
