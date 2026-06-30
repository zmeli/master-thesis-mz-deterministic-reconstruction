# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `test_20_loopDouble.csv` |
| **Noise Threshold** | `0.0` |
| **Fitness** | `N/A (skipped)` |
| **Precision** | `N/A (skipped)` |
| **Total Cases in Log** | `5` |
| **Unique Activities** | `7` |
| **XOR Operators** | `5` |
| **LOOP Operators** | `4` |
| **SEQ Operators** | `3` |
| **PAR Operators** | `3` |
| **Binarization Additions** | `2` |
| **Tau Operators Added** | `3` |
| **Total Found Patterns** | `30` |
| **Verified Patterns** | `17` |
| **Discrepancy Patterns** | `3` |
| **Ghost Patterns** | `1` |
| **Nested LOOPs** | `4` |
| **Nested PARs** | `3` |
| **Tree Exposure (Strict, End-to-End % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `14.96%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `0.00%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `0.00%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `100.00%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `100.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `87.38%` |
| **Data Exposure, ST-only (% confirmed)** | `100.00%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `100.00%` |
| **Data Coverage, ST-only (% of real log)** | `26.32%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `73.68%` |
| **Data Coverage, Total (% of real log)** | `100.00%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `100.00%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `100.00%` |
| **Mean Absolute Exposure Volume (events/case)** | `6.69` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_test_20_loopDouble.png)


```text
->( 'A', +( *( 'B', tau ), ->( X( tau, 'D' ), X( tau, +( X( tau, *( 'C', tau ) ), X( tau, *( 'E', tau ) ), X( tau, *( 'F', tau ) ) ) ) ) ), 'G' )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_test_20_loopDouble.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST]` | `A` | Exact Token Match | $\ge$ 5 | **5** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `B` | Exact Token Match | $\ge$ 10 | **10** | ✅ **VERIFIED** |
| `[AS (in PAR_1)]` | `[nested LOOP_2]` | Exact Token Match | $\ge$ 1 | **10** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `τ` | Trivial (no observable event) | $\ge$ 3 | **3** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `D` | Exact Token Match | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `τ` | Trivial (no observable event) | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[ST (in LOOP_4)]` | `C` | Exact Token Match | $\ge$ 5 | **5** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨C⟩` | Exact Token Match | $\ge$ 5 | **5** | ✅ **VERIFIED** |
| `[ST (in LOOP_6)]` | `E` | Exact Token Match | $\ge$ 7 | **7** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨E⟩` | Exact Token Match | $\ge$ 7 | **7** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `F` | Exact Token Match | $\ge$ 4 | **4** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨F⟩` | Exact Token Match | $\ge$ 4 | **4** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_1]` | Exact Token Match | $\ge$ 5 | **5** | ✅ **VERIFIED** |
| `[ST]` | `G` | Exact Token Match | $\ge$ 5 | **5** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], G⟩` | Exact Token Match | $\ge$ 5 | **5** | ✅ **VERIFIED** |
| `[ST]` | `⟨A, [nested PAR_1], G⟩` | Exact Token Match | $\ge$ 5 | **5** | ✅ **VERIFIED** |
| `[ST]` | `⟨A, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 5 | **5** | ✅ **VERIFIED** |
| `[AS (in PAR_3)]` | `[nested PAR_5]` | Exact Token Match | $\ge$ 7 | **4** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_1)]` | `[nested PAR_3]` | Exact Token Match | $\ge$ 7 | **3** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_1)]` | `⟨τ, [nested PAR_3]⟩` | Exact Token Match | $\ge$ 5 | **3** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_1)]` | `⟨D, [nested PAR_3]⟩` | Exact Token Match | $\ge$ 4 | **0** | ❌ **GHOST PATTERN** |

## Audit Summary
- **Perfect Pattern Verifications:** 17
- **Frequency Discrepancies:** 3
- **Ghost Patterns (Fatal):** 1
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 14.96%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 0.00%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 0.00%
- **Total Forced Volume (incl. unresolved AS, % of N):** 100.00%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 100.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 87.38%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 100.00%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 100.00%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 26.32%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 73.68%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 100.00%
- **Max Fractional Exposure (Worst-Case Normalized):** 100.00% (expected length: 10.69 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 100.00% (expected length: 6.69 events)
- **Mean Absolute Exposure Volume:** 6.69 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_2]`
- **Internal Structure:** `(B ∗ τ)`
- **Block Frequency:** 5

- **Max Loop Iterations:** `5`
- **Max Sub-Sequence Length:** `11` steps (if one case consumes all iterations)

![nested LOOP_2 Internal Diagram](images/nested_ref_audit_test_20_loopDouble_nested_LOOP_2.png)

### `[nested LOOP_4]`
- **Internal Structure:** `(C ∗ τ)`
- **Block Frequency:** 5

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_4 Internal Diagram](images/nested_ref_audit_test_20_loopDouble_nested_LOOP_4.png)

### `[nested LOOP_6]`
- **Internal Structure:** `(E ∗ τ)`
- **Block Frequency:** 7

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_6 Internal Diagram](images/nested_ref_audit_test_20_loopDouble_nested_LOOP_6.png)

### `[nested LOOP_7]`
- **Internal Structure:** `(F ∗ τ)`
- **Block Frequency:** 4

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_7 Internal Diagram](images/nested_ref_audit_test_20_loopDouble_nested_LOOP_7.png)

### `[nested PAR_5]`
- **Internal Structure:** `{[τ │ (E ∗ τ)], [τ │ (F ∗ τ)]}`
- **Block Frequency:** 7



![nested PAR_5 Internal Diagram](images/nested_ref_audit_test_20_loopDouble_nested_PAR_5.png)

### `[nested PAR_3]`
- **Internal Structure:** `{[τ │ (C ∗ τ)], [τ │ (E ∗ τ)], [τ │ (F ∗ τ)]}`
- **Block Frequency:** 7



![nested PAR_3 Internal Diagram](images/nested_ref_audit_test_20_loopDouble_nested_PAR_3.png)

### `[nested PAR_1]`
- **Internal Structure:** `{(B ∗ τ), ⟨[τ │ D], [τ │ {[τ │ (C ∗ τ)], [τ │ (E ∗ τ)], [τ │ (F ∗ τ)]}]⟩}`
- **Block Frequency:** 5



![nested PAR_1 Internal Diagram](images/nested_ref_audit_test_20_loopDouble_nested_PAR_1.png)
