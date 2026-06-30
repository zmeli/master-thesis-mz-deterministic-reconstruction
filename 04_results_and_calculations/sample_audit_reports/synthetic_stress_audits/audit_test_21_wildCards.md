# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `test_21_wildCards.csv` |
| **Noise Threshold** | `0.0` |
| **Fitness** | `N/A (skipped)` |
| **Precision** | `N/A (skipped)` |
| **Total Cases in Log** | `20` |
| **Unique Activities** | `6` |
| **XOR Operators** | `6` |
| **LOOP Operators** | `0` |
| **SEQ Operators** | `3` |
| **PAR Operators** | `1` |
| **Binarization Additions** | `0` |
| **Tau Operators Added** | `4` |
| **Total Found Patterns** | `43` |
| **Verified Patterns** | `24` |
| **Discrepancy Patterns** | `0` |
| **Ghost Patterns** | `0` |
| **Nested LOOPs** | `0` |
| **Nested PARs** | `1` |
| **Tree Exposure (Strict, End-to-End % of N)** | `15.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `53.96%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `23.38%` |
| **Tree Exposure (Local-Strict % of N)** | `92.92%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `23.38%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `70.00%` |
| **AS-Resolved Volume (% of N)** | `55.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `55.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `0.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `100.00%` |
| **Data Exposure, ST-only (% confirmed)** | `100.00%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `100.00%` |
| **Data Coverage, ST-only (% of real log)** | `61.04%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `100.00%` |
| **Data Coverage, Total (% of real log)** | `100.00%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `100.00%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `100.00%` |
| **Mean Absolute Exposure Volume (events/case)** | `3.28` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_test_21_wildCards.png)


```text
->( 'A', X( tau, ->( +( X( tau, 'C' ), X( tau, 'B' ) ), X( tau, ->( X( 'E', 'D' ), X( tau, 'F' ) ) ) ) ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_test_21_wildCards.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST]` | `A` | Exact Token Match | $\ge$ 20 | **20** | ✅ **VERIFIED** |
| `[ST]` | `τ` | Trivial (no observable event) | $\ge$ 3 | **3** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `τ` | Trivial (no observable event) | $\ge$ 4 | **4** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `C` | Exact Token Match | $\ge$ 13 | **13** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `B` | Exact Token Match | $\ge$ 17 | **17** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_1]` | Exact Token Match | $\ge$ 17 | **19** | ✅ **VERIFIED** |
| `[ST]` | `τ` | Trivial (no observable event) | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[ST]` | `E` | Exact Token Match | $\ge$ 5 | **5** | ✅ **VERIFIED** |
| `[ST]` | `D` | Exact Token Match | $\ge$ 10 | **10** | ✅ **VERIFIED** |
| `[ST]` | `F` | Exact Token Match | $\ge$ 12 | **12** | ✅ **VERIFIED** |
| `[ST]` | `⟨E, F⟩` | Exact Token Match | $\ge$ 2 | **4** | ✅ **VERIFIED** |
| `[ST]` | `⟨D, F⟩` | Exact Token Match | $\ge$ 7 | **8** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], τ⟩` | Exact Token Match | $\ge$ 2 | **19** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], E, F⟩` | Exact Token Match | $\ge$ 2 | **4** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], D, F⟩` | Exact Token Match | $\ge$ 7 | **8** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], E⟩` | Exact Token Match | $\ge$ 5 | **5** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], D⟩` | Exact Token Match | $\ge$ 10 | **10** | ✅ **VERIFIED** |
| `[ST]` | `⟨A, τ⟩` | Exact Token Match | $\ge$ 3 | **20** | ✅ **VERIFIED** |
| `[ST]` | `⟨A, [nested PAR_1], τ⟩` | Exact Token Match | $\ge$ 2 | **19** | ✅ **VERIFIED** |
| `[ST]` | `⟨A, [nested PAR_1], E, F⟩` | Exact Token Match | $\ge$ 2 | **4** | ✅ **VERIFIED** |
| `[ST]` | `⟨A, [nested PAR_1], D, F⟩` | Exact Token Match | $\ge$ 7 | **8** | ✅ **VERIFIED** |
| `[ST]` | `⟨A, [nested PAR_1], E⟩` | Exact Token Match | $\ge$ 5 | **5** | ✅ **VERIFIED** |
| `[ST]` | `⟨A, [nested PAR_1], D⟩` | Exact Token Match | $\ge$ 10 | **10** | ✅ **VERIFIED** |
| `[ST]` | `⟨A, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 17 | **19** | ✅ **VERIFIED** |

## Audit Summary
- **Perfect Pattern Verifications:** 24
- **Frequency Discrepancies:** 0
- **Ghost Patterns (Fatal):** 0
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 15.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 53.96%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 23.38%
- **Tree Exposure (Local-Strict % of N):** 92.92% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 23.38%
- **Total Forced Volume (incl. unresolved AS, % of N):** 70.00%
- **AS-Resolved Volume (% of N):** 55.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 55.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 0.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 100.00%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 100.00%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 100.00%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 61.04%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 100.00%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 100.00%
- **Max Fractional Exposure (Worst-Case Normalized):** 100.00% (expected length: 3.85 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 100.00% (expected length: 3.85 events)
- **Mean Absolute Exposure Volume:** 3.28 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested PAR_1]`
- **Internal Structure:** `{[τ │ C], [τ │ B]}`
- **Block Frequency:** 17



![nested PAR_1 Internal Diagram](images/nested_ref_audit_test_21_wildCards_nested_PAR_1.png)
