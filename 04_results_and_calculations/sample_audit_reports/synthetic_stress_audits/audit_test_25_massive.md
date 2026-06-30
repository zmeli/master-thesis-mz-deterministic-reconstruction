# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `test_25_massive.csv` |
| **Noise Threshold** | `0.0` |
| **Fitness** | `N/A (skipped)` |
| **Precision** | `N/A (skipped)` |
| **Total Cases in Log** | `20` |
| **Unique Activities** | `6` |
| **XOR Operators** | `1` |
| **LOOP Operators** | `1` |
| **SEQ Operators** | `2` |
| **PAR Operators** | `1` |
| **Binarization Additions** | `0` |
| **Tau Operators Added** | `0` |
| **Total Found Patterns** | `22` |
| **Verified Patterns** | `14` |
| **Discrepancy Patterns** | `0` |
| **Ghost Patterns** | `0` |
| **Nested LOOPs** | `1` |
| **Nested PARs** | `1` |
| **Tree Exposure (Strict, End-to-End % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `45.24%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `28.57%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `28.57%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `75.00%` |
| **AS-Resolved Volume (% of N)** | `75.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `70.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `0.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `100.00%` |
| **Data Exposure, ST-only (% confirmed)** | `100.00%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `100.00%` |
| **Data Coverage, ST-only (% of real log)** | `30.95%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `78.57%` |
| **Data Coverage, Total (% of real log)** | `100.00%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `99.36%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `100.00%` |
| **Mean Absolute Exposure Volume (events/case)** | `3.52` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_test_25_massive.png)


```text
->( +( 'A', 'B' ), X( *( 'E', 'F' ), ->( 'C', 'D' ) ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_test_25_massive.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST (in PAR_1)]` | `A` | Exact Token Match | $\ge$ 20 | **20** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `B` | Exact Token Match | $\ge$ 20 | **20** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_1]` | Exact Token Match | $\ge$ 20 | **20** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `E` | Exact Token Match | $\ge$ 14 | **14** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `F` | Exact Token Match | $\ge$ 6 | **6** | ✅ **VERIFIED** |
| `[ST]` | `⟨E⟩` | Exact Token Match | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_2]` | Exact Token Match | $\ge$ 1 | **8** | ✅ **VERIFIED** |
| `[ST]` | `C` | Exact Token Match | $\ge$ 12 | **12** | ✅ **VERIFIED** |
| `[ST]` | `D` | Exact Token Match | $\ge$ 12 | **12** | ✅ **VERIFIED** |
| `[ST]` | `⟨C, D⟩` | Exact Token Match | $\ge$ 12 | **12** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], E⟩` | Exact Token Match | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], [nested LOOP_2]⟩` | Exact Token Match | $\ge$ 1 | **8** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], C, D⟩` | Exact Token Match | $\ge$ 12 | **12** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], C⟩` | Exact Token Match | $\ge$ 12 | **12** | ✅ **VERIFIED** |

## Audit Summary
- **Perfect Pattern Verifications:** 14
- **Frequency Discrepancies:** 0
- **Ghost Patterns (Fatal):** 0
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 45.24%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 28.57%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 28.57%
- **Total Forced Volume (incl. unresolved AS, % of N):** 75.00%
- **AS-Resolved Volume (% of N):** 75.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 70.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 0.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 100.00%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 100.00%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 100.00%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 30.95%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 78.57%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 100.00%
- **Max Fractional Exposure (Worst-Case Normalized):** 99.36% (expected length: 15.60 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 100.00% (expected length: 4.20 events)
- **Mean Absolute Exposure Volume:** 3.52 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested PAR_1]`
- **Internal Structure:** `{A, B}`
- **Block Frequency:** 20



![nested PAR_1 Internal Diagram](images/nested_ref_audit_test_25_massive_nested_PAR_1.png)

### `[nested LOOP_2]`
- **Internal Structure:** `(E ∗ F)`
- **Block Frequency:** 8

- **Max Loop Iterations:** `6`
- **Max Sub-Sequence Length:** `13` steps (if one case consumes all iterations)

![nested LOOP_2 Internal Diagram](images/nested_ref_audit_test_25_massive_nested_LOOP_2.png)
