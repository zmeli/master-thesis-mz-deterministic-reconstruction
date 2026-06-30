# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `test_14_asymTree.csv` |
| **Noise Threshold** | `0.0` |
| **Fitness** | `N/A (skipped)` |
| **Precision** | `N/A (skipped)` |
| **Total Cases in Log** | `5` |
| **Unique Activities** | `8` |
| **XOR Operators** | `4` |
| **LOOP Operators** | `2` |
| **SEQ Operators** | `4` |
| **PAR Operators** | `2` |
| **Binarization Additions** | `1` |
| **Tau Operators Added** | `3` |
| **Total Found Patterns** | `36` |
| **Verified Patterns** | `24` |
| **Discrepancy Patterns** | `0` |
| **Ghost Patterns** | `0` |
| **Nested LOOPs** | `2` |
| **Nested PARs** | `2` |
| **Tree Exposure (Strict, End-to-End % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `6.45%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `0.00%` |
| **Tree Exposure (Local-Strict % of N)** | `96.77%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `0.00%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `0.00%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `0.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `100.00%` |
| **Data Exposure, ST-only (% confirmed)** | `100.00%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `100.00%` |
| **Data Coverage, ST-only (% of real log)** | `18.18%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `51.52%` |
| **Data Coverage, Total (% of real log)** | `100.00%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `100.00%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `100.00%` |
| **Mean Absolute Exposure Volume (events/case)** | `4.33` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_test_14_asymTree.png)


```text
->( *( 'A', tau ), X( tau, ->( 'D', X( tau, 'E' ) ) ), +( 'F', ->( X( tau, +( 'C', 'B' ) ), *( 'G', 'H' ) ) ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_test_14_asymTree.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST (in LOOP_1)]` | `A` | Exact Token Match | $\ge$ 8 | **8** | ✅ **VERIFIED** |
| `[ST]` | `⟨A⟩` | Exact Token Match | $\ge$ 2 | **3** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_1]` | Exact Token Match | $\ge$ 1 | **5** | ✅ **VERIFIED** |
| `[ST]` | `τ` | Trivial (no observable event) | $\ge$ 3 | **3** | ✅ **VERIFIED** |
| `[ST]` | `D` | Exact Token Match | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[ST]` | `τ` | Trivial (no observable event) | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `E` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨D, τ⟩` | Exact Token Match | $\ge$ 1 | **2** | ✅ **VERIFIED** |
| `[ST]` | `⟨D, E⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST (in PAR_2)]` | `F` | Exact Token Match | $\ge$ 5 | **5** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `C` | Exact Token Match | $\ge$ 3 | **3** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `B` | Exact Token Match | $\ge$ 3 | **3** | ✅ **VERIFIED** |
| `[AS (in PAR_2)]` | `[nested PAR_3]` | Exact Token Match | $\ge$ 3 | **3** | ✅ **VERIFIED** |
| `[ST (in LOOP_4)]` | `G` | Exact Token Match | $\ge$ 6 | **8** | ✅ **VERIFIED** |
| `[ST (in LOOP_4)]` | `H` | Exact Token Match | $\ge$ 3 | **3** | ✅ **VERIFIED** |
| `[AS (in PAR_2)]` | `[nested LOOP_4]` | Exact Token Match | $\ge$ 1 | **3** | ✅ **VERIFIED** |
| `[ST (in PAR_2)]` | `⟨[nested PAR_3], [nested LOOP_4]⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST (in PAR_2)]` | `τ` | Trivial (no observable event) | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_2]` | Exact Token Match | $\ge$ 5 | **5** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_2]⟩` | Exact Token Match | $\ge$ 3 | **5** | ✅ **VERIFIED** |
| `[ST]` | `⟨D, τ, [nested PAR_2]⟩` | Exact Token Match | $\ge$ 1 | **2** | ✅ **VERIFIED** |
| `[ST]` | `⟨D, E, [nested PAR_2]⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_2]⟩` | Exact Token Match | $\ge$ 1 | **5** | ✅ **VERIFIED** |
| `[ST]` | `⟨E, [nested PAR_2]⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |

## Audit Summary
- **Perfect Pattern Verifications:** 24
- **Frequency Discrepancies:** 0
- **Ghost Patterns (Fatal):** 0
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 6.45%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 0.00%
- **Tree Exposure (Local-Strict % of N):** 96.77% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 0.00%
- **Total Forced Volume (incl. unresolved AS, % of N):** 0.00%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 0.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 100.00%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 100.00%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 100.00%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 18.18%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 51.52%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 100.00%
- **Max Fractional Exposure (Worst-Case Normalized):** 100.00% (expected length: 10.40 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 100.00% (expected length: 6.20 events)
- **Mean Absolute Exposure Volume:** 4.33 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_1]`
- **Internal Structure:** `(A ∗ τ)`
- **Block Frequency:** 5

- **Max Loop Iterations:** `3`
- **Max Sub-Sequence Length:** `7` steps (if one case consumes all iterations)

![nested LOOP_1 Internal Diagram](images/nested_ref_audit_test_14_asymTree_nested_LOOP_1.png)

### `[nested PAR_3]`
- **Internal Structure:** `{C, B}`
- **Block Frequency:** 3



![nested PAR_3 Internal Diagram](images/nested_ref_audit_test_14_asymTree_nested_PAR_3.png)

### `[nested LOOP_4]`
- **Internal Structure:** `(G ∗ H)`
- **Block Frequency:** 3

- **Max Loop Iterations:** `3`
- **Max Sub-Sequence Length:** `7` steps (if one case consumes all iterations)

![nested LOOP_4 Internal Diagram](images/nested_ref_audit_test_14_asymTree_nested_LOOP_4.png)

### `[nested PAR_2]`
- **Internal Structure:** `{F, [⟨[τ │ {C, B}], (G ∗ H)⟩ │ τ]}`
- **Block Frequency:** 5



![nested PAR_2 Internal Diagram](images/nested_ref_audit_test_14_asymTree_nested_PAR_2.png)
