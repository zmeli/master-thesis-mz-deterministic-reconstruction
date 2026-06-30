# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_110101.xes` |
| **Noise Threshold** | `0.4` |
| **Fitness** | `0.9381044331467835` |
| **Precision** | `0.2740726775698732` |
| **Total Cases in Log** | `250` |
| **Unique Activities** | `39` |
| **XOR Operators** | `28` |
| **LOOP Operators** | `21` |
| **SEQ Operators** | `24` |
| **PAR Operators** | `8` |
| **Binarization Additions** | `15` |
| **Tau Operators Added** | `20` |
| **Total Found Patterns** | `188` |
| **Verified Patterns** | `114` |
| **Discrepancy Patterns** | `16` |
| **Ghost Patterns** | `1` |
| **Nested LOOPs** | `21` |
| **Nested PARs** | `8` |
| **Tree Exposure (Strict, End-to-End % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `13.27%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `9.02%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `40.68%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `0.00%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `0.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `93.02%` |
| **Data Exposure, ST-only (% confirmed)** | `98.59%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `99.56%` |
| **Data Coverage, ST-only (% of real log)** | `9.73%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `54.40%` |
| **Data Coverage, Total (% of real log)** | `99.72%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `2.19%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `100.00%` |
| **Mean Absolute Exposure Volume (events/case)** | `26.51` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_110101__noise0.4__test.png)


```text
->( 't10', X( tau, ->( X( 't06', 't11' ), X( tau, *( 't04', 't07' ) ), +( X( tau, *( 't15', tau ) ), *( 't05', tau ) ), X( tau, 't16' ) ) ), 't20', +( *( 't17', tau ), ->( *( 't21', tau ), X( tau, ->( 't24', 't23' ) ) ) ), X( tau, 't22' ), +( X( tau, *( 't34', tau ) ), ->( X( tau, ->( 't26', 't27', 't28' ) ), *( *( 't42', tau ), 't41' ), X( tau, 't71' ), +( *( 't40', tau ), ->( *( ->( 't39', X( tau, ->( 't43', *( 't44', tau ) ) ), *( 't36', tau ) ), 't32' ), *( ->( X( tau, 't46' ), X( *( 't69', tau ), *( 't70', tau ), ->( X( tau, ->( 't47', X( tau, 't37' ) ) ), X( tau, +( *( 't62', tau ), *( 't48', tau ), *( 't68', tau ) ) ), +( X( tau, *( 't52', tau ) ), *( 't55', tau ), X( tau, *( 't56', tau ) ) ) ) ), X( tau, 't65' ) ), tau ) ) ) ) ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_110101__noise0.4__test.png)



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
| `[ST (in PAR_2)]` | `⟨t05⟩` | Exact Token Match | $\ge$ 20 | **144** | ✅ **VERIFIED** |
| `[AS (in PAR_2)]` | `[nested LOOP_4]` | Exact Token Match | $\ge$ 1 | **144** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_2]` | Exact Token Match | $\ge$ 82 | **125** | ✅ **VERIFIED** |
| `[ST]` | `t16` | Exact Token Match | $\ge$ 84 | **84** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t16⟩` | Exact Token Match | $\ge$ 2 | **84** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, τ, t16⟩` | Exact Token Match | $\ge$ 1 | **84** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_2]⟩` | Exact Token Match | $\ge$ 81 | **125** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, τ⟩` | Exact Token Match | $\ge$ 62 | **146** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, τ, [nested PAR_2]⟩` | Exact Token Match | $\ge$ 80 | **124** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, τ⟩` | Exact Token Match | $\ge$ 82 | **146** | ✅ **VERIFIED** |
| `[ST]` | `t20` | Exact Token Match | $\ge$ 205 | **205** | ✅ **VERIFIED** |
| `[ST (in LOOP_6)]` | `t17` | Exact Token Match | $\ge$ 295 | **295** | ✅ **VERIFIED** |
| `[AS (in PAR_5)]` | `[nested LOOP_6]` | Exact Token Match | $\ge$ 1 | **295** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `t21` | Exact Token Match | $\ge$ 293 | **293** | ✅ **VERIFIED** |
| `[AS (in PAR_5)]` | `[nested LOOP_7]` | Exact Token Match | $\ge$ 1 | **293** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t24` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t23` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t24, t23⟩` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨[nested LOOP_7], t24, t23⟩` | Exact Token Match | $\ge$ 1 | **118** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨[nested LOOP_7], t24⟩` | Exact Token Match | $\ge$ 1 | **118** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_5]` | Exact Token Match | $\ge$ 118 | **249** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `t34` | Exact Token Match | $\ge$ 164 | **164** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨t34⟩` | Exact Token Match | $\ge$ 164 | **164** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `t26` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `t27` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `t28` | Exact Token Match | $\ge$ 77 | **77** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨t27, t28⟩` | Exact Token Match | $\ge$ 77 | **77** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨t27, τ⟩` | Exact Token Match | $\ge$ 41 | **118** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨t26, t27, t28⟩` | Exact Token Match | $\ge$ 77 | **77** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨t26, t27, τ⟩` | Exact Token Match | $\ge$ 41 | **118** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨t26, t27⟩` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `t42` | Exact Token Match | $\ge$ 431 | **431** | ✅ **VERIFIED** |
| `[ST (in LOOP_10)]` | `⟨t42⟩` | Exact Token Match | $\ge$ 427 | **431** | ✅ **VERIFIED** |
| `[AS (in LOOP_10)]` | `[nested LOOP_11]` | Exact Token Match | $\ge$ 1 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_10)]` | `t41` | Exact Token Match | $\ge$ 179 | **179** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨t42⟩` | Exact Token Match | $\ge$ 69 | **431** | ✅ **VERIFIED** |
| `[AS (in PAR_8)]` | `⟨[nested LOOP_11]⟩` | Exact Token Match | $\ge$ 1 | **431** | ✅ **VERIFIED** |
| `[AS (in PAR_8)]` | `[nested LOOP_10]` | Exact Token Match | $\ge$ 1 | **179** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `t71` | Exact Token Match | $\ge$ 41 | **41** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `t40` | Exact Token Match | $\ge$ 221 | **221** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t40⟩` | Exact Token Match | $\ge$ 221 | **221** | ✅ **VERIFIED** |
| `[ST (in LOOP_14)]` | `t39` | Exact Token Match | $\ge$ 391 | **391** | ✅ **VERIFIED** |
| `[ST (in LOOP_14)]` | `t43` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `t44` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_14)]` | `⟨t44⟩` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_14)]` | `⟨t43, t44⟩` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_16)]` | `t36` | Exact Token Match | $\ge$ 523 | **523** | ✅ **VERIFIED** |
| `[AS (in LOOP_14)]` | `[nested LOOP_16]` | Exact Token Match | $\ge$ 1 | **208** | ✅ **VERIFIED** |
| `[ST (in LOOP_14)]` | `⟨t43, t44, [nested LOOP_16]⟩` | Exact Token Match | $\ge$ 1 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_14)]` | `⟨t44, [nested LOOP_16]⟩` | Exact Token Match | $\ge$ 1 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_14)]` | `⟨t39, t43, t44, [nested LOOP_16]⟩` | Exact Token Match | $\ge$ 1 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_14)]` | `⟨t39, τ⟩` | Exact Token Match | $\ge$ 201 | **391** | ✅ **VERIFIED** |
| `[ST (in LOOP_14)]` | `⟨t39, t43, t44⟩` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_14)]` | `⟨t39, t43⟩` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_14)]` | `t32` | Exact Token Match | $\ge$ 155 | **155** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t39, [nested XOR_17]⟩` | Exact Token Match | $\ge$ 81.0 | **190** | ✅ **VERIFIED** |
| `[AS (in PAR_12)]` | `[nested LOOP_14]` | Exact Token Match | $\ge$ 1 | **134** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `t46` | Exact Token Match | $\ge$ 420 | **420** | ✅ **VERIFIED** |
| `[ST (in LOOP_19)]` | `t69` | Exact Token Match | $\ge$ 170 | **170** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `⟨t69⟩` | Exact Token Match | $\ge$ 170 | **170** | ✅ **VERIFIED** |
| `[ST (in LOOP_20)]` | `t70` | Exact Token Match | $\ge$ 150 | **150** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `⟨t70⟩` | Exact Token Match | $\ge$ 150 | **150** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `t47` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `t37` | Exact Token Match | $\ge$ 180 | **180** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `⟨t47, τ⟩` | Exact Token Match | $\ge$ 10 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `t62` | Exact Token Match | $\ge$ 225 | **225** | ✅ **VERIFIED** |
| `[ST (in PAR_21)]` | `⟨t62⟩` | Exact Token Match | $\ge$ 151 | **225** | ✅ **VERIFIED** |
| `[AS (in PAR_21)]` | `[nested LOOP_22]` | Exact Token Match | $\ge$ 1 | **225** | ✅ **VERIFIED** |
| `[ST (in LOOP_24)]` | `t48` | Exact Token Match | $\ge$ 188 | **188** | ✅ **VERIFIED** |
| `[ST (in PAR_23)]` | `⟨t48⟩` | Exact Token Match | $\ge$ 188 | **188** | ✅ **VERIFIED** |
| `[ST (in LOOP_25)]` | `t68` | Exact Token Match | $\ge$ 188 | **188** | ✅ **VERIFIED** |
| `[ST (in PAR_23)]` | `⟨t68⟩` | Exact Token Match | $\ge$ 188 | **188** | ✅ **VERIFIED** |
| `[AS (in PAR_21)]` | `[nested PAR_23]` | Exact Token Match | $\ge$ 188 | **188** | ✅ **VERIFIED** |
| `[ST (in LOOP_27)]` | `t52` | Exact Token Match | $\ge$ 248 | **248** | ✅ **VERIFIED** |
| `[ST (in PAR_26)]` | `⟨t52⟩` | Exact Token Match | $\ge$ 248 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_29)]` | `t55` | Exact Token Match | $\ge$ 622 | **622** | ✅ **VERIFIED** |
| `[ST (in PAR_28)]` | `⟨t55⟩` | Exact Token Match | $\ge$ 590 | **622** | ✅ **VERIFIED** |
| `[AS (in PAR_28)]` | `[nested LOOP_29]` | Exact Token Match | $\ge$ 1 | **622** | ✅ **VERIFIED** |
| `[ST (in LOOP_30)]` | `t56` | Exact Token Match | $\ge$ 606 | **606** | ✅ **VERIFIED** |
| `[ST (in PAR_28)]` | `⟨t56⟩` | Exact Token Match | $\ge$ 606 | **606** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `⟨[nested PAR_21], [nested PAR_26]⟩` | Exact Token Match | $\ge$ 188 | **255** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `t65` | Exact Token Match | $\ge$ 432 | **432** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `⟨[nested PAR_26], τ⟩` | Exact Token Match | $\ge$ 174 | **226** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `⟨[nested PAR_26], t65⟩` | Exact Token Match | $\ge$ 112 | **312** | ✅ **VERIFIED** |
| `[AS (in PAR_12)]` | `[nested LOOP_18]` | Exact Token Match | $\ge$ 1 | **16** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨t42, τ⟩` | Exact Token Match | $\ge$ 28 | **431** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_8]⟩` | Exact Token Match | $\ge$ 105 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_5], t22, [nested PAR_8]⟩` | Exact Token Match | $\ge$ 13 | **110** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t22, [nested PAR_8]⟩` | Exact Token Match | $\ge$ 27 | **114** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_5], t22⟩` | Exact Token Match | $\ge$ 13 | **117** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t22⟩` | Exact Token Match | $\ge$ 27 | **122** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 73 | **205** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, τ⟩` | Exact Token Match | $\ge$ 87 | **205** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t20⟩` | Exact Token Match | $\ge$ 58 | **205** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, τ, [nested PAR_2], t16, t20⟩` | Exact Token Match | $\ge$ 35 | **69** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, τ, t20⟩` | Exact Token Match | $\ge$ 17 | **102** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ, t20⟩` | Exact Token Match | $\ge$ 58 | **205** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, τ, [nested PAR_2], t16, t20⟩` | Exact Token Match | $\ge$ 35 | **69** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, τ, t20⟩` | Exact Token Match | $\ge$ 17 | **102** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 103 | **250** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, τ, [nested PAR_2]⟩` | Exact Token Match | $\ge$ 80 | **124** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, τ⟩` | Exact Token Match | $\ge$ 82 | **146** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, τ⟩` | Exact Token Match | $\ge$ 62 | **146** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11⟩` | Exact Token Match | $\ge$ 146 | **146** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_2], t16⟩` | Exact Token Match | $\ge$ 82 | **69** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨τ, [nested PAR_2], t16⟩` | Exact Token Match | $\ge$ 81 | **69** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t11, τ, [nested PAR_2], t16⟩` | Exact Token Match | $\ge$ 80 | **69** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t22` | Exact Token Match | $\ge$ 145 | **122** | ⚠️ **DISCREPANCY** |
| `[ST (in LOOP_18)]` | `⟨t47, t37⟩` | Exact Token Match | $\ge$ 180 | **156** | ⚠️ **DISCREPANCY** |
| `[AS (in LOOP_18)]` | `[nested PAR_21]` | Exact Token Match | $\ge$ 188 | **156** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_26)]` | `[nested PAR_28]` | Exact Token Match | $\ge$ 606 | **534** | ⚠️ **DISCREPANCY** |
| `[AS (in LOOP_18)]` | `[nested PAR_26]` | Exact Token Match | $\ge$ 606 | **226** | ⚠️ **DISCREPANCY** |
| `[ST (in LOOP_18)]` | `⟨τ, [nested PAR_26]⟩` | Exact Token Match | $\ge$ 418 | **226** | ⚠️ **DISCREPANCY** |
| `[ST (in LOOP_18)]` | `⟨τ, τ, [nested PAR_26]⟩` | Exact Token Match | $\ge$ 228 | **226** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_8)]` | `[nested PAR_12]` | Exact Token Match | $\ge$ 250 | **6** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_8)]` | `⟨τ, [nested PAR_12]⟩` | Exact Token Match | $\ge$ 209 | **6** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_8)]` | `⟨t42, τ, [nested PAR_12]⟩` | Exact Token Match | $\ge$ 28 | **6** | ⚠️ **DISCREPANCY** |
| `[AS]` | `[nested PAR_8]` | Exact Token Match | $\ge$ 250 | **249** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t22, [nested PAR_8]⟩` | Exact Token Match | $\ge$ 145 | **114** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, t11, τ, [nested PAR_2], t16⟩` | Exact Token Match | $\ge$ 80 | **69** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_8)]` | `⟨t71, [nested PAR_12]⟩` | Exact Token Match | $\ge$ 41 | **0** | ❌ **GHOST PATTERN** |

