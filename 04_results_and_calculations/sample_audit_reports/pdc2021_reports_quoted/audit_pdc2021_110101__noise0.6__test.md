# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_110101.xes` |
| **Noise Threshold** | `0.6` |
| **Fitness** | `0.8639011430891784` |
| **Precision** | `0.6968031968031968` |
| **Total Cases in Log** | `250` |
| **Unique Activities** | `39` |
| **XOR Operators** | `24` |
| **LOOP Operators** | `23` |
| **SEQ Operators** | `22` |
| **PAR Operators** | `8` |
| **Binarization Additions** | `18` |
| **Tau Operators Added** | `19` |
| **Total Found Patterns** | `163` |
| **Verified Patterns** | `106` |
| **Discrepancy Patterns** | `20` |
| **Ghost Patterns** | `0` |
| **Nested LOOPs** | `23` |
| **Nested PARs** | `8` |
| **Tree Exposure (Strict, End-to-End % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `12.58%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `7.08%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `20.48%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `0.00%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `0.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `89.79%` |
| **Data Exposure, ST-only (% confirmed)** | `92.24%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `95.94%` |
| **Data Coverage, ST-only (% of real log)** | `15.61%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `53.31%` |
| **Data Coverage, Total (% of real log)** | `99.17%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `1.97%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `100.00%` |
| **Mean Absolute Exposure Volume (events/case)** | `20.50` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_110101__noise0.6__test.png)


```text
->( 't10', X( 't06', 't11' ), X( tau, *( 't04', 't07' ) ), +( *( 't15', tau ), *( 't05', tau ) ), 't16', 't20', +( *( 't17', tau ), *( 't21', tau ), ->( 't24', *( 't23', tau ) ) ), X( *( 't22', tau ), ->( 't34', 't26', 't27', *( 't28', tau ) ) ), *( *( 't42', tau ), 't41' ), X( tau, 't71' ), +( *( 't40', tau ), ->( *( ->( 't39', 't43', *( 't44', tau ), *( 't36', tau ) ), 't32' ), *( ->( 't46', X( *( 't69', tau ), *( 't70', tau ), +( *( 't55', tau ), X( tau, *( 't37', tau ) ), ->( X( tau, 't47' ), +( *( 't62', tau ), *( 't56', tau ), X( *( 't52', tau ), ->( 't48', *( 't68', tau ) ) ) ) ) ) ), 't65' ), tau ) ) ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_110101__noise0.6__test.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST]` | `t10` | Exact Token Match | $\ge$ 250 | **250** | ✅ **VERIFIED** |
| `[ST]` | `t06` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `t11` | Exact Token Match | $\ge$ 146 | **146** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `t04` | Exact Token Match | $\ge$ 3 | **3** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `t07` | Exact Token Match | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_1]` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t15` | Exact Token Match | $\ge$ 82 | **82** | ✅ **VERIFIED** |
| `[ST (in PAR_2)]` | `⟨t15⟩` | Exact Token Match | $\ge$ 82 | **82** | ✅ **VERIFIED** |
| `[ST (in LOOP_4)]` | `t05` | Exact Token Match | $\ge$ 144 | **144** | ✅ **VERIFIED** |
| `[ST (in PAR_2)]` | `⟨t05⟩` | Exact Token Match | $\ge$ 144 | **144** | ✅ **VERIFIED** |
| `[ST]` | `t16` | Exact Token Match | $\ge$ 84 | **84** | ✅ **VERIFIED** |
| `[ST]` | `t20` | Exact Token Match | $\ge$ 205 | **205** | ✅ **VERIFIED** |
| `[ST (in LOOP_6)]` | `t17` | Exact Token Match | $\ge$ 295 | **295** | ✅ **VERIFIED** |
| `[AS (in PAR_5)]` | `[nested LOOP_6]` | Exact Token Match | $\ge$ 1 | **295** | ✅ **VERIFIED** |
| `[ST (in LOOP_8)]` | `t21` | Exact Token Match | $\ge$ 293 | **293** | ✅ **VERIFIED** |
| `[AS (in PAR_7)]` | `[nested LOOP_8]` | Exact Token Match | $\ge$ 1 | **293** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `t24` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `t23` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨t23⟩` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨t24, t23⟩` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[AS (in PAR_5)]` | `[nested PAR_7]` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_5]` | Exact Token Match | $\ge$ 118 | **249** | ✅ **VERIFIED** |
| `[ST (in LOOP_10)]` | `t22` | Exact Token Match | $\ge$ 145 | **145** | ✅ **VERIFIED** |
| `[ST]` | `⟨t22⟩` | Exact Token Match | $\ge$ 89 | **122** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_10]` | Exact Token Match | $\ge$ 1 | **133** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `t28` | Exact Token Match | $\ge$ 77 | **77** | ✅ **VERIFIED** |
| `[ST]` | `⟨t27, τ⟩` | Exact Token Match | $\ge$ 41 | **107** | ✅ **VERIFIED** |
| `[ST]` | `⟨t26, t27, τ⟩` | Exact Token Match | $\ge$ 41 | **107** | ✅ **VERIFIED** |
| `[ST]` | `⟨t34, t26, t27, τ⟩` | Exact Token Match | $\ge$ 41 | **58** | ✅ **VERIFIED** |
| `[ST]` | `⟨t34, τ⟩` | Exact Token Match | $\ge$ 15 | **117** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `t42` | Exact Token Match | $\ge$ 431 | **431** | ✅ **VERIFIED** |
| `[ST (in LOOP_12)]` | `⟨t42⟩` | Exact Token Match | $\ge$ 427 | **431** | ✅ **VERIFIED** |
| `[AS (in LOOP_12)]` | `[nested LOOP_13]` | Exact Token Match | $\ge$ 1 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_12)]` | `t41` | Exact Token Match | $\ge$ 179 | **179** | ✅ **VERIFIED** |
| `[ST]` | `⟨t42⟩` | Exact Token Match | $\ge$ 69 | **116** | ✅ **VERIFIED** |
| `[AS]` | `⟨[nested LOOP_13]⟩` | Exact Token Match | $\ge$ 1 | **213** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_12]` | Exact Token Match | $\ge$ 1 | **213** | ✅ **VERIFIED** |
| `[ST]` | `t71` | Exact Token Match | $\ge$ 41 | **41** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `t40` | Exact Token Match | $\ge$ 221 | **221** | ✅ **VERIFIED** |
| `[ST (in PAR_14)]` | `⟨t40⟩` | Exact Token Match | $\ge$ 221 | **221** | ✅ **VERIFIED** |
| `[ST (in LOOP_16)]` | `t39` | Exact Token Match | $\ge$ 391 | **391** | ✅ **VERIFIED** |
| `[ST (in LOOP_16)]` | `t43` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `t44` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_16)]` | `⟨t44⟩` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `t36` | Exact Token Match | $\ge$ 523 | **523** | ✅ **VERIFIED** |
| `[ST (in LOOP_16)]` | `⟨t36⟩` | Exact Token Match | $\ge$ 287 | **523** | ✅ **VERIFIED** |
| `[AS (in LOOP_16)]` | `[nested LOOP_18]` | Exact Token Match | $\ge$ 1 | **208** | ✅ **VERIFIED** |
| `[ST (in LOOP_16)]` | `⟨t44, t36⟩` | Exact Token Match | $\ge$ 72 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_16)]` | `⟨τ, t36⟩` | Exact Token Match | $\ge$ 97 | **523** | ✅ **VERIFIED** |
| `[ST (in LOOP_16)]` | `⟨t39, τ, τ⟩` | Exact Token Match | $\ge$ 11 | **391** | ✅ **VERIFIED** |
| `[ST (in LOOP_16)]` | `⟨t39, t43⟩` | Exact Token Match | $\ge$ 176 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_16)]` | `⟨t39, τ⟩` | Exact Token Match | $\ge$ 201 | **391** | ✅ **VERIFIED** |
| `[ST (in LOOP_16)]` | `t32` | Exact Token Match | $\ge$ 155 | **155** | ✅ **VERIFIED** |
| `[AS (in PAR_14)]` | `[nested LOOP_16]` | Exact Token Match | $\ge$ 1 | **134** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `t46` | Exact Token Match | $\ge$ 420 | **420** | ✅ **VERIFIED** |
| `[ST (in LOOP_23)]` | `t69` | Exact Token Match | $\ge$ 170 | **170** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `⟨t69⟩` | Exact Token Match | $\ge$ 170 | **170** | ✅ **VERIFIED** |
| `[ST (in LOOP_24)]` | `t70` | Exact Token Match | $\ge$ 150 | **150** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `⟨t70⟩` | Exact Token Match | $\ge$ 150 | **150** | ✅ **VERIFIED** |
| `[ST (in LOOP_26)]` | `t55` | Exact Token Match | $\ge$ 622 | **622** | ✅ **VERIFIED** |
| `[ST (in PAR_25)]` | `⟨t55⟩` | Exact Token Match | $\ge$ 250 | **622** | ✅ **VERIFIED** |
| `[AS (in PAR_25)]` | `[nested LOOP_26]` | Exact Token Match | $\ge$ 1 | **622** | ✅ **VERIFIED** |
| `[ST (in LOOP_28)]` | `t37` | Exact Token Match | $\ge$ 180 | **180** | ✅ **VERIFIED** |
| `[ST (in PAR_27)]` | `⟨t37⟩` | Exact Token Match | $\ge$ 180 | **180** | ✅ **VERIFIED** |
| `[ST (in PAR_27)]` | `t47` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_30)]` | `t62` | Exact Token Match | $\ge$ 225 | **225** | ✅ **VERIFIED** |
| `[ST (in PAR_29)]` | `⟨t62⟩` | Exact Token Match | $\ge$ 225 | **225** | ✅ **VERIFIED** |
| `[ST (in LOOP_32)]` | `t56` | Exact Token Match | $\ge$ 606 | **606** | ✅ **VERIFIED** |
| `[ST (in PAR_31)]` | `⟨t56⟩` | Exact Token Match | $\ge$ 266 | **606** | ✅ **VERIFIED** |
| `[AS (in PAR_31)]` | `[nested LOOP_32]` | Exact Token Match | $\ge$ 1 | **606** | ✅ **VERIFIED** |
| `[ST (in LOOP_33)]` | `t52` | Exact Token Match | $\ge$ 248 | **248** | ✅ **VERIFIED** |
| `[ST (in PAR_31)]` | `⟨t52⟩` | Exact Token Match | $\ge$ 248 | **248** | ✅ **VERIFIED** |
| `[ST (in PAR_31)]` | `t48` | Exact Token Match | $\ge$ 188 | **188** | ✅ **VERIFIED** |
| `[ST (in LOOP_34)]` | `t68` | Exact Token Match | $\ge$ 188 | **188** | ✅ **VERIFIED** |
| `[ST (in PAR_31)]` | `⟨t68⟩` | Exact Token Match | $\ge$ 188 | **188** | ✅ **VERIFIED** |
| `[ST (in PAR_31)]` | `⟨t48, t68⟩` | Exact Token Match | $\ge$ 188 | **188** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `t65` | Exact Token Match | $\ge$ 432 | **432** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `⟨[nested PAR_25], t65⟩` | Exact Token Match | $\ge$ 112 | **335** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `⟨[nested PAR_25], τ⟩` | Exact Token Match | $\ge$ 4 | **240** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `⟨t46, [nested PAR_25]⟩` | Exact Token Match | $\ge$ 100 | **401** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `⟨τ, [nested PAR_25]⟩` | Exact Token Match | $\ge$ 16 | **240** | ✅ **VERIFIED** |
| `[AS (in PAR_14)]` | `[nested LOOP_22]` | Exact Token Match | $\ge$ 1 | **16** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_14]⟩` | Exact Token Match | $\ge$ 209 | **248** | ✅ **VERIFIED** |
| `[ST]` | `⟨t42, τ, [nested PAR_14]⟩` | Exact Token Match | $\ge$ 28 | **116** | ✅ **VERIFIED** |
| `[ST]` | `⟨t42, τ⟩` | Exact Token Match | $\ge$ 28 | **116** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_5], t34⟩` | Exact Token Match | $\ge$ 1 | **114** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t34⟩` | Exact Token Match | $\ge$ 15 | **117** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 73 | **205** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, τ⟩` | Exact Token Match | $\ge$ 87 | **205** | ✅ **VERIFIED** |
| `[ST]` | `⟨t16, t20⟩` | Exact Token Match | $\ge$ 39 | **84** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t20, τ⟩` | Exact Token Match | $\ge$ 3 | **205** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t20⟩` | Exact Token Match | $\ge$ 121 | **205** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_2], τ, t20⟩` | Exact Token Match | $\ge$ 15 | **80** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_2], τ⟩` | Exact Token Match | $\ge$ 60 | **125** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_2], τ, t20⟩` | Exact Token Match | $\ge$ 14 | **80** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_2], τ⟩` | Exact Token Match | $\ge$ 59 | **125** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, τ, [nested PAR_2]⟩` | Exact Token Match | $\ge$ 39 | **124** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, τ, τ⟩` | Exact Token Match | $\ge$ 1 | **146** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, τ⟩` | Exact Token Match | $\ge$ 145 | **146** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, τ, [nested PAR_2]⟩` | Exact Token Match | $\ge$ 39 | **124** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, τ, τ⟩` | Exact Token Match | $\ge$ 1 | **146** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, τ⟩` | Exact Token Match | $\ge$ 145 | **146** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ, τ⟩` | Exact Token Match | $\ge$ 102 | **250** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11⟩` | Exact Token Match | $\ge$ 146 | **146** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 103 | **250** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_2]` | Exact Token Match | $\ge$ 144 | **125** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t34` | Exact Token Match | $\ge$ 133 | **117** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t26` | Exact Token Match | $\ge$ 118 | **107** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t27` | Exact Token Match | $\ge$ 118 | **107** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t28⟩` | Exact Token Match | $\ge$ 77 | **71** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t27, t28⟩` | Exact Token Match | $\ge$ 77 | **69** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t26, t27, t28⟩` | Exact Token Match | $\ge$ 77 | **69** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t26, t27⟩` | Exact Token Match | $\ge$ 118 | **107** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t34, t26, t27, t28⟩` | Exact Token Match | $\ge$ 77 | **36** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t34, t26, t27⟩` | Exact Token Match | $\ge$ 118 | **58** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t34, t26⟩` | Exact Token Match | $\ge$ 118 | **58** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_29)]` | `[nested PAR_31]` | Exact Token Match | $\ge$ 436 | **81** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_27)]` | `[nested PAR_29]` | Exact Token Match | $\ge$ 436 | **81** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_27)]` | `⟨τ, [nested PAR_29]⟩` | Exact Token Match | $\ge$ 246 | **81** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_27)]` | `⟨t47, [nested PAR_29]⟩` | Exact Token Match | $\ge$ 190 | **72** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_25)]` | `[nested PAR_27]` | Exact Token Match | $\ge$ 436 | **65** | ⚠️ **DISCREPANCY** |
| `[AS (in LOOP_22)]` | `[nested PAR_25]` | Exact Token Match | $\ge$ 436 | **240** | ⚠️ **DISCREPANCY** |
| `[AS]` | `[nested PAR_14]` | Exact Token Match | $\ge$ 250 | **248** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t71, [nested PAR_14]⟩` | Exact Token Match | $\ge$ 41 | **40** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨τ, [nested PAR_2]⟩` | Exact Token Match | $\ge$ 143 | **125** | ⚠️ **DISCREPANCY** |

