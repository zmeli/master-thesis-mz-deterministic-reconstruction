# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_110101.xes` |
| **Noise Threshold** | `0.2` |
| **Fitness** | `0.9675058642289371` |
| **Precision** | `0.21856579878069315` |
| **Total Cases in Log** | `250` |
| **Unique Activities** | `39` |
| **XOR Operators** | `29` |
| **LOOP Operators** | `20` |
| **SEQ Operators** | `21` |
| **PAR Operators** | `9` |
| **Binarization Additions** | `14` |
| **Tau Operators Added** | `22` |
| **Total Found Patterns** | `195` |
| **Verified Patterns** | `118` |
| **Discrepancy Patterns** | `16` |
| **Ghost Patterns** | `1` |
| **Nested LOOPs** | `20` |
| **Nested PARs** | `9` |
| **Tree Exposure (Strict, End-to-End % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `13.27%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `9.02%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `40.88%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `44.00%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `44.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `82.37%` |
| **Data Exposure, ST-only (% confirmed)** | `100.00%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `100.00%` |
| **Data Coverage, ST-only (% of real log)** | `8.26%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `53.22%` |
| **Data Coverage, Total (% of real log)** | `100.00%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `47.25%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `100.00%` |
| **Mean Absolute Exposure Volume (events/case)** | `32.18` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_110101__noise0.2.png)


```text
->( 't10', X( tau, ->( X( 't06', 't11' ), X( tau, *( 't04', 't07' ) ), +( X( tau, *( 't15', tau ) ), *( 't05', tau ) ), X( tau, 't16' ) ) ), 't20', +( X( tau, *( 't34', tau ) ), ->( *( ->( +( *( 't17', tau ), 't21', X( tau, ->( 't24', 't23' ) ) ), X( 't22', ->( 't26', 't27', X( tau, 't28' ) ) ), *( 't42', 't41' ) ), tau ), X( tau, 't71' ), +( X( tau, *( 't40', tau ) ), ->( *( ->( 't39', X( tau, ->( 't43', *( 't44', tau ) ) ), *( 't36', tau ) ), 't32' ), *( ->( X( tau, 't46' ), X( *( 't69', tau ), *( 't70', tau ), ->( X( tau, 't47' ), +( X( tau, *( 't62', tau ) ), X( tau, *( 't52', tau ) ), X( tau, *( 't37', tau ) ), X( tau, *( 't56', tau ) ), X( *( 't55', tau ), ->( 't48', *( 't68', tau ) ) ) ) ) ), X( tau, 't65' ) ), tau ) ) ) ) ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_110101__noise0.2.png)



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
| `[ST (in LOOP_6)]` | `t34` | Exact Token Match | $\ge$ 164 | **164** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t34⟩` | Exact Token Match | $\ge$ 164 | **164** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `t17` | Exact Token Match | $\ge$ 295 | **295** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨t17⟩` | Exact Token Match | $\ge$ 291 | **295** | ✅ **VERIFIED** |
| `[AS (in PAR_8)]` | `[nested LOOP_9]` | Exact Token Match | $\ge$ 1 | **295** | ✅ **VERIFIED** |
| `[ST (in PAR_10)]` | `t21` | Exact Token Match | $\ge$ 293 | **293** | ✅ **VERIFIED** |
| `[ST (in PAR_10)]` | `t24` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[ST (in PAR_10)]` | `t23` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[ST (in PAR_10)]` | `⟨t24, t23⟩` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `t22` | Exact Token Match | $\ge$ 145 | **145** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `t26` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `t27` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `t28` | Exact Token Match | $\ge$ 77 | **77** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨t27, τ⟩` | Exact Token Match | $\ge$ 41 | **118** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨t27, t28⟩` | Exact Token Match | $\ge$ 77 | **77** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨t26, t27, τ⟩` | Exact Token Match | $\ge$ 41 | **118** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨t26, t27, t28⟩` | Exact Token Match | $\ge$ 77 | **77** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨t26, t27⟩` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `t42` | Exact Token Match | $\ge$ 431 | **431** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `t41` | Exact Token Match | $\ge$ 179 | **179** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨t42⟩` | Exact Token Match | $\ge$ 73 | **431** | ✅ **VERIFIED** |
| `[AS (in LOOP_7)]` | `[nested LOOP_11]` | Exact Token Match | $\ge$ 1 | **252** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨[nested PAR_8], τ⟩` | Exact Token Match | $\ge$ 30 | **276** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨[nested PAR_8], t22⟩` | Exact Token Match | $\ge$ 145 | **145** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨[nested PAR_8], t26, t27, τ⟩` | Exact Token Match | $\ge$ 41 | **118** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨[nested PAR_8], t26, t27, t28⟩` | Exact Token Match | $\ge$ 77 | **77** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨[nested PAR_8], t26, t27⟩` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨[nested PAR_8], t26⟩` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[AS (in PAR_5)]` | `[nested LOOP_7]` | Exact Token Match | $\ge$ 1 | **10** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t71` | Exact Token Match | $\ge$ 41 | **41** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `t40` | Exact Token Match | $\ge$ 221 | **221** | ✅ **VERIFIED** |
| `[ST (in PAR_16)]` | `⟨t40⟩` | Exact Token Match | $\ge$ 221 | **221** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `t39` | Exact Token Match | $\ge$ 391 | **391** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `t43` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_19)]` | `t44` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `⟨t44⟩` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `⟨t43, t44⟩` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_20)]` | `t36` | Exact Token Match | $\ge$ 523 | **523** | ✅ **VERIFIED** |
| `[AS (in LOOP_18)]` | `[nested LOOP_20]` | Exact Token Match | $\ge$ 1 | **208** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `⟨t43, t44, [nested LOOP_20]⟩` | Exact Token Match | $\ge$ 1 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `⟨t44, [nested LOOP_20]⟩` | Exact Token Match | $\ge$ 1 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `⟨t39, t43, t44, [nested LOOP_20]⟩` | Exact Token Match | $\ge$ 1 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `⟨t39, τ⟩` | Exact Token Match | $\ge$ 201 | **391** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `⟨t39, t43, t44⟩` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `⟨t39, t43⟩` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `t32` | Exact Token Match | $\ge$ 155 | **155** | ✅ **VERIFIED** |
| `[ST (in PAR_16)]` | `⟨t39, [nested XOR_21]⟩` | Exact Token Match | $\ge$ 81.0 | **190** | ✅ **VERIFIED** |
| `[AS (in PAR_16)]` | `[nested LOOP_18]` | Exact Token Match | $\ge$ 1 | **134** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `t46` | Exact Token Match | $\ge$ 420 | **420** | ✅ **VERIFIED** |
| `[ST (in LOOP_23)]` | `t69` | Exact Token Match | $\ge$ 170 | **170** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `⟨t69⟩` | Exact Token Match | $\ge$ 170 | **170** | ✅ **VERIFIED** |
| `[ST (in LOOP_24)]` | `t70` | Exact Token Match | $\ge$ 150 | **150** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `⟨t70⟩` | Exact Token Match | $\ge$ 150 | **150** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `t47` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_26)]` | `t62` | Exact Token Match | $\ge$ 225 | **225** | ✅ **VERIFIED** |
| `[ST (in PAR_25)]` | `⟨t62⟩` | Exact Token Match | $\ge$ 225 | **225** | ✅ **VERIFIED** |
| `[ST (in LOOP_28)]` | `t52` | Exact Token Match | $\ge$ 248 | **248** | ✅ **VERIFIED** |
| `[ST (in PAR_27)]` | `⟨t52⟩` | Exact Token Match | $\ge$ 248 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_30)]` | `t37` | Exact Token Match | $\ge$ 180 | **180** | ✅ **VERIFIED** |
| `[ST (in PAR_29)]` | `⟨t37⟩` | Exact Token Match | $\ge$ 180 | **180** | ✅ **VERIFIED** |
| `[ST (in LOOP_32)]` | `t56` | Exact Token Match | $\ge$ 606 | **606** | ✅ **VERIFIED** |
| `[ST (in PAR_31)]` | `⟨t56⟩` | Exact Token Match | $\ge$ 606 | **606** | ✅ **VERIFIED** |
| `[ST (in LOOP_33)]` | `t55` | Exact Token Match | $\ge$ 622 | **622** | ✅ **VERIFIED** |
| `[ST (in PAR_31)]` | `⟨t55⟩` | Exact Token Match | $\ge$ 622 | **622** | ✅ **VERIFIED** |
| `[ST (in PAR_31)]` | `t48` | Exact Token Match | $\ge$ 188 | **188** | ✅ **VERIFIED** |
| `[ST (in LOOP_34)]` | `t68` | Exact Token Match | $\ge$ 188 | **188** | ✅ **VERIFIED** |
| `[ST (in PAR_31)]` | `⟨t68⟩` | Exact Token Match | $\ge$ 188 | **188** | ✅ **VERIFIED** |
| `[ST (in PAR_31)]` | `⟨t48, t68⟩` | Exact Token Match | $\ge$ 188 | **188** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `⟨t47, [nested PAR_25]⟩` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `t65` | Exact Token Match | $\ge$ 432 | **432** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `⟨τ, [nested PAR_25], τ⟩` | Exact Token Match | $\ge$ 188 | **240** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `⟨[nested PAR_25], t65⟩` | Exact Token Match | $\ge$ 112 | **335** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `⟨τ, τ, [nested PAR_25]⟩` | Exact Token Match | $\ge$ 200 | **240** | ✅ **VERIFIED** |
| `[AS (in PAR_16)]` | `[nested LOOP_22]` | Exact Token Match | $\ge$ 1 | **16** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 205 | **205** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 45 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t20, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 58 | **205** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, τ, [nested PAR_2], t16, t20, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 35 | **69** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, τ, t20, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 17 | **102** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t20⟩` | Exact Token Match | $\ge$ 58 | **205** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, τ, [nested PAR_2], t16, t20⟩` | Exact Token Match | $\ge$ 35 | **69** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, τ, t20⟩` | Exact Token Match | $\ge$ 17 | **102** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_2], t16, t20, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 36 | **69** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_2], t16, t20, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 37 | **69** | ✅ **VERIFIED** |
| `[ST]` | `⟨t16, t20, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 39 | **84** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t20, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 18 | **205** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ, t20, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 58 | **205** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, τ, [nested PAR_2], t16, t20, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 35 | **69** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, τ, t20, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 17 | **102** | ✅ **VERIFIED** |
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
| `[AS (in PAR_8)]` | `[nested PAR_10]` | Exact Token Match | $\ge$ 293 | **118** | ⚠️ **DISCREPANCY** |
| `[AS (in LOOP_7)]` | `[nested PAR_8]` | Exact Token Match | $\ge$ 293 | **276** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨[nested PAR_8], [nested XOR_15]⟩` | Exact Token Match | $\ge$ 30.0 | **10** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_29)]` | `[nested PAR_31]` | Exact Token Match | $\ge$ 810 | **159** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_27)]` | `[nested PAR_29]` | Exact Token Match | $\ge$ 810 | **142** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_25)]` | `[nested PAR_27]` | Exact Token Match | $\ge$ 810 | **71** | ⚠️ **DISCREPANCY** |
| `[AS (in LOOP_22)]` | `[nested PAR_25]` | Exact Token Match | $\ge$ 810 | **240** | ⚠️ **DISCREPANCY** |
| `[ST (in LOOP_22)]` | `⟨τ, [nested PAR_25]⟩` | Exact Token Match | $\ge$ 620 | **240** | ⚠️ **DISCREPANCY** |
| `[ST (in LOOP_22)]` | `⟨[nested PAR_25], τ⟩` | Exact Token Match | $\ge$ 378 | **240** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_5)]` | `[nested PAR_16]` | Exact Token Match | $\ge$ 250 | **6** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨τ, [nested PAR_16]⟩` | Exact Token Match | $\ge$ 209 | **6** | ⚠️ **DISCREPANCY** |
| `[AS]` | `[nested PAR_5]` | Exact Token Match | $\ge$ 250 | **249** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, t11, τ, [nested PAR_2], t16⟩` | Exact Token Match | $\ge$ 80 | **69** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨t71, [nested PAR_16]⟩` | Exact Token Match | $\ge$ 41 | **0** | ❌ **GHOST PATTERN** |

