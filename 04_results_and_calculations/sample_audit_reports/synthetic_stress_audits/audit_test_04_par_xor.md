# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `test_04_par_xor.csv` |
| **Noise Threshold** | `0.0` |
| **Fitness** | `N/A (skipped)` |
| **Precision** | `N/A (skipped)` |
| **Total Cases in Log** | `34` |
| **Unique Activities** | `4` |
| **XOR Operators** | `1` |
| **LOOP Operators** | `0` |
| **SEQ Operators** | `1` |
| **PAR Operators** | `1` |
| **Binarization Additions** | `0` |
| **Tau Operators Added** | `0` |
| **Total Found Patterns** | `8` |
| **Verified Patterns** | `6` |
| **Discrepancy Patterns** | `0` |
| **Ghost Patterns** | `0` |
| **Nested LOOPs** | `0` |
| **Nested PARs** | `1` |
| **Tree Exposure (Strict, End-to-End % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `33.33%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `0.00%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `0.00%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `100.00%` |
| **AS-Resolved Volume (% of N)** | `100.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `100.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `0.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `100.00%` |
| **Data Exposure, ST-only (% confirmed)** | `100.00%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `100.00%` |
| **Data Coverage, ST-only (% of real log)** | `33.33%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `100.00%` |
| **Data Coverage, Total (% of real log)** | `100.00%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `100.00%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `100.00%` |
| **Mean Absolute Exposure Volume (events/case)** | `3.00` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_test_04_par_xor.png)


```text
->( +( 'A', X( 'C', 'B' ) ), 'D' )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_test_04_par_xor.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST (in PAR_1)]` | `A` | Exact Token Match | $\ge$ 34 | **34** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `C` | Exact Token Match | $\ge$ 17 | **17** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `B` | Exact Token Match | $\ge$ 17 | **17** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_1]` | Exact Token Match | $\ge$ 34 | **34** | ✅ **VERIFIED** |
| `[ST]` | `D` | Exact Token Match | $\ge$ 34 | **34** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], D⟩` | Exact Token Match | $\ge$ 34 | **34** | ✅ **VERIFIED** |

## Audit Summary
- **Perfect Pattern Verifications:** 6
- **Frequency Discrepancies:** 0
- **Ghost Patterns (Fatal):** 0
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 33.33%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 0.00%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 0.00%
- **Total Forced Volume (incl. unresolved AS, % of N):** 100.00%
- **AS-Resolved Volume (% of N):** 100.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 100.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 0.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 100.00%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 100.00%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 100.00%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 33.33%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 100.00%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 100.00%
- **Max Fractional Exposure (Worst-Case Normalized):** 100.00% (expected length: 3.00 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 100.00% (expected length: 3.00 events)
- **Mean Absolute Exposure Volume:** 3.00 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested PAR_1]`
- **Internal Structure:** `{A, [C │ B]}`
- **Block Frequency:** 34



![nested PAR_1 Internal Diagram](images/nested_ref_audit_test_04_par_xor_nested_PAR_1.png)