## Audit Summary
- **Perfect Pattern Verifications:** 106
- **Frequency Discrepancies:** 20
- **Ghost Patterns (Fatal):** 0
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 12.58%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 7.08%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 20.48%
- **Total Forced Volume (incl. unresolved AS, % of N):** 0.00%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 0.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 89.79%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 92.24%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 95.94%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 15.61%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 53.31%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 99.17%
- **Max Fractional Exposure (Worst-Case Normalized):** 1.97% (expected length: 2201.03 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 100.00% (expected length: 33.09 events)
- **Mean Absolute Exposure Volume:** 20.50 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_1]`
- **Internal Structure:** `(t04 ∗ t07)`
- **Block Frequency:** 1

- **Max Loop Iterations:** `2`
- **Max Sub-Sequence Length:** `5` steps (if one case consumes all iterations)

![nested LOOP_1 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_LOOP_1.png)

### `[nested LOOP_3]`
- **Internal Structure:** `(t15 ∗ τ)`
- **Block Frequency:** 82

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_3 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_LOOP_3.png)

### `[nested LOOP_4]`
- **Internal Structure:** `(t05 ∗ τ)`
- **Block Frequency:** 144

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_4 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_LOOP_4.png)

### `[nested PAR_2]`
- **Internal Structure:** `{[(t15 ∗ τ) │ τ], (t05 ∗ τ)}`
- **Block Frequency:** 144



![nested PAR_2 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_PAR_2.png)

### `[nested LOOP_6]`
- **Internal Structure:** `(t17 ∗ τ)`
- **Block Frequency:** 118

- **Max Loop Iterations:** `177`
- **Max Sub-Sequence Length:** `355` steps (if one case consumes all iterations)

![nested LOOP_6 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_LOOP_6.png)

### `[nested LOOP_8]`
- **Internal Structure:** `(t21 ∗ τ)`
- **Block Frequency:** 118

- **Max Loop Iterations:** `175`
- **Max Sub-Sequence Length:** `351` steps (if one case consumes all iterations)

![nested LOOP_8 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_LOOP_8.png)

### `[nested LOOP_9]`
- **Internal Structure:** `(t23 ∗ τ)`
- **Block Frequency:** 118

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_9 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_LOOP_9.png)

### `[nested PAR_7]`
- **Internal Structure:** `{(t21 ∗ τ), ⟨t24, (t23 ∗ τ)⟩}`
- **Block Frequency:** 118



![nested PAR_7 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_PAR_7.png)

### `[nested PAR_5]`
- **Internal Structure:** `{(t17 ∗ τ), (t21 ∗ τ), ⟨t24, (t23 ∗ τ)⟩}`
- **Block Frequency:** 118



![nested PAR_5 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_PAR_5.png)

### `[nested LOOP_10]`
- **Internal Structure:** `(t22 ∗ τ)`
- **Block Frequency:** 117

- **Max Loop Iterations:** `28`
- **Max Sub-Sequence Length:** `57` steps (if one case consumes all iterations)

![nested LOOP_10 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_LOOP_10.png)

### `[nested LOOP_11]`
- **Internal Structure:** `(t28 ∗ τ)`
- **Block Frequency:** 77

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_11 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_LOOP_11.png)

### `[nested LOOP_13]`
- **Internal Structure:** `(t42 ∗ τ)`
- **Block Frequency:** 429

- **Max Loop Iterations:** `2`
- **Max Sub-Sequence Length:** `5` steps (if one case consumes all iterations)

![nested LOOP_13 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_LOOP_13.png)

### `[nested LOOP_12]`
- **Internal Structure:** `((t42 ∗ τ) ∗ t41)`
- **Block Frequency:** 250

- **Max Loop Iterations:** `179`
- **Max Sub-Sequence Length:** `359` steps (if one case consumes all iterations)

![nested LOOP_12 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_LOOP_12.png)

### `[nested LOOP_15]`
- **Internal Structure:** `(t40 ∗ τ)`
- **Block Frequency:** 221

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_15 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_LOOP_15.png)

### `[nested LOOP_17]`
- **Internal Structure:** `(t44 ∗ τ)`
- **Block Frequency:** 190

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_17 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_LOOP_17.png)

### `[nested LOOP_18]`
- **Internal Structure:** `(t36 ∗ τ)`
- **Block Frequency:** 405

- **Max Loop Iterations:** `118`
- **Max Sub-Sequence Length:** `237` steps (if one case consumes all iterations)

![nested LOOP_18 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_LOOP_18.png)

### `[nested LOOP_16]`
- **Internal Structure:** `(⟨[t39 │ τ], [t43 │ τ], [(t44 ∗ τ) │ τ], (t36 ∗ τ)⟩ ∗ t32)`
- **Block Frequency:** 250

- **Max Loop Iterations:** `155`
- **Max Sub-Sequence Length:** `311` steps (if one case consumes all iterations)

![nested LOOP_16 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_LOOP_16.png)

### `[nested XOR_19]`
- **Internal Structure:** `[t39 │ τ]`
- **Block Frequency:** 405



![nested XOR_19 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_XOR_19.png)

### `[nested XOR_20]`
- **Internal Structure:** `[t43 │ τ]`
- **Block Frequency:** 405



![nested XOR_20 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_XOR_20.png)

### `[nested XOR_21]`
- **Internal Structure:** `[(t44 ∗ τ) │ τ]`
- **Block Frequency:** 405



![nested XOR_21 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_XOR_21.png)

### `[nested LOOP_23]`
- **Internal Structure:** `(t69 ∗ τ)`
- **Block Frequency:** 170

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_23 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_LOOP_23.png)

### `[nested LOOP_24]`
- **Internal Structure:** `(t70 ∗ τ)`
- **Block Frequency:** 150

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_24 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_LOOP_24.png)

### `[nested LOOP_26]`
- **Internal Structure:** `(t55 ∗ τ)`
- **Block Frequency:** 436

- **Max Loop Iterations:** `186`
- **Max Sub-Sequence Length:** `373` steps (if one case consumes all iterations)

![nested LOOP_26 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_LOOP_26.png)

### `[nested LOOP_28]`
- **Internal Structure:** `(t37 ∗ τ)`
- **Block Frequency:** 180

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_28 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_LOOP_28.png)

### `[nested LOOP_30]`
- **Internal Structure:** `(t62 ∗ τ)`
- **Block Frequency:** 225

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_30 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_LOOP_30.png)

### `[nested LOOP_32]`
- **Internal Structure:** `(t56 ∗ τ)`
- **Block Frequency:** 436

- **Max Loop Iterations:** `170`
- **Max Sub-Sequence Length:** `341` steps (if one case consumes all iterations)

![nested LOOP_32 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_LOOP_32.png)

### `[nested LOOP_33]`
- **Internal Structure:** `(t52 ∗ τ)`
- **Block Frequency:** 248

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_33 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_LOOP_33.png)

### `[nested LOOP_34]`
- **Internal Structure:** `(t68 ∗ τ)`
- **Block Frequency:** 188

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_34 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_LOOP_34.png)

### `[nested PAR_31]`
- **Internal Structure:** `{(t56 ∗ τ), [(t52 ∗ τ) │ ⟨t48, (t68 ∗ τ)⟩]}`
- **Block Frequency:** 436



![nested PAR_31 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_PAR_31.png)

### `[nested PAR_29]`
- **Internal Structure:** `{[(t62 ∗ τ) │ τ], (t56 ∗ τ), [(t52 ∗ τ) │ ⟨t48, (t68 ∗ τ)⟩]}`
- **Block Frequency:** 436



![nested PAR_29 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_PAR_29.png)

### `[nested PAR_27]`
- **Internal Structure:** `{[τ │ (t37 ∗ τ)], ⟨[τ │ t47], {[(t62 ∗ τ) │ τ], (t56 ∗ τ), [(t52 ∗ τ) │ ⟨t48, (t68 ∗ τ)⟩]}⟩}`
- **Block Frequency:** 436



![nested PAR_27 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_PAR_27.png)

### `[nested PAR_25]`
- **Internal Structure:** `{(t55 ∗ τ), [τ │ (t37 ∗ τ)], ⟨[τ │ t47], {[(t62 ∗ τ) │ τ], (t56 ∗ τ), [(t52 ∗ τ) │ ⟨t48, (t68 ∗ τ)⟩]}⟩}`
- **Block Frequency:** 436



![nested PAR_25 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_PAR_25.png)

### `[nested LOOP_22]`
- **Internal Structure:** `(⟨[t46 │ τ], [(t69 ∗ τ) │ (t70 ∗ τ) │ {(t55 ∗ τ), [τ │ (t37 ∗ τ)], ⟨[τ │ t47], {[(t62 ∗ τ) │ τ], (t56 ∗ τ), [(t52 ∗ τ) │ ⟨t48, (t68 ∗ τ)⟩]}⟩}], [t65 │ τ]⟩ ∗ τ)`
- **Block Frequency:** 250

- **Max Loop Iterations:** `506`
- **Max Sub-Sequence Length:** `1013` steps (if one case consumes all iterations)

![nested LOOP_22 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_LOOP_22.png)

### `[nested PAR_14]`
- **Internal Structure:** `{[(t40 ∗ τ) │ τ], ⟨(⟨[t39 │ τ], [t43 │ τ], [(t44 ∗ τ) │ τ], (t36 ∗ τ)⟩ ∗ t32), (⟨[t46 │ τ], [(t69 ∗ τ) │ (t70 ∗ τ) │ {(t55 ∗ τ), [τ │ (t37 ∗ τ)], ⟨[τ │ t47], {[(t62 ∗ τ) │ τ], (t56 ∗ τ), [(t52 ∗ τ) │ ⟨t48, (t68 ∗ τ)⟩]}⟩}], [t65 │ τ]⟩ ∗ τ)⟩}`
- **Block Frequency:** 250



![nested PAR_14 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.6__test_nested_PAR_14.png)
