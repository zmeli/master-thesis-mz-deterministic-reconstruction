# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `test_03_loop_std.csv` |
| **Noise Threshold** | `0.0` |
| **Fitness** | `N/A (skipped)` |
| **Precision** | `N/A (skipped)` |
| **Total Cases in Log** | `20` |
| **Unique Activities** | `4` |
| **XOR Operators** | `0` |
| **LOOP Operators** | `1` |
| **SEQ Operators** | `2` |
| **PAR Operators** | `0` |
| **Binarization Additions** | `1` |
| **Tau Operators Added** | `0` |
| **Total Found Patterns** | `12` |
| **Verified Patterns** | `8` |
| **Discrepancy Patterns** | `0` |
| **Ghost Patterns** | `0` |
| **Nested LOOPs** | `1` |
| **Nested PARs** | `0` |
| **Tree Exposure (Strict, End-to-End % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `20.00%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `0.00%` |
| **Tree Exposure (Local-Strict % of N)** | `80.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `0.00%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `5.00%` |
| **AS-Resolved Volume (% of N)** | `5.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `5.00%` |
| **AS-Opaque Volume (% of N)** | `0.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `100.00%` |
| **Data Exposure, ST-only (% confirmed)** | `100.00%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `100.00%` |
| **Data Coverage, ST-only (% of real log)** | `40.00%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `40.00%` |
| **Data Coverage, Total (% of real log)** | `100.00%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `7.79%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `29.00%` |
| **Mean Absolute Exposure Volume (events/case)** | `1.34` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_test_03_loop_std.png)


```text
->( 'A', *( 'B', 'C' ), 'D' )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_test_03_loop_std.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST]` | `A` | Exact Token Match | $\ge$ 20 | **20** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `B` | Exact Token Match | $\ge$ 40 | **40** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `C` | Exact Token Match | $\ge$ 20 | **20** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_1]` | Exact Token Match | $\ge$ 1 | **20** | ✅ **VERIFIED** |
| `[ST]` | `D` | Exact Token Match | $\ge$ 20 | **20** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested LOOP_1], D⟩` | Exact Token Match | $\ge$ 1 | **20** | ✅ **VERIFIED** |
| `[ST]` | `⟨A, [nested LOOP_1], D⟩` | Exact Token Match | $\ge$ 1 | **20** | ✅ **VERIFIED** |
| `[ST]` | `⟨A, [nested LOOP_1]⟩` | Exact Token Match | $\ge$ 1 | **20** | ✅ **VERIFIED** |

## Audit Summary
- **Perfect Pattern Verifications:** 8
- **Frequency Discrepancies:** 0
- **Ghost Patterns (Fatal):** 0
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 20.00%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 0.00%
- **Tree Exposure (Local-Strict % of N):** 80.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 0.00%
- **Total Forced Volume (incl. unresolved AS, % of N):** 5.00%
- **AS-Resolved Volume (% of N):** 5.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 5.00%
- **AS-Opaque Volume (% of N):** 0.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 100.00%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 100.00%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 100.00%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 40.00%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 40.00%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 100.00%
- **Max Fractional Exposure (Worst-Case Normalized):** 7.79% (expected length: 43.00 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 29.00% (expected length: 5.00 events)
- **Mean Absolute Exposure Volume:** 1.34 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_1]`
- **Internal Structure:** `(B ∗ C)`
- **Block Frequency:** 20

- **Max Loop Iterations:** `20`
- **Max Sub-Sequence Length:** `41` steps (if one case consumes all iterations)

![nested LOOP_1 Internal Diagram](images/nested_ref_audit_test_03_loop_std_nested_LOOP_1.png)
