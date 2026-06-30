# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `test_06_xor_xor.csv` |
| **Noise Threshold** | `0.0` |
| **Fitness** | `N/A (skipped)` |
| **Precision** | `N/A (skipped)` |
| **Total Cases in Log** | `34` |
| **Unique Activities** | `5` |
| **XOR Operators** | `2` |
| **LOOP Operators** | `0` |
| **SEQ Operators** | `2` |
| **PAR Operators** | `0` |
| **Binarization Additions** | `1` |
| **Tau Operators Added** | `0` |
| **Total Found Patterns** | `19` |
| **Verified Patterns** | `11` |
| **Discrepancy Patterns** | `0` |
| **Ghost Patterns** | `0` |
| **Nested LOOPs** | `0` |
| **Nested PARs** | `0` |
| **Tree Exposure (Strict, End-to-End % of N)** | `5.88%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `100.00%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `72.55%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `72.55%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `5.88%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `0.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `100.00%` |
| **Data Exposure, ST-only (% confirmed)** | `100.00%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `100.00%` |
| **Data Coverage, ST-only (% of real log)** | `100.00%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `100.00%` |
| **Data Coverage, Total (% of real log)** | `100.00%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `100.00%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `100.00%` |
| **Mean Absolute Exposure Volume (events/case)** | `1.59` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_test_06_xor_xor.png)


```text
->( X( 'A', 'B' ), X( 'C', 'D' ), 'E' )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_test_06_xor_xor.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST]` | `A` | Exact Token Match | $\ge$ 16 | **16** | ✅ **VERIFIED** |
| `[ST]` | `B` | Exact Token Match | $\ge$ 18 | **18** | ✅ **VERIFIED** |
| `[ST]` | `C` | Exact Token Match | $\ge$ 17 | **17** | ✅ **VERIFIED** |
| `[ST]` | `D` | Exact Token Match | $\ge$ 17 | **17** | ✅ **VERIFIED** |
| `[ST]` | `E` | Exact Token Match | $\ge$ 34 | **34** | ✅ **VERIFIED** |
| `[ST]` | `⟨C, E⟩` | Exact Token Match | $\ge$ 17 | **17** | ✅ **VERIFIED** |
| `[ST]` | `⟨D, E⟩` | Exact Token Match | $\ge$ 17 | **17** | ✅ **VERIFIED** |
| `[ST]` | `⟨B, C, E⟩` | Exact Token Match | $\ge$ 1 | **8** | ✅ **VERIFIED** |
| `[ST]` | `⟨B, D, E⟩` | Exact Token Match | $\ge$ 1 | **10** | ✅ **VERIFIED** |
| `[ST]` | `⟨B, C⟩` | Exact Token Match | $\ge$ 1 | **8** | ✅ **VERIFIED** |
| `[ST]` | `⟨B, D⟩` | Exact Token Match | $\ge$ 1 | **10** | ✅ **VERIFIED** |

## Audit Summary
- **Perfect Pattern Verifications:** 11
- **Frequency Discrepancies:** 0
- **Ghost Patterns (Fatal):** 0
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 5.88%
- **Tree Exposure (Strict, Fragment-Level % of N):** 100.00%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 72.55%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 72.55%
- **Total Forced Volume (incl. unresolved AS, % of N):** 5.88%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 0.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 100.00%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 100.00%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 100.00%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 100.00%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 100.00%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 100.00%
- **Max Fractional Exposure (Worst-Case Normalized):** 100.00% (expected length: 3.00 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 100.00% (expected length: 3.00 events)
- **Mean Absolute Exposure Volume:** 1.59 events/case