---
status: FIXED — core/analyzer.py RULE 2 (XOR) now injects a zero-length
  placeholder for a branch that resolves to nothing observable; a companion fix
  in auto_verifier_v2.py treats a pattern that reduces to pure tau as trivially
  verified instead of asking either matcher to find a literal "tau" token in
  the raw log. Validated via full 29-file suite diff: 7 files changed (all
  within the 10 originally flagged below), 22 byte-identical, zero crashes.
severity: HIGH (was) — affected 10 of 29 stress-test files' Full-bucket
  frequencies, and therefore every downstream metric computed from them
found: while building a worked example for the thesis's "Paradox of Noise
  Filtering" section (Chapter 5.5 / `sec:noise-paradox`)
---

## Fix summary (added after the fact)

Two changes, both confirmed via the full-suite diff:

1. **`core/analyzer.py`, RULE 2 (XOR):** after recursing into both children, if
   either child's resulting state is completely empty (`not l_state["all"]` /
   `not r_state["all"]`) while that child's case volume is nonzero, inject a
   placeholder entry `(LEAF "τ", that_frequency, "ST")` before the union. This
   is exactly what SEQ's existing tau-absorption check does conceptually, but
   adapted for XOR's disjoint-population semantics (SEQ can safely collapse to
   "return the other side" because both children share the same case
   population; XOR's children are different, non-overlapping case populations,
   so the branch's volume has to survive as its own entry rather than being
   discarded or folded into the sibling).
2. **`auto_verifier_v2.py`, main per-pattern loop:** a pattern that reduces to
   pure tau (`valid_permutations == [[]]`) is now short-circuited to
   "trivially VERIFIED" before either matcher runs, since neither matcher can
   meaningfully search the raw log for a literal "tau" token (tau is never
   recorded) -- without this, the new placeholder from fix (1) surfaced as a
   spurious Ghost Pattern on every affected file.

**Impact on the 7 files that changed:** most significant were
`test_16_tauabiyss.csv` (End-to-End and Total Forced Volume both 25%→100%) and
`test_21_wildCards.csv` (End-to-End 0%→15%, Total Forced 45%→70%, AS-Resolved
45%→55%). Two files moved slightly in the unexpected direction
(`test_12_skiping.csv` Data Exposure 92.98%→92.06%; `test_20_loopDouble.csv`
88.17%→87.38%) -- investigated separately and found to be a different,
pre-existing bug surfaced by this fix rather than caused by it; see
`output/BUG_unordered_par_matcher_optional_content.md`.

# Bug: XOR rule silently drops case volume when one branch is a silent (tau) leaf

## One-paragraph summary

In `core/analyzer.py`'s recursive trace-extraction engine, an Exclusive Choice
(`XOR`) between a silent (`tau`/`τ`) branch and a real branch loses track of every
case that took the silent branch. The `LEAF` rule returns a completely empty
state for a tau leaf (by design — see below), and the `XOR` rule combines its two
children's buckets by plain list concatenation (`l_state[bucket] + r_state[bucket]`)
with no mechanism to represent "N cases took this branch and produced nothing."
The result: the Full bucket this tree produces under-reports the true case count by
exactly the tau branch's frequency, on every file where this structure occurs.

## Where it lives

`core/analyzer.py`, `_analyze_recursive()`:

- **`RULE 1: LEAF`** (around line 197-205): a tau leaf returns `state` unchanged —
  i.e. completely empty (`{"all": [], "full": [], "prefix": [], "suffix": []}`).
  This is *correct* on its own: a tau leaf truly contributes zero observable
  events, so it shouldn't add anything to a sequence's content.
- **`RULE 2: XOR`** (around line 207-230): combines `l_state` and `r_state` via
  plain concatenation per bucket:
  ```python
  state["all"]    = list(itertools.islice(l_state["all"]    + r_state["all"],    self.max_traces))
  state["full"]   = list(itertools.islice(l_state["full"]   + r_state["full"],   self.max_traces))
  state["prefix"] = list(itertools.islice(l_state["prefix"] + r_state["prefix"], self.max_traces))
  state["suffix"] = list(itertools.islice(l_state["suffix"] + r_state["suffix"], self.max_traces))
  ```
  If one child's state is empty (the tau branch), the union is just the other
  child's state — **the tau branch's frequency is nowhere in the result.**

