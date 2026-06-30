# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `test_16_tauabiyss.csv` |
| **Noise Threshold** | `0.0` |
| **Fitness** | `N/A (skipped)` |
| **Precision** | `N/A (skipped)` |
| **Total Cases in Log** | `8` |
| **Unique Activities** | `6` |
| **XOR Operators** | `4` |
| **LOOP Operators** | `0` |
| **SEQ Operators** | `5` |
| **PAR Operators** | `0` |
| **Binarization Additions** | `1` |
| **Tau Operators Added** | `4` |
| **Total Found Patterns** | `87` |
| **Verified Patterns** | `45` |
| **Discrepancy Patterns** | `0` |
| **Ghost Patterns** | `0` |
| **Nested LOOPs** | `0` |
| **Nested PARs** | `0` |
| **Tree Exposure (Strict, End-to-End % of N)** | `100.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `100.00%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `100.00%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `100.00%` |
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
| **Mean Absolute Exposure Volume (events/case)** | `3.88` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_test_16_tauabiyss.png)


```text
->( 'A', X( tau, ->( 'B', X( tau, ->( 'C', X( tau, ->( 'D', X( tau, 'E' ) ) ) ) ) ) ), 'F' )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_test_16_tauabiyss.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST]` | `A` | Exact Token Match | $\ge$ 8 | **8** | ✅ **VERIFIED** |
| `[ST]` | `τ` | Trivial (no observable event) | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[ST]` | `B` | Exact Token Match | $\ge$ 6 | **6** | ✅ **VERIFIED** |
| `[ST]` | `C` | Exact Token Match | $\ge$ 4 | **4** | ✅ **VERIFIED** |
| `[ST]` | `τ` | Trivial (no observable event) | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `D` | Exact Token Match | $\ge$ 3 | **3** | ✅ **VERIFIED** |
| `[ST]` | `E` | Exact Token Match | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[ST]` | `⟨D, τ⟩` | Exact Token Match | $\ge$ 1 | **3** | ✅ **VERIFIED** |
| `[ST]` | `⟨D, E⟩` | Exact Token Match | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[ST]` | `⟨C, τ⟩` | Exact Token Match | $\ge$ 1 | **4** | ✅ **VERIFIED** |
| `[ST]` | `⟨C, D, τ⟩` | Exact Token Match | $\ge$ 1 | **3** | ✅ **VERIFIED** |
| `[ST]` | `⟨C, D, E⟩` | Exact Token Match | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[ST]` | `⟨C, D⟩` | Exact Token Match | $\ge$ 3 | **3** | ✅ **VERIFIED** |
| `[ST]` | `⟨B, τ⟩` | Exact Token Match | $\ge$ 2 | **6** | ✅ **VERIFIED** |
| `[ST]` | `⟨B, C, τ⟩` | Exact Token Match | $\ge$ 1 | **4** | ✅ **VERIFIED** |
| `[ST]` | `⟨B, C, D, τ⟩` | Exact Token Match | $\ge$ 1 | **3** | ✅ **VERIFIED** |
| `[ST]` | `⟨B, C, D, E⟩` | Exact Token Match | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[ST]` | `⟨B, C, D⟩` | Exact Token Match | $\ge$ 3 | **3** | ✅ **VERIFIED** |
| `[ST]` | `⟨B, C⟩` | Exact Token Match | $\ge$ 4 | **4** | ✅ **VERIFIED** |
| `[ST]` | `F` | Exact Token Match | $\ge$ 8 | **8** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, F⟩` | Exact Token Match | $\ge$ 2 | **8** | ✅ **VERIFIED** |
| `[ST]` | `⟨B, τ, F⟩` | Exact Token Match | $\ge$ 2 | **6** | ✅ **VERIFIED** |
| `[ST]` | `⟨B, C, τ, F⟩` | Exact Token Match | $\ge$ 1 | **4** | ✅ **VERIFIED** |
| `[ST]` | `⟨B, C, D, τ, F⟩` | Exact Token Match | $\ge$ 1 | **3** | ✅ **VERIFIED** |
| `[ST]` | `⟨B, C, D, E, F⟩` | Exact Token Match | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[ST]` | `⟨C, τ, F⟩` | Exact Token Match | $\ge$ 1 | **4** | ✅ **VERIFIED** |
| `[ST]` | `⟨C, D, τ, F⟩` | Exact Token Match | $\ge$ 1 | **3** | ✅ **VERIFIED** |
| `[ST]` | `⟨C, D, E, F⟩` | Exact Token Match | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, F⟩` | Exact Token Match | $\ge$ 1 | **8** | ✅ **VERIFIED** |
| `[ST]` | `⟨D, τ, F⟩` | Exact Token Match | $\ge$ 1 | **3** | ✅ **VERIFIED** |
| `[ST]` | `⟨D, E, F⟩` | Exact Token Match | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[ST]` | `⟨E, F⟩` | Exact Token Match | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[ST]` | `⟨A, τ, F⟩` | Exact Token Match | $\ge$ 2 | **8** | ✅ **VERIFIED** |
| `[ST]` | `⟨A, B, τ, F⟩` | Exact Token Match | $\ge$ 2 | **6** | ✅ **VERIFIED** |
| `[ST]` | `⟨A, B, C, τ, F⟩` | Exact Token Match | $\ge$ 1 | **4** | ✅ **VERIFIED** |
| `[ST]` | `⟨A, B, C, D, τ, F⟩` | Exact Token Match | $\ge$ 1 | **3** | ✅ **VERIFIED** |
| `[ST]` | `⟨A, B, C, D, E, F⟩` | Exact Token Match | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[ST]` | `⟨A, τ⟩` | Exact Token Match | $\ge$ 2 | **8** | ✅ **VERIFIED** |
| `[ST]` | `⟨A, B, τ⟩` | Exact Token Match | $\ge$ 2 | **6** | ✅ **VERIFIED** |
| `[ST]` | `⟨A, B, C, τ⟩` | Exact Token Match | $\ge$ 1 | **4** | ✅ **VERIFIED** |
| `[ST]` | `⟨A, B, C, D, τ⟩` | Exact Token Match | $\ge$ 1 | **3** | ✅ **VERIFIED** |
| `[ST]` | `⟨A, B, C, D, E⟩` | Exact Token Match | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[ST]` | `⟨A, B, C, D⟩` | Exact Token Match | $\ge$ 3 | **3** | ✅ **VERIFIED** |
| `[ST]` | `⟨A, B, C⟩` | Exact Token Match | $\ge$ 4 | **4** | ✅ **VERIFIED** |
| `[ST]` | `⟨A, B⟩` | Exact Token Match | $\ge$ 6 | **6** | ✅ **VERIFIED** |

## Audit Summary
- **Perfect Pattern Verifications:** 45
- **Frequency Discrepancies:** 0
- **Ghost Patterns (Fatal):** 0
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 100.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 100.00%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 100.00%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 100.00%
- **Total Forced Volume (incl. unresolved AS, % of N):** 100.00%
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
- **Max Fractional Exposure (Worst-Case Normalized):** 100.00% (expected length: 3.88 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 100.00% (expected length: 3.88 events)
- **Mean Absolute Exposure Volume:** 3.88 events/case