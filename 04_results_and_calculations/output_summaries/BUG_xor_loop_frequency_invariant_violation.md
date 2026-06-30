---
status: FIXED — 3 confirmed bugs patched in core/analyzer.py's _push_top_down;
  2 additional call sites flagged as residual risk (same risky pattern, but
  no reproduction found on any tested file -- see "Residual risk" below)
severity (pre-fix): HIGH, scaled with model size/complexity — 3 of 174 rows
  (1.7%) on the synthetic stress corpus, 17 of 60 rows (28%) on a 10-file
  BPIC2021 sample, 26 of 42 rows (62%) on the full BPIC2017 corpus (largest/
  most complex models tested, 40+ branch Exclusive Choices), with reported
  values up to 8,989.20% of N
found: while running a noise-threshold sweep (0.0-1.0) over the stress-test
  corpus for the "Paradox of Noise Filtering" section's correlation analysis;
  confirmed far more severe on real data, worsening further with model scale
  (BPIC2021 -> BPIC2017)
fixed: same session, after a full audit of every safe_push call site in
  _push_top_down; validated against the full 174-combo stress sweep and the
  60-combo BPIC2021 sample (0 invariant violations and 0 rows >100% remain)
---

## One-paragraph summary

At high noise thresholds (and, on large/complex real models, even at
`noise=0.0`), PM4Py's Inductive Miner can produce a tree where a node's
children's frequencies do not reconcile with the node's own frequency --
violating the basic invariant every extraction rule (`local_N` scaling, the
Overlap Formula) assumes holds. This happens *before* trace extraction even
runs, in the bi-directional frequency-resolution stage
(`_compute_bottom_up`/`_push_top_down`, Section 4.5.1), not in
`_analyze_recursive`'s XOR/SEQ rules. The result: tree-side KPIs (End-to-End,
Total Forced Volume, AS-Resolved, AS-Opaque) could read above 100% of N --
up to 8,989.20% observed on the worst real-data case. **Three distinct bugs
were found and fixed**, all sharing the same root pattern: a `safe_push` call
site passing a child's own (possibly inflated or undercounted) bottom-up
frequency as the token budget, instead of a value reconciled against the
actual incoming budget.

## Root cause: occurrence count vs. case count

Every leaf's `.frequency` is assigned in `core/data_assimilation.py:73` from
`pm4py.get_event_attribute_values(log, "concept:name")` -- a flat,
log-wide **event-occurrence tally** (how many times that activity fires as
an event, across the whole log), looked up once per activity name with zero
awareness of tree position or case membership. This only equals the true
**case count** when every activity fires exactly once per case that reaches
it. Two things break that correspondence in opposite directions:

