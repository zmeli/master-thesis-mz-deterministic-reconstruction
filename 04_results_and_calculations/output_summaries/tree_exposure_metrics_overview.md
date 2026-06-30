# Tree Exposure Metrics & Alternatives — Full Reference

Grounded against all 29 files in `data/stress_tests/` (28 synthetic stress trees +
`sample_log.csv`), not just `test_27_par_loop_noxor.csv`. Raw per-file numbers are
in `output/_all_metrics_summary.csv`; aggregate ranges are quoted inline below.
All percentages are normalized against `N` = `root_tree.frequency` (the root-level
case count the engine actually used).

Notation: $\mathcal{F}$ = the engine's Full-state partition (Strict Traces +
Activity Sets). $\mathcal{F}_{\text{ST}}$ = the globally-strict subset of
$\mathcal{F}$ (zero embedded `[nested ·]` placeholders anywhere). A fragment is
"globally strict" iff `is_globally_strict()` returns true for it — structurally
checked, not by trusting the `[ST]`/`[AS]` tag.

---

## 1. Tree Exposure (Strict, End-to-End)

**Looking for:** cases whose *entire* order, start to finish, is known with zero
ambiguity anywhere in the chain — the strictest possible claim.

**Calculation:** `st_volume` from `classify_full_bucket()` — sum of frequencies of
every entry in the root's `full` bucket that is globally strict, divided by `N`.

$$
\text{End-to-End} = \frac{\sum_{(n,f,t)\in\mathcal{F}_{\text{ST}}} f}{N}\times100\%
$$

**Includes:** only root-level `full`-bucket entries with no nested placeholder
anywhere in their structure. Excludes Prefix/Suffix entries entirely (a case that's
only partially pinned down from one end scores 0 here, even at 99% known).

**Statement you can make:** "X% of cases in this log have their complete order
reconstructed by the model, with no remaining uncertainty anywhere."

**Observed across the suite (post-fix, see "Bug fixed" note below):** min 0%,
max 100%, mean 18.53%.
- 100% on pure SEQ/XOR trees with no PAR/LOOP at all (`test_02_seq_xor`,
  `test_05_xor_seq`, `test_09_deep_seq`) — expected, since with no opaque operator
  every `full`-bucket entry is trivially globally strict by construction.
- 0% on almost anything containing an unresolved PAR/LOOP (`test_01`, `03`, `04`,
  `07`, `10_nested_par`, `12`, `17`, `20`, `26`, `27`, …) — confirms the metric is
  genuinely all-or-nothing per case, exactly as designed.

