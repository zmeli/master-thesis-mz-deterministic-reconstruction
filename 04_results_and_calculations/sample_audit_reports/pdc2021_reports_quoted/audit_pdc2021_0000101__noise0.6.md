# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_0000101.xes` |
| **Noise Threshold** | `0.6` |
| **Fitness** | `0.9548763499979144` |
| **Precision** | `0.5400780673066778` |
| **Total Cases in Log** | `1000` |
| **Unique Activities** | `42` |
| **XOR Operators** | `33` |
| **LOOP Operators** | `6` |
| **SEQ Operators** | `26` |
| **PAR Operators** | `5` |
| **Binarization Additions** | `21` |
| **Tau Operators Added** | `22` |
| **Total Found Patterns** | `369` |
| **Verified Patterns** | `221` |
| **Discrepancy Patterns** | `28` |
| **Ghost Patterns** | `14` |
| **Nested LOOPs** | `6` |
| **Nested PARs** | `5` |
| **Tree Exposure (Strict, End-to-End % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `0.00%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `100.00%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `0.10%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `0.10%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `94.53%` |
| **Data Exposure, ST-only (% confirmed)** | `0.00%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `97.68%` |
| **Data Coverage, ST-only (% of real log)** | `0.00%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `61.35%` |
| **Data Coverage, Total (% of real log)** | `100.00%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `0.10%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `0.10%` |
| **Mean Absolute Exposure Volume (events/case)** | `0.01` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_0000101__noise0.6.png)