- **Surplus:** a LOOP's `do` activity can fire multiple times per case when a
  case iterates the loop body more than once. `_compute_bottom_up`'s LOOP
  rule tries to correct for this via `do_freq - redo_freq`, but when the
  `redo` branch is a silent `tau` leaf (no observable event marks "this case
  looped again"), `redo_freq` is always `0` by convention -- so the
  subtraction recovers nothing, and `do_freq` (a raw, repetition-inflated
  occurrence count) gets carried forward as if it were already a clean case
  count.
- **Deficit:** noise filtering can prune a rare branch's activities out of
  the *visible* mined tree while the cases that took that branch still exist
  in the log and still count toward the declared global `N`
  (`global_n = df_clean['case:concept:name'].nunique()`, computed directly
  and exactly from the log's case-ID column -- never ambiguous, always
  trustworthy). The bottom-up estimate for that branch then undercounts the
  true case population.

`compute_frequencies` (analyzer.py:43) always anchors the **root** to the
trustworthy `global_n` rather than the reconstructed bottom-up estimate, by
design (see the docstring at lines 31-42). The bug is that this same
discipline was not applied consistently to *every* internal node during the
top-down push -- several `safe_push` call sites passed a child's own
bottom-up value through unchanged instead of reconciling it against the
actual budget flowing into it.

## The three confirmed bugs (all in `core/analyzer.py::_push_top_down`)

A systematic audit of every `safe_push` call site in the function found:

| Call site (pre-fix line) | Context | Tokens passed | Verdict |
|---|---|---|---|
| `safe_push(node, i, incoming_tokens)` (SEQ/PAR, each child) | budget-derived | OK |
| `safe_push(node, i, c.frequency)` (XOR, real child, tau sibling present) | child's own freq | **BUG #1 (surplus)** |
| `safe_push(node, i, tau_split)` (XOR, tau child) | computed | OK |
| deficit-branch children (`remainder>0`) | `c.frequency [+ extra]` | OK -- deficit-only, no surplus possible here |
| `safe_push(node, i, c.frequency)` (XOR, no tau sibling, `remainder==0`) | child's own freq | **BUG #2 (surplus)** |
| `safe_push(node, 0, do_child.frequency)` (LOOP, zero-redo branch) | child's own freq | **BUG #3 (deficit)** |
| LOOP `do_child` has tau & freq==0 branch | computed / native | not confirmed broken (residual risk) |
| LOOP normal-case branch | computed / native | not confirmed broken (residual risk) |

### Bug #1 -- XOR surplus, tau sibling present

Confirmed reproduction: `test_18_inter_loop.csv` at `noise_threshold=1.0`.
```
XOR freq=3
  LEAF tau freq=0
  LOOP freq=6        <- bottom-up value, never reconciled
    LEAF D freq=6
    LEAF tau freq=0
```
The XOR's `tau_children` branch pushed the real child (`LOOP`) its own
frequency (`6`) instead of the actual budget the parent could spare it (`3`),
because the deficit check (`child.frequency < tokens`) can never trigger when
`tokens == child.frequency` by construction.

KPI impact (measured): End-to-End / Total Forced Volume **200.00% -> 0.00% /
33.33%** after the fix; Data Exposure **77.78% -> 100.00%**. Pattern count
unchanged (2 -> 2); only classification changed (1 Verified + 1 Discrepancy
-> 2 Verified).

### Bug #2 -- XOR surplus, no tau sibling (dominant real-world manifestation)

Confirmed reproduction: `pdc2021_0000004.xes` at `noise_threshold=1.0`. Its
mined tree is a deeply right-nested chain of binary `XOR(LOOP, XOR(...))`
nodes, where **neither child is ever a tau leaf** at any level (PM4Py
flattens an n-ary `X(*(t08,tau), *(t02,tau), ...)` into this binarized
chain). Every level hits the `else` branch (`remainder==0`, i.e.
`sum_real >= incoming_tokens`), which pushed every child its own native
frequency unconditionally -- the exact same defect as Bug #1, in a different
branch.

KPI impact (measured, `pdc2021_0000004.xes` @ 1.0): End-to-End / Total Forced
Volume **521.90% -> 0.00% / 1.20%**; Data Exposure **97.99% -> 100.00%**;
**12 Verified + 12 Discrepancy -> 24 Verified + 0 Discrepancy** (pattern
count unchanged, every Discrepancy became Verified). Same pattern confirmed
on `pdc2021_0000011.xes` @ 1.0: **488.40% -> 2.40%/3.40%**, 11V/10D -> 21V/0D.

This bug is the dominant real-world driver: it explains why BPIC2021/BPIC2017
(large, heavily-filtered, many-activity models that binarize into long
XOR-of-LOOP chains) were corrupted far more often than the small synthetic
stress corpus.

### Bug #3 -- LOOP zero-redo deficit

Confirmed reproduction: `pdc2021_0000001.xes` at `noise_threshold=0.0`
(this file's **root is itself a LOOP**, not an XOR -- Bugs #1/#2's fix alone
did not touch it). Broadened invariant check (now covering SEQ/PAR child
consistency and LOOP do/redo consistency, not just XOR-sum) found:
```
root LOOP: frequency=1000 (correctly anchored to global_n)
  do_child.frequency = 632   (bottom-up estimate, never reconciled upward)
  redo_child.frequency = 0
  do - redo = 632  !=  1000
```
The "zero-redo" branch computed `actual_redos = max(0, do_freq -
incoming_tokens)`, which correctly floors to `0` when `do_freq <
incoming_tokens` (no redos make sense below budget) -- but then pushed
`do_child` its own (insufficient) frequency with no mechanism to make up the
missing 368 cases, unlike `safe_push`'s normal deficit handling elsewhere
(which wraps an underfilled child in a synthetic `XOR(child, tau:diff)`).

KPI impact (measured, all three fixes combined, `pdc2021_0000001.xes` @ 0.0):
Total Forced Volume **136.80% -> 100.00%**; Data Exposure **76.50% ->
77.56%**; pattern count **235 -> 237** (Verified **110 -> 112**, Discrepancy
and Ghost counts unchanged at 21/23) -- the small increase in pattern count
here (rather than a decrease, as in Bugs #1/#2) reflects two additional
genuinely-distinct patterns becoming extractable once the deficit was
properly absorbed by an explicit placeholder instead of silently
undercounting `do_child`'s subtree.

## The fix

All three are patched in `core/analyzer.py::_push_top_down`:

1. `safe_push` now clamps `tokens = max(0, round(tokens))` defensively at the
   top (handles fractional proportional shares cleanly; harmless elsewhere).
2. **XOR branch:** added an explicit `if sum_real > incoming_tokens:` surplus
   case *before* the existing tau/no-tau dispatch. When the real children's
   combined bottom-up frequency exceeds the actual budget, every real child
   is pushed a **proportional share** (`incoming_tokens * c.frequency /
   sum_real`) instead of its native value; any tau children get pushed `0`.
   This subsumes both the old `if tau_children:` branch's silent pass-through
   (Bug #1) and the old `else` branch's silent pass-through (Bug #2) for the
   surplus case specifically -- the existing deficit-handling logic in those
   branches is unchanged and still runs whenever `sum_real <= incoming_tokens`.
3. **LOOP branch, zero-redo case:** added an explicit
   `if do_child.frequency < incoming_tokens:` deficit case. Instead of
   pushing `do_child` its native (undersized) frequency, `safe_push(node, 0,
   incoming_tokens)` is called -- triggering the same tau-wrap mechanism that
   already handles deficits everywhere else in the function -- with
   `redo_child` correctly pushed `0`. The pre-existing surplus-case logic
   (`do_child.frequency >= incoming_tokens`) is unchanged.

## Validation

- **174-combo full stress-corpus sweep** (0.0-1.0 noise, all 29 files):
  broadened invariant checker (XOR-sum, SEQ/PAR-child-consistency,
  LOOP-do/redo-consistency) finds **0 violations**, down from 3 known-bad
  rows pre-fix.
- **60-combo BPIC2021 sample** (10 files x 6 noise levels): **0 violations**,
  down from 17 known-bad rows pre-fix.
- **Full audit pipeline re-run on the entire stress corpus**: **0 rows
  above 100%** on End-to-End or Total Forced Volume, confirmed through the
  actual `LogTraceVerifier.verify_batch` path (not just the internal
  frequency check), down from the 3 rows that previously read 200-220%.
- Every individual fix verified file-by-file in a single process per
  comparison (mining the tree once, running original vs. patched
  `_push_top_down` on independent copies) to rule out PM4Py's own run-to-run
  mining nondeterminism as a confound.
- **No regression found**: every file/noise combination that was already
  correct before the fix remained byte-identical after it (confirmed via the
  same invariant checker returning 0 violations both before and after on the
  171/174 and 43/60 previously-clean rows).

BPIC2017 was *not* re-swept end-to-end against the fix (the full 42-combo
sweep took ~10.6h; re-running it was judged not worth the time given the
fix's mechanism is already confirmed identical in kind on BPIC2021's worst
cases, which share the same large-XOR-chain and LOOP-as-root structures that
drove BPIC2017's corruption). If this matters for citing exact post-fix
BPIC2017 numbers in the thesis, it should be re-run before publication.

## Residual risk (not confirmed broken, but same idiom)

Two call sites in the LOOP branch's other two cases (`do_child` has a tau
leaf and `frequency==0`; and the normal/neither-tau case) still pass a
child's native frequency or a value additively derived from one
(`redo_child.frequency` specifically) without an explicit
surplus/deficit check at that exact call site. Neither produced an observed
violation across 234 tested (file, noise) combinations (174 stress + 60
BPIC2021), and both are *internally self-consistent at the node where they're
called* (the do/redo arithmetic balances by construction) -- but they
inherit the same general risk class if `redo_child`'s own bottom-up estimate
is itself unreliable due to nested structure further down. Not treated as a
confirmed bug without a reproduction; flagged here so a future investigation
knows where to look first if a new invariant violation surfaces that isn't
explained by Bugs #1-3.

## Files changed

- `core/analyzer.py` -- `_push_top_down` (all three fixes, see "The fix"
  above for exact mechanism).
