# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_101010.xes` |
| **Noise Threshold** | `0.4` |
| **Fitness** | `0.8622967273456791` |
| **Precision** | `0.5500864915867274` |
| **Total Cases in Log** | `250` |
| **Unique Activities** | `48` |
| **XOR Operators** | `34` |
| **LOOP Operators** | `17` |
| **SEQ Operators** | `32` |
| **PAR Operators** | `9` |
| **Binarization Additions** | `25` |
| **Tau Operators Added** | `26` |
| **Total Found Patterns** | `247` |
| **Verified Patterns** | `144` |
| **Discrepancy Patterns** | `42` |
| **Ghost Patterns** | `1` |
| **Nested LOOPs** | `17` |
| **Nested PARs** | `9` |
| **Tree Exposure (Strict, End-to-End % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `8.69%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `5.15%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `43.14%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `0.00%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `0.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `90.98%` |
| **Data Exposure, ST-only (% confirmed)** | `89.91%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `93.74%` |
| **Data Coverage, ST-only (% of real log)** | `28.64%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `69.57%` |
| **Data Coverage, Total (% of real log)** | `94.75%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `3.04%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `56.32%` |
| **Mean Absolute Exposure Volume (events/case)** | `3.94` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_101010__noise0.4__gt.png)


```text
->( 't09', 't10', X( ->( 't06', 't04', 't03', 't02' ), ->( +( X( tau, 't13' ), ->( X( 't19', ->( 't11', X( 't14', 't05' ), X( tau, *( 't15', tau ) ), X( tau, 't16' ) ) ), 't20' ) ), 't17', *( 't21', tau ), X( tau, ->( 't24', +( 't23', 't29' ) ) ), X( 't22', 't25' ), +( X( tau, *( 't34', tau ) ), ->( X( tau, ->( 't26', 't27', *( 't28', tau ) ) ), *( 't42', tau ), 't38', *( ->( 't39', X( ->( 't43', 't44' ), 't40' ), *( 't36', tau ) ), tau ) ) ), X( ->( 't30', X( tau, 't71' ) ), 't33' ), 't46', X( tau, +( *( 't69', tau ), X( tau, *( 't70', tau ) ) ) ), 't47', +( *( 't62', tau ), *( 't45', tau ), *( 't48', tau ), *( 't60', tau ), *( 't37', tau ), *( 't68', tau ) ), *( 't64', tau ), *( 't65', tau ), 't66' ) ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_101010__noise0.4__gt.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST]` | `t09` | Exact Token Match | $\ge$ 182 | **182** | ✅ **VERIFIED** |
| `[ST]` | `t10` | Exact Token Match | $\ge$ 250 | **250** | ✅ **VERIFIED** |
| `[ST]` | `t06` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `t04` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `t03` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `t02` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t03, t02⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t04, t03, t02⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t04, t03⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t06, t04, t03, t02⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t06, t04, t03⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t06, t04⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `t13` | Exact Token Match | $\ge$ 26 | **26** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `t19` | Exact Token Match | $\ge$ 77 | **77** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `t11` | Exact Token Match | $\ge$ 141 | **141** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `t14` | Exact Token Match | $\ge$ 121 | **121** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `t05` | Exact Token Match | $\ge$ 37 | **37** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `t15` | Exact Token Match | $\ge$ 54 | **54** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t15⟩` | Exact Token Match | $\ge$ 54 | **54** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `t16` | Exact Token Match | $\ge$ 74 | **74** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨τ, t16⟩` | Exact Token Match | $\ge$ 20 | **74** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t14, τ⟩` | Exact Token Match | $\ge$ 47 | **121** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t14, t15⟩` | Exact Token Match | $\ge$ 17 | **39** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t11, t14, τ⟩` | Exact Token Match | $\ge$ 30 | **114** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t11, t14⟩` | Exact Token Match | $\ge$ 104 | **114** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t11, t05⟩` | Exact Token Match | $\ge$ 20 | **27** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `t20` | Exact Token Match | $\ge$ 212 | **212** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t19, t20⟩` | Exact Token Match | $\ge$ 54 | **77** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t11, t14, τ, t20⟩` | Exact Token Match | $\ge$ 7 | **82** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t14, τ, t20⟩` | Exact Token Match | $\ge$ 24 | **82** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t16, t20⟩` | Exact Token Match | $\ge$ 51 | **74** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨τ, t20⟩` | Exact Token Match | $\ge$ 61 | **212** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_1]` | Exact Token Match | $\ge$ 235 | **249** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t21` | Exact Token Match | $\ge$ 290 | **290** | ✅ **VERIFIED** |
| `[ST]` | `⟨t21⟩` | Exact Token Match | $\ge$ 208 | **223** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_3]` | Exact Token Match | $\ge$ 1 | **249** | ✅ **VERIFIED** |
| `[ST (in PAR_4)]` | `t23` | Exact Token Match | $\ge$ 112 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_4)]` | `t29` | Exact Token Match | $\ge$ 78 | **78** | ✅ **VERIFIED** |
| `[ST (in LOOP_6)]` | `t34` | Exact Token Match | $\ge$ 104 | **104** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t34⟩` | Exact Token Match | $\ge$ 104 | **104** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t26` | Exact Token Match | $\ge$ 112 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t27` | Exact Token Match | $\ge$ 112 | **112** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `t28` | Exact Token Match | $\ge$ 87 | **87** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t28⟩` | Exact Token Match | $\ge$ 87 | **87** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t27, t28⟩` | Exact Token Match | $\ge$ 87 | **87** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t27, τ⟩` | Exact Token Match | $\ge$ 25 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t26, t27, t28⟩` | Exact Token Match | $\ge$ 87 | **87** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t26, t27, τ⟩` | Exact Token Match | $\ge$ 25 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t26, t27⟩` | Exact Token Match | $\ge$ 112 | **112** | ✅ **VERIFIED** |
| `[ST (in LOOP_8)]` | `t42` | Exact Token Match | $\ge$ 368 | **368** | ✅ **VERIFIED** |
| `[AS (in PAR_5)]` | `[nested LOOP_8]` | Exact Token Match | $\ge$ 1 | **368** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t38` | Exact Token Match | $\ge$ 165 | **165** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `t39` | Exact Token Match | $\ge$ 337 | **337** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `t43` | Exact Token Match | $\ge$ 115 | **115** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `t44` | Exact Token Match | $\ge$ 115 | **115** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨t43, t44⟩` | Exact Token Match | $\ge$ 115 | **115** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `t40` | Exact Token Match | $\ge$ 148 | **148** | ✅ **VERIFIED** |
| `[ST (in LOOP_10)]` | `t36` | Exact Token Match | $\ge$ 438 | **438** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨t36⟩` | Exact Token Match | $\ge$ 88 | **438** | ✅ **VERIFIED** |
| `[AS (in LOOP_9)]` | `[nested LOOP_10]` | Exact Token Match | $\ge$ 1 | **224** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨t39, τ⟩` | Exact Token Match | $\ge$ 74 | **337** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨t39, t43, t44⟩` | Exact Token Match | $\ge$ 115 | **115** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨t39, t43⟩` | Exact Token Match | $\ge$ 115 | **115** | ✅ **VERIFIED** |
| `[AS (in PAR_5)]` | `[nested LOOP_9]` | Exact Token Match | $\ge$ 1 | **37** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t38, [nested LOOP_9]⟩` | Exact Token Match | $\ge$ 1 | **14** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨[nested LOOP_8], t38⟩` | Exact Token Match | $\ge$ 1 | **165** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_5]` | Exact Token Match | $\ge$ 165 | **249** | ✅ **VERIFIED** |
| `[ST]` | `t30` | Exact Token Match | $\ge$ 36 | **36** | ✅ **VERIFIED** |
| `[ST]` | `t71` | Exact Token Match | $\ge$ 25 | **25** | ✅ **VERIFIED** |
| `[ST]` | `⟨t30, τ⟩` | Exact Token Match | $\ge$ 11 | **36** | ✅ **VERIFIED** |
| `[ST]` | `t33` | Exact Token Match | $\ge$ 145 | **145** | ✅ **VERIFIED** |
| `[ST (in LOOP_12)]` | `t69` | Exact Token Match | $\ge$ 110 | **110** | ✅ **VERIFIED** |
| `[ST (in PAR_11)]` | `⟨t69⟩` | Exact Token Match | $\ge$ 88 | **110** | ✅ **VERIFIED** |
| `[AS (in PAR_11)]` | `[nested LOOP_12]` | Exact Token Match | $\ge$ 1 | **110** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `t70` | Exact Token Match | $\ge$ 99 | **99** | ✅ **VERIFIED** |
| `[ST (in PAR_11)]` | `⟨t70⟩` | Exact Token Match | $\ge$ 99 | **99** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_11]` | Exact Token Match | $\ge$ 99 | **106** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `t62` | Exact Token Match | $\ge$ 250 | **250** | ✅ **VERIFIED** |
| `[ST (in PAR_14)]` | `⟨t62⟩` | Exact Token Match | $\ge$ 158 | **250** | ✅ **VERIFIED** |
| `[AS (in PAR_14)]` | `[nested LOOP_15]` | Exact Token Match | $\ge$ 1 | **250** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `t45` | Exact Token Match | $\ge$ 198 | **198** | ✅ **VERIFIED** |
| `[ST (in PAR_16)]` | `⟨t45⟩` | Exact Token Match | $\ge$ 198 | **198** | ✅ **VERIFIED** |
| `[ST (in LOOP_19)]` | `t48` | Exact Token Match | $\ge$ 204 | **204** | ✅ **VERIFIED** |
| `[ST (in PAR_18)]` | `⟨t48⟩` | Exact Token Match | $\ge$ 204 | **204** | ✅ **VERIFIED** |
| `[ST (in LOOP_21)]` | `t60` | Exact Token Match | $\ge$ 155 | **155** | ✅ **VERIFIED** |
| `[ST (in PAR_20)]` | `⟨t60⟩` | Exact Token Match | $\ge$ 155 | **155** | ✅ **VERIFIED** |
| `[ST (in LOOP_23)]` | `t37` | Exact Token Match | $\ge$ 193 | **193** | ✅ **VERIFIED** |
| `[ST (in PAR_22)]` | `⟨t37⟩` | Exact Token Match | $\ge$ 193 | **193** | ✅ **VERIFIED** |
| `[ST (in LOOP_24)]` | `t68` | Exact Token Match | $\ge$ 204 | **204** | ✅ **VERIFIED** |
| `[ST (in PAR_22)]` | `⟨t68⟩` | Exact Token Match | $\ge$ 204 | **204** | ✅ **VERIFIED** |
| `[ST (in LOOP_25)]` | `t64` | Exact Token Match | $\ge$ 182 | **182** | ✅ **VERIFIED** |
| `[ST (in LOOP_26)]` | `t65` | Exact Token Match | $\ge$ 341 | **341** | ✅ **VERIFIED** |
| `[ST]` | `⟨t65⟩` | Exact Token Match | $\ge$ 53 | **192** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_26]` | Exact Token Match | $\ge$ 1 | **240** | ✅ **VERIFIED** |
| `[ST]` | `t66` | Exact Token Match | $\ge$ 197 | **197** | ✅ **VERIFIED** |
| `[ST]` | `⟨t65, t66⟩` | Exact Token Match | $\ge$ 53 | **160** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested LOOP_26], t66⟩` | Exact Token Match | $\ge$ 1 | **189** | ✅ **VERIFIED** |
| `[ST]` | `⟨t64, t65, t66⟩` | Exact Token Match | $\ge$ 38 | **111** | ✅ **VERIFIED** |
| `[ST]` | `⟨t64, t65⟩` | Exact Token Match | $\ge$ 38 | **119** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_14], t64, t65, t66⟩` | Exact Token Match | $\ge$ 38 | **111** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_14], τ⟩` | Exact Token Match | $\ge$ 7 | **182** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_14], t64, t65⟩` | Exact Token Match | $\ge$ 38 | **119** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_14], τ⟩` | Exact Token Match | $\ge$ 15 | **182** | ✅ **VERIFIED** |
| `[ST]` | `⟨t47, [nested PAR_14], t64, t65, t66⟩` | Exact Token Match | $\ge$ 11 | **74** | ✅ **VERIFIED** |
| `[ST]` | `⟨t47, [nested PAR_14], t64, t65⟩` | Exact Token Match | $\ge$ 11 | **81** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_14], t64⟩` | Exact Token Match | $\ge$ 5 | **125** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_14]⟩` | Exact Token Match | $\ge$ 27 | **182** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t47, [nested PAR_14], t64⟩` | Exact Token Match | $\ge$ 56 | **85** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t47, [nested PAR_14]⟩` | Exact Token Match | $\ge$ 78 | **107** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t47⟩` | Exact Token Match | $\ge$ 78 | **111** | ✅ **VERIFIED** |
| `[ST]` | `⟨t46, τ⟩` | Exact Token Match | $\ge$ 45 | **191** | ✅ **VERIFIED** |
| `[ST]` | `⟨t46, τ, t47, [nested PAR_14], t64⟩` | Exact Token Match | $\ge$ 56 | **80** | ✅ **VERIFIED** |
| `[ST]` | `⟨t46, τ, t47, [nested PAR_14]⟩` | Exact Token Match | $\ge$ 78 | **91** | ✅ **VERIFIED** |
| `[ST]` | `⟨t46, τ, t47⟩` | Exact Token Match | $\ge$ 78 | **92** | ✅ **VERIFIED** |
| `[ST]` | `⟨t46, τ⟩` | Exact Token Match | $\ge$ 105 | **191** | ✅ **VERIFIED** |
| `[ST]` | `⟨t30, τ, t46⟩` | Exact Token Match | $\ge$ 11 | **17** | ✅ **VERIFIED** |
| `[ST]` | `⟨t33, t46, τ⟩` | Exact Token Match | $\ge$ 1 | **132** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t46⟩` | Exact Token Match | $\ge$ 68 | **191** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_5], t33, t46⟩` | Exact Token Match | $\ge$ 61 | **132** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_5], t33⟩` | Exact Token Match | $\ge$ 61 | **145** | ✅ **VERIFIED** |
| `[ST]` | `⟨t22, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 37 | **102** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t22⟩` | Exact Token Match | $\ge$ 9 | **106** | ✅ **VERIFIED** |
| `[ST]` | `⟨t21, τ⟩` | Exact Token Match | $\ge$ 96 | **223** | ✅ **VERIFIED** |
| `[ST]` | `⟨t21, t24, [nested PAR_4]⟩` | Exact Token Match | $\ge$ 71 | **81** | ✅ **VERIFIED** |
| `[ST]` | `⟨t21, t24⟩` | Exact Token Match | $\ge$ 71 | **81** | ✅ **VERIFIED** |
| `[ST]` | `⟨t17, t21, τ⟩` | Exact Token Match | $\ge$ 93 | **169** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], t17, t21, τ⟩` | Exact Token Match | $\ge$ 79 | **169** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t17⟩` | Exact Token Match | $\ge$ 11 | **185** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06, t04, t03, t02⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06, t04, t03⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06, t04⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, [nested PAR_1], t17, t21, τ⟩` | Exact Token Match | $\ge$ 79 | **169** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ, t17⟩` | Exact Token Match | $\ge$ 11 | **185** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 235 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 14 | **250** | ✅ **VERIFIED** |
| `[ST]` | `⟨t09, t10, [nested PAR_1], t17, t21, τ⟩` | Exact Token Match | $\ge$ 11 | **133** | ✅ **VERIFIED** |
| `[ST]` | `⟨t09, t10, [nested PAR_1], t17, t21⟩` | Exact Token Match | $\ge$ 123 | **133** | ✅ **VERIFIED** |
| `[ST]` | `⟨t09, t10, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 167 | **181** | ✅ **VERIFIED** |
| `[ST]` | `⟨t09, t10⟩` | Exact Token Match | $\ge$ 182 | **182** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t10, [nested PAR_1], t17, t21⟩` | Exact Token Match | $\ge$ 9 | **169** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t10, [nested PAR_1], t17⟩` | Exact Token Match | $\ge$ 50 | **185** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t10, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 53 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t10⟩` | Exact Token Match | $\ge$ 68 | **250** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t15, t16⟩` | Exact Token Match | $\ge$ 54 | **7** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_1)]` | `⟨t14, t15, t16⟩` | Exact Token Match | $\ge$ 17 | **3** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_1)]` | `⟨t15, t16, t20⟩` | Exact Token Match | $\ge$ 31 | **7** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t17` | Exact Token Match | $\ge$ 246 | **185** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t24` | Exact Token Match | $\ge$ 112 | **95** | ⚠️ **DISCREPANCY** |
| `[AS]` | `[nested PAR_4]` | Exact Token Match | $\ge$ 112 | **103** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t24, [nested PAR_4]⟩` | Exact Token Match | $\ge$ 112 | **95** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t22` | Exact Token Match | $\ge$ 121 | **106** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t25` | Exact Token Match | $\ge$ 60 | **54** | ⚠️ **DISCREPANCY** |
| `[ST (in LOOP_9)]` | `⟨t39, t40⟩` | Exact Token Match | $\ge$ 148 | **122** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t30, t71⟩` | Exact Token Match | $\ge$ 25 | **16** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t46` | Exact Token Match | $\ge$ 249 | **191** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t47` | Exact Token Match | $\ge$ 177 | **111** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_20)]` | `[nested PAR_22]` | Exact Token Match | $\ge$ 204 | **176** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_18)]` | `[nested PAR_20]` | Exact Token Match | $\ge$ 204 | **140** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_16)]` | `[nested PAR_18]` | Exact Token Match | $\ge$ 204 | **140** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_14)]` | `[nested PAR_16]` | Exact Token Match | $\ge$ 204 | **140** | ⚠️ **DISCREPANCY** |
| `[AS]` | `[nested PAR_14]` | Exact Token Match | $\ge$ 204 | **182** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t64⟩` | Exact Token Match | $\ge$ 182 | **125** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_14], t64⟩` | Exact Token Match | $\ge$ 182 | **125** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t47, [nested PAR_14], t64⟩` | Exact Token Match | $\ge$ 155 | **85** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t47, [nested PAR_14]⟩` | Exact Token Match | $\ge$ 177 | **107** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_11], t47, [nested PAR_14], t64⟩` | Exact Token Match | $\ge$ 50 | **1** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_11], t47, [nested PAR_14]⟩` | Exact Token Match | $\ge$ 72 | **6** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_11], t47⟩` | Exact Token Match | $\ge$ 72 | **8** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t46, [nested PAR_11], t47, [nested PAR_14]⟩` | Exact Token Match | $\ge$ 72 | **1** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t46, [nested PAR_11], t47⟩` | Exact Token Match | $\ge$ 72 | **1** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t46, [nested PAR_11]⟩` | Exact Token Match | $\ge$ 99 | **58** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t30, t71, t46⟩` | Exact Token Match | $\ge$ 25 | **2** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t33, t46⟩` | Exact Token Match | $\ge$ 145 | **132** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t17, t21, t24, [nested PAR_4]⟩` | Exact Token Match | $\ge$ 68 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t17, t21, t24⟩` | Exact Token Match | $\ge$ 68 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t17, t21⟩` | Exact Token Match | $\ge$ 205 | **169** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_1], t17, t21, t24, [nested PAR_4]⟩` | Exact Token Match | $\ge$ 54 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_1], t17, t21, t24⟩` | Exact Token Match | $\ge$ 54 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_1], t17, t21⟩` | Exact Token Match | $\ge$ 191 | **169** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_1], t17⟩` | Exact Token Match | $\ge$ 232 | **185** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, [nested PAR_1], t17, t21, t24, [nested PAR_4]⟩` | Exact Token Match | $\ge$ 54 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, [nested PAR_1], t17, t21, t24⟩` | Exact Token Match | $\ge$ 54 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, [nested PAR_1], t17, t21⟩` | Exact Token Match | $\ge$ 191 | **169** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, [nested PAR_1], t17⟩` | Exact Token Match | $\ge$ 232 | **185** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t09, t10, [nested PAR_1], t17⟩` | Exact Token Match | $\ge$ 164 | **141** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t46, [nested PAR_11], t47, [nested PAR_14], t64⟩` | Exact Token Match | $\ge$ 50 | **0** | ❌ **GHOST PATTERN** |

