---
status: FIXED — core/analyzer.py RULE 2 (XOR) and RULE 3 (SEQ) now use the
  Overlap Formula (Section 3.2.2) to determine each child's guaranteed share of
  a requested local_N, instead of proportional scaling. A companion fix in
  fractional_exposure.py's pattern_length() adds the missing XOR case for
  expanding the new opaque [nested XOR_k] blocks this produces. Validated via
  full 29-file suite diff: 7 files changed, all in the expected direction
  (lower End-to-End/Fragment-Level/Mean, higher AS-Opaque -- removing
  overstated certainty, never adding it), zero crashes, zero unexpected shifts
  in Data Exposure/Coverage.
severity: MEDIUM-HIGH — affected any file where a LOOP's zero-redo cohort
  extraction recurses into a do-subtree containing its own further XOR split;
  produced non-integer "predicted frequency" values for literal traces, which
  cannot be correct (a deterministic minimum guarantee about a discrete trace
  must be an integer)
found: user noticed a literal trace's predicted frequency displaying as
  2.545454545454545 in an audit report and asked how that could be correct
---

## One-paragraph summary

The `local_N` proportional-scaling fix introduced earlier in this engine (to
resolve `test_11_nesting.csv`'s >100% End-to-End bug) correctly capped a
cohort's total credited volume, but did so by **assuming** that a smaller
sub-cohort's internal choices are distributed in the same proportion as the
whole population -- a statistical assumption, not a derived guarantee. This
produced confident-looking but mathematically unjustified fractional
"predicted frequencies" for composite patterns (e.g. `2.545454545454545` =
28/11), whenever a LOOP's zero-redo extraction recursed into a do-subtree
containing its own further nested XOR split. The true, overlap-based
guaranteed minimum for that exact pattern was actually **0**, not 2.545 --
the proportional estimate wasn't just imprecise, it was claiming certainty
the mathematics didn't support.

## Where it lived (root cause)

`core/analyzer.py`, RULE 2 (XOR) and RULE 3 (SEQ), in their child-frequency
computation:
```python
scale = (local_N / node.frequency) if node.frequency > 0 else 0.0
l_n = node.children[0].frequency * scale
r_n = node.children[1].frequency * scale
```

## Confirmed reproduction (pre-fix)

On `test_15_loop3.csv`, `LOOP_3` (frequency 9, redo count 2) proves at least 7
of its 9 cases never redo (`zero_redo_freq = 9 - 2 = 7`). Recursing into its
do-subtree with `local_N = 7` (natural frequency 11) and following the chain
of nested XOR/SEQ scaling down to a `τ:4 / E:6` split (natural frequency 10,
itself recursed with a propagated `local_N = 70/11`), the engine reported:
```
[ST (in PAR_2)]  <D, [nested PAR_4], tau>   expected >= 2.545454545454545
```
Manually re-deriving via the Overlap Formula at each level (`max(0, A+B-N)`)
instead of proportional multiplication gives a *true* guaranteed minimum of
**0** for this exact pattern -- the engine cannot actually prove any
zero-redo case took the `τ` branch specifically; it can only prove `τ`
happened 4 times *somewhere* among all 11 do-executions.

## Fix summary

Two coordinated changes:

1. **`core/analyzer.py`, RULE 2 (XOR) and RULE 3 (SEQ):** replaced
   proportional scaling with the Overlap Formula per child:
   `child_n = max(0, child.frequency + local_N - node.frequency)`. Under the
   normal case (`local_N == node.frequency`), this reduces to
   `child_n == child.frequency` exactly, identical to before -- the change
   only has an effect when `local_N` differs from `node.frequency` (the LOOP
   zero-redo path). For SEQ specifically, under its own invariant (both
   children's frequency equal `node.frequency`, since they describe the same
   case population), this is provably a no-op; the real behavior change is
   confined to XOR.
2. **A new problem this surfaces, and how it's handled:** the Overlap
   Formula's two child shares can legitimately sum to *less* than `local_N`.
   That gap is the volume genuinely too ambiguous to assign to either
   specific branch -- the honest counterpart to the old formula's
   overstatement. It must not simply vanish (the same class of bug already
   found and fixed for tau dissolution, `output/BUG_tau_xor_dissolution.md`),
   but it also cannot be claimed as a Strict Trace for either branch. It is
   now registered as an opaque `[nested XOR_k]` block, exactly the same
   mechanism PAR/LOOP already use for their own irreducible uncertainty, so
   every existing structural check (`is_globally_strict`,
   `is_block_internally_resolved`, the auditor's `block_alphabets`/
   `block_patterns`) handles it automatically.
3. **A genuine gap this exposed, fixed separately:**
   `fractional_exposure.py`'s `pattern_length()` had explicit cases for
   `LEAF` and `LOOP` when expanding a registry block, falling through to
   `sum(children)` for everything else. That default is correct for `PAR`
   (every branch executes) but was never previously exercised for `XOR`
   (only `PAR`/`LOOP` were ever registered before this fix) -- summing both
   of an XOR's branches would double-count content that never co-occurs in
   the same case. Added an explicit `XOR` case using the same
   frequency-weighted-average treatment already used by
   `baseline_length()`/`expected_length_avg()` elsewhere in the same file.

## Validation

Full 29-file stress suite diff (`output/_all_metrics_summary.csv`): 7 files
changed, 22 byte-identical, zero crashes. Every change moved in the expected
direction -- removing previously-overstated certainty, never adding new
overstatement:
- `test_11_nesting.csv`: End-to-End 25.0%→**12.5%**, Fragment-Level
  31.9%→19.4%, AS-Opaque 0.0%→**12.5%** (the fractional `K`/`L` entries that
  used to count as ST are now a single clean `AS [nested XOR_4]:1.0`, exactly
  matching the hand-derived overlap calculation).
- `test_15_loop3.csv`: the `2.545454545454545` value is gone entirely;
  Local-Strict (≥2 activities) drops from 2.31%→0.0% (that figure was itself
  a downstream symptom of the same overstatement).
- Five files' Mean Absolute Exposure Volume decreased slightly
  (`test_04_par_xor`, `test_12_skiping`, `test_14_asymTree`, `test_15_loop3`,
  `test_20_loopDouble`, `test_21_wildCards`) -- Mean sums realized ST content,
  so removing falsely-credited fractional ST content correctly lowers it.

Re-checked all 29 files' "all" bucket directly for any remaining
non-integer-valued entries: zero found.

## Reviewed and confirmed safe without further changes

- `baseline_length()`, `expected_length_avg()`, `best_loop_extra()`
  (`fractional_exposure.py`) -- all three already had explicit, correct `XOR`
  handling (frequency-weighted average or max) before this fix, since they
  were written anticipating XOR nodes appearing directly in a tree, not only
  via registry expansion.
- `is_globally_strict()` / `extract_nested_refs()` -- check leaf *names* for
  the `[nested ·]` pattern structurally, never the registry's expanded
  content's operator type, so the new `[nested XOR_k]` leaves are recognized
  correctly with no changes needed.
- `is_block_internally_resolved()` (`fractional_exposure.py`) -- only has
  explicit cases for `PAR`/`LOOP`; an XOR-type block falls through to
  `return False` (always AS-Opaque, never AS-Resolved), which is the
  conceptually correct answer -- "which branch happened" is a fundamentally
  different, more severe kind of uncertainty than PAR's "which interleaving"
  or LOOP's "how many iterations," so it should never be eligible for
  "resolved" status.
- `_generate_valid_patterns()` (`auto_verifier_v2.py`) -- already had a
  correct `XOR` case (returns both branches' patterns as alternatives) before
  this fix, so the verifier already searches for *either* branch's content
  when checking an ambiguous `[nested XOR_k]` block against the raw log.

## Known residual limitation (separate, already-queued bug)

If an ambiguous `[nested XOR_k]` block ends up referenced from inside a
`(in PAR_x)`-tagged composite pattern routed through the *unordered* matcher
(`auto_verifier_v2.py`'s `is_unordered_par` branch), it would hit the same
flat-alphabet-requires-everything bug already documented in
`output/BUG_unordered_par_matcher_optional_content.md` -- that bug is
pre-existing and not something this fix introduces, but this fix's new block
type is one more way it can be triggered. No action needed beyond what's
already queued there.
