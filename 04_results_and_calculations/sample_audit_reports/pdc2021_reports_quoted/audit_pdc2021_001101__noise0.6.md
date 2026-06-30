# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_001101.xes` |
| **Noise Threshold** | `0.6` |
| **Fitness** | `0.8181728468990936` |
| **Precision** | `0.7052810902896082` |
| **Total Cases in Log** | `250` |
| **Unique Activities** | `33` |
| **XOR Operators** | `19` |
| **LOOP Operators** | `15` |
| **SEQ Operators** | `22` |
| **PAR Operators** | `6` |
| **Binarization Additions** | `17` |
| **Tau Operators Added** | `15` |
| **Total Found Patterns** | `152` |
| **Verified Patterns** | `95` |
| **Discrepancy Patterns** | `14` |
| **Ghost Patterns** | `0` |
| **Nested LOOPs** | `15` |
| **Nested PARs** | `6` |
| **Tree Exposure (Strict, End-to-End % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `11.78%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `5.68%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `39.30%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `0.00%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `0.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `97.93%` |
| **Data Exposure, ST-only (% confirmed)** | `94.09%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `96.25%` |
| **Data Coverage, ST-only (% of real log)** | `21.06%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `50.47%` |
| **Data Coverage, Total (% of real log)** | `97.46%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `2.92%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `100.00%` |
| **Mean Absolute Exposure Volume (events/case)** | `17.67` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_001101__noise0.6.png)


```text
->( 't10', X( 't06', 't11' ), +( *( 't05', tau ), X( *( 't15', tau ), *( 't04', tau ) ) ), 't16', 't20', +( *( 't17', tau ), ->( *( 't21', tau ), 't24' ) ), 't23', X( 't22', ->( 't34', 't26', 't27', 't28' ) ), *( 't42', tau ), X( tau, 't71' ), +( *( 't40', tau ), ->( *( ->( 't39', 't43', 't44', *( 't36', tau ) ), tau ), *( ->( X( tau, 't46' ), +( *( 't62', tau ), X( tau, *( 't37', tau ) ), *( 't56', tau ), ->( *( 't47', tau ), 't48', *( 't68', tau ) ) ), X( 't65', 't55' ) ), tau ) ) ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_001101__noise0.6.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST]` | `t10` | Exact Token Match | $\ge$ 250 | **250** | ✅ **VERIFIED** |
| `[ST]` | `t06` | Exact Token Match | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[ST]` | `t11` | Exact Token Match | $\ge$ 133 | **133** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `t05` | Exact Token Match | $\ge$ 117 | **117** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t05⟩` | Exact Token Match | $\ge$ 49 | **117** | ✅ **VERIFIED** |
| `[AS (in PAR_1)]` | `[nested LOOP_2]` | Exact Token Match | $\ge$ 1 | **117** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t15` | Exact Token Match | $\ge$ 77 | **77** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t15⟩` | Exact Token Match | $\ge$ 77 | **77** | ✅ **VERIFIED** |
| `[ST (in LOOP_4)]` | `t04` | Exact Token Match | $\ge$ 6 | **6** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t04⟩` | Exact Token Match | $\ge$ 6 | **6** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_1]` | Exact Token Match | $\ge$ 83 | **118** | ✅ **VERIFIED** |
| `[ST]` | `t16` | Exact Token Match | $\ge$ 64 | **64** | ✅ **VERIFIED** |
| `[ST]` | `t20` | Exact Token Match | $\ge$ 192 | **192** | ✅ **VERIFIED** |
| `[ST (in LOOP_6)]` | `t17` | Exact Token Match | $\ge$ 266 | **266** | ✅ **VERIFIED** |
| `[AS (in PAR_5)]` | `[nested LOOP_6]` | Exact Token Match | $\ge$ 1 | **266** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `t21` | Exact Token Match | $\ge$ 273 | **273** | ✅ **VERIFIED** |
| `[AS (in PAR_5)]` | `[nested LOOP_7]` | Exact Token Match | $\ge$ 1 | **273** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t24` | Exact Token Match | $\ge$ 110 | **110** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨[nested LOOP_7], t24⟩` | Exact Token Match | $\ge$ 1 | **110** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_5]` | Exact Token Match | $\ge$ 110 | **248** | ✅ **VERIFIED** |
| `[ST]` | `t22` | Exact Token Match | $\ge$ 123 | **130** | ✅ **VERIFIED** |
| `[ST]` | `t28` | Exact Token Match | $\ge$ 72 | **72** | ✅ **VERIFIED** |
| `[ST]` | `⟨t27, τ⟩` | Exact Token Match | $\ge$ 38 | **106** | ✅ **VERIFIED** |
| `[ST]` | `⟨t26, t27, τ⟩` | Exact Token Match | $\ge$ 38 | **106** | ✅ **VERIFIED** |
| `[ST]` | `⟨t34, t26, t27, τ⟩` | Exact Token Match | $\ge$ 38 | **56** | ✅ **VERIFIED** |
| `[ST]` | `⟨t34, τ⟩` | Exact Token Match | $\ge$ 17 | **106** | ✅ **VERIFIED** |
| `[ST (in LOOP_8)]` | `t42` | Exact Token Match | $\ge$ 316 | **316** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_8]` | Exact Token Match | $\ge$ 1 | **217** | ✅ **VERIFIED** |
| `[ST]` | `t71` | Exact Token Match | $\ge$ 38 | **38** | ✅ **VERIFIED** |
| `[ST (in LOOP_10)]` | `t40` | Exact Token Match | $\ge$ 229 | **229** | ✅ **VERIFIED** |
| `[ST (in PAR_9)]` | `⟨t40⟩` | Exact Token Match | $\ge$ 229 | **229** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `t39` | Exact Token Match | $\ge$ 337 | **337** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `t43` | Exact Token Match | $\ge$ 154 | **154** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `t44` | Exact Token Match | $\ge$ 154 | **154** | ✅ **VERIFIED** |
| `[ST (in LOOP_12)]` | `t36` | Exact Token Match | $\ge$ 438 | **438** | ✅ **VERIFIED** |
| `[AS (in LOOP_11)]` | `[nested LOOP_12]` | Exact Token Match | $\ge$ 1 | **210** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `⟨t44, [nested LOOP_12]⟩` | Exact Token Match | $\ge$ 1 | **154** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `⟨t43, t44, [nested LOOP_12]⟩` | Exact Token Match | $\ge$ 1 | **154** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `⟨t43, t44⟩` | Exact Token Match | $\ge$ 154 | **154** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `⟨t39, t43, t44, [nested LOOP_12]⟩` | Exact Token Match | $\ge$ 1 | **154** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `⟨t39, τ⟩` | Exact Token Match | $\ge$ 183 | **337** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `⟨t39, t43, t44⟩` | Exact Token Match | $\ge$ 154 | **154** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `⟨t39, t43⟩` | Exact Token Match | $\ge$ 154 | **154** | ✅ **VERIFIED** |
| `[ST (in PAR_9)]` | `⟨t39, τ⟩` | Exact Token Match | $\ge$ 9 | **337** | ✅ **VERIFIED** |
| `[ST (in PAR_9)]` | `⟨t39, [nested XOR_13]⟩` | Exact Token Match | $\ge$ 154.0 | **154** | ✅ **VERIFIED** |
| `[AS (in PAR_9)]` | `[nested LOOP_11]` | Exact Token Match | $\ge$ 1 | **154** | ✅ **VERIFIED** |
| `[ST (in LOOP_14)]` | `t46` | Exact Token Match | $\ge$ 327 | **327** | ✅ **VERIFIED** |
| `[ST (in LOOP_16)]` | `t62` | Exact Token Match | $\ge$ 264 | **264** | ✅ **VERIFIED** |
| `[ST (in PAR_15)]` | `⟨t62⟩` | Exact Token Match | $\ge$ 120 | **264** | ✅ **VERIFIED** |
| `[AS (in PAR_15)]` | `[nested LOOP_16]` | Exact Token Match | $\ge$ 1 | **264** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `t37` | Exact Token Match | $\ge$ 192 | **192** | ✅ **VERIFIED** |
| `[ST (in PAR_17)]` | `⟨t37⟩` | Exact Token Match | $\ge$ 192 | **192** | ✅ **VERIFIED** |
| `[ST (in LOOP_20)]` | `t56` | Exact Token Match | $\ge$ 495 | **495** | ✅ **VERIFIED** |
| `[AS (in PAR_19)]` | `[nested LOOP_20]` | Exact Token Match | $\ge$ 1 | **495** | ✅ **VERIFIED** |
| `[ST (in LOOP_21)]` | `t47` | Exact Token Match | $\ge$ 222 | **222** | ✅ **VERIFIED** |
| `[ST (in PAR_19)]` | `⟨t47⟩` | Exact Token Match | $\ge$ 148 | **222** | ✅ **VERIFIED** |
| `[AS (in PAR_19)]` | `[nested LOOP_21]` | Exact Token Match | $\ge$ 1 | **222** | ✅ **VERIFIED** |
| `[ST (in PAR_19)]` | `t48` | Exact Token Match | $\ge$ 185 | **185** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `t68` | Exact Token Match | $\ge$ 185 | **185** | ✅ **VERIFIED** |
| `[ST (in PAR_19)]` | `⟨t68⟩` | Exact Token Match | $\ge$ 185 | **185** | ✅ **VERIFIED** |
| `[ST (in PAR_19)]` | `⟨t48, t68⟩` | Exact Token Match | $\ge$ 185 | **185** | ✅ **VERIFIED** |
| `[ST (in PAR_19)]` | `⟨t47, t48, t68⟩` | Exact Token Match | $\ge$ 148 | **167** | ✅ **VERIFIED** |
| `[ST (in PAR_19)]` | `⟨[nested LOOP_21], t48, t68⟩` | Exact Token Match | $\ge$ 1 | **167** | ✅ **VERIFIED** |
| `[ST (in PAR_19)]` | `⟨t47, t48⟩` | Exact Token Match | $\ge$ 148 | **167** | ✅ **VERIFIED** |
| `[ST (in PAR_19)]` | `⟨[nested LOOP_21], t48⟩` | Exact Token Match | $\ge$ 1 | **167** | ✅ **VERIFIED** |
| `[AS (in LOOP_14)]` | `[nested PAR_15]` | Exact Token Match | $\ge$ 192 | **206** | ✅ **VERIFIED** |
| `[ST (in LOOP_14)]` | `t65` | Exact Token Match | $\ge$ 366 | **366** | ✅ **VERIFIED** |
| `[ST (in LOOP_14)]` | `t55` | Exact Token Match | $\ge$ 465 | **465** | ✅ **VERIFIED** |
| `[ST (in LOOP_14)]` | `⟨τ, t65⟩` | Exact Token Match | $\ge$ 174 | **366** | ✅ **VERIFIED** |
| `[ST (in LOOP_14)]` | `⟨τ, t55⟩` | Exact Token Match | $\ge$ 273 | **465** | ✅ **VERIFIED** |
| `[ST (in LOOP_14)]` | `⟨t46, τ⟩` | Exact Token Match | $\ge$ 135 | **327** | ✅ **VERIFIED** |
| `[AS (in PAR_9)]` | `[nested LOOP_14]` | Exact Token Match | $\ge$ 1 | **126** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_9]⟩` | Exact Token Match | $\ge$ 212 | **248** | ✅ **VERIFIED** |
| `[ST]` | `⟨t71, [nested PAR_9]⟩` | Exact Token Match | $\ge$ 38 | **38** | ✅ **VERIFIED** |
| `[ST]` | `⟨t42, τ, [nested PAR_9]⟩` | Exact Token Match | $\ge$ 146 | **179** | ✅ **VERIFIED** |
| `[ST]` | `⟨t42, τ⟩` | Exact Token Match | $\ge$ 146 | **179** | ✅ **VERIFIED** |
| `[ST]` | `⟨t22, t42, τ, [nested PAR_9]⟩` | Exact Token Match | $\ge$ 19 | **107** | ✅ **VERIFIED** |
| `[ST]` | `⟨t22, t42, τ⟩` | Exact Token Match | $\ge$ 19 | **107** | ✅ **VERIFIED** |
| `[ST]` | `⟨t22, t42⟩` | Exact Token Match | $\ge$ 57 | **107** | ✅ **VERIFIED** |
| `[ST]` | `⟨t34, t26, t27, t28, t42⟩` | Exact Token Match | $\ge$ 6 | **40** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t22⟩` | Exact Token Match | $\ge$ 13 | **130** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t34⟩` | Exact Token Match | $\ge$ 17 | **106** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 52 | **192** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, τ⟩` | Exact Token Match | $\ge$ 82 | **192** | ✅ **VERIFIED** |
| `[ST]` | `⟨t16, t20⟩` | Exact Token Match | $\ge$ 6 | **64** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t20, τ⟩` | Exact Token Match | $\ge$ 18 | **192** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t20⟩` | Exact Token Match | $\ge$ 128 | **192** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], τ⟩` | Exact Token Match | $\ge$ 19 | **118** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, τ, t20⟩` | Exact Token Match | $\ge$ 45 | **192** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, τ⟩` | Exact Token Match | $\ge$ 50 | **133** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, τ⟩` | Exact Token Match | $\ge$ 50 | **133** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ, τ⟩` | Exact Token Match | $\ge$ 32 | **250** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06⟩` | Exact Token Match | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11⟩` | Exact Token Match | $\ge$ 133 | **133** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 115 | **250** | ✅ **VERIFIED** |
| `[ST]` | `t23` | Exact Token Match | $\ge$ 110 | **106** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t34` | Exact Token Match | $\ge$ 127 | **106** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t26` | Exact Token Match | $\ge$ 110 | **106** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t27` | Exact Token Match | $\ge$ 110 | **106** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t27, t28⟩` | Exact Token Match | $\ge$ 72 | **70** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t26, t27, t28⟩` | Exact Token Match | $\ge$ 72 | **70** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t26, t27⟩` | Exact Token Match | $\ge$ 110 | **106** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t34, t26, t27, t28⟩` | Exact Token Match | $\ge$ 72 | **42** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t34, t26, t27⟩` | Exact Token Match | $\ge$ 110 | **56** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t34, t26⟩` | Exact Token Match | $\ge$ 110 | **56** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t42⟩` | Exact Token Match | $\ge$ 184 | **179** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_17)]` | `[nested PAR_19]` | Exact Token Match | $\ge$ 185 | **162** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_15)]` | `[nested PAR_17]` | Exact Token Match | $\ge$ 192 | **139** | ⚠️ **DISCREPANCY** |
| `[AS]` | `[nested PAR_9]` | Exact Token Match | $\ge$ 250 | **248** | ⚠️ **DISCREPANCY** |