```text
*( X( 't01', ->( X( tau, 't06' ), X( 't02', ->( X( 't09', 't10', 't04', ->( +( 't65', ->( X( tau, +( *( 't21', tau ), ->( 't19', +( X( tau, *( 't71', tau ) ), ->( 't11', 't14', X( tau, 't16' ), 't20', 't17', X( tau, ->( 't15', 't13' ) ), X( 't22', ->( 't24', +( 't23', 't29' ), 't25', 't26', 't27', 't28' ) ), *( 't42', tau ), 't38', 't39', X( ->( 't43', 't44' ), 't40', 't34' ), 't36', 't33', 't46', X( tau, 't30' ) ) ) ) ) ), X( 't69', 't70' ) ) ), 't66' ) ), X( tau, 't03', +( *( 't08', tau ), *( 't05', tau ) ) ) ) ) ) ), tau )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_0000101__noise0.6.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST (in LOOP_1)]` | `t01` | Exact Token Match | $\ge$ 215 | **215** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `t06` | Exact Token Match | $\ge$ 189 | **189** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `t02` | Exact Token Match | $\ge$ 513 | **513** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `t09` | Exact Token Match | $\ge$ 1003 | **1003** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `t10` | Exact Token Match | $\ge$ 997 | **997** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `t04` | Exact Token Match | $\ge$ 194 | **194** | ✅ **VERIFIED** |
| `[ST (in PAR_2)]` | `t65` | Exact Token Match | $\ge$ 326 | **326** | ✅ **VERIFIED** |
| `[ST (in LOOP_4)]` | `t21` | Exact Token Match | $\ge$ 385 | **385** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t21⟩` | Exact Token Match | $\ge$ 273 | **385** | ✅ **VERIFIED** |
| `[AS (in PAR_3)]` | `[nested LOOP_4]` | Exact Token Match | $\ge$ 1 | **385** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `t19` | Exact Token Match | $\ge$ 193 | **193** | ✅ **VERIFIED** |
| `[ST (in LOOP_6)]` | `t71` | Exact Token Match | $\ge$ 63 | **63** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t71⟩` | Exact Token Match | $\ge$ 63 | **63** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t11` | Exact Token Match | $\ge$ 195 | **195** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t14` | Exact Token Match | $\ge$ 194 | **194** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t16` | Exact Token Match | $\ge$ 69 | **69** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t20` | Exact Token Match | $\ge$ 328 | **328** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t17` | Exact Token Match | $\ge$ 329 | **329** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t15` | Exact Token Match | $\ge$ 58 | **58** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t13` | Exact Token Match | $\ge$ 58 | **58** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t15, t13⟩` | Exact Token Match | $\ge$ 58 | **58** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t22` | Exact Token Match | $\ge$ 126 | **126** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t24` | Exact Token Match | $\ge$ 113 | **113** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `t23` | Exact Token Match | $\ge$ 112 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `t29` | Exact Token Match | $\ge$ 112 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t25` | Exact Token Match | $\ge$ 57 | **57** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t26` | Exact Token Match | $\ge$ 113 | **113** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t27` | Exact Token Match | $\ge$ 113 | **113** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t28` | Exact Token Match | $\ge$ 52 | **52** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t27, t28⟩` | Exact Token Match | $\ge$ 52 | **52** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t27, τ⟩` | Exact Token Match | $\ge$ 61 | **113** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t26, t27, t28⟩` | Exact Token Match | $\ge$ 52 | **52** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t26, t27, τ⟩` | Exact Token Match | $\ge$ 61 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t25, t26, t27, τ⟩` | Exact Token Match | $\ge$ 5 | **57** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, t26, t27, τ⟩` | Exact Token Match | $\ge$ 4 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t25, t26, t27⟩` | Exact Token Match | $\ge$ 57 | **57** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t25, t26⟩` | Exact Token Match | $\ge$ 57 | **57** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, t26, t27⟩` | Exact Token Match | $\ge$ 56 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, t26⟩` | Exact Token Match | $\ge$ 56 | **113** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨[nested PAR_7], t25, t26, t27, τ⟩` | Exact Token Match | $\ge$ 4 | **55** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨[nested PAR_7], τ, t26, t27, τ⟩` | Exact Token Match | $\ge$ 3 | **110** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨[nested PAR_7], τ, t26, t27⟩` | Exact Token Match | $\ge$ 55 | **110** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨[nested PAR_7], τ, t26⟩` | Exact Token Match | $\ge$ 55 | **111** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨[nested PAR_7], τ⟩` | Exact Token Match | $\ge$ 55 | **111** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t24, [nested PAR_7], t25, t26, t27, τ⟩` | Exact Token Match | $\ge$ 4 | **55** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t24, [nested PAR_7], τ, t26, t27, τ⟩` | Exact Token Match | $\ge$ 3 | **110** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t24, [nested PAR_7], τ, t26, t27⟩` | Exact Token Match | $\ge$ 55 | **110** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t24, [nested PAR_7], τ, t26⟩` | Exact Token Match | $\ge$ 55 | **111** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t24, [nested PAR_7], τ⟩` | Exact Token Match | $\ge$ 55 | **111** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t24, τ⟩` | Exact Token Match | $\ge$ 1 | **113** | ✅ **VERIFIED** |
| `[ST (in LOOP_8)]` | `t42` | Exact Token Match | $\ge$ 326 | **326** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t42⟩` | Exact Token Match | $\ge$ 326 | **326** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t38` | Exact Token Match | $\ge$ 324 | **324** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t39` | Exact Token Match | $\ge$ 327 | **327** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t43` | Exact Token Match | $\ge$ 91 | **91** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t44` | Exact Token Match | $\ge$ 91 | **91** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t43, t44⟩` | Exact Token Match | $\ge$ 91 | **91** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t40` | Exact Token Match | $\ge$ 82 | **82** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t34` | Exact Token Match | $\ge$ 70 | **70** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t36` | Exact Token Match | $\ge$ 325 | **325** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t33` | Exact Token Match | $\ge$ 325 | **325** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t46` | Exact Token Match | $\ge$ 325 | **325** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t30` | Exact Token Match | $\ge$ 60 | **60** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t46, τ⟩` | Exact Token Match | $\ge$ 265 | **325** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t33, t46, τ⟩` | Exact Token Match | $\ge$ 265 | **323** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t36, t33, t46, τ⟩` | Exact Token Match | $\ge$ 265 | **320** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t43, t44, t36, t33, t46, τ⟩` | Exact Token Match | $\ge$ 31 | **88** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t40, t36, t33, t46, τ⟩` | Exact Token Match | $\ge$ 22 | **82** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t34, t36, t33, t46, τ⟩` | Exact Token Match | $\ge$ 10 | **69** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, t36, t33, t46, τ⟩` | Exact Token Match | $\ge$ 22 | **320** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t40, t36, t33, t46⟩` | Exact Token Match | $\ge$ 82 | **82** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t40, t36, t33⟩` | Exact Token Match | $\ge$ 82 | **82** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t40, t36⟩` | Exact Token Match | $\ge$ 82 | **82** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, t36, t33, t46⟩` | Exact Token Match | $\ge$ 82 | **320** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, t36, t33⟩` | Exact Token Match | $\ge$ 82 | **322** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, t36⟩` | Exact Token Match | $\ge$ 82 | **325** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t44, t36, t33, t46, τ⟩` | Exact Token Match | $\ge$ 31 | **88** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t39, t43, t44, t36, t33, t46, τ⟩` | Exact Token Match | $\ge$ 31 | **88** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t39, t40, t36, t33, t46, τ⟩` | Exact Token Match | $\ge$ 22 | **82** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t39, t34, t36, t33, t46, τ⟩` | Exact Token Match | $\ge$ 10 | **69** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t39, τ, t36, t33, t46, τ⟩` | Exact Token Match | $\ge$ 22 | **320** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t39, τ⟩` | Exact Token Match | $\ge$ 2 | **327** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t39, t40, t36, t33, t46⟩` | Exact Token Match | $\ge$ 82 | **82** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t39, t40, t36, t33⟩` | Exact Token Match | $\ge$ 82 | **82** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t39, t40, t36⟩` | Exact Token Match | $\ge$ 82 | **82** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t39, τ, t36, t33, t46⟩` | Exact Token Match | $\ge$ 82 | **320** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t39, τ, t36, t33⟩` | Exact Token Match | $\ge$ 82 | **322** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t39, τ, t36⟩` | Exact Token Match | $\ge$ 82 | **323** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t39, t43, t44⟩` | Exact Token Match | $\ge$ 91 | **91** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t39, t43⟩` | Exact Token Match | $\ge$ 91 | **91** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t39, t40⟩` | Exact Token Match | $\ge$ 82 | **82** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t39, t34⟩` | Exact Token Match | $\ge$ 70 | **70** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t39, τ⟩` | Exact Token Match | $\ge$ 82 | **327** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t38, t39, t43, t44, t36, t33, t46, τ⟩` | Exact Token Match | $\ge$ 28 | **88** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t38, t39, t40, t36, t33, t46, τ⟩` | Exact Token Match | $\ge$ 19 | **80** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t38, t39, t34, t36, t33, t46, τ⟩` | Exact Token Match | $\ge$ 7 | **68** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t38, t39, τ, t36, t33, t46, τ⟩` | Exact Token Match | $\ge$ 19 | **317** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t38, t39, t43, t44, t36, t33, t46⟩` | Exact Token Match | $\ge$ 88 | **88** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t38, t39, t43, t44, t36, t33⟩` | Exact Token Match | $\ge$ 88 | **90** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t38, t39, t43, t44, t36⟩` | Exact Token Match | $\ge$ 88 | **90** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t38, t39, t40, t36, t33, t46⟩` | Exact Token Match | $\ge$ 79 | **80** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t38, t39, t40, t36, t33⟩` | Exact Token Match | $\ge$ 79 | **80** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t38, t39, t40, t36⟩` | Exact Token Match | $\ge$ 79 | **80** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t38, t39, t34, t36, t33, t46⟩` | Exact Token Match | $\ge$ 67 | **68** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t38, t39, t34, t36, t33⟩` | Exact Token Match | $\ge$ 67 | **68** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t38, t39, t34, t36⟩` | Exact Token Match | $\ge$ 67 | **68** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t38, t39, τ, t36, t33, t46⟩` | Exact Token Match | $\ge$ 79 | **317** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t38, t39, τ, t36, t33⟩` | Exact Token Match | $\ge$ 79 | **319** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t38, t39, τ, t36⟩` | Exact Token Match | $\ge$ 79 | **320** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t38, t39, t43, t44⟩` | Exact Token Match | $\ge$ 88 | **91** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t38, t39, t43⟩` | Exact Token Match | $\ge$ 88 | **91** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t38, t39, t40⟩` | Exact Token Match | $\ge$ 79 | **80** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t38, t39, t34⟩` | Exact Token Match | $\ge$ 67 | **69** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t38, t39, τ⟩` | Exact Token Match | $\ge$ 79 | **323** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, t39⟩` | Exact Token Match | $\ge$ 3 | **327** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t42, t38, t39, t43, t44, t36, t33, t46, τ⟩` | Exact Token Match | $\ge$ 27 | **87** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t42, t38, t39, t40, t36, t33, t46, τ⟩` | Exact Token Match | $\ge$ 18 | **80** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t42, t38, t39, t34, t36, t33, t46, τ⟩` | Exact Token Match | $\ge$ 6 | **68** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t42, t38, t39, τ, t36, t33, t46, τ⟩` | Exact Token Match | $\ge$ 18 | **316** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t42, t38, t39, t43, t44, t36, t33, t46⟩` | Exact Token Match | $\ge$ 87 | **87** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t42, t38, t39, t43, t44, t36, t33⟩` | Exact Token Match | $\ge$ 87 | **89** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t42, t38, t39, t43, t44, t36⟩` | Exact Token Match | $\ge$ 87 | **89** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t42, t38, t39, t40, t36, t33, t46⟩` | Exact Token Match | $\ge$ 78 | **80** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t42, t38, t39, t40, t36, t33⟩` | Exact Token Match | $\ge$ 78 | **80** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t42, t38, t39, t40, t36⟩` | Exact Token Match | $\ge$ 78 | **80** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t42, t38, t39, t34, t36, t33, t46⟩` | Exact Token Match | $\ge$ 66 | **68** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t42, t38, t39, t34, t36, t33⟩` | Exact Token Match | $\ge$ 66 | **68** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t42, t38, t39, t34, t36⟩` | Exact Token Match | $\ge$ 66 | **68** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t42, t38, t39, τ, t36, t33, t46⟩` | Exact Token Match | $\ge$ 78 | **316** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t42, t38, t39, τ, t36, t33⟩` | Exact Token Match | $\ge$ 78 | **318** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t42, t38, t39, τ, t36⟩` | Exact Token Match | $\ge$ 78 | **319** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t42, t38, t39, t43, t44⟩` | Exact Token Match | $\ge$ 87 | **90** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t42, t38, t39, t43⟩` | Exact Token Match | $\ge$ 87 | **90** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t42, t38, t39, t40⟩` | Exact Token Match | $\ge$ 78 | **80** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t42, t38, t39, t34⟩` | Exact Token Match | $\ge$ 66 | **69** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t42, t38, t39, τ⟩` | Exact Token Match | $\ge$ 78 | **322** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t42, τ, t39⟩` | Exact Token Match | $\ge$ 2 | **325** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t42, τ⟩` | Exact Token Match | $\ge$ 2 | **326** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t22, t42, t38, t39⟩` | Exact Token Match | $\ge$ 122 | **125** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t22, t42, t38⟩` | Exact Token Match | $\ge$ 122 | **125** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t22, t42⟩` | Exact Token Match | $\ge$ 125 | **125** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t24, [nested PAR_7], t25, t26, t27, τ, t42⟩` | Exact Token Match | $\ge$ 3 | **27** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t24, [nested PAR_7], τ, t26, t27, τ, t42⟩` | Exact Token Match | $\ge$ 2 | **50** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, t42, t38, t39⟩` | Exact Token Match | $\ge$ 84 | **322** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, t42, t38⟩` | Exact Token Match | $\ge$ 84 | **322** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, t42⟩` | Exact Token Match | $\ge$ 87 | **326** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, t22, t42, t38, t39⟩` | Exact Token Match | $\ge$ 64 | **125** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, t22, t42, t38⟩` | Exact Token Match | $\ge$ 64 | **125** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, t22, t42⟩` | Exact Token Match | $\ge$ 67 | **125** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, τ, t42, t38, t39⟩` | Exact Token Match | $\ge$ 26 | **322** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, τ, t42, t38⟩` | Exact Token Match | $\ge$ 26 | **322** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, τ, t42⟩` | Exact Token Match | $\ge$ 29 | **326** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, t22⟩` | Exact Token Match | $\ge$ 68 | **126** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, t24, [nested PAR_7]⟩` | Exact Token Match | $\ge$ 54 | **111** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, t24⟩` | Exact Token Match | $\ge$ 55 | **113** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t17, τ⟩` | Exact Token Match | $\ge$ 2 | **329** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t17, τ, t22, t42, t38, t39⟩` | Exact Token Match | $\ge$ 64 | **102** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t17, τ, t22, t42, t38⟩` | Exact Token Match | $\ge$ 64 | **102** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t17, τ, t22, t42⟩` | Exact Token Match | $\ge$ 67 | **102** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t17, τ, τ, t42, t38, t39⟩` | Exact Token Match | $\ge$ 26 | **275** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t17, τ, τ, t42, t38⟩` | Exact Token Match | $\ge$ 26 | **275** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t17, τ, τ, t42⟩` | Exact Token Match | $\ge$ 29 | **277** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t17, τ, t22⟩` | Exact Token Match | $\ge$ 68 | **102** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t17, τ, t24, [nested PAR_7]⟩` | Exact Token Match | $\ge$ 54 | **91** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t17, τ, t24⟩` | Exact Token Match | $\ge$ 55 | **93** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t17, τ, τ⟩` | Exact Token Match | $\ge$ 30 | **329** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t17, τ⟩` | Exact Token Match | $\ge$ 269 | **329** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t20, t17, τ⟩` | Exact Token Match | $\ge$ 1 | **326** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t20, t17, τ, t22, t42, t38, t39⟩` | Exact Token Match | $\ge$ 63 | **102** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t20, t17, τ, t22, t42, t38⟩` | Exact Token Match | $\ge$ 63 | **102** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t20, t17, τ, t22, t42⟩` | Exact Token Match | $\ge$ 66 | **102** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t20, t17, τ, τ, t42, t38, t39⟩` | Exact Token Match | $\ge$ 25 | **274** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t20, t17, τ, τ, t42, t38⟩` | Exact Token Match | $\ge$ 25 | **274** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t20, t17, τ, τ, t42⟩` | Exact Token Match | $\ge$ 28 | **276** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t20, t17, τ, t22⟩` | Exact Token Match | $\ge$ 67 | **102** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t20, t17, τ, t24, [nested PAR_7]⟩` | Exact Token Match | $\ge$ 53 | **91** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t20, t17, τ, t24⟩` | Exact Token Match | $\ge$ 54 | **93** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t20, t17, τ, τ⟩` | Exact Token Match | $\ge$ 29 | **326** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t20, t17, τ⟩` | Exact Token Match | $\ge$ 268 | **326** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, t17⟩` | Exact Token Match | $\ge$ 1 | **329** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, t20, t17, τ⟩` | Exact Token Match | $\ge$ 199 | **326** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, t20, t17⟩` | Exact Token Match | $\ge$ 259 | **326** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, t20⟩` | Exact Token Match | $\ge$ 259 | **328** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t16, t20, t17, τ⟩` | Exact Token Match | $\ge$ 8 | **68** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t16, t20, t17⟩` | Exact Token Match | $\ge$ 68 | **68** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t16, t20⟩` | Exact Token Match | $\ge$ 68 | **69** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t14, τ, t20, t17, τ⟩` | Exact Token Match | $\ge$ 64 | **135** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t14, τ, t20, t17⟩` | Exact Token Match | $\ge$ 124 | **135** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t14, τ, t20⟩` | Exact Token Match | $\ge$ 124 | **136** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t14, τ⟩` | Exact Token Match | $\ge$ 125 | **194** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, τ, t20, t17, τ⟩` | Exact Token Match | $\ge$ 5 | **326** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, τ, t20, t17⟩` | Exact Token Match | $\ge$ 65 | **326** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, τ, t20⟩` | Exact Token Match | $\ge$ 65 | **328** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t11, t14⟩` | Exact Token Match | $\ge$ 60 | **193** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t11, τ⟩` | Exact Token Match | $\ge$ 1 | **195** | ✅ **VERIFIED** |
| `[ST (in PAR_2)]` | `t69` | Exact Token Match | $\ge$ 88 | **88** | ✅ **VERIFIED** |
| `[ST (in PAR_2)]` | `t70` | Exact Token Match | $\ge$ 70 | **70** | ✅ **VERIFIED** |
| `[AS (in LOOP_1)]` | `[nested PAR_2]` | Exact Token Match | $\ge$ 329 | **387** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `t66` | Exact Token Match | $\ge$ 386 | **386** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `⟨[nested PAR_2], t66⟩` | Exact Token Match | $\ge$ 329 | **386** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `⟨τ, t66⟩` | Exact Token Match | $\ge$ 57 | **386** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `t03` | Exact Token Match | $\ge$ 92 | **92** | ✅ **VERIFIED** |
| `[ST (in LOOP_10)]` | `t08` | Exact Token Match | $\ge$ 99 | **99** | ✅ **VERIFIED** |
| `[ST (in PAR_9)]` | `⟨t08⟩` | Exact Token Match | $\ge$ 99 | **99** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `t05` | Exact Token Match | $\ge$ 99 | **99** | ✅ **VERIFIED** |
| `[ST (in PAR_9)]` | `⟨t05⟩` | Exact Token Match | $\ge$ 99 | **99** | ✅ **VERIFIED** |
| `[AS (in LOOP_1)]` | `[nested PAR_9]` | Exact Token Match | $\ge$ 99 | **100** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `⟨t09, τ⟩` | Exact Token Match | $\ge$ 812 | **1003** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 806 | **997** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `⟨t04, τ⟩` | Exact Token Match | $\ge$ 3 | **194** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `⟨[nested PAR_2], t66, τ⟩` | Exact Token Match | $\ge$ 138 | **386** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `⟨t66, τ⟩` | Exact Token Match | $\ge$ 195 | **386** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `⟨τ, t02⟩` | Exact Token Match | $\ge$ 324 | **513** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `⟨τ, t09, τ⟩` | Exact Token Match | $\ge$ 623 | **1003** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `⟨τ, t10, τ⟩` | Exact Token Match | $\ge$ 617 | **997** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `⟨τ, t09⟩` | Exact Token Match | $\ge$ 814 | **1003** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `⟨τ, t10⟩` | Exact Token Match | $\ge$ 808 | **997** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `⟨τ, t04⟩` | Exact Token Match | $\ge$ 5 | **194** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `⟨τ, [nested PAR_2], t66⟩` | Exact Token Match | $\ge$ 140 | **386** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `⟨τ, [nested PAR_2]⟩` | Exact Token Match | $\ge$ 140 | **387** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_1]` | Exact Token Match | $\ge$ 1 | **1000** | ✅ **VERIFIED** |
| `[AS (in PAR_5)]` | `[nested PAR_7]` | Exact Token Match | $\ge$ 112 | **111** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨t26, t27⟩` | Exact Token Match | $\ge$ 113 | **112** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨[nested PAR_7], t25, t26, t27⟩` | Exact Token Match | $\ge$ 56 | **55** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨[nested PAR_7], t25, t26⟩` | Exact Token Match | $\ge$ 56 | **55** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨[nested PAR_7], t25⟩` | Exact Token Match | $\ge$ 56 | **55** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨t24, [nested PAR_7], t25, t26, t27⟩` | Exact Token Match | $\ge$ 56 | **55** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨t24, [nested PAR_7], t25, t26⟩` | Exact Token Match | $\ge$ 56 | **55** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨t24, [nested PAR_7], t25⟩` | Exact Token Match | $\ge$ 56 | **55** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨t24, [nested PAR_7]⟩` | Exact Token Match | $\ge$ 112 | **111** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨t33, t46⟩` | Exact Token Match | $\ge$ 325 | **323** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨t36, t33, t46⟩` | Exact Token Match | $\ge$ 325 | **320** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨t36, t33⟩` | Exact Token Match | $\ge$ 325 | **322** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨t43, t44, t36, t33, t46⟩` | Exact Token Match | $\ge$ 91 | **88** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨t43, t44, t36, t33⟩` | Exact Token Match | $\ge$ 91 | **90** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨t43, t44, t36⟩` | Exact Token Match | $\ge$ 91 | **90** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨t34, t36, t33, t46⟩` | Exact Token Match | $\ge$ 70 | **69** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨t34, t36, t33⟩` | Exact Token Match | $\ge$ 70 | **69** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨t34, t36⟩` | Exact Token Match | $\ge$ 70 | **69** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨t39, t43, t44, t36, t33, t46⟩` | Exact Token Match | $\ge$ 91 | **88** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨t39, t43, t44, t36, t33⟩` | Exact Token Match | $\ge$ 91 | **90** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨t39, t43, t44, t36⟩` | Exact Token Match | $\ge$ 91 | **90** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨t39, t34, t36, t33, t46⟩` | Exact Token Match | $\ge$ 70 | **69** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨t39, t34, t36, t33⟩` | Exact Token Match | $\ge$ 70 | **69** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨t39, t34, t36⟩` | Exact Token Match | $\ge$ 70 | **69** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨t38, t39⟩` | Exact Token Match | $\ge$ 324 | **323** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨t42, t38, t39⟩` | Exact Token Match | $\ge$ 323 | **322** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨t42, t38⟩` | Exact Token Match | $\ge$ 323 | **322** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨t20, t17⟩` | Exact Token Match | $\ge$ 328 | **326** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨t46, t30⟩` | Exact Token Match | $\ge$ 60 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_5)]` | `⟨t33, t46, t30⟩` | Exact Token Match | $\ge$ 60 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_5)]` | `⟨t36, t33, t46, t30⟩` | Exact Token Match | $\ge$ 60 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_5)]` | `⟨t17, t15, t13⟩` | Exact Token Match | $\ge$ 58 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_5)]` | `⟨t17, t15⟩` | Exact Token Match | $\ge$ 58 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_5)]` | `⟨t20, t17, t15, t13⟩` | Exact Token Match | $\ge$ 57 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_5)]` | `⟨t20, t17, t15⟩` | Exact Token Match | $\ge$ 57 | **0** | ❌ **GHOST PATTERN** |
| `[AS (in PAR_3)]` | `[nested PAR_5]` | Exact Token Match | $\ge$ 329 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_3)]` | `⟨t19, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 193 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_3)]` | `⟨τ, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 136 | **0** | ❌ **GHOST PATTERN** |
| `[AS (in PAR_2)]` | `[nested PAR_3]` | Exact Token Match | $\ge$ 329 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_2)]` | `⟨[nested PAR_3], t69⟩` | Exact Token Match | $\ge$ 88 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_2)]` | `⟨[nested PAR_3], t70⟩` | Exact Token Match | $\ge$ 70 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_2)]` | `⟨[nested PAR_3], τ⟩` | Exact Token Match | $\ge$ 171 | **0** | ❌ **GHOST PATTERN** |

## Audit Summary
- **Perfect Pattern Verifications:** 221
- **Frequency Discrepancies:** 28
- **Ghost Patterns (Fatal):** 14
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 0.00%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 100.00%
- **Total Forced Volume (incl. unresolved AS, % of N):** 0.10%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 0.10%
- **Data Exposure (Confirmed % of Claimed Volume):** 94.53%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 0.00%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 97.68%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 0.00%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 61.35%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 100.00%
- **Max Fractional Exposure (Worst-Case Normalized):** 0.10% (expected length: 6443.28 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 0.10% (expected length: 9.29 events)
- **Mean Absolute Exposure Volume:** 0.01 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_4]`
- **Internal Structure:** `(t21 ∗ τ)`
- **Block Frequency:** 329

