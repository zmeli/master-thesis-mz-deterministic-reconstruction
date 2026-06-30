# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_0011013.xes` |
| **Noise Threshold** | `1.0` |
| **Fitness** | `0.9335166666666667` |
| **Precision** | `0.20284128328158813` |
| **Total Cases in Log** | `1000` |
| **Unique Activities** | `4` |
| **XOR Operators** | `4` |
| **LOOP Operators** | `1` |
| **SEQ Operators** | `0` |
| **PAR Operators** | `0` |
| **Binarization Additions** | `3` |
| **Tau Operators Added** | `0` |
| **Total Found Patterns** | `6` |
| **Verified Patterns** | `6` |
| **Discrepancy Patterns** | `0` |
| **Ghost Patterns** | `0` |
| **Nested LOOPs** | `1` |
| **Nested PARs** | `0` |
| **Tree Exposure (Strict, End-to-End % of N)** | `76.20%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `76.20%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `0.00%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `0.00%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `76.30%` |
| **AS-Resolved Volume (% of N)** | `0.10%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.10%` |
| **AS-Opaque Volume (% of N)** | `0.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `100.00%` |
| **Data Exposure, ST-only (% confirmed)** | `100.00%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `100.00%` |
| **Data Coverage, ST-only (% of real log)** | `78.04%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `78.04%` |
| **Data Coverage, Total (% of real log)** | `100.00%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `76.30%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `76.30%` |
| **Mean Absolute Exposure Volume (events/case)** | `0.76` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_0011013__noise1.0.png)


```text
X( tau, 't65', 't06', 't71', *( 't17', tau ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_0011013__noise1.0.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST]` | `t65` | Exact Token Match | $\ge$ 245 | **397** | ✅ **VERIFIED** |
| `[ST]` | `t06` | Exact Token Match | $\ge$ 299 | **485** | ✅ **VERIFIED** |
| `[ST]` | `t71` | Exact Token Match | $\ge$ 73 | **118** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `t17` | Exact Token Match | $\ge$ 621 | **621** | ✅ **VERIFIED** |
| `[ST]` | `⟨t17⟩` | Exact Token Match | $\ge$ 145 | **265** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_1]` | Exact Token Match | $\ge$ 1 | **443** | ✅ **VERIFIED** |

## Audit Summary
- **Perfect Pattern Verifications:** 6
- **Frequency Discrepancies:** 0
- **Ghost Patterns (Fatal):** 0
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 76.20%
- **Tree Exposure (Strict, Fragment-Level % of N):** 76.20%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 0.00%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 0.00%
- **Total Forced Volume (incl. unresolved AS, % of N):** 76.30%
- **AS-Resolved Volume (% of N):** 0.10%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.10%
- **AS-Opaque Volume (% of N):** 0.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 100.00%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 100.00%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 100.00%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 78.04%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 78.04%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 100.00%
- **Max Fractional Exposure (Worst-Case Normalized):** 76.30% (expected length: 239.00 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 76.30% (expected length: 1.24 events)
- **Mean Absolute Exposure Volume:** 0.76 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_1]`
- **Internal Structure:** `(t17 ∗ τ)`
- **Block Frequency:** 383

- **Max Loop Iterations:** `238`
- **Max Sub-Sequence Length:** `477` steps (if one case consumes all iterations)

![nested LOOP_1 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise1.0_nested_LOOP_1.png)