Contrast this with **`RULE 3: SEQ`** (around line 232-244), which has an explicit
tau-absorption check:
```python
if not l_state["all"]: return r_state
if not r_state["all"]: return l_state
```
This correctly handles `SEQ(tau, X)` / `SEQ(X, tau)` — but it only works because in
a `SEQ`, both children represent the *same* case population (every case passes
through both children), so "one side is empty" means "the whole sequence reduces to
the other side," which is a safe, lossless simplification. **`XOR` has no analogous
rule, and structurally can't reuse the same fix**, because in an `XOR` the two
children represent *different, disjoint* case populations (this case took branch A,
that case took branch B) — losing one side's bucket loses real cases, not a
redundant simplification.

## Minimal reproduction

Tree:
```
T = →(A, C, ×(τ:9, D:1), E),   N = 10
```
9 of 10 cases skip `D` (take the tau branch); 1 case includes it.

```python
import sys; sys.path.insert(0, '.')
from core.data_assimilation import DataAssimilation
from core.analyzer import ProcessTreeAnalyzer
from fractional_exposure import classify_full_bucket

analyzer = ProcessTreeAnalyzer(max_traces_per_node=10000)
# build/assimilate a log matching T above (9 cases <A,C,E>, 1 case <A,C,D,E>)
# e.g. via DataAssimilation.assimilate_from_file on a small CSV, noise_threshold=0.0
root_tree = DataAssimilation.assimilate_from_file('path/to/log.csv', analyzer, noise_threshold=0.0, compute_metrics=False)
analyzer.analyze_forced_traces(root_tree, root_tree.frequency)
full = analyzer.last_root_full
print(sum(f for _, f, _ in full))  # prints 1.0, should print 10.0
```

**Expected** Full bucket (a correct, lossless partition of all 10 cases):
```
F_expected = { <A,C,E>:9,  <A,C,D,E>:1 },   sum f = 10
```

**Actual** Full bucket (confirmed by running the above):
```
F_found = { <A,C,D,E>:1 },   sum f = 1
```

The 9 cases that skipped `D` have no representation anywhere in the bucket — not
merged into another entry, not present at all.

## Confirmed impact on the existing stress-test corpus

A structural scan (walk every mined tree, flag any `XOR` node where exactly one
child is a tau leaf and the other is not) found **this structure present in 10 of
the 29 files in `data/stress_tests/`**, at `noise_threshold=0.0` (so this is not a
noise-filtering-specific issue — it fires on perfectly clean, zero-noise logs too):

```
test_12_skiping.csv
test_13_deepLoop.csv
test_14_asymTree.csv
test_15_loop3.csv
test_16_tauabiyss.csv
test_17_spagetti.csv
test_18_inter_loop.csv
test_19_phantomBranch.csv
test_20_loopDouble.csv
test_21_wildCards.csv
```

