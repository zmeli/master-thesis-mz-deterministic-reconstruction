# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `test_18_inter_loop.csv` |
| **Noise Threshold** | `0.0` |
| **Fitness** | `N/A (skipped)` |
| **Precision** | `N/A (skipped)` |
| **Total Cases in Log** | `3` |
| **Unique Activities** | `5` |
| **XOR Operators** | `6` |
| **LOOP Operators** | `2` |
| **SEQ Operators** | `2` |
| **PAR Operators** | `1` |
| **Binarization Additions** | `0` |
| **Tau Operators Added** | `6` |
| **Total Found Patterns** | `16` |
| **Verified Patterns** | `12` |
| **Discrepancy Patterns** | `0` |
| **Ghost Patterns** | `0` |
| **Nested LOOPs** | `2` |
| **Nested PARs** | `1` |
| **Tree Exposure (Strict, End-to-End % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `0.00%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `37.04%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `33.33%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `33.33%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `100.00%` |
| **Data Exposure, ST-only (% confirmed)** | `0.00%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `100.00%` |
| **Data Coverage, ST-only (% of real log)** | `0.00%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `55.56%` |
| **Data Coverage, Total (% of real log)** | `100.00%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `33.33%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `33.33%` |
| **Mean Absolute Exposure Volume (events/case)** | `3.00` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_test_18_inter_loop.png)


```text
*( *( ->( X( 'C', 'A' ), X( tau, +( X( tau, 'B' ), X( tau, ->( X( tau, 'D' ), X( tau, 'E' ) ) ) ) ) ), tau ), tau )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_test_18_inter_loop.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST (in LOOP_2)]` | `C` | Exact Token Match | $\ge$ 6 | **6** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `A` | Exact Token Match | $\ge$ 6 | **6** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `τ` | Trivial (no observable event) | $\ge$ 6 | **6** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `τ` | Trivial (no observable event) | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `B` | Exact Token Match | $\ge$ 4 | **4** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `D` | Exact Token Match | $\ge$ 6 | **6** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `τ` | Trivial (no observable event) | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `E` | Exact Token Match | $\ge$ 5 | **5** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨D, τ⟩` | Exact Token Match | $\ge$ 1 | **6** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨D, E⟩` | Exact Token Match | $\ge$ 5 | **5** | ✅ **VERIFIED** |
| `[AS (in LOOP_2)]` | `[nested PAR_3]` | Exact Token Match | $\ge$ 6 | **6** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_1]` | Exact Token Match | $\ge$ 1 | **3** | ✅ **VERIFIED** |

## Audit Summary
- **Perfect Pattern Verifications:** 12
- **Frequency Discrepancies:** 0
- **Ghost Patterns (Fatal):** 0
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 0.00%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 37.04%
- **Total Forced Volume (incl. unresolved AS, % of N):** 33.33%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 33.33%
- **Data Exposure (Confirmed % of Claimed Volume):** 100.00%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 0.00%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 100.00%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 0.00%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 55.56%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 100.00%
- **Max Fractional Exposure (Worst-Case Normalized):** 33.33% (expected length: 22.50 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 33.33% (expected length: 9.00 events)
- **Mean Absolute Exposure Volume:** 3.00 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested PAR_3]`
- **Internal Structure:** `{[τ │ B], [τ │ ⟨[τ │ D], [τ │ E]⟩]}`
- **Block Frequency:** 6



![nested PAR_3 Internal Diagram](images/nested_ref_audit_test_18_inter_loop_nested_PAR_3.png)

### `[nested LOOP_2]`
- **Internal Structure:** `(⟨[C │ A], [τ │ {[τ │ B], [τ │ ⟨[τ │ D], [τ │ E]⟩]}]⟩ ∗ τ)`
- **Block Frequency:** 12

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_2 Internal Diagram](images/nested_ref_audit_test_18_inter_loop_nested_LOOP_2.png)

### `[nested LOOP_1]`
- **Internal Structure:** `((⟨[C │ A], [τ │ {[τ │ B], [τ │ ⟨[τ │ D], [τ │ E]⟩]}]⟩ ∗ τ) ∗ τ)`
- **Block Frequency:** 3

- **Max Loop Iterations:** `9`
- **Max Sub-Sequence Length:** `19` steps (if one case consumes all iterations)

![nested LOOP_1 Internal Diagram](images/nested_ref_audit_test_18_inter_loop_nested_LOOP_1.png)