> **Bug fixed:** `test_11_nesting.csv` previously reported **125%** End-to-End and
> **162.5%** Total Forced Volume — both above N, which is structurally impossible.
> Root cause: in `core/analyzer.py`'s XOR and SEQ rules, child recursion always used
> `node.children[i].frequency` directly, ignoring the `local_N` actually passed into
> the call. This is harmless at every normal call site (where `local_N` always equals
> `node.frequency` by construction) — but the LOOP zero-redo path deliberately
> recurses into its do-child with a *smaller* `local_N` (`zero_redo_freq`, isolating
> just the never-redone cases). When that do-child was itself an XOR (as in
> `test_11_nesting`'s `*(X(K,L), X(M,→(N,O,P,Q)))`), the XOR rule recursed using K/L's
> full stored frequencies (5 and 4, spanning *all* 9 do-executions including
> post-redo ones) regardless of the much smaller `zero_redo_freq=1` it was called
> with — double-crediting post-redo do-executions into the zero-redo bucket. Fixed by
> scaling children's frequencies proportionally to the requested `local_N`
> (`scale = local_N / node.frequency`) in both the XOR and SEQ rules, which is a
> no-op (`scale == 1`) at every other call site. Confirmed via full-suite diff:
> only `test_11_nesting.csv` (End-to-End 125%→**25%**, Total Forced Volume
> 162.5%→**62.5%**) and `test_15_loop3.csv` (Data Exposure 79.31%→84.92%, an
> unrelated correctness improvement from the same fix) changed; the other 27 files
> are byte-identical to their pre-fix numbers.

---

## 2. Tree Exposure (Strict, Fragment-Level)

**Looking for:** any sub-chain — not necessarily the whole case — whose order is
fully known, as long as it sits *outside* every opaque PAR/LOOP wrapper. Generalizes
End-to-End from binary (whole case or nothing) to partial credit, but stays strict
about *where* the fragment was found.

**Calculation:** `fragment_strict_exposure()`. Full-bucket globally-strict entries
contribute their frequency directly; for the residual `(N - full_freq_total)` cases,
take whichever of Prefix/Suffix's globally-strict residual entries gives the larger
length-ratio credit (`freq * min(len/expected_len, 1)`), capped at the residual.

**Includes:** root-level `full`/`prefix`/`suffix` buckets only, filtered to globally
strict entries. Deliberately **excludes** `all`'s `(in PAR_x)`/`(in LOOP_x)`-tagged
internal sub-fragments, even individually-deterministic ones — their position is
only known relative to their own branch, not globally.

**Statement you can make:** "X% of the population's expected content sits in some
fully order-known chain that isn't trapped inside an unresolved parallel/loop
block" — a looser, complementary read to End-to-End that still respects "global"
order-knowledge.

**Observed across the suite:** min 0%, max 100%, mean 45.67%. Always ≥ End-to-End
for the same file (confirmed across all 29 rows). Notably:
- `test_18_inter_loop.csv` → **0%**, same as its End-to-End — a deeply nested
  `*(*(→(X(C,A), X(τ,+(...))), τ), τ)` structure where literally nothing escapes
  some opaque LOOP/PAR wrapper.
- `test_19_phantomBranch.csv` → **100%**, despite End-to-End being 0% — the model's
  `X(τ, →(A,B,C,D,E,F))` choice plus trailing `'G', *('H','I'), +('K','J')` apparently
  lets Prefix/Suffix fragments outside the PAR/LOOP fully cover the expected length
  even though no single `full`-bucket entry spans the whole case.

---

## 3. Tree Exposure (Strict, Fragment-Level, ≥2 activities)

**Looking for:** the same content as Fragment-Level, but only chains long enough to
actually demonstrate an order *relation* between activities — a single activity has
no internal sequence, so crediting an isolated leaf overstates the "fixed order, no
part of it up for interpretation" claim this metric licenses. This is the metric
that precisely answers: *"how much of the tree's volume sits in a subtree that is
100% guaranteed — start-to-finish ST, or a partial ST that doesn't span the whole
case but is still at least 2 activities long with a fully fixed order, no part of it
up for interpretation."*

**Calculation:** `fragment_strict_exposure(..., min_length=2.0)` — identical
mechanics to Fragment-Level, but every candidate fragment (root-level `full` or
residual `prefix`/`suffix`) must additionally satisfy
`pattern_length(n, registry) >= 2`, else it's dropped from the numerator entirely.

**Includes:** the ≥2-activity-long subset of Fragment-Level's candidate set — a
*reduction*, not a separate union. Still excludes anything sitting inside an opaque
PAR/LOOP wrapper (that's Local-Strict's job, not this one).

**Statement you can make:** "X% of expected content sits in a fully order-fixed
chain of at least two activities, found outside any opaque block."

**Observed across the suite:** min 0%, max 100%, mean **32.09%** — noticeably lower
than unfiltered Fragment-Level's mean (45.67%), confirming single-leaf fragments
were inflating the unfiltered number on several files too (not just Local-Strict).
Always ≤ Fragment-Level for the same file (0 violations confirmed across all 29
rows) — this is a true subset/reduction, unlike the Local-Strict family below where
filter-level orderings don't generalize across metrics.

---

## 4. Tree Exposure (Local-Strict)

**Looking for:** the same as Fragment-Level, but also credits individually
globally-strict sub-fragments found *inside* an opaque PAR/LOOP branch — i.e. "is
any part of this case's content, anywhere, sitting in some deterministic chain,
whether that chain's position is globally or only locally (within its own branch)
known."

**Calculation:** `local_strict_exposure(..., min_length=0.0)`. Same root-level
credit as Fragment-Level, **plus** additional credit summed over `all`-bucket
entries tagged `(in PAR_x)`/`(in LOOP_x)` that are individually globally strict,
weighted by `freq * min(len/expected_len, 1)`, deduplicated by signature, with the
total capped at `N`.

**Includes:** root `full`/`prefix`/`suffix` (Fragment-Level's set) **union**
internal sub-fragments from `all` carrying an `(in ...)` tag. Still excludes content
whose own internal order is unresolved (e.g. an opaque block whose LOOP branch has
a nonzero, unbounded redo count never contributes here, since that sub-fragment
itself isn't globally strict).

**Statement you can make:** "X% of this case's content sits in *some* deterministic
chain, somewhere — local or global." **Cannot** be read as "X% of order is known" —
that overstates the claim; a deterministic branch inside an unresolved PAR still
leaves the cross-branch interleaving (or a LOOP's redo count) genuinely unknown.

**Observed across the suite:** min **75%**, max 100%, mean **95.01%** — i.e. in this
stress suite it never drops below 75%, and usually saturates near 100% regardless
of how little is actually End-to-End-known. This is exactly the documented warning
in practice, not just theory: e.g. `test_18_inter_loop.csv` is 0% End-to-End /
0% Fragment-Level, but **100%** Local-Strict; `test_27_par_loop_noxor.csv` is 0%
End-to-End but **85.07%** Local-Strict. Always report this one next to End-to-End,
never alone.

---

## 5. Tree Exposure (Local-Strict, ≥2 activities)

**Looking for:** the same content as Local-Strict, but only chains long enough to
actually demonstrate an *order relation* — a single activity has no internal
sequence to speak of, so a length-1 fragment is excluded regardless of where it sits.

**Calculation:** `local_strict_exposure(..., min_length=2.0)` — identical mechanics
to Local-Strict, but every candidate fragment (root-level or internal) must satisfy
`pattern_length(n, registry) >= 2`, else it's dropped from the numerator entirely
(binary gate, not a partial ratio below length 2).

**Includes:** the ≥2-activity-long subset of Local-Strict's candidate set. This
*reduces* the unfiltered set; it is not a separate union.

**Statement you can make:** "X% of expected content sits in a deterministic chain
of at least two activities, local or global" — the more defensible version of
Local-Strict's claim, since it can no longer be inflated purely by isolated leaves.

**Observed across the suite:** min 0%, max 100%, mean **36.60%** — roughly a third
of the value of unfiltered Local-Strict (95.01% mean), confirming that single-leaf
fragments were doing most of the work in the unfiltered number. Concretely:
`test_03_loop_std.csv` goes from 80% (Local-Strict) to **0%** once length-1 leaves
are excluded — its only "locally known" content was isolated single activities, not
real chains. `test_24_zero_redo.csv` stays flat at 60% in both — its qualifying
content was already ≥2 activities long, so the filter changes nothing there.

⚠️ Important nuance found while building this table: Local-Strict ≥2 is **not**
guaranteed to be ≥ Fragment-Level (unfiltered) for the same file —
`test_06_xor_xor.csv` has Fragment-Level=100% but Local-Strict≥2=72.55%, because
Fragment-Level's root-level credit there comes partly from length-1 fragments that
the ≥2 filter removes, while Local-Strict≥2's *extra* internal credit doesn't fully
make up the difference. The only orderings actually guaranteed by construction are
same-filter-level ones: End-to-End ≤ Fragment-Level(≥2) ≤ Fragment-Level ≤
Total Forced Volume, and End-to-End ≤ Local-Strict(≥2) ≤ Local-Strict ≤ N. Don't
assume a single universal ladder across both filter levels.

---

## 6. Total Forced Volume

**Looking for:** everything the engine can say *anything* forced about — the
original, pre-redefinition "Tree Exposure" number, kept exactly so every figure
cited elsewhere in the thesis stays correct under this new name.

**Calculation:** `st_volume + as_resolved_volume + as_opaque_volume` from
`classify_full_bucket()`, divided by `N`. No filtering by content quality — every
`full`-bucket entry counts, strict or not.

$$
\text{Total Forced Volume} = \frac{\sum_{(n,f,t)\in\mathcal{F}} f}{N}\times100\%
$$

**Includes:** the entirety of the root `full` bucket — Strict Traces (`[ST]`) and
Activity Sets (`[AS]`) alike, resolved or opaque. Excludes Prefix/Suffix entries
(by definition — those aren't in `full`).

**Statement you can make:** "X% of cases have *some* non-redundant, end-to-end
account in the model" — says nothing about whether that account's order is known,
only that the case isn't left completely unaccounted for.

**Observed across the suite (post-fix):** min 0%, max 100%, mean 66.11%. Several
files sit at exactly **0%** (`test_10_xor_loop`, `test_13_deepLoop`,
`test_14_asymTree`, `test_19_phantomBranch`) — meaning their `full` bucket is
literally empty; every case's content is only ever reconstructed via Prefix/Suffix
or internal fragments, never a single root-spanning Full entry. That's a genuinely
different (and worse) situation than "100% Total Forced but all AS-Opaque" — here
the case isn't even nominally accounted for end-to-end at all.

---

## 7. AS-Resolved Volume

**Looking for:** cases whose `full`-bucket entry references an opaque block, but
where that block's *own* children independently resolve into pure strict traces —
only the block's own boundary (a PAR's interleaving, or a LOOP's redo count) stays
open.

**Calculation:** from `classify_full_bucket()` — for non-globally-strict `full`
entries, check `is_block_internally_resolved()` for every referenced
`[nested X]` block; if all of them resolve, the entry's frequency goes here.

**Includes:** the subset of $\mathcal{F}\setminus\mathcal{F}_{\text{ST}}$ where
every referenced opaque block resolves internally (weakest-link: all blocks must
pass, not just one).

**Statement you can make:** "X% of cases are AS-tagged, but the uncertainty is
narrow and specific — we know the branches' internal order, only the
cross-branch/loop-count boundary is unresolved."

**Observed across the suite:** min 0%, max 100%, mean 20.91%. Nonzero on
`test_01_seq_par` (100%), `test_04_par_xor` (100%), `test_07_par_par` (100%),
`test_23_precTest2` (100%), `test_25_massive` (75%), `sample_log` (40%),
`test_11_nesting` (37.5%), `test_21_wildCards` (45%) — all relatively simple
single-PAR-block trees where the PAR's two branches are each individually
deterministic.

---

## 8. AS-Resolved Volume, PAR-only / LOOP-only

**Looking for:** the same as AS-Resolved Volume, but split by what kind of "open
question" remains. A resolved **PAR** block's open question is "which interleaving
order" — i.e. *these activities are guaranteed to co-occur in the same trace, but
their relative order is unknown*. A resolved **LOOP** block's open question is "how
many redo iterations" — a count, not an ordering. These are different claims, so
mixing them into one number (as plain AS-Resolved Volume does) obscures which kind
of uncertainty is actually present. This is the metric that precisely answers:
*"how much ST was found inside PAR blocks, leading to a combination of activities
guaranteed to happen together somewhere in the same trace, with unknown order."*

**Calculation:** in `classify_full_bucket()`, for every AS-Resolved entry, collect
the operator (`PAR`/`LOOP`) of every block it references via the registry. If the
set of referenced operators is exactly `{PAR}`, the frequency goes into
`as_resolved_par_volume`; if exactly `{LOOP}`, into `as_resolved_loop_volume`. An
entry referencing a mix of both operator types lands in neither sub-bucket (its
frequency still counts toward the AS-Resolved *total*, via weakest-link resolution).

**Includes:** the PAR-only-referencing subset (or LOOP-only-referencing subset) of
AS-Resolved Volume. `PAR-only + LOOP-only ≤ AS-Resolved Volume` — the gap, when
nonzero, is mixed-block-type entries that don't belong to either pure sub-bucket.

**Statement you can make:** "X% of cases have a guaranteed combination of activities
known to occur together in the same trace, in an order that isn't fixed" (PAR-only) —
versus "X% of cases have a fully deterministic do/redo chain whose exact repeat
count is the only open question" (LOOP-only). These license very different privacy
claims and shouldn't be reported as one undifferentiated number.

**Observed across the suite:** AS-Resolved PAR-only is nonzero on 8 files —
`test_01_seq_par` (100%), `test_04_par_xor` (100%), `test_07_par_par` (100%),
`test_23_precTest2` (100%), `sample_log` (40%), `test_21_wildCards` (45%),
`test_25_massive` (70%), `test_11_nesting` (12.5%). AS-Resolved LOOP-only is nonzero
on only 3 files — `test_03_loop_std` (5%), `test_08_xor_loop` (3.85%),
`test_11_nesting` (12.5%) — confirming resolved-LOOP cases are much rarer in this
suite than resolved-PAR cases (most LOOP-containing trees here have a nonzero redo
count on every case, so they land in AS-Opaque instead, never reaching "resolved").
`test_11_nesting.csv` and `test_25_massive.csv` both show `PAR-only + LOOP-only <
AS-Resolved Volume` (37.5% vs 12.5+12.5=25%, and 75% vs 70+0=70%, respectively) —
the residual is a mixed-block-type entry referencing both a PAR and a LOOP block
simultaneously.

---

## 9. AS-Opaque Volume

**Looking for:** the complement of AS-Resolved — cases whose `full`-bucket entry
references at least one opaque block that does *not* resolve even internally; the
genuinely irreducible remainder.

**Calculation:** from `classify_full_bucket()` — non-globally-strict entries where
at least one referenced block fails `is_block_internally_resolved()`.

**Includes:** $\mathcal{F}\setminus(\mathcal{F}_{\text{ST}}\cup\mathcal{F}_{\text{AS-res}})$.

**Statement you can make:** "X% of cases carry a fundamentally open question
somewhere — a branch with its own internal choice/loop that the model cannot pin
down even in principle from this structure."

**Observed across the suite:** min 0%, max 100%, mean 26.67%. 100% on
`test_10_nested_par`, `test_17_spagetti`, `test_20_loopDouble`, `test_22_precTest`,
`test_26_loop_par_noxor`, `test_27_par_loop_noxor` — these are exactly the files
with a LOOP nested inside a PAR branch (or vice versa) where the loop's redo count
is never zero across any case, so there's never a "clean" resolved instance to
credit.

---

## 10. Data Exposure (Confirmed % of Claimed Volume)

**Looking for:** whether the engine's claims about expected pattern frequency are
actually borne out by the real log — a sanity/confirmation check, not a structural
exposure measure.

**Calculation:** `total_confirmed_volume / total_expected_volume`, accumulated while
replaying every non-`COMPLEX` pattern against the log; confirmed count is capped at
the expected minimum per pattern so surplus matches don't inflate the ratio.

**Includes:** every auditable (non-skipped) pattern, both macro (End-to-End) and
internal (`(in ...)`-tagged) ones — anything actually checked against the log, ST
and AS alike. Excludes patterns skipped for combinatorial complexity (`COMPLEX`,
>1000 permutations) since those were never evaluated either way.

**Statement you can make:** "X% of the volume the model claims to have forced is
independently confirmed present in the actual log" — a correctness/trust check on
the other metrics, not an exposure metric itself.

**Observed across the suite (post-fix):** min **88.17%** (`test_20_loopDouble.csv`),
max 100%, mean 98.96%. Mostly 100%; the remaining sub-100% files are
`test_12_skiping` (92.98%), `test_15_loop3` (88.69%), and `test_20_loopDouble`
(88.17%) — all deep nested-loop trees.

> **Bug found and partially fixed:** the dip on these files was traced to
> `_count_fragment_matches()` (`auto_verifier_v2.py`), the scanner used for
> internal `(in PAR_x)`/`(in LOOP_x)`-tagged patterns. For a pattern containing a
> nested-block token, it used to greedily absorb the *entire* contiguous run of
> events belonging to that block's alphabet as a single match — collapsing
> multiple genuine back-to-back repetitions of the block (caused by an outer Loop
> redoing it several times, with nothing but a silent `tau` between repeats) into
> one counted occurrence. Confirmed precisely on `test_15_loop3.csv`'s
> `[nested PAR_2]` pattern: expected ≥9 (the engine correctly derives 9 total
> do-executions), found only 5 — one per case, undercounting by exactly the outer
> Loop's redo count of 4. Fixed by precomputing each nested block's own valid
> sub-patterns and matching exactly *one* instance at a time, letting the
> existing outer scan loop pick up subsequent repetitions as separate matches,
> with a fallback to the old flat-absorption behavior when a block's own pattern
> set is too large to enumerate (`COMPLEX`, >1000 permutations — the same cap
> used elsewhere in the engine). Confirmed via full-suite diff to be a no-op on
> 26/29 files; `test_13_deepLoop.csv` and `test_18_inter_loop.csv` now reach a
> clean 100% Data Exposure, and `test_15_loop3.csv` improved from 84.92% to
> 88.69% but not further, since its own `[nested PAR_2]`/`[nested LOOP_3]` blocks
> are themselves too large to enumerate and still fall back to the
> pre-fix approximation — a genuine tractability limit, not a remaining bug.

---

## 11. Data Exposure, ST-only

**Looking for:** of the real log's data, how much is confirmed *specifically* by
genuinely strict (order-known, macro-level) patterns — not by AS patterns, and not
by internal PAR/LOOP sub-fragments. This is the metric that precisely answers
*"how much of the original data does the ST uncover"* — the confirmation-rate
counterpart to End-to-End (§1), checked against the real log instead of structural
volume.

**Calculation:** same replay/confirmation mechanism as Data Exposure, but the
accumulation is restricted to patterns where `is_globally_strict(node)` is true
*and* the pattern is not internal (`"(in " not in t_type`) — i.e. macro-level,
structurally-strict patterns only. Deliberately checks `is_globally_strict()`
rather than trusting the raw `t_type == "ST"` tag, since the SEQ rule's
`lazy_cross_multiply()` can mislabel a chain `"ST"` even when it still embeds a
nested placeholder (the same pitfall already documented for End-to-End).

**Includes:** macro-level (non-internal) globally-strict patterns only. Excludes
all AS-tagged patterns and all `(in PAR_x)`/`(in LOOP_x)`-tagged internal patterns,
regardless of how individually deterministic they are.

**Statement you can make:** "X% of the real log's data is confirmed present by
genuinely order-known, end-to-end strict patterns" — a stricter, ST-specific
narrowing of Data Exposure's general confirmation-rate claim.

**Observed across the suite:** min **0%** (`test_18_inter_loop.csv` — no qualifying
macro-level strict pattern exists at all for this file, so the ratio falls back to
0/0→0%, the same "not applicable" ambiguity Data Exposure itself has when its
denominator is empty), max 100%, mean 96.55%. Notably **higher** than overall Data
Exposure on every file where the two still diverge after the §10 fix
(`test_12_skiping`, `test_15_loop3`, `test_20_loopDouble` — all at 100% ST-only,
vs. 88–93% overall) — confirming that the remaining Data Exposure dips come
specifically from AS/internal patterns, never from genuinely strict ones; the
engine's strict claims are never the source of a confirmation gap in this stress
suite.

---

## 12. Data Exposure, ST + ST-in-PAR

**Looking for:** the same as ST-only, but additionally folds in individually
deterministic sub-fragments tagged `(in PAR_x)` — excluding `(in LOOP_x)`-tagged
ones, since those carry a redo-count ambiguity rather than a pure order guarantee.
This is the metric that precisely answers *"how much of the original data do the ST
and the ST-within-PAR-blocks uncover, together."*

**Calculation:** same mechanism as ST-only, but the inclusion test is
`is_globally_strict(node) AND (not internal OR "(in PAR" in t_type)` — i.e. macro
strict patterns *plus* PAR-internal strict patterns, still excluding LOOP-internal
and any AS-tagged pattern.

**Includes:** ST-only's set (§11), union PAR-internal globally-strict sub-fragments.
A strict superset of ST-only's accumulation.

**Statement you can make:** "X% of the real log's data is confirmed present by
strict patterns, either globally known or known within a PAR branch" — broadens §11
exactly as far as the PAR-co-occurrence claim in §8 extends it structurally.

**Observed across the suite:** **100% on every one of the 29 files**, including
`test_18_inter_loop.csv` (0% on ST-only alone, since that file's only strict content
lives inside a PAR branch). This uniform 100% is a property of this *specific,
noise-free synthetic suite* — every pattern the engine claims to have found here is
trivially present in its own generating log, since there's no noise to break the
match. Expect genuine sub-100% variance once this metric is run against a noisy or
real-world log (e.g. BPIC2017/2021); on this suite it mainly serves to confirm the
ST-in-PAR accumulation logic is wired correctly (it picks up real volume on files
where ST-only alone is 0, rather than silently defaulting to 0/0).

---

## 13. Max Fractional Exposure

**Looking for:** a partial-credit reading of exposure normalized against the
*worst-case* expected case length (every loop at one do-pass, plus only the single
largest loop's own max-iteration extra, added once — avoiding double-spending a
loop's redo budget across nested loops).

**Calculation:** `fractional_exposure(..., expected_len=expected_length_max(...))`.
Full-bucket entries credited unconditionally; residual credit from whichever of
Prefix/Suffix gives the larger `freq * min(len/expected_len, 1)` sum, capped at the
residual population, total capped at `N`.

**Includes:** `full` (unconditionally) plus the better of `prefix`/`suffix` for the
remainder — no filtering by global strictness; an AS-tagged entry counts too, since
this metric measures length coverage, not order-certainty.

**Statement you can make:** "Even under a pessimistic (long-loop) assumption about
case length, X% of expected content is accounted for."

**Observed across the suite:** min **4.55%** (`test_10_xor_loop.csv`), max 100%,
mean 83.07%. Low values correspond to loop-heavy trees where the worst-case expected
length is dominated by one loop's max-iteration blowup, making the same realized
content look small relative to that pessimistic denominator.

---

## 14. Avg Fractional Exposure

**Looking for:** the same partial-credit reading as Max, but normalized against the
*typical-case* expected length (every loop's average iteration count, summed
additively across all loops rather than compounded multiplicatively).

**Calculation:** `fractional_exposure(..., expected_len=expected_length_avg_additive(...))`
— same mechanics as Max Fractional Exposure, different denominator only.

**Includes:** identical inclusion rule to Max Fractional Exposure.

**Statement you can make:** "Under a realistic, population-average assumption about
case length, X% of expected content is accounted for" — the more citable of the two
for typical-case framing; Max is the conservative/worst-case bound.

**Observed across the suite:** min **18.75%** (`test_10_xor_loop.csv`,
`test_13_deepLoop.csv`), max 100%, mean 88.15% — consistently ≥ Max Fractional
Exposure for the same file (a smaller, more realistic denominator), confirmed across
all 29 rows.

---

## 15. Mean Absolute Exposure Volume

**Looking for:** not a percentage at all — how many real (non-tau) events an
observer actually learns per case, in absolute terms. Directly comparable across
files regardless of structural complexity, unlike the two Fractional variants which
hide case-length differences behind a relative ratio.

**Calculation:** `absolute_exposure_volume()` — full-bucket entries contribute
`freq * pattern_length`; the better (by total events, not ratio) of Prefix/Suffix
covers the residual population, scaled down if it would over-credit more cases than
actually remain. Result divided by `N` (events per case, not a percentage).

**Includes:** same source buckets as the Fractional variants (`full` plus the
better of `prefix`/`suffix`), but reports raw event count instead of a length-ratio.

**Statement you can make:** "An attacker/observer learns, on average, X real
activities per case" — the metric the thesis ties most directly to privacy impact
(Section 8.2), since a high relative-exposure percentage on a short case can still
mean very little is actually learned.

**Observed across the suite:** min **1.00** events/case (`test_10_xor_loop.csv`),
max **8.00** events/case (`test_20_loopDouble.csv`), mean 4.21. Notably,
`test_10_xor_loop` is simultaneously the file with the lowest Max and Avg Fractional
Exposure *and* the lowest absolute volume — for that file, both readings agree the
exposure is genuinely thin, not just relatively thin against an inflated denominator.

---

## Mapping to plain-language exposure statements

| You want to say... | Use this metric |
|---|---|
| "How much start-to-finish ST was found, relative to tree volume" | **§1 End-to-End** |
| "How much is 100%-guaranteed, fixed-order, ≥2 activities long — start-to-finish ST plus partial ST that doesn't span the whole case but still has zero room for interpretation" | **§3 Fragment-Level (≥2 activities)** |
| "How much ST was found inside PAR blocks — a combination of activities guaranteed to happen together in the same trace, order unknown" | **§8 AS-Resolved Volume, PAR-only** |
| "How much of the original data the ST uncovers" | **§11 Data Exposure, ST-only** |
| "How much of the original data the ST and the ST-within-PAR-blocks uncover, together" | **§12 Data Exposure, ST + ST-in-PAR** |

---

## Cross-cutting takeaways from the full suite (not visible from `test_27` alone)

1. **(Fixed)** End-to-End and Total Forced Volume used to exceed 100% on
   `test_11_nesting.csv` (125% and 162.5%) because the XOR/SEQ rules in
   `core/analyzer.py` ignored the `local_N` they were actually called with,
   double-crediting post-redo do-executions into a LOOP's zero-redo bucket whenever
   the do-child was itself a complex (XOR/SEQ) operator. Fixed by scaling children's
   frequencies to the requested `local_N` instead of trusting their stored
   frequencies outright — confirmed via full-suite diff to be a no-op everywhere
   except `test_11_nesting.csv` (now 25% / 62.5%, both ≤ N) and a secondary
   correctness improvement on `test_15_loop3.csv`'s Data Exposure (79.31%→84.92%).
2. **Local-Strict saturates hard in this suite** (never below 75%, mean 95%) —
   confirms the ⚠️ caveat is not a theoretical worst-case, it's the *typical* case
   for this engine's output whenever any PAR/LOOP nesting exists at all.
3. **The ≥2-activity filter does real work on both families**: Local-Strict's mean
   drops from 95.01% to 36.60%, and Fragment-Level's mean drops from 45.67% to
   32.09% — most "locally known" *and* a meaningful share of "globally known"
   credit in this suite comes from isolated single-leaf fragments, not genuine
   multi-activity chains.
4. **Total Forced Volume hitting exactly 0%** (4 files) is a qualitatively different,
   worse outcome than "100% Total Forced but all AS-Opaque" — the former means no
   root-spanning account exists at all; worth distinguishing in any reporting rather
   than treating "low Total Forced" and "high AS-Opaque" as equivalent bad news.
5. **AS-Resolved is dominated by PAR, not LOOP, in this suite**: PAR-only resolution
   is nonzero on 8 files (up to 100%); LOOP-only resolution is nonzero on only 3
   files (max 12.5%) — most LOOP-containing trees here have a nonzero redo count on
   every case, landing them in AS-Opaque instead of ever reaching "resolved."
6. **(Fixed)** Two of the five originally-sub-100% Data Exposure files
   (`test_13_deepLoop.csv`, `test_18_inter_loop.csv`) were not measuring genuine
   model/log divergence at all — `_count_fragment_matches()`'s opaque-token
   consumption was silently absorbing multiple back-to-back repetitions of an
   internally-looping nested block into a single counted match. Fixed by matching
   one block instance at a time against its own enumerated sub-patterns; both
   files now reach a clean 100%. `test_15_loop3.csv` improved (84.92%→88.69%) but
   not fully, since its own nested blocks are themselves too combinatorially large
   to enumerate and still fall back to the pre-fix approximation.
7. **Data Exposure dips never come from genuinely strict content**: Data Exposure,
   ST-only is 100% on every file where overall Data Exposure still dips below
   100% post-fix (`test_12_skiping`, `test_15_loop3`, `test_20_loopDouble`) — the
   confirmation gap is always in AS/internal patterns, never in the engine's
   strict claims, on this suite.
8. **Data Exposure, ST + ST-in-PAR is 100% on all 29 files** — a property of this
   noise-free synthetic suite (every claimed pattern trivially appears in its own
   generating log), not a general guarantee. Expect real variance once this metric
   is run against a noisy or real-world log.