## Audit Summary
- **Perfect Pattern Verifications:** 144
- **Frequency Discrepancies:** 42
- **Ghost Patterns (Fatal):** 1
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 8.69%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 5.15%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 43.14%
- **Total Forced Volume (incl. unresolved AS, % of N):** 0.00%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 0.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 90.98%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 89.91%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 93.74%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 28.64%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 69.57%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 94.75%
- **Max Fractional Exposure (Worst-Case Normalized):** 3.04% (expected length: 522.93 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 56.32% (expected length: 28.25 events)
- **Mean Absolute Exposure Volume:** 3.94 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_2]`
- **Internal Structure:** `(t15 ∗ τ)`
- **Block Frequency:** 54

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_2 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.4__gt_nested_LOOP_2.png)

### `[nested PAR_1]`
- **Internal Structure:** `{[τ │ t13], ⟨[t19 │ ⟨[t11 │ τ], [t14 │ t05], [⟨[τ │ (t15 ∗ τ)], [τ │ t16]⟩ │ τ]⟩], [t20 │ τ]⟩}`
- **Block Frequency:** 235



![nested PAR_1 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.4__gt_nested_PAR_1.png)

### `[nested LOOP_3]`
- **Internal Structure:** `(t21 ∗ τ)`
- **Block Frequency:** 249

- **Max Loop Iterations:** `41`
- **Max Sub-Sequence Length:** `83` steps (if one case consumes all iterations)

![nested LOOP_3 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.4__gt_nested_LOOP_3.png)

### `[nested PAR_4]`
- **Internal Structure:** `{t23, [t29 │ τ]}`
- **Block Frequency:** 112



![nested PAR_4 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.4__gt_nested_PAR_4.png)

### `[nested LOOP_6]`
- **Internal Structure:** `(t34 ∗ τ)`
- **Block Frequency:** 104

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_6 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.4__gt_nested_LOOP_6.png)

### `[nested LOOP_7]`
- **Internal Structure:** `(t28 ∗ τ)`
- **Block Frequency:** 87

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_7 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.4__gt_nested_LOOP_7.png)

### `[nested LOOP_8]`
- **Internal Structure:** `(t42 ∗ τ)`
- **Block Frequency:** 165

- **Max Loop Iterations:** `203`
- **Max Sub-Sequence Length:** `407` steps (if one case consumes all iterations)

![nested LOOP_8 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.4__gt_nested_LOOP_8.png)

### `[nested LOOP_10]`
- **Internal Structure:** `(t36 ∗ τ)`
- **Block Frequency:** 263

- **Max Loop Iterations:** `175`
- **Max Sub-Sequence Length:** `351` steps (if one case consumes all iterations)

![nested LOOP_10 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.4__gt_nested_LOOP_10.png)

### `[nested LOOP_9]`
- **Internal Structure:** `(⟨t39, [⟨[⟨t43, t44⟩ │ t40], (t36 ∗ τ)⟩ │ τ]⟩ ∗ τ)`
- **Block Frequency:** 165

- **Max Loop Iterations:** `172`
- **Max Sub-Sequence Length:** `345` steps (if one case consumes all iterations)

![nested LOOP_9 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.4__gt_nested_LOOP_9.png)

### `[nested PAR_5]`
- **Internal Structure:** `{[τ │ (t34 ∗ τ)], ⟨[τ │ ⟨t26, t27, [(t28 ∗ τ) │ τ]⟩], (t42 ∗ τ), t38, (⟨t39, [⟨[⟨t43, t44⟩ │ t40], (t36 ∗ τ)⟩ │ τ]⟩ ∗ τ)⟩}`
- **Block Frequency:** 165



![nested PAR_5 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.4__gt_nested_PAR_5.png)

### `[nested LOOP_12]`
- **Internal Structure:** `(t69 ∗ τ)`
- **Block Frequency:** 99

- **Max Loop Iterations:** `11`
- **Max Sub-Sequence Length:** `23` steps (if one case consumes all iterations)

![nested LOOP_12 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.4__gt_nested_LOOP_12.png)

### `[nested LOOP_13]`
- **Internal Structure:** `(t70 ∗ τ)`
- **Block Frequency:** 99

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_13 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.4__gt_nested_LOOP_13.png)

### `[nested PAR_11]`
- **Internal Structure:** `{(t69 ∗ τ), [τ │ (t70 ∗ τ)]}`
- **Block Frequency:** 99



![nested PAR_11 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.4__gt_nested_PAR_11.png)

### `[nested LOOP_15]`
- **Internal Structure:** `(t62 ∗ τ)`
- **Block Frequency:** 204

- **Max Loop Iterations:** `46`
- **Max Sub-Sequence Length:** `93` steps (if one case consumes all iterations)

![nested LOOP_15 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.4__gt_nested_LOOP_15.png)

### `[nested LOOP_17]`
- **Internal Structure:** `(t45 ∗ τ)`
- **Block Frequency:** 198

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_17 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.4__gt_nested_LOOP_17.png)

### `[nested LOOP_19]`
- **Internal Structure:** `(t48 ∗ τ)`
- **Block Frequency:** 204

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_19 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.4__gt_nested_LOOP_19.png)

### `[nested LOOP_21]`
- **Internal Structure:** `(t60 ∗ τ)`
- **Block Frequency:** 155

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_21 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.4__gt_nested_LOOP_21.png)

### `[nested LOOP_23]`
- **Internal Structure:** `(t37 ∗ τ)`
- **Block Frequency:** 193

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_23 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.4__gt_nested_LOOP_23.png)

### `[nested LOOP_24]`
- **Internal Structure:** `(t68 ∗ τ)`
- **Block Frequency:** 204

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_24 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.4__gt_nested_LOOP_24.png)

### `[nested PAR_22]`
- **Internal Structure:** `{[(t37 ∗ τ) │ τ], (t68 ∗ τ)}`
- **Block Frequency:** 204



![nested PAR_22 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.4__gt_nested_PAR_22.png)

### `[nested PAR_20]`
- **Internal Structure:** `{[(t60 ∗ τ) │ τ], [(t37 ∗ τ) │ τ], (t68 ∗ τ)}`
- **Block Frequency:** 204



![nested PAR_20 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.4__gt_nested_PAR_20.png)

### `[nested PAR_18]`
- **Internal Structure:** `{(t48 ∗ τ), [(t60 ∗ τ) │ τ], [(t37 ∗ τ) │ τ], (t68 ∗ τ)}`
- **Block Frequency:** 204



![nested PAR_18 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.4__gt_nested_PAR_18.png)

### `[nested PAR_16]`
- **Internal Structure:** `{[(t45 ∗ τ) │ τ], (t48 ∗ τ), [(t60 ∗ τ) │ τ], [(t37 ∗ τ) │ τ], (t68 ∗ τ)}`
- **Block Frequency:** 204



![nested PAR_16 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.4__gt_nested_PAR_16.png)

### `[nested PAR_14]`
- **Internal Structure:** `{(t62 ∗ τ), [(t45 ∗ τ) │ τ], (t48 ∗ τ), [(t60 ∗ τ) │ τ], [(t37 ∗ τ) │ τ], (t68 ∗ τ)}`
- **Block Frequency:** 204



![nested PAR_14 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.4__gt_nested_PAR_14.png)

### `[nested LOOP_25]`
- **Internal Structure:** `(t64 ∗ τ)`
- **Block Frequency:** 182

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_25 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.4__gt_nested_LOOP_25.png)

### `[nested LOOP_26]`
- **Internal Structure:** `(t65 ∗ τ)`
- **Block Frequency:** 197

- **Max Loop Iterations:** `144`
- **Max Sub-Sequence Length:** `289` steps (if one case consumes all iterations)

![nested LOOP_26 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.4__gt_nested_LOOP_26.png)