## Audit Summary
- **Perfect Pattern Verifications:** 114
- **Frequency Discrepancies:** 16
- **Ghost Patterns (Fatal):** 1
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 13.27%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 9.02%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 40.68%
- **Total Forced Volume (incl. unresolved AS, % of N):** 0.00%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 0.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 93.02%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 98.59%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 99.56%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 9.73%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 54.40%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 99.72%
- **Max Fractional Exposure (Worst-Case Normalized):** 2.19% (expected length: 2619.26 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 100.00% (expected length: 33.21 events)
- **Mean Absolute Exposure Volume:** 26.51 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_1]`
- **Internal Structure:** `(t04 ∗ t07)`
- **Block Frequency:** 1

- **Max Loop Iterations:** `2`
- **Max Sub-Sequence Length:** `5` steps (if one case consumes all iterations)

![nested LOOP_1 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.4__test_nested_LOOP_1.png)

### `[nested LOOP_3]`
- **Internal Structure:** `(t15 ∗ τ)`
- **Block Frequency:** 82

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_3 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.4__test_nested_LOOP_3.png)

### `[nested LOOP_4]`
- **Internal Structure:** `(t05 ∗ τ)`
- **Block Frequency:** 82

- **Max Loop Iterations:** `62`
- **Max Sub-Sequence Length:** `125` steps (if one case consumes all iterations)

![nested LOOP_4 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.4__test_nested_LOOP_4.png)

### `[nested PAR_2]`
- **Internal Structure:** `{[τ │ (t15 ∗ τ)], (t05 ∗ τ)}`
- **Block Frequency:** 82



![nested PAR_2 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.4__test_nested_PAR_2.png)

### `[nested LOOP_6]`
- **Internal Structure:** `(t17 ∗ τ)`
- **Block Frequency:** 118

- **Max Loop Iterations:** `177`
- **Max Sub-Sequence Length:** `355` steps (if one case consumes all iterations)

![nested LOOP_6 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.4__test_nested_LOOP_6.png)

### `[nested LOOP_7]`
- **Internal Structure:** `(t21 ∗ τ)`
- **Block Frequency:** 118

- **Max Loop Iterations:** `175`
- **Max Sub-Sequence Length:** `351` steps (if one case consumes all iterations)

![nested LOOP_7 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.4__test_nested_LOOP_7.png)

### `[nested PAR_5]`
- **Internal Structure:** `{(t17 ∗ τ), ⟨(t21 ∗ τ), [τ │ ⟨t24, t23⟩]⟩}`
- **Block Frequency:** 118



![nested PAR_5 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.4__test_nested_PAR_5.png)

### `[nested LOOP_9]`
- **Internal Structure:** `(t34 ∗ τ)`
- **Block Frequency:** 164

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_9 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.4__test_nested_LOOP_9.png)

### `[nested LOOP_11]`
- **Internal Structure:** `(t42 ∗ τ)`
- **Block Frequency:** 429

- **Max Loop Iterations:** `2`
- **Max Sub-Sequence Length:** `5` steps (if one case consumes all iterations)

![nested LOOP_11 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.4__test_nested_LOOP_11.png)

### `[nested LOOP_10]`
- **Internal Structure:** `((t42 ∗ τ) ∗ t41)`
- **Block Frequency:** 250

- **Max Loop Iterations:** `179`
- **Max Sub-Sequence Length:** `359` steps (if one case consumes all iterations)

![nested LOOP_10 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.4__test_nested_LOOP_10.png)

### `[nested LOOP_13]`
- **Internal Structure:** `(t40 ∗ τ)`
- **Block Frequency:** 221

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_13 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.4__test_nested_LOOP_13.png)

### `[nested LOOP_15]`
- **Internal Structure:** `(t44 ∗ τ)`
- **Block Frequency:** 190

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_15 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.4__test_nested_LOOP_15.png)

### `[nested LOOP_16]`
- **Internal Structure:** `(t36 ∗ τ)`
- **Block Frequency:** 190

- **Max Loop Iterations:** `333`
- **Max Sub-Sequence Length:** `667` steps (if one case consumes all iterations)

![nested LOOP_16 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.4__test_nested_LOOP_16.png)

### `[nested LOOP_14]`
- **Internal Structure:** `(⟨t39, [⟨[τ │ ⟨t43, (t44 ∗ τ)⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ t32)`
- **Block Frequency:** 236

- **Max Loop Iterations:** `155`
- **Max Sub-Sequence Length:** `311` steps (if one case consumes all iterations)

![nested LOOP_14 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.4__test_nested_LOOP_14.png)

### `[nested XOR_17]`
- **Internal Structure:** `[⟨[τ │ ⟨t43, (t44 ∗ τ)⟩], (t36 ∗ τ)⟩ │ τ]`
- **Block Frequency:** 391



![nested XOR_17 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.4__test_nested_XOR_17.png)

### `[nested LOOP_19]`
- **Internal Structure:** `(t69 ∗ τ)`
- **Block Frequency:** 170

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_19 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.4__test_nested_LOOP_19.png)

### `[nested LOOP_20]`
- **Internal Structure:** `(t70 ∗ τ)`
- **Block Frequency:** 150

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_20 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.4__test_nested_LOOP_20.png)

### `[nested LOOP_22]`
- **Internal Structure:** `(t62 ∗ τ)`
- **Block Frequency:** 188

- **Max Loop Iterations:** `37`
- **Max Sub-Sequence Length:** `75` steps (if one case consumes all iterations)

![nested LOOP_22 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.4__test_nested_LOOP_22.png)

### `[nested LOOP_24]`
- **Internal Structure:** `(t48 ∗ τ)`
- **Block Frequency:** 188

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_24 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.4__test_nested_LOOP_24.png)

### `[nested LOOP_25]`
- **Internal Structure:** `(t68 ∗ τ)`
- **Block Frequency:** 188

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_25 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.4__test_nested_LOOP_25.png)

### `[nested PAR_23]`
- **Internal Structure:** `{(t48 ∗ τ), (t68 ∗ τ)}`
- **Block Frequency:** 188



![nested PAR_23 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.4__test_nested_PAR_23.png)

### `[nested PAR_21]`
- **Internal Structure:** `{(t62 ∗ τ), (t48 ∗ τ), (t68 ∗ τ)}`
- **Block Frequency:** 188



![nested PAR_21 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.4__test_nested_PAR_21.png)

### `[nested LOOP_27]`
- **Internal Structure:** `(t52 ∗ τ)`
- **Block Frequency:** 248

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_27 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.4__test_nested_LOOP_27.png)

### `[nested LOOP_29]`
- **Internal Structure:** `(t55 ∗ τ)`
- **Block Frequency:** 606

- **Max Loop Iterations:** `16`
- **Max Sub-Sequence Length:** `33` steps (if one case consumes all iterations)

![nested LOOP_29 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.4__test_nested_LOOP_29.png)

### `[nested LOOP_30]`
- **Internal Structure:** `(t56 ∗ τ)`
- **Block Frequency:** 606

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_30 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.4__test_nested_LOOP_30.png)

### `[nested PAR_28]`
- **Internal Structure:** `{(t55 ∗ τ), [τ │ (t56 ∗ τ)]}`
- **Block Frequency:** 606



![nested PAR_28 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.4__test_nested_PAR_28.png)

### `[nested PAR_26]`
- **Internal Structure:** `{[τ │ (t52 ∗ τ)], (t55 ∗ τ), [τ │ (t56 ∗ τ)]}`
- **Block Frequency:** 606



![nested PAR_26 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.4__test_nested_PAR_26.png)

### `[nested LOOP_18]`
- **Internal Structure:** `(⟨[τ │ t46], [(t69 ∗ τ) │ (t70 ∗ τ) │ ⟨[τ │ ⟨t47, [τ │ t37]⟩], [τ │ {(t62 ∗ τ), (t48 ∗ τ), (t68 ∗ τ)}], {[τ │ (t52 ∗ τ)], (t55 ∗ τ), [τ │ (t56 ∗ τ)]}⟩], [τ │ t65]⟩ ∗ τ)`
- **Block Frequency:** 250

- **Max Loop Iterations:** `676`
- **Max Sub-Sequence Length:** `1353` steps (if one case consumes all iterations)

![nested LOOP_18 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.4__test_nested_LOOP_18.png)

### `[nested PAR_12]`
- **Internal Structure:** `{[(t40 ∗ τ) │ τ], ⟨[(⟨t39, [⟨[τ │ ⟨t43, (t44 ∗ τ)⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ t32) │ τ], (⟨[τ │ t46], [(t69 ∗ τ) │ (t70 ∗ τ) │ ⟨[τ │ ⟨t47, [τ │ t37]⟩], [τ │ {(t62 ∗ τ), (t48 ∗ τ), (t68 ∗ τ)}], {[τ │ (t52 ∗ τ)], (t55 ∗ τ), [τ │ (t56 ∗ τ)]}⟩], [τ │ t65]⟩ ∗ τ)⟩}`
- **Block Frequency:** 250



![nested PAR_12 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.4__test_nested_PAR_12.png)

### `[nested PAR_8]`
- **Internal Structure:** `{[τ │ (t34 ∗ τ)], ⟨[τ │ ⟨t26, t27, [t28 │ τ]⟩], ((t42 ∗ τ) ∗ t41), [τ │ t71], {[(t40 ∗ τ) │ τ], ⟨[(⟨t39, [⟨[τ │ ⟨t43, (t44 ∗ τ)⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ t32) │ τ], (⟨[τ │ t46], [(t69 ∗ τ) │ (t70 ∗ τ) │ ⟨[τ │ ⟨t47, [τ │ t37]⟩], [τ │ {(t62 ∗ τ), (t48 ∗ τ), (t68 ∗ τ)}], {[τ │ (t52 ∗ τ)], (t55 ∗ τ), [τ │ (t56 ∗ τ)]}⟩], [τ │ t65]⟩ ∗ τ)⟩}⟩}`
- **Block Frequency:** 250



![nested PAR_8 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.4__test_nested_PAR_8.png)