- **Max Loop Iterations:** `56`
- **Max Sub-Sequence Length:** `113` steps (if one case consumes all iterations)

![nested LOOP_4 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_4.png)

### `[nested LOOP_6]`
- **Internal Structure:** `(t71 ∗ τ)`
- **Block Frequency:** 63

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_6 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_6.png)

### `[nested PAR_7]`
- **Internal Structure:** `{t23, t29}`
- **Block Frequency:** 112



![nested PAR_7 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_PAR_7.png)

### `[nested LOOP_8]`
- **Internal Structure:** `(t42 ∗ τ)`
- **Block Frequency:** 326

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_8 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_8.png)

### `[nested PAR_5]`
- **Internal Structure:** `{[τ │ (t71 ∗ τ)], ⟨[t11 │ τ], [t14 │ τ], [τ │ t16], [t20 │ τ], t17, [⟨[τ │ ⟨t15, t13⟩], [t22 │ ⟨t24, [{t23, t29} │ τ], [t25 │ τ], t26, t27, [t28 │ τ]⟩ │ τ], [(t42 ∗ τ) │ τ], [t38 │ τ], t39, [⟨[⟨t43, t44⟩ │ t40 │ t34 │ τ], t36, t33, t46, [τ │ t30]⟩ │ τ]⟩ │ τ]⟩}`
- **Block Frequency:** 329