This means **every metric reported for these 10 files in
`output/_all_metrics_summary.csv` and `output/tree_exposure_metrics_overview.md`
should be treated as suspect** until this is fixed and the suite is re-run. Every
metric downstream of `analyzer.last_root_full` / `final_state["all"]` is affected:
End-to-End, Total Forced Volume, AS-Resolved, AS-Opaque (all in
`fractional_exposure.py`'s `classify_full_bucket()`), Fragment-Level, Local-Strict,
Mean Absolute Exposure Volume, Data Exposure (all variants), and Data Coverage (all
variants, in `auto_verifier_v2.py`) — because all of them are computed from the
same `last_root_full` / `last_root_state` / `engine_traces` objects this bug
corrupts.

(Caveat on the scan script: it flags every `XOR(tau-leaf, anything)` structurally,
including cases nested deep inside an already-opaque PAR/LOOP block where the
specific frequency loss might be absorbed without changing the *final reported*
metric. Treat the file list as "needs re-checking after the fix," not as "every
number on these 10 files is definitely wrong by a known amount" — some may turn out
unaffected in their final percentages even though the intermediate bucket is
short, depending on whether that bucket ever reaches the root unmodified.)

## Why this blocks Section 5.5 (Paradox of Noise Filtering)

Noise filtering's typical effect on a mined model is exactly this shape: it prunes
a rare alternative down to "doesn't happen," which PM4Py represents as
`XOR(tau, rare_activity)`. Any live, mined before/after noise-threshold example
would necessarily run through this exact structure — so right now, a live example
would be reporting numbers already corrupted by this bug, indistinguishable from
the actual noise-filtering effect the section is trying to demonstrate. The thesis
text currently uses a hand-checked, non-mined illustration instead, with this
limitation noted explicitly in-line and a TODO to replace it once fixed.

## Suggested fix directions (not yet attempted)

The core problem: a tau leaf needs to represent "this branch happened, for N cases,
and contributed zero events" — not "this branch doesn't exist." Some options:

1. **Make the tau-LEAF rule return a non-empty placeholder entry** instead of a
   truly empty state — e.g. `(empty_seq_node, local_N, "ST")` with a zero-length
   node — so it survives XOR's union and downstream SEQ cross-multiplication
   treats it as "the identity element" (contributes 0 to length, but its frequency
   still participates in overlap arithmetic). This would need care in
   `lazy_cross_multiply`'s `overlap = (l_f + r_f) - local_N` formula and in
   `pattern_length()` (`fractional_exposure.py`) to make sure a zero-length node
   doesn't break length-based calculations elsewhere.
2. **Special-case XOR with one tau child** explicitly (mirroring SEQ's
   `if not l_state["all"]: return r_state` pattern, but adapted for XOR's
   disjoint-population semantics): if one child is tau, the OTHER child's bucket
   entries need their frequency left as-is (only that many cases took the real
   branch), but something must still represent the tau-branch's N cases at the
   point where THIS XOR's result gets consumed by its parent SEQ — likely meaning
   the parent SEQ needs awareness that this child's "missing" population is valid
   and should pass through unmodified, similar to a `prefix`/`suffix` partial
   credit rather than vanishing.
3. **Audit every other place `_is_tau_node` triggers an early return** in
   `_analyze_recursive` (PAR and LOOP rules also have tau-related special cases —
   re-check those for the same class of bug, even though they weren't directly
   implicated by the scan above).

Whichever approach is chosen, the **acceptance test** should be: the minimal
reproduction above must yield `sum(f for _, f, _ in last_root_full) == 10` (not 1),
with both `<A,C,E>:9` and `<A,C,D,E>:1` present as separate Full-bucket entries.

## How to validate a fix

1. Confirm the minimal reproduction above now yields the expected Full bucket.
2. Re-run the full stress suite and diff against the current baseline:
   ```
   cp output/_all_metrics_summary.csv output/_all_metrics_summary_PRE_TAU_FIX.csv
   py -3.12 output/_run_all_metrics.py
   ```
   then diff the two CSVs (see the diff pattern used for the two earlier bug fixes
   in this codebase — `core/analyzer.py`'s `local_N` scaling fix and
   `auto_verifier_v2.py`'s fragment-matcher repeat-counting fix — both validated
   this way: confirm the 10 flagged files change, and the other 19 do **not**
   change at all, byte-for-byte).
3. Re-run the structural tau/XOR scan (the Python snippet under "Confirmed impact"
   above, generalized to all 29 files) — it should still correctly *detect* the
   same 10 files (the scan just looks at tree shape, unaffected by the fix), but
   their reported metrics should now reflect the corrected, lossless Full bucket.
4. Once validated, update `output/tree_exposure_metrics_overview.md` and the
   relevant thesis chapter sections (5.2/5.3/5.4's worked examples — check whether
   any of the 10 affected files are cited there with now-stale numbers) the same
   way the two earlier bug fixes were documented there (a `> **Bug fixed:** ...`
   callout with before/after numbers and a full-suite-diff confirmation).

## Related, already-fixed bugs in the same area (for pattern reference)

Two other bugs were found and fixed earlier in this same engine/verifier, both
documented in `output/tree_exposure_metrics_overview.md` with the same
"diagnose → fix → validate via full-suite diff" structure used above:

1. **XOR/SEQ ignoring `local_N`** (`core/analyzer.py`, the `scale = local_N /
   node.frequency` lines visible above RULE 2 and RULE 3) — fixed when it was
   found that `test_11_nesting.csv` reported End-to-End/Total Forced Volume above
   100%, because the LOOP zero-redo path's recursion into a complex do-child
   wasn't being scaled to the smaller `zero_redo_freq` it was called with.
2. **Fragment scanner collapsing repeated nested-block instances into one match**
   (`auto_verifier_v2.py`, `_count_fragment_matches`) — fixed when
   `test_15_loop3.csv` showed Data Exposure below 100% even at zero noise; the
   scanner's greedy single-token absorption was swallowing multiple back-to-back
   repetitions of a looping nested block as a single counted match.

This tau/XOR bug is a third, structurally distinct issue in the same family
(silent/degenerate-case handling during recursive extraction) — worth checking
whether a similar audit of *all* tau-related and degenerate-frequency special
cases across the engine (not just XOR) is warranted once this one is fixed.
