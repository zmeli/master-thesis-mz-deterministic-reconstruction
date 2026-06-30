# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `test_27_par_loop_noxor.csv` |
| **Noise Threshold** | `0.0` |
| **Fitness** | `N/A (skipped)` |
| **Precision** | `N/A (skipped)` |
| **Total Cases in Log** | `20` |
| **Unique Activities** | `5` |
| **XOR Operators** | `0` |
| **LOOP Operators** | `1` |
| **SEQ Operators** | `2` |
| **PAR Operators** | `1` |
| **Binarization Additions** | `1` |
| **Tau Operators Added** | `0` |
| **Total Found Patterns** | `14` |
| **Verified Patterns** | `10` |
| **Discrepancy Patterns** | `0` |
| **Ghost Patterns** | `0` |
| **Nested LOOPs** | `1` |
| **Nested PARs** | `1` |
| **Tree Exposure (Strict, End-to-End % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `14.93%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `0.00%` |
| **Tree Exposure (Local-Strict % of N)** | `85.07%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `0.00%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `100.00%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `100.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `100.00%` |
| **Data Exposure, ST-only (% confirmed)** | `100.00%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `100.00%` |
| **Data Coverage, ST-only (% of real log)** | `29.85%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `44.78%` |
| **Data Coverage, Total (% of real log)** | `100.00%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `100.00%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `100.00%` |
| **Mean Absolute Exposure Volume (events/case)** | `6.70` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_test_27_par_loop_noxor.png)


```text
->( 'A', +( *( 'B', 'C' ), 'D' ), 'E' )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_test_27_par_loop_noxor.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST]` | `A` | Exact Token Match | $\ge$ 20 | **20** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `B` | Exact Token Match | $\ge$ 47 | **47** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `C` | Exact Token Match | $\ge$ 27 | **27** | ✅ **VERIFIED** |
| `[AS (in PAR_1)]` | `[nested LOOP_2]` | Exact Token Match | $\ge$ 1 | **27** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `D` | Exact Token Match | $\ge$ 20 | **20** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_1]` | Exact Token Match | $\ge$ 20 | **20** | ✅ **VERIFIED** |
| `[ST]` | `E` | Exact Token Match | $\ge$ 20 | **20** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], E⟩` | Exact Token Match | $\ge$ 20 | **20** | ✅ **VERIFIED** |
| `[ST]` | `⟨A, [nested PAR_1], E⟩` | Exact Token Match | $\ge$ 20 | **20** | ✅ **VERIFIED** |
| `[ST]` | `⟨A, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 20 | **20** | ✅ **VERIFIED** |

## Audit Summary
- **Perfect Pattern Verifications:** 10
- **Frequency Discrepancies:** 0
- **Ghost Patterns (Fatal):** 0
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 14.93%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 0.00%
- **Tree Exposure (Local-Strict % of N):** 85.07% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 0.00%
- **Total Forced Volume (incl. unresolved AS, % of N):** 100.00%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 100.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 100.00%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 100.00%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 100.00%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 29.85%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 44.78%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 100.00%
- **Max Fractional Exposure (Worst-Case Normalized):** 100.00% (expected length: 58.00 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 100.00% (expected length: 6.70 events)
- **Mean Absolute Exposure Volume:** 6.70 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_2]`
- **Internal Structure:** `(B ∗ C)`
- **Block Frequency:** 20

- **Max Loop Iterations:** `27`
- **Max Sub-Sequence Length:** `55` steps (if one case consumes all iterations)

![nested LOOP_2 Internal Diagram](images/nested_ref_audit_test_27_par_loop_noxor_nested_LOOP_2.png)

### `[nested PAR_1]`
- **Internal Structure:** `{(B ∗ C), D}`
- **Block Frequency:** 20



![nested PAR_1 Internal Diagram](images/nested_ref_audit_test_27_par_loop_noxor_nested_PAR_1.png)