## Audit Summary
- **Perfect Pattern Verifications:** 95
- **Frequency Discrepancies:** 14
- **Ghost Patterns (Fatal):** 0
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 11.78%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 5.68%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 39.30%
- **Total Forced Volume (incl. unresolved AS, % of N):** 0.00%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 0.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 97.93%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 94.09%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 96.25%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 21.06%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 50.47%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 97.46%
- **Max Fractional Exposure (Worst-Case Normalized):** 2.92% (expected length: 1609.82 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 100.00% (expected length: 26.04 events)
- **Mean Absolute Exposure Volume:** 17.67 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_2]`
- **Internal Structure:** `(t05 ∗ τ)`
- **Block Frequency:** 83

- **Max Loop Iterations:** `34`
- **Max Sub-Sequence Length:** `69` steps (if one case consumes all iterations)

![nested LOOP_2 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_2.png)

### `[nested LOOP_3]`
- **Internal Structure:** `(t15 ∗ τ)`
- **Block Frequency:** 77

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_3 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_3.png)

### `[nested LOOP_4]`
- **Internal Structure:** `(t04 ∗ τ)`
- **Block Frequency:** 6

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_4 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_4.png)

### `[nested PAR_1]`
- **Internal Structure:** `{(t05 ∗ τ), [(t15 ∗ τ) │ (t04 ∗ τ)]}`
- **Block Frequency:** 83



![nested PAR_1 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_1.png)

### `[nested LOOP_6]`
- **Internal Structure:** `(t17 ∗ τ)`
- **Block Frequency:** 110

- **Max Loop Iterations:** `156`
- **Max Sub-Sequence Length:** `313` steps (if one case consumes all iterations)

![nested LOOP_6 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_6.png)

### `[nested LOOP_7]`
- **Internal Structure:** `(t21 ∗ τ)`
- **Block Frequency:** 110

- **Max Loop Iterations:** `163`
- **Max Sub-Sequence Length:** `327` steps (if one case consumes all iterations)

![nested LOOP_7 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_7.png)

### `[nested PAR_5]`
- **Internal Structure:** `{(t17 ∗ τ), ⟨(t21 ∗ τ), t24⟩}`
- **Block Frequency:** 110



![nested PAR_5 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_5.png)

### `[nested LOOP_8]`
- **Internal Structure:** `(t42 ∗ τ)`
- **Block Frequency:** 250

- **Max Loop Iterations:** `66`
- **Max Sub-Sequence Length:** `133` steps (if one case consumes all iterations)

![nested LOOP_8 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_8.png)

### `[nested LOOP_10]`
- **Internal Structure:** `(t40 ∗ τ)`
- **Block Frequency:** 229

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_10 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_10.png)

### `[nested LOOP_12]`
- **Internal Structure:** `(t36 ∗ τ)`
- **Block Frequency:** 154

- **Max Loop Iterations:** `284`
- **Max Sub-Sequence Length:** `569` steps (if one case consumes all iterations)

![nested LOOP_12 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_12.png)

### `[nested LOOP_11]`
- **Internal Structure:** `(⟨t39, [⟨t43, t44, (t36 ∗ τ)⟩ │ τ]⟩ ∗ τ)`
- **Block Frequency:** 250

- **Max Loop Iterations:** `87`
- **Max Sub-Sequence Length:** `175` steps (if one case consumes all iterations)

![nested LOOP_11 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_11.png)

### `[nested XOR_13]`
- **Internal Structure:** `[⟨t43, t44, (t36 ∗ τ)⟩ │ τ]`
- **Block Frequency:** 337



![nested XOR_13 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_XOR_13.png)

### `[nested LOOP_16]`
- **Internal Structure:** `(t62 ∗ τ)`
- **Block Frequency:** 192

- **Max Loop Iterations:** `72`
- **Max Sub-Sequence Length:** `145` steps (if one case consumes all iterations)

![nested LOOP_16 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_16.png)

### `[nested LOOP_18]`
- **Internal Structure:** `(t37 ∗ τ)`
- **Block Frequency:** 192

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_18 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_18.png)

### `[nested LOOP_20]`
- **Internal Structure:** `(t56 ∗ τ)`
- **Block Frequency:** 185

- **Max Loop Iterations:** `310`
- **Max Sub-Sequence Length:** `621` steps (if one case consumes all iterations)

![nested LOOP_20 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_20.png)

### `[nested LOOP_21]`
- **Internal Structure:** `(t47 ∗ τ)`
- **Block Frequency:** 185

- **Max Loop Iterations:** `37`
- **Max Sub-Sequence Length:** `75` steps (if one case consumes all iterations)

![nested LOOP_21 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_21.png)

### `[nested LOOP_22]`
- **Internal Structure:** `(t68 ∗ τ)`
- **Block Frequency:** 185

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_22 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_22.png)

### `[nested PAR_19]`
- **Internal Structure:** `{(t56 ∗ τ), ⟨(t47 ∗ τ), t48, (t68 ∗ τ)⟩}`
- **Block Frequency:** 185



![nested PAR_19 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_19.png)

### `[nested PAR_17]`
- **Internal Structure:** `{[τ │ (t37 ∗ τ)], [{(t56 ∗ τ), ⟨(t47 ∗ τ), t48, (t68 ∗ τ)⟩} │ τ]}`
- **Block Frequency:** 192



![nested PAR_17 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_17.png)

### `[nested PAR_15]`
- **Internal Structure:** `{(t62 ∗ τ), [τ │ (t37 ∗ τ)], [{(t56 ∗ τ), ⟨(t47 ∗ τ), t48, (t68 ∗ τ)⟩} │ τ]}`
- **Block Frequency:** 192



![nested PAR_15 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_15.png)

### `[nested LOOP_14]`
- **Internal Structure:** `(⟨[τ │ t46], [{(t62 ∗ τ), [τ │ (t37 ∗ τ)], [{(t56 ∗ τ), ⟨(t47 ∗ τ), t48, (t68 ∗ τ)⟩} │ τ]} │ τ], [t65 │ t55]⟩ ∗ τ)`
- **Block Frequency:** 250

- **Max Loop Iterations:** `581`
- **Max Sub-Sequence Length:** `1163` steps (if one case consumes all iterations)

![nested LOOP_14 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_14.png)

### `[nested PAR_9]`
- **Internal Structure:** `{[(t40 ∗ τ) │ τ], ⟨(⟨t39, [⟨t43, t44, (t36 ∗ τ)⟩ │ τ]⟩ ∗ τ), (⟨[τ │ t46], [{(t62 ∗ τ), [τ │ (t37 ∗ τ)], [{(t56 ∗ τ), ⟨(t47 ∗ τ), t48, (t68 ∗ τ)⟩} │ τ]} │ τ], [t65 │ t55]⟩ ∗ τ)⟩}`
- **Block Frequency:** 250



![nested PAR_9 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_9.png)
