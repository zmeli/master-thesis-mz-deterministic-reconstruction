---
status: OPEN — confirmed, not yet fixed
severity: MEDIUM — affects PAR-internal pattern matching whenever a Parallel
  block's own content contains an optional (XOR-with-tau) branch
found: while investigating two files whose Data Exposure shifted slightly after
  the tau/XOR dissolution fix (output/BUG_tau_xor_dissolution.md)
---

# Bug: unordered PAR-internal matcher requires every block-alphabet activity unconditionally

## One-paragraph summary

`auto_verifier_v2.py`'s `_count_fragment_matches()`, in its `is_unordered_par`
branch (used for patterns tagged `(in PAR_$k$)` when `ignore_par_order=True`,
the default), expands a nested block token into a flat requirement that *every*
activity in the block's alphabet must appear exactly once per matched instance.
This is correct only when every branch of the Parallel block is mandatory. The
moment a block's own content contains an optional branch (an `XOR(tau, X)`
inside the block), the matcher undercounts: cases where the optional activity
was skipped are not recognized as valid instances of the block at all, even
though "the optional activity didn't happen this time" is exactly the behavior
that branch represents.

## Where it lives

`auto_verifier_v2.py`, `_count_fragment_matches()`, inside the `if
is_unordered_par:` branch:
```python
for token in perm:
    if token.startswith("[nested"):
        allowed_alphabet = block_alphabets.get(token, set())
        for act in allowed_alphabet:
            req_counts[act] += 1          # <-- every alphabet member required, count 1
    else:
        req_counts[token] += 1

possible_matches = min((trace_counts[act] // count for act, count in req_counts.items() if count > 0), default=0)
```
`block_alphabets` (built by `_compute_block_alphabets()`) is a flat *set* of
activity names reachable inside the block — it carries no information about
which of those activities are optional, nor how many times each can legitimately
appear per instance. Treating "is in the alphabet" as "required exactly once"
is the bug.

## Confirmed reproduction

On `test_12_skiping.csv`, the block referred to as `[nested PAR_2]` is:
```
PAR_2 = +( ×(τ, E),  B )
```
5 cases pass through this block: $E$ occurs in only 2 of them (the other 3 take
the silent branch and produce only $B$). Both "B alone" and "B and E together"
are valid, complete instances of this block. The audit reports:
```
[AS (in PAR_1)]  [nested PAR_2]   expected >= 5.0   found 2   DISCREPANCY
```
Tracing the arithmetic directly:
```python
trace_counts = {'B': 5, 'E': 2}          # totals across all 5 cases
req_counts   = {'B': 1, 'E': 1}          # current (incorrect) requirement
possible_matches = min(5 // 1, 2 // 1) = 2
```
The true count is $5$ -- every case contains a valid instance of `PAR_2`, three
of them via the "B-only" variant. The matcher reports $2$ because it refuses to
count any instance that doesn't also include $E$.

The same mechanism is responsible for the related Discrepancy/Ghost rows seen
on `test_20_loopDouble.csv` (`[nested PAR_3]`, `[nested PAR_5]`, and the
composite patterns built on top of them) -- same root cause, deeper nesting.

## Why this surfaced only now

This bug almost certainly predates the tau/XOR dissolution fix
(`output/BUG_tau_xor_dissolution.md`) -- it lives in a completely different code
path (the auditor's Counter-based matcher, not the engine's XOR rule). Before
that fix, the specific Full-bucket / internal-fragment entries this matcher is
now being asked to verify on these two files either didn't exist or were
structured differently, so this particular flat-alphabet miscount was never
triggered on them. The tau/XOR fix changed what gets harvested and audited,
which is what exposed it -- it did not introduce it.

## Suggested fix direction (not yet attempted)

`block_alphabets` needs to carry more than a flat set if this matcher is to stay
order-independent but still respect optionality. Options:

1. **Use `block_patterns`** (already computed by `_compute_block_patterns()` for
   the tau/XOR-adjacent fix in the ordered branch) instead of `block_alphabets`
   for the unordered case too: rather than building `req_counts` from the flat
   alphabet, check whether *any* of the block's own enumerated valid patterns
   (Section on `_generate_valid_patterns()`) is satisfiable against the
   remaining trace activity counts, and credit the best-fitting one. More
   correct, more expensive.
2. **Compute a per-activity minimum occurrence count** for the block (0 for any
   activity reachable only via a branch that the block's own structure marks as
   optional, 1 or more otherwise) instead of a flat "all required" set, and use
   that as `req_counts`'s baseline instead of `{act: 1 for act in alphabet}`.
   Cheaper than option 1, but needs a new helper to compute "minimum guaranteed
   occurrences per activity inside this block," which doesn't currently exist
   anywhere in the codebase.

Either way, the **acceptance test** should be: on a block `+(×(τ,E), B)` with 3
cases taking the silent branch and 2 taking $E$, matching `[nested <block>]`
against a 5-case log where every case has $B$ should report `5`, not `2`.

## How to validate a fix

1. Confirm the reproduction above (`test_12_skiping.csv`, `[nested PAR_2]`)
   reports `found = 5`, not `2`, and the Discrepancy status clears.
2. Re-run the full 29-file stress suite and diff against the current baseline
   (`output/_all_metrics_summary.csv`) the same way the two earlier fixes were
   validated -- confirm only files containing a Parallel block with an internal
   optional branch change, and nothing else regresses.
3. Re-check `test_20_loopDouble.csv` specifically, since it has the same pattern
   at two nesting depths (`PAR_3` and `PAR_5`).

## Related bugs in the same area

- `output/BUG_tau_xor_dissolution.md` -- the engine-side bug whose fix surfaced
  this one. Different code path, different root cause, but the two are easy to
  conflate when reading a diff that touches both areas at once.
- The fragment-scanner repeat-counting bug fixed earlier in this engine
  (documented in `output/tree_exposure_metrics_overview.md`) is the same
  *family* of issue as this one -- a matcher making an unconditional assumption
  ("every repeat looks the same," "every alphabet member is mandatory") that
  breaks once the underlying structure has genuine optionality or repetition.
  Worth a dedicated audit of every remaining flat-alphabet-based matching
  shortcut in `auto_verifier_v2.py` once this one is fixed, rather than treating
  each occurrence as an isolated surprise.
