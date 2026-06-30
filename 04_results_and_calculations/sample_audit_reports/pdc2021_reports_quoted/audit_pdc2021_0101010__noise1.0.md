# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_0101010.xes` |
| **Noise Threshold** | `1.0` |
| **Fitness** | `0.7717413018336531` |
| **Precision** | `0.6783006722929481` |
| **Total Cases in Log** | `1000` |
| **Unique Activities** | `13` |
| **XOR Operators** | `10` |
| **LOOP Operators** | `5` |
| **SEQ Operators** | `7` |
| **PAR Operators** | `0` |
| **Binarization Additions** | `8` |
| **Tau Operators Added** | `4` |
| **Total Found Patterns** | `31` |
| **Verified Patterns** | `30` |
| **Discrepancy Patterns** | `1` |
| **Ghost Patterns** | `0` |
| **Nested LOOPs** | `5` |
| **Nested PARs** | `0` |
| **Tree Exposure (Strict, End-to-End % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `37.22%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `20.20%` |
| **Tree Exposure (Local-Strict % of N)** | `90.52%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `20.20%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `0.00%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `0.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `97.86%` |
| **Data Exposure, ST-only (% confirmed)** | `96.51%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `96.51%` |
| **Data Coverage, ST-only (% of real log)** | `57.01%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `57.01%` |
| **Data Coverage, Total (% of real log)** | `99.09%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `0.28%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `37.22%` |
| **Mean Absolute Exposure Volume (events/case)** | `1.37` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_0101010__noise1.0.png)


```text
->( 't10', X( 't06', 't11' ), X( 't15', *( 't05', tau ), *( 't04', tau ) ), 't16', 't20', X( tau, *( 't17', tau ), 't21' ), 't22', X( *( 't42', tau ), *( 't55', tau ) ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_0101010__noise1.0.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST]` | `t10` | Exact Token Match | $\ge$ 1000 | **1000** | ✅ **VERIFIED** |
| `[ST]` | `t06` | Exact Token Match | $\ge$ 496 | **496** | ✅ **VERIFIED** |
| `[ST]` | `t11` | Exact Token Match | $\ge$ 249 | **249** | ✅ **VERIFIED** |
| `[ST]` | `t15` | Exact Token Match | $\ge$ 402 | **487** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `t05` | Exact Token Match | $\ge$ 504 | **504** | ✅ **VERIFIED** |
| `[ST]` | `⟨t05⟩` | Exact Token Match | $\ge$ 224 | **284** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_1]` | Exact Token Match | $\ge$ 1 | **383** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `t04` | Exact Token Match | $\ge$ 324 | **324** | ✅ **VERIFIED** |
| `[ST]` | `⟨t04⟩` | Exact Token Match | $\ge$ 144 | **192** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_2]` | Exact Token Match | $\ge$ 1 | **251** | ✅ **VERIFIED** |
| `[ST]` | `t16` | Exact Token Match | $\ge$ 171 | **171** | ✅ **VERIFIED** |
| `[ST]` | `t20` | Exact Token Match | $\ge$ 426 | **426** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t17` | Exact Token Match | $\ge$ 662 | **662** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_3]` | Exact Token Match | $\ge$ 1 | **459** | ✅ **VERIFIED** |
| `[ST]` | `t21` | Exact Token Match | $\ge$ 432 | **504** | ✅ **VERIFIED** |
| `[ST]` | `t22` | Exact Token Match | $\ge$ 268 | **268** | ✅ **VERIFIED** |
| `[ST (in LOOP_4)]` | `t42` | Exact Token Match | $\ge$ 792 | **792** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_4]` | Exact Token Match | $\ge$ 1 | **375** | ✅ **VERIFIED** |
| `[ST (in LOOP_5)]` | `t55` | Exact Token Match | $\ge$ 1649 | **1649** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_5]` | Exact Token Match | $\ge$ 1 | **504** | ✅ **VERIFIED** |
| `[ST]` | `⟨t17, τ⟩` | Exact Token Match | $\ge$ 206 | **256** | ✅ **VERIFIED** |
| `[ST]` | `⟨t21, τ⟩` | Exact Token Match | $\ge$ 164 | **504** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t17⟩` | Exact Token Match | $\ge$ 48 | **256** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t21⟩` | Exact Token Match | $\ge$ 6 | **504** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t20⟩` | Exact Token Match | $\ge$ 255 | **426** | ✅ **VERIFIED** |
| `[ST]` | `⟨t15, τ⟩` | Exact Token Match | $\ge$ 231 | **487** | ✅ **VERIFIED** |
| `[ST]` | `⟨t05, τ⟩` | Exact Token Match | $\ge$ 53 | **284** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06⟩` | Exact Token Match | $\ge$ 496 | **496** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11⟩` | Exact Token Match | $\ge$ 249 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 255 | **1000** | ✅ **VERIFIED** |
| `[ST]` | `⟨t17⟩` | Exact Token Match | $\ge$ 474 | **256** | ⚠️ **DISCREPANCY** |

## Audit Summary
- **Perfect Pattern Verifications:** 30
- **Frequency Discrepancies:** 1
- **Ghost Patterns (Fatal):** 0
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 37.22%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 20.20%
- **Tree Exposure (Local-Strict % of N):** 90.52% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 20.20%
- **Total Forced Volume (incl. unresolved AS, % of N):** 0.00%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 0.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 97.86%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 96.51%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 96.51%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 57.01%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 57.01%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 99.09%
- **Max Fractional Exposure (Worst-Case Normalized):** 0.28% (expected length: 978.61 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 37.22% (expected length: 7.38 events)
- **Mean Absolute Exposure Volume:** 1.37 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_1]`
- **Internal Structure:** `(t05 ∗ τ)`
- **Block Frequency:** 364

- **Max Loop Iterations:** `140`
- **Max Sub-Sequence Length:** `281` steps (if one case consumes all iterations)

![nested LOOP_1 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise1.0_nested_LOOP_1.png)

### `[nested LOOP_2]`
- **Internal Structure:** `(t04 ∗ τ)`
- **Block Frequency:** 234

- **Max Loop Iterations:** `90`
- **Max Sub-Sequence Length:** `181` steps (if one case consumes all iterations)

![nested LOOP_2 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise1.0_nested_LOOP_2.png)

### `[nested LOOP_3]`
- **Internal Structure:** `(t17 ∗ τ)`
- **Block Frequency:** 568

- **Max Loop Iterations:** `94`
- **Max Sub-Sequence Length:** `189` steps (if one case consumes all iterations)

![nested LOOP_3 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise1.0_nested_LOOP_3.png)

### `[nested LOOP_4]`
- **Internal Structure:** `(t42 ∗ τ)`
- **Block Frequency:** 324

- **Max Loop Iterations:** `468`
- **Max Sub-Sequence Length:** `937` steps (if one case consumes all iterations)

![nested LOOP_4 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise1.0_nested_LOOP_4.png)

### `[nested LOOP_5]`
- **Internal Structure:** `(t55 ∗ τ)`
- **Block Frequency:** 676

- **Max Loop Iterations:** `973`
- **Max Sub-Sequence Length:** `1947` steps (if one case consumes all iterations)

![nested LOOP_5 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise1.0_nested_LOOP_5.png)