## Audit Summary
- **Perfect Pattern Verifications:** 118
- **Frequency Discrepancies:** 16
- **Ghost Patterns (Fatal):** 1
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 13.27%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 9.02%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 40.88%
- **Total Forced Volume (incl. unresolved AS, % of N):** 44.00%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 44.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 82.37%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 100.00%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 100.00%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 8.26%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 53.22%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 100.00%
- **Max Fractional Exposure (Worst-Case Normalized):** 47.25% (expected length: 2834.20 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 100.00% (expected length: 33.21 events)
- **Mean Absolute Exposure Volume:** 32.18 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_1]`
- **Internal Structure:** `(t04 ∗ t07)`
- **Block Frequency:** 1

- **Max Loop Iterations:** `2`
- **Max Sub-Sequence Length:** `5` steps (if one case consumes all iterations)

![nested LOOP_1 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_LOOP_1.png)

### `[nested LOOP_3]`
- **Internal Structure:** `(t15 ∗ τ)`
- **Block Frequency:** 82

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_3 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_LOOP_3.png)

### `[nested LOOP_4]`
- **Internal Structure:** `(t05 ∗ τ)`
- **Block Frequency:** 82

- **Max Loop Iterations:** `62`
- **Max Sub-Sequence Length:** `125` steps (if one case consumes all iterations)

![nested LOOP_4 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_LOOP_4.png)

### `[nested PAR_2]`
- **Internal Structure:** `{[τ │ (t15 ∗ τ)], (t05 ∗ τ)}`
- **Block Frequency:** 82



![nested PAR_2 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_PAR_2.png)

### `[nested LOOP_6]`
- **Internal Structure:** `(t34 ∗ τ)`
- **Block Frequency:** 164

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_6 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_LOOP_6.png)

### `[nested LOOP_9]`
- **Internal Structure:** `(t17 ∗ τ)`
- **Block Frequency:** 293

- **Max Loop Iterations:** `2`
- **Max Sub-Sequence Length:** `5` steps (if one case consumes all iterations)

![nested LOOP_9 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_LOOP_9.png)

### `[nested PAR_10]`
- **Internal Structure:** `{t21, [τ │ ⟨t24, t23⟩]}`
- **Block Frequency:** 293



![nested PAR_10 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_PAR_10.png)

### `[nested PAR_8]`
- **Internal Structure:** `{(t17 ∗ τ), t21, [τ │ ⟨t24, t23⟩]}`
- **Block Frequency:** 293



![nested PAR_8 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_PAR_8.png)

### `[nested LOOP_11]`
- **Internal Structure:** `(t42 ∗ t41)`
- **Block Frequency:** 252

- **Max Loop Iterations:** `179`
- **Max Sub-Sequence Length:** `359` steps (if one case consumes all iterations)

![nested LOOP_11 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_LOOP_11.png)

### `[nested LOOP_7]`
- **Internal Structure:** `(⟨{(t17 ∗ τ), t21, [τ │ ⟨t24, t23⟩]}, [⟨[t22 │ ⟨t26, t27, [τ │ t28]⟩], [(t42 ∗ t41) │ τ]⟩ │ τ]⟩ ∗ τ)`
- **Block Frequency:** 250

- **Max Loop Iterations:** `43`
- **Max Sub-Sequence Length:** `87` steps (if one case consumes all iterations)

![nested LOOP_7 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_LOOP_7.png)

### `[nested XOR_12]`
- **Internal Structure:** `[τ │ t28]`
- **Block Frequency:** 118



![nested XOR_12 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_XOR_12.png)

### `[nested XOR_13]`
- **Internal Structure:** `[t22 │ ⟨t26, t27, [τ │ t28]⟩]`
- **Block Frequency:** 263



![nested XOR_13 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_XOR_13.png)

### `[nested XOR_14]`
- **Internal Structure:** `[(t42 ∗ t41) │ τ]`
- **Block Frequency:** 263



![nested XOR_14 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_XOR_14.png)

### `[nested XOR_15]`
- **Internal Structure:** `[⟨[t22 │ ⟨t26, t27, [τ │ t28]⟩], [(t42 ∗ t41) │ τ]⟩ │ τ]`
- **Block Frequency:** 293



![nested XOR_15 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_XOR_15.png)

### `[nested LOOP_17]`
- **Internal Structure:** `(t40 ∗ τ)`
- **Block Frequency:** 221

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_17 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_LOOP_17.png)

### `[nested LOOP_19]`
- **Internal Structure:** `(t44 ∗ τ)`
- **Block Frequency:** 190

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_19 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_LOOP_19.png)

### `[nested LOOP_20]`
- **Internal Structure:** `(t36 ∗ τ)`
- **Block Frequency:** 190

- **Max Loop Iterations:** `333`
- **Max Sub-Sequence Length:** `667` steps (if one case consumes all iterations)

![nested LOOP_20 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_LOOP_20.png)

### `[nested LOOP_18]`
- **Internal Structure:** `(⟨t39, [⟨[τ │ ⟨t43, (t44 ∗ τ)⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ t32)`
- **Block Frequency:** 236

- **Max Loop Iterations:** `155`
- **Max Sub-Sequence Length:** `311` steps (if one case consumes all iterations)

![nested LOOP_18 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_LOOP_18.png)

### `[nested XOR_21]`
- **Internal Structure:** `[⟨[τ │ ⟨t43, (t44 ∗ τ)⟩], (t36 ∗ τ)⟩ │ τ]`
- **Block Frequency:** 391



![nested XOR_21 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_XOR_21.png)

### `[nested LOOP_23]`
- **Internal Structure:** `(t69 ∗ τ)`
- **Block Frequency:** 170

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_23 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_LOOP_23.png)

### `[nested LOOP_24]`
- **Internal Structure:** `(t70 ∗ τ)`
- **Block Frequency:** 150

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_24 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_LOOP_24.png)

### `[nested LOOP_26]`
- **Internal Structure:** `(t62 ∗ τ)`
- **Block Frequency:** 225

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_26 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_LOOP_26.png)

### `[nested LOOP_28]`
- **Internal Structure:** `(t52 ∗ τ)`
- **Block Frequency:** 248

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_28 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_LOOP_28.png)

### `[nested LOOP_30]`
- **Internal Structure:** `(t37 ∗ τ)`
- **Block Frequency:** 180

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_30 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_LOOP_30.png)

### `[nested LOOP_32]`
- **Internal Structure:** `(t56 ∗ τ)`
- **Block Frequency:** 606

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_32 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_LOOP_32.png)

### `[nested LOOP_33]`
- **Internal Structure:** `(t55 ∗ τ)`
- **Block Frequency:** 622

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_33 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_LOOP_33.png)

### `[nested LOOP_34]`
- **Internal Structure:** `(t68 ∗ τ)`
- **Block Frequency:** 188

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_34 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_LOOP_34.png)

### `[nested PAR_31]`
- **Internal Structure:** `{[τ │ (t56 ∗ τ)], [(t55 ∗ τ) │ ⟨t48, (t68 ∗ τ)⟩]}`
- **Block Frequency:** 810



![nested PAR_31 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_PAR_31.png)

### `[nested PAR_29]`
- **Internal Structure:** `{[τ │ (t37 ∗ τ)], [τ │ (t56 ∗ τ)], [(t55 ∗ τ) │ ⟨t48, (t68 ∗ τ)⟩]}`
- **Block Frequency:** 810



![nested PAR_29 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_PAR_29.png)

### `[nested PAR_27]`
- **Internal Structure:** `{[τ │ (t52 ∗ τ)], [τ │ (t37 ∗ τ)], [τ │ (t56 ∗ τ)], [(t55 ∗ τ) │ ⟨t48, (t68 ∗ τ)⟩]}`
- **Block Frequency:** 810



![nested PAR_27 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_PAR_27.png)

### `[nested PAR_25]`
- **Internal Structure:** `{[τ │ (t62 ∗ τ)], [τ │ (t52 ∗ τ)], [τ │ (t37 ∗ τ)], [τ │ (t56 ∗ τ)], [(t55 ∗ τ) │ ⟨t48, (t68 ∗ τ)⟩]}`
- **Block Frequency:** 810



![nested PAR_25 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_PAR_25.png)

### `[nested LOOP_22]`
- **Internal Structure:** `(⟨[τ │ t46], [(t69 ∗ τ) │ (t70 ∗ τ) │ ⟨[τ │ t47], {[τ │ (t62 ∗ τ)], [τ │ (t52 ∗ τ)], [τ │ (t37 ∗ τ)], [τ │ (t56 ∗ τ)], [(t55 ∗ τ) │ ⟨t48, (t68 ∗ τ)⟩]}⟩], [τ │ t65]⟩ ∗ τ)`
- **Block Frequency:** 250

- **Max Loop Iterations:** `880`
- **Max Sub-Sequence Length:** `1761` steps (if one case consumes all iterations)

![nested LOOP_22 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_LOOP_22.png)

### `[nested PAR_16]`
- **Internal Structure:** `{[τ │ (t40 ∗ τ)], ⟨[(⟨t39, [⟨[τ │ ⟨t43, (t44 ∗ τ)⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ t32) │ τ], (⟨[τ │ t46], [(t69 ∗ τ) │ (t70 ∗ τ) │ ⟨[τ │ t47], {[τ │ (t62 ∗ τ)], [τ │ (t52 ∗ τ)], [τ │ (t37 ∗ τ)], [τ │ (t56 ∗ τ)], [(t55 ∗ τ) │ ⟨t48, (t68 ∗ τ)⟩]}⟩], [τ │ t65]⟩ ∗ τ)⟩}`
- **Block Frequency:** 250



![nested PAR_16 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_PAR_16.png)

### `[nested PAR_5]`
- **Internal Structure:** `{[τ │ (t34 ∗ τ)], ⟨(⟨{(t17 ∗ τ), t21, [τ │ ⟨t24, t23⟩]}, [⟨[t22 │ ⟨t26, t27, [τ │ t28]⟩], [(t42 ∗ t41) │ τ]⟩ │ τ]⟩ ∗ τ), [τ │ t71], {[τ │ (t40 ∗ τ)], ⟨[(⟨t39, [⟨[τ │ ⟨t43, (t44 ∗ τ)⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ t32) │ τ], (⟨[τ │ t46], [(t69 ∗ τ) │ (t70 ∗ τ) │ ⟨[τ │ t47], {[τ │ (t62 ∗ τ)], [τ │ (t52 ∗ τ)], [τ │ (t37 ∗ τ)], [τ │ (t56 ∗ τ)], [(t55 ∗ τ) │ ⟨t48, (t68 ∗ τ)⟩]}⟩], [τ │ t65]⟩ ∗ τ)⟩}⟩}`
- **Block Frequency:** 250



![nested PAR_5 Internal Diagram](images/nested_ref_audit_pdc2021_110101_nested_PAR_5.png)
