# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_0000101.xes` |
| **Noise Threshold** | `1.0` |
| **Fitness** | `0.6707962121212122` |
| **Precision** | `0.5383019038166561` |
| **Total Cases in Log** | `1000` |
| **Unique Activities** | `10` |
| **XOR Operators** | `10` |
| **LOOP Operators** | `9` |
| **SEQ Operators** | `0` |
| **PAR Operators** | `0` |
| **Binarization Additions** | `9` |
| **Tau Operators Added** | `0` |
| **Total Found Patterns** | `19` |
| **Verified Patterns** | `19` |
| **Discrepancy Patterns** | `0` |
| **Ghost Patterns** | `0` |
| **Nested LOOPs** | `9` |
| **Nested PARs** | `0` |
| **Tree Exposure (Strict, End-to-End % of N)** | `9.90%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `9.90%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `0.00%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `0.00%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `10.80%` |
| **AS-Resolved Volume (% of N)** | `0.90%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.90%` |
| **AS-Opaque Volume (% of N)** | `0.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `100.00%` |
| **Data Exposure, ST-only (% confirmed)** | `100.00%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `100.00%` |
| **Data Coverage, ST-only (% of real log)** | `9.90%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `9.90%` |
| **Data Coverage, Total (% of real log)** | `100.00%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `10.80%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `10.80%` |
| **Mean Absolute Exposure Volume (events/case)** | `0.13` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_0000101__noise1.0.png)


```text
X( tau, *( 't08', tau ), *( 't02', tau ), *( 't09', tau ), *( 't71', tau ), *( 't17', tau ), *( 't01', tau ), *( 't05', tau ), *( 't10', tau ), 't66', *( 't04', tau ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_0000101__noise1.0.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST (in LOOP_1)]` | `t08` | Exact Token Match | $\ge$ 99 | **99** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_1]` | Exact Token Match | $\ge$ 1 | **97** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `t02` | Exact Token Match | $\ge$ 513 | **513** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_2]` | Exact Token Match | $\ge$ 1 | **505** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t09` | Exact Token Match | $\ge$ 1003 | **1003** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_3]` | Exact Token Match | $\ge$ 1 | **985** | ✅ **VERIFIED** |
| `[ST (in LOOP_4)]` | `t71` | Exact Token Match | $\ge$ 63 | **63** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_4]` | Exact Token Match | $\ge$ 1 | **61** | ✅ **VERIFIED** |
| `[ST (in LOOP_5)]` | `t17` | Exact Token Match | $\ge$ 329 | **329** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_5]` | Exact Token Match | $\ge$ 1 | **327** | ✅ **VERIFIED** |
| `[ST (in LOOP_6)]` | `t01` | Exact Token Match | $\ge$ 215 | **215** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_6]` | Exact Token Match | $\ge$ 1 | **210** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `t05` | Exact Token Match | $\ge$ 99 | **99** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_7]` | Exact Token Match | $\ge$ 1 | **95** | ✅ **VERIFIED** |
| `[ST (in LOOP_8)]` | `t10` | Exact Token Match | $\ge$ 997 | **997** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_8]` | Exact Token Match | $\ge$ 1 | **981** | ✅ **VERIFIED** |
| `[ST]` | `t66` | Exact Token Match | $\ge$ 99 | **386** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `t04` | Exact Token Match | $\ge$ 194 | **194** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_9]` | Exact Token Match | $\ge$ 1 | **190** | ✅ **VERIFIED** |

## Audit Summary
- **Perfect Pattern Verifications:** 19
- **Frequency Discrepancies:** 0
- **Ghost Patterns (Fatal):** 0
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 9.90%
- **Tree Exposure (Strict, Fragment-Level % of N):** 9.90%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 0.00%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 0.00%
- **Total Forced Volume (incl. unresolved AS, % of N):** 10.80%
- **AS-Resolved Volume (% of N):** 0.90%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.90%
- **AS-Opaque Volume (% of N):** 0.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 100.00%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 100.00%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 100.00%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 9.90%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 9.90%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 100.00%
- **Max Fractional Exposure (Worst-Case Normalized):** 10.80% (expected length: 747.00 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 10.80% (expected length: 3.61 events)
- **Mean Absolute Exposure Volume:** 0.13 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_1]`
- **Internal Structure:** `(t08 ∗ τ)`
- **Block Frequency:** 25

- **Max Loop Iterations:** `74`
- **Max Sub-Sequence Length:** `149` steps (if one case consumes all iterations)

![nested LOOP_1 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_1.png)

### `[nested LOOP_2]`
- **Internal Structure:** `(t02 ∗ τ)`
- **Block Frequency:** 132

- **Max Loop Iterations:** `381`
- **Max Sub-Sequence Length:** `763` steps (if one case consumes all iterations)

![nested LOOP_2 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_2.png)

### `[nested LOOP_3]`
- **Internal Structure:** `(t09 ∗ τ)`
- **Block Frequency:** 257

- **Max Loop Iterations:** `746`
- **Max Sub-Sequence Length:** `1493` steps (if one case consumes all iterations)

![nested LOOP_3 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_3.png)

### `[nested LOOP_4]`
- **Internal Structure:** `(t71 ∗ τ)`
- **Block Frequency:** 16

- **Max Loop Iterations:** `47`
- **Max Sub-Sequence Length:** `95` steps (if one case consumes all iterations)

![nested LOOP_4 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_4.png)

### `[nested LOOP_5]`
- **Internal Structure:** `(t17 ∗ τ)`
- **Block Frequency:** 84

- **Max Loop Iterations:** `245`
- **Max Sub-Sequence Length:** `491` steps (if one case consumes all iterations)

![nested LOOP_5 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_5.png)

### `[nested LOOP_6]`
- **Internal Structure:** `(t01 ∗ τ)`
- **Block Frequency:** 55

- **Max Loop Iterations:** `160`
- **Max Sub-Sequence Length:** `321` steps (if one case consumes all iterations)

![nested LOOP_6 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_6.png)

### `[nested LOOP_7]`
- **Internal Structure:** `(t05 ∗ τ)`
- **Block Frequency:** 25

- **Max Loop Iterations:** `74`
- **Max Sub-Sequence Length:** `149` steps (if one case consumes all iterations)

![nested LOOP_7 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_7.png)

### `[nested LOOP_8]`
- **Internal Structure:** `(t10 ∗ τ)`
- **Block Frequency:** 257

- **Max Loop Iterations:** `740`
- **Max Sub-Sequence Length:** `1481` steps (if one case consumes all iterations)

![nested LOOP_8 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_8.png)

### `[nested LOOP_9]`
- **Internal Structure:** `(t04 ∗ τ)`
- **Block Frequency:** 50

- **Max Loop Iterations:** `144`
- **Max Sub-Sequence Length:** `289` steps (if one case consumes all iterations)

![nested LOOP_9 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_9.png)