![nested PAR_5 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_PAR_5.png)

### `[nested PAR_3]`
- **Internal Structure:** `{(t21 ∗ τ), ⟨[t19 │ τ], {[τ │ (t71 ∗ τ)], ⟨[t11 │ τ], [t14 │ τ], [τ │ t16], [t20 │ τ], t17, [⟨[τ │ ⟨t15, t13⟩], [t22 │ ⟨t24, [{t23, t29} │ τ], [t25 │ τ], t26, t27, [t28 │ τ]⟩ │ τ], [(t42 ∗ τ) │ τ], [t38 │ τ], t39, [⟨[⟨t43, t44⟩ │ t40 │ t34 │ τ], t36, t33, t46, [τ │ t30]⟩ │ τ]⟩ │ τ]⟩}⟩}`
- **Block Frequency:** 329



![nested PAR_3 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_PAR_3.png)

### `[nested PAR_2]`
- **Internal Structure:** `{[t65 │ τ], ⟨[τ │ {(t21 ∗ τ), ⟨[t19 │ τ], {[τ │ (t71 ∗ τ)], ⟨[t11 │ τ], [t14 │ τ], [τ │ t16], [t20 │ τ], t17, [⟨[τ │ ⟨t15, t13⟩], [t22 │ ⟨t24, [{t23, t29} │ τ], [t25 │ τ], t26, t27, [t28 │ τ]⟩ │ τ], [(t42 ∗ τ) │ τ], [t38 │ τ], t39, [⟨[⟨t43, t44⟩ │ t40 │ t34 │ τ], t36, t33, t46, [τ │ t30]⟩ │ τ]⟩ │ τ]⟩}⟩}], [t69 │ t70 │ τ]⟩}`
- **Block Frequency:** 329



