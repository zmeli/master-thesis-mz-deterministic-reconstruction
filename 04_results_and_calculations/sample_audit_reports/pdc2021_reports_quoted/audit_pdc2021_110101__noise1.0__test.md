# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_110101.xes` |
| **Noise Threshold** | `1.0` |
| **Fitness** | `0.8067451486847893` |
| **Precision** | `0.4601100412654745` |
| **Total Cases in Log** | `250` |
| **Unique Activities** | `10` |
| **XOR Operators** | `9` |
| **LOOP Operators** | `5` |
| **SEQ Operators** | `5` |
| **PAR Operators** | `0` |
| **Binarization Additions** | `6` |
| **Tau Operators Added** | `4` |
| **Total Found Patterns** | `24` |
| **Verified Patterns** | `22` |
| **Discrepancy Patterns** | `2` |
| **Ghost Patterns** | `0` |
| **Nested LOOPs** | `5` |
| **Nested PARs** | `0` |
| **Tree Exposure (Strict, End-to-End % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `33.92%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `18.31%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `18.31%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `0.00%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `0.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `97.02%` |
| **Data Exposure, ST-only (% confirmed)** | `93.84%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `93.84%` |
| **Data Coverage, ST-only (% of real log)** | `34.28%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `34.28%` |
| **Data Coverage, Total (% of real log)** | `100.00%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `0.60%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `33.92%` |
| **Mean Absolute Exposure Volume (events/case)** | `1.42` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_110101__noise1.0__test.png)


```text
->( 't10', X( 't06', 't11' ), X( *( 't15', tau ), *( 't05', tau ) ), 't16', 't20', X( tau, *( 't65', tau ), *( 't17', tau ), *( 't55', tau ) ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_110101__noise1.0__test.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST]` | `t10` | Exact Token Match | $\ge$ 250 | **250** | ✅ **VERIFIED** |
| `[ST]` | `t06` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `t11` | Exact Token Match | $\ge$ 146 | **146** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `t15` | Exact Token Match | $\ge$ 82 | **82** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `t05` | Exact Token Match | $\ge$ 144 | **144** | ✅ **VERIFIED** |
| `[ST]` | `t16` | Exact Token Match | $\ge$ 84 | **84** | ✅ **VERIFIED** |
| `[ST]` | `t20` | Exact Token Match | $\ge$ 205 | **205** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t65` | Exact Token Match | $\ge$ 432 | **432** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_3]` | Exact Token Match | $\ge$ 1 | **247** | ✅ **VERIFIED** |
| `[ST (in LOOP_4)]` | `t17` | Exact Token Match | $\ge$ 295 | **295** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_4]` | Exact Token Match | $\ge$ 1 | **220** | ✅ **VERIFIED** |
| `[ST (in LOOP_5)]` | `t55` | Exact Token Match | $\ge$ 622 | **622** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_5]` | Exact Token Match | $\ge$ 1 | **224** | ✅ **VERIFIED** |
| `[ST]` | `⟨t16, t20⟩` | Exact Token Match | $\ge$ 39 | **84** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t20⟩` | Exact Token Match | $\ge$ 121 | **205** | ✅ **VERIFIED** |
| `[ST]` | `⟨t05, τ, t20⟩` | Exact Token Match | $\ge$ 15 | **62** | ✅ **VERIFIED** |
| `[ST]` | `⟨t05, τ⟩` | Exact Token Match | $\ge$ 60 | **89** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, t05⟩` | Exact Token Match | $\ge$ 40 | **89** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, t05⟩` | Exact Token Match | $\ge$ 40 | **89** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11⟩` | Exact Token Match | $\ge$ 146 | **146** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 103 | **250** | ✅ **VERIFIED** |
| `[ST]` | `⟨t15⟩` | Exact Token Match | $\ge$ 82 | **46** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t05⟩` | Exact Token Match | $\ge$ 144 | **89** | ⚠️ **DISCREPANCY** |

## Audit Summary
- **Perfect Pattern Verifications:** 22
- **Frequency Discrepancies:** 2
- **Ghost Patterns (Fatal):** 0
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 33.92%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 18.31%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 18.31%
- **Total Forced Volume (incl. unresolved AS, % of N):** 0.00%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 0.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 97.02%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 93.84%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 93.84%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 34.28%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 34.28%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 100.00%
- **Max Fractional Exposure (Worst-Case Normalized):** 0.60% (expected length: 511.65 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 33.92% (expected length: 9.04 events)
- **Mean Absolute Exposure Volume:** 1.42 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_1]`
- **Internal Structure:** `(t15 ∗ τ)`
- **Block Frequency:** 82

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_1 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise1.0__test_nested_LOOP_1.png)

### `[nested LOOP_2]`
- **Internal Structure:** `(t05 ∗ τ)`
- **Block Frequency:** 144

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_2 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise1.0__test_nested_LOOP_2.png)

### `[nested LOOP_3]`
- **Internal Structure:** `(t65 ∗ τ)`
- **Block Frequency:** 80

- **Max Loop Iterations:** `352`
- **Max Sub-Sequence Length:** `705` steps (if one case consumes all iterations)

![nested LOOP_3 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise1.0__test_nested_LOOP_3.png)

### `[nested LOOP_4]`
- **Internal Structure:** `(t17 ∗ τ)`
- **Block Frequency:** 55

- **Max Loop Iterations:** `240`
- **Max Sub-Sequence Length:** `481` steps (if one case consumes all iterations)

![nested LOOP_4 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise1.0__test_nested_LOOP_4.png)

### `[nested LOOP_5]`
- **Internal Structure:** `(t55 ∗ τ)`
- **Block Frequency:** 115

- **Max Loop Iterations:** `507`
- **Max Sub-Sequence Length:** `1015` steps (if one case consumes all iterations)

![nested LOOP_5 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise1.0__test_nested_LOOP_5.png)