![nested PAR_2 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_PAR_2.png)

### `[nested LOOP_10]`
- **Internal Structure:** `(t08 ∗ τ)`
- **Block Frequency:** 99

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_10 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_10.png)

### `[nested LOOP_11]`
- **Internal Structure:** `(t05 ∗ τ)`
- **Block Frequency:** 99

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_11 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_11.png)

### `[nested PAR_9]`
- **Internal Structure:** `{(t08 ∗ τ), (t05 ∗ τ)}`
- **Block Frequency:** 99



![nested PAR_9 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_PAR_9.png)

### `[nested LOOP_1]`
- **Internal Structure:** `([t01 │ ⟨[τ │ t06], [t02 │ ⟨[t09 │ t10 │ t04 │ ⟨[{[t65 │ τ], ⟨[τ │ {(t21 ∗ τ), ⟨[t19 │ τ], {[τ │ (t71 ∗ τ)], ⟨[t11 │ τ], [t14 │ τ], [τ │ t16], [t20 │ τ], t17, [⟨[τ │ ⟨t15, t13⟩], [t22 │ ⟨t24, [{t23, t29} │ τ], [t25 │ τ], t26, t27, [t28 │ τ]⟩ │ τ], [(t42 ∗ τ) │ τ], [t38 │ τ], t39, [⟨[⟨t43, t44⟩ │ t40 │ t34 │ τ], t36, t33, t46, [τ │ t30]⟩ │ τ]⟩ │ τ]⟩}⟩}], [t69 │ t70 │ τ]⟩} │ τ], t66⟩], [τ │ t03 │ {(t08 ∗ τ), (t05 ∗ τ)}]⟩]⟩] ∗ τ)`
- **Block Frequency:** 1000

- **Max Loop Iterations:** `2308`
- **Max Sub-Sequence Length:** `4617` steps (if one case consumes all iterations)

![nested LOOP_1 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_1.png)
