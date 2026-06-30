# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_101010.xes` |
| **Noise Threshold** | `0.6` |
| **Fitness** | `0.8019719455619262` |
| **Precision** | `0.7355148604022816` |
| **Total Cases in Log** | `250` |
| **Unique Activities** | `48` |
| **XOR Operators** | `31` |
| **LOOP Operators** | `16` |
| **SEQ Operators** | `35` |
| **PAR Operators** | `6` |
| **Binarization Additions** | `28` |
| **Tau Operators Added** | `26` |
| **Total Found Patterns** | `305` |
| **Verified Patterns** | `139` |
| **Discrepancy Patterns** | `99` |
| **Ghost Patterns** | `4` |
| **Nested LOOPs** | `16` |
| **Nested PARs** | `6` |
| **Tree Exposure (Strict, End-to-End % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `8.75%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `5.19%` |
| **Tree Exposure (Local-Strict % of N)** | `91.32%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `13.18%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `0.00%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `0.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `82.13%` |
| **Data Exposure, ST-only (% confirmed)** | `80.41%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `84.78%` |
| **Data Coverage, ST-only (% of real log)** | `42.10%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `68.28%` |
| **Data Coverage, Total (% of real log)** | `87.17%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `9.11%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `84.22%` |
| **Mean Absolute Exposure Volume (events/case)** | `4.56` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_101010__noise0.6.png)


```text
->( 't09', 't10', X( ->( 't06', 't04', 't03', 't02' ), ->( +( X( tau, 't13' ), ->( X( 't19', ->( 't11', X( *( 't14', tau ), *( ->( 't05', 't15' ), tau ) ), 't16' ) ), 't20' ) ), 't17', 't21', X( 't22', ->( 't24', +( 't23', 't29' ), 't25', 't26', 't27', *( 't28', tau ) ) ), *( 't42', tau ), 't38', 't39', 't40', X( ->( 't43', *( 't44', tau ) ), 't34' ), *( 't36', tau ), X( ->( 't30', 't71' ), 't33' ), X( tau, +( *( 't69', tau ), *( 't70', tau ) ) ), *( 't46', tau ), 't47', +( *( 't48', tau ), *( 't60', tau ), *( 't37', tau ), *( 't68', tau ) ), 't45', *( 't62', tau ), *( 't64', tau ), *( 't65', tau ), 't66' ) ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_101010__noise0.6.png)



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
| `[ST (in PAR_1)]` | `t19` | Exact Token Match | $\ge$ 76 | **77** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `t11` | Exact Token Match | $\ge$ 141 | **141** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `t14` | Exact Token Match | $\ge$ 121 | **121** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t14⟩` | Exact Token Match | $\ge$ 119 | **121** | ✅ **VERIFIED** |
| `[AS (in PAR_1)]` | `[nested LOOP_2]` | Exact Token Match | $\ge$ 1 | **121** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t05` | Exact Token Match | $\ge$ 37 | **37** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t15` | Exact Token Match | $\ge$ 54 | **54** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨τ, t15⟩` | Exact Token Match | $\ge$ 17 | **54** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨τ, t15⟩` | Exact Token Match | $\ge$ 15 | **54** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨[nested XOR_4], t15⟩` | Exact Token Match | $\ge$ 2 | **15** | ✅ **VERIFIED** |
| `[AS (in PAR_1)]` | `[nested LOOP_3]` | Exact Token Match | $\ge$ 1 | **15** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `t16` | Exact Token Match | $\ge$ 74 | **74** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t14, t16⟩` | Exact Token Match | $\ge$ 20 | **57** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t14, τ⟩` | Exact Token Match | $\ge$ 45 | **121** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t11, t14, τ⟩` | Exact Token Match | $\ge$ 13 | **114** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t11, t14⟩` | Exact Token Match | $\ge$ 87 | **114** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t11, t05, t15⟩` | Exact Token Match | $\ge$ 3 | **11** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `t20` | Exact Token Match | $\ge$ 212 | **212** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t19, t20⟩` | Exact Token Match | $\ge$ 39 | **77** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t14, τ, t20⟩` | Exact Token Match | $\ge$ 8 | **82** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t16, t20⟩` | Exact Token Match | $\ge$ 37 | **74** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨τ, t20⟩` | Exact Token Match | $\ge$ 62 | **212** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_1]` | Exact Token Match | $\ge$ 249 | **249** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t23` | Exact Token Match | $\ge$ 112 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t29` | Exact Token Match | $\ge$ 78 | **78** | ✅ **VERIFIED** |
| `[ST (in LOOP_6)]` | `t28` | Exact Token Match | $\ge$ 87 | **87** | ✅ **VERIFIED** |
| `[ST]` | `⟨t27, τ⟩` | Exact Token Match | $\ge$ 25 | **95** | ✅ **VERIFIED** |
| `[ST]` | `⟨t26, t27, τ⟩` | Exact Token Match | $\ge$ 25 | **95** | ✅ **VERIFIED** |
| `[ST]` | `⟨t25, t26, t27, t28⟩` | Exact Token Match | $\ge$ 35 | **43** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t26, t27, t28⟩` | Exact Token Match | $\ge$ 27 | **73** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t26, t27⟩` | Exact Token Match | $\ge$ 52 | **95** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t26⟩` | Exact Token Match | $\ge$ 52 | **95** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_5], t25, t26, t27, t28⟩` | Exact Token Match | $\ge$ 35 | **43** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_5], τ, t26, t27, t28⟩` | Exact Token Match | $\ge$ 27 | **73** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_5], τ, t26, t27⟩` | Exact Token Match | $\ge$ 52 | **95** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_5], τ, t26⟩` | Exact Token Match | $\ge$ 52 | **95** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_5], τ⟩` | Exact Token Match | $\ge$ 52 | **103** | ✅ **VERIFIED** |
| `[ST]` | `⟨t24, [nested PAR_5], t25, t26, t27, t28⟩` | Exact Token Match | $\ge$ 35 | **43** | ✅ **VERIFIED** |
| `[ST]` | `⟨t24, [nested PAR_5], τ, t26, t27, t28⟩` | Exact Token Match | $\ge$ 27 | **73** | ✅ **VERIFIED** |
| `[ST]` | `⟨t24, [nested PAR_5], τ, t26, t27⟩` | Exact Token Match | $\ge$ 52 | **95** | ✅ **VERIFIED** |
| `[ST]` | `⟨t24, [nested PAR_5], τ, t26⟩` | Exact Token Match | $\ge$ 52 | **95** | ✅ **VERIFIED** |
| `[ST]` | `⟨t24, [nested PAR_5], τ⟩` | Exact Token Match | $\ge$ 52 | **95** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `t42` | Exact Token Match | $\ge$ 368 | **368** | ✅ **VERIFIED** |
| `[ST]` | `⟨t42⟩` | Exact Token Match | $\ge$ 130 | **178** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_7]` | Exact Token Match | $\ge$ 1 | **233** | ✅ **VERIFIED** |
| `[ST]` | `t38` | Exact Token Match | $\ge$ 165 | **165** | ✅ **VERIFIED** |
| `[ST (in LOOP_8)]` | `t44` | Exact Token Match | $\ge$ 115 | **115** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `t36` | Exact Token Match | $\ge$ 438 | **438** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_9]` | Exact Token Match | $\ge$ 1 | **224** | ✅ **VERIFIED** |
| `[ST]` | `t30` | Exact Token Match | $\ge$ 36 | **36** | ✅ **VERIFIED** |
| `[ST]` | `t71` | Exact Token Match | $\ge$ 25 | **25** | ✅ **VERIFIED** |
| `[ST]` | `⟨t30, τ⟩` | Exact Token Match | $\ge$ 11 | **36** | ✅ **VERIFIED** |
| `[ST]` | `t33` | Exact Token Match | $\ge$ 145 | **145** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `t69` | Exact Token Match | $\ge$ 110 | **110** | ✅ **VERIFIED** |
| `[ST (in PAR_10)]` | `⟨t69⟩` | Exact Token Match | $\ge$ 110 | **110** | ✅ **VERIFIED** |
| `[ST (in LOOP_12)]` | `t70` | Exact Token Match | $\ge$ 99 | **99** | ✅ **VERIFIED** |
| `[ST (in PAR_10)]` | `⟨t70⟩` | Exact Token Match | $\ge$ 99 | **99** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `t46` | Exact Token Match | $\ge$ 333 | **333** | ✅ **VERIFIED** |
| `[ST]` | `⟨t46⟩` | Exact Token Match | $\ge$ 75 | **191** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_13]` | Exact Token Match | $\ge$ 1 | **236** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `t48` | Exact Token Match | $\ge$ 204 | **204** | ✅ **VERIFIED** |
| `[ST (in PAR_14)]` | `⟨t48⟩` | Exact Token Match | $\ge$ 204 | **204** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `t60` | Exact Token Match | $\ge$ 155 | **155** | ✅ **VERIFIED** |
| `[ST (in PAR_16)]` | `⟨t60⟩` | Exact Token Match | $\ge$ 155 | **155** | ✅ **VERIFIED** |
| `[ST (in LOOP_19)]` | `t37` | Exact Token Match | $\ge$ 193 | **193** | ✅ **VERIFIED** |
| `[ST (in PAR_18)]` | `⟨t37⟩` | Exact Token Match | $\ge$ 193 | **193** | ✅ **VERIFIED** |
| `[ST (in LOOP_20)]` | `t68` | Exact Token Match | $\ge$ 204 | **204** | ✅ **VERIFIED** |
| `[ST (in PAR_18)]` | `⟨t68⟩` | Exact Token Match | $\ge$ 204 | **204** | ✅ **VERIFIED** |
| `[ST (in LOOP_21)]` | `t62` | Exact Token Match | $\ge$ 250 | **250** | ✅ **VERIFIED** |
| `[ST]` | `⟨t62⟩` | Exact Token Match | $\ge$ 144 | **152** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_21]` | Exact Token Match | $\ge$ 1 | **182** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `t64` | Exact Token Match | $\ge$ 182 | **182** | ✅ **VERIFIED** |
| `[ST (in LOOP_23)]` | `t65` | Exact Token Match | $\ge$ 341 | **341** | ✅ **VERIFIED** |
| `[ST]` | `⟨t65⟩` | Exact Token Match | $\ge$ 53 | **192** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_23]` | Exact Token Match | $\ge$ 1 | **240** | ✅ **VERIFIED** |
| `[ST]` | `t66` | Exact Token Match | $\ge$ 197 | **197** | ✅ **VERIFIED** |
| `[ST]` | `⟨t65, t66⟩` | Exact Token Match | $\ge$ 53 | **160** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested LOOP_23], t66⟩` | Exact Token Match | $\ge$ 1 | **189** | ✅ **VERIFIED** |
| `[ST]` | `⟨t64, t65, t66⟩` | Exact Token Match | $\ge$ 38 | **111** | ✅ **VERIFIED** |
| `[ST]` | `⟨t64, t65⟩` | Exact Token Match | $\ge$ 38 | **119** | ✅ **VERIFIED** |
| `[ST]` | `⟨t45, τ⟩` | Exact Token Match | $\ge$ 1 | **130** | ✅ **VERIFIED** |
| `[ST]` | `⟨t45, [nested LOOP_21]⟩` | Exact Token Match | $\ge$ 1 | **130** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_14], t45, τ⟩` | Exact Token Match | $\ge$ 1 | **22** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_14], τ⟩` | Exact Token Match | $\ge$ 6 | **167** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_14], t45, [nested LOOP_21]⟩` | Exact Token Match | $\ge$ 1 | **22** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_14], t45⟩` | Exact Token Match | $\ge$ 21 | **22** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_14]⟩` | Exact Token Match | $\ge$ 27 | **167** | ✅ **VERIFIED** |
| `[ST]` | `⟨t46, t47, [nested PAR_14]⟩` | Exact Token Match | $\ge$ 48 | **84** | ✅ **VERIFIED** |
| `[ST]` | `⟨t46, t47⟩` | Exact Token Match | $\ge$ 48 | **92** | ✅ **VERIFIED** |
| `[ST]` | `⟨t33, τ⟩` | Exact Token Match | $\ge$ 35 | **145** | ✅ **VERIFIED** |
| `[ST]` | `⟨t39, τ⟩` | Exact Token Match | $\ge$ 30 | **172** | ✅ **VERIFIED** |
| `[ST]` | `⟨t39, τ⟩` | Exact Token Match | $\ge$ 71 | **172** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t39⟩` | Exact Token Match | $\ge$ 84 | **172** | ✅ **VERIFIED** |
| `[ST]` | `⟨t42, t38, t39⟩` | Exact Token Match | $\ge$ 46 | **134** | ✅ **VERIFIED** |
| `[ST]` | `⟨t42, t38⟩` | Exact Token Match | $\ge$ 46 | **145** | ✅ **VERIFIED** |
| `[ST]` | `⟨t22, t42⟩` | Exact Token Match | $\ge$ 2 | **81** | ✅ **VERIFIED** |
| `[ST]` | `⟨t21, t22, t42⟩` | Exact Token Match | $\ge$ 2 | **77** | ✅ **VERIFIED** |
| `[ST]` | `⟨t21, t24, [nested PAR_5], t25, t26, t27, t28⟩` | Exact Token Match | $\ge$ 35 | **38** | ✅ **VERIFIED** |
| `[ST]` | `⟨t21, t24, [nested PAR_5], τ, t26, t27, t28⟩` | Exact Token Match | $\ge$ 27 | **65** | ✅ **VERIFIED** |
| `[ST]` | `⟨t21, t24, [nested PAR_5], τ, t26, t27⟩` | Exact Token Match | $\ge$ 52 | **81** | ✅ **VERIFIED** |
| `[ST]` | `⟨t21, t24, [nested PAR_5], τ, t26⟩` | Exact Token Match | $\ge$ 52 | **81** | ✅ **VERIFIED** |
| `[ST]` | `⟨t21, t24, [nested PAR_5], τ⟩` | Exact Token Match | $\ge$ 52 | **81** | ✅ **VERIFIED** |
| `[ST]` | `⟨t21, τ⟩` | Exact Token Match | $\ge$ 16 | **223** | ✅ **VERIFIED** |
| `[ST]` | `⟨t17, t21, t24, [nested PAR_5], τ, t26, t27, t28⟩` | Exact Token Match | $\ge$ 24 | **35** | ✅ **VERIFIED** |
| `[ST]` | `⟨t17, t21, τ⟩` | Exact Token Match | $\ge$ 13 | **169** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t21⟩` | Exact Token Match | $\ge$ 3 | **223** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], t17, t21, t24, [nested PAR_5], τ, t26, t27, t28⟩` | Exact Token Match | $\ge$ 24 | **35** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], t17, t21, τ⟩` | Exact Token Match | $\ge$ 13 | **169** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], τ, t21⟩` | Exact Token Match | $\ge$ 3 | **223** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], τ⟩` | Exact Token Match | $\ge$ 3 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06, t04, t03, t02⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06, t04, t03⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06, t04⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, [nested PAR_1], t17, t21, t24, [nested PAR_5], τ, t26, t27, t28⟩` | Exact Token Match | $\ge$ 24 | **35** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, [nested PAR_1], t17, t21, τ⟩` | Exact Token Match | $\ge$ 13 | **169** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, [nested PAR_1], τ, t21⟩` | Exact Token Match | $\ge$ 3 | **223** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, [nested PAR_1], τ⟩` | Exact Token Match | $\ge$ 3 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 249 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨t09, t10, [nested PAR_1], t17, t21, t22⟩` | Exact Token Match | $\ge$ 50 | **59** | ✅ **VERIFIED** |
| `[ST]` | `⟨t09, t10, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 181 | **181** | ✅ **VERIFIED** |
| `[ST]` | `⟨t09, t10⟩` | Exact Token Match | $\ge$ 182 | **182** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t10, [nested PAR_1], t17, t21⟩` | Exact Token Match | $\ge$ 64 | **169** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t10, [nested PAR_1], t17⟩` | Exact Token Match | $\ge$ 64 | **185** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t10, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 67 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t10⟩` | Exact Token Match | $\ge$ 68 | **250** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨t05, t15⟩` | Exact Token Match | $\ge$ 37 | **15** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_1)]` | `⟨t05, t15⟩` | Exact Token Match | $\ge$ 35 | **15** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t17` | Exact Token Match | $\ge$ 246 | **185** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t21` | Exact Token Match | $\ge$ 249 | **223** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t22` | Exact Token Match | $\ge$ 121 | **106** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t24` | Exact Token Match | $\ge$ 112 | **95** | ⚠️ **DISCREPANCY** |
| `[AS]` | `[nested PAR_5]` | Exact Token Match | $\ge$ 112 | **103** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t25` | Exact Token Match | $\ge$ 60 | **54** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t26` | Exact Token Match | $\ge$ 112 | **95** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t27` | Exact Token Match | $\ge$ 112 | **95** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t28⟩` | Exact Token Match | $\ge$ 87 | **76** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t27, t28⟩` | Exact Token Match | $\ge$ 87 | **73** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t26, t27, t28⟩` | Exact Token Match | $\ge$ 87 | **73** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t26, t27⟩` | Exact Token Match | $\ge$ 112 | **95** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t25, t26, t27⟩` | Exact Token Match | $\ge$ 60 | **53** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t25, t26⟩` | Exact Token Match | $\ge$ 60 | **53** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_5], t25, t26, t27⟩` | Exact Token Match | $\ge$ 60 | **53** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_5], t25, t26⟩` | Exact Token Match | $\ge$ 60 | **53** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_5], t25⟩` | Exact Token Match | $\ge$ 60 | **54** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t24, [nested PAR_5], t25, t26, t27⟩` | Exact Token Match | $\ge$ 60 | **53** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t24, [nested PAR_5], t25, t26⟩` | Exact Token Match | $\ge$ 60 | **53** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t24, [nested PAR_5], t25⟩` | Exact Token Match | $\ge$ 60 | **53** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t24, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 112 | **95** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t39` | Exact Token Match | $\ge$ 249 | **172** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t40` | Exact Token Match | $\ge$ 148 | **98** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t43` | Exact Token Match | $\ge$ 115 | **51** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t44⟩` | Exact Token Match | $\ge$ 115 | **51** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t43, t44⟩` | Exact Token Match | $\ge$ 115 | **51** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t34` | Exact Token Match | $\ge$ 104 | **72** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t30, t71⟩` | Exact Token Match | $\ge$ 25 | **16** | ⚠️ **DISCREPANCY** |
| `[AS]` | `[nested PAR_10]` | Exact Token Match | $\ge$ 110 | **106** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t47` | Exact Token Match | $\ge$ 177 | **111** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_16)]` | `[nested PAR_18]` | Exact Token Match | $\ge$ 204 | **176** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_14)]` | `[nested PAR_16]` | Exact Token Match | $\ge$ 204 | **140** | ⚠️ **DISCREPANCY** |
| `[AS]` | `[nested PAR_14]` | Exact Token Match | $\ge$ 204 | **167** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t45` | Exact Token Match | $\ge$ 198 | **130** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t64⟩` | Exact Token Match | $\ge$ 182 | **125** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t62, t64⟩` | Exact Token Match | $\ge$ 129 | **125** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t45, t62, t64⟩` | Exact Token Match | $\ge$ 129 | **114** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t45, t62⟩` | Exact Token Match | $\ge$ 144 | **130** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_14], t45, t62, t64⟩` | Exact Token Match | $\ge$ 129 | **20** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_14], t45, t62⟩` | Exact Token Match | $\ge$ 144 | **22** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_14], t45⟩` | Exact Token Match | $\ge$ 198 | **22** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t47, [nested PAR_14], t45, t62, t64⟩` | Exact Token Match | $\ge$ 102 | **12** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t47, [nested PAR_14], t45, t62⟩` | Exact Token Match | $\ge$ 117 | **13** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t47, [nested PAR_14], t45⟩` | Exact Token Match | $\ge$ 171 | **13** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t47, [nested PAR_14]⟩` | Exact Token Match | $\ge$ 177 | **97** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t46, t47, [nested PAR_14], t45⟩` | Exact Token Match | $\ge$ 42 | **12** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t33, [nested PAR_10]⟩` | Exact Token Match | $\ge$ 51 | **35** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t40, t43, t44⟩` | Exact Token Match | $\ge$ 44 | **8** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t40, t43⟩` | Exact Token Match | $\ge$ 44 | **8** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t39, t40⟩` | Exact Token Match | $\ge$ 148 | **69** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t38, t39, t40⟩` | Exact Token Match | $\ge$ 64 | **59** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t38, t39⟩` | Exact Token Match | $\ge$ 165 | **140** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t21, t22⟩` | Exact Token Match | $\ge$ 121 | **92** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t21, t24, [nested PAR_5], t25, t26, t27⟩` | Exact Token Match | $\ge$ 60 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t21, t24, [nested PAR_5], t25, t26⟩` | Exact Token Match | $\ge$ 60 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t21, t24, [nested PAR_5], t25⟩` | Exact Token Match | $\ge$ 60 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t21, t24, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 112 | **81** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t21, t24⟩` | Exact Token Match | $\ge$ 112 | **81** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t17, t21, t22⟩` | Exact Token Match | $\ge$ 118 | **80** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t17, t21, t24, [nested PAR_5], t25, t26, t27, t28⟩` | Exact Token Match | $\ge$ 32 | **26** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t17, t21, t24, [nested PAR_5], t25, t26, t27⟩` | Exact Token Match | $\ge$ 57 | **31** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t17, t21, t24, [nested PAR_5], t25, t26⟩` | Exact Token Match | $\ge$ 57 | **31** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t17, t21, t24, [nested PAR_5], τ, t26, t27⟩` | Exact Token Match | $\ge$ 49 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t17, t21, t24, [nested PAR_5], τ, t26⟩` | Exact Token Match | $\ge$ 49 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t17, t21, t24, [nested PAR_5], t25⟩` | Exact Token Match | $\ge$ 57 | **31** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t17, t21, t24, [nested PAR_5], τ⟩` | Exact Token Match | $\ge$ 49 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t17, t21, t24, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 109 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t17, t21, t24⟩` | Exact Token Match | $\ge$ 109 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t17, t21⟩` | Exact Token Match | $\ge$ 246 | **169** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_1], t17, t21, t22⟩` | Exact Token Match | $\ge$ 118 | **80** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_1], t17, t21, t24, [nested PAR_5], t25, t26, t27, t28⟩` | Exact Token Match | $\ge$ 32 | **26** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_1], t17, t21, t24, [nested PAR_5], t25, t26, t27⟩` | Exact Token Match | $\ge$ 57 | **31** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_1], t17, t21, t24, [nested PAR_5], t25, t26⟩` | Exact Token Match | $\ge$ 57 | **31** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_1], t17, t21, t24, [nested PAR_5], τ, t26, t27⟩` | Exact Token Match | $\ge$ 49 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_1], t17, t21, t24, [nested PAR_5], τ, t26⟩` | Exact Token Match | $\ge$ 49 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_1], t17, t21, t24, [nested PAR_5], t25⟩` | Exact Token Match | $\ge$ 57 | **31** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_1], t17, t21, t24, [nested PAR_5], τ⟩` | Exact Token Match | $\ge$ 49 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_1], t17, t21, t24, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 109 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_1], t17, t21, t24⟩` | Exact Token Match | $\ge$ 109 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_1], t17, t21⟩` | Exact Token Match | $\ge$ 246 | **169** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_1], t17⟩` | Exact Token Match | $\ge$ 246 | **185** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, [nested PAR_1], t17, t21, t22⟩` | Exact Token Match | $\ge$ 118 | **80** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, [nested PAR_1], t17, t21, t24, [nested PAR_5], t25, t26, t27, t28⟩` | Exact Token Match | $\ge$ 32 | **26** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, [nested PAR_1], t17, t21, t24, [nested PAR_5], t25, t26, t27⟩` | Exact Token Match | $\ge$ 57 | **31** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, [nested PAR_1], t17, t21, t24, [nested PAR_5], t25, t26⟩` | Exact Token Match | $\ge$ 57 | **31** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, [nested PAR_1], t17, t21, t24, [nested PAR_5], τ, t26, t27⟩` | Exact Token Match | $\ge$ 49 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, [nested PAR_1], t17, t21, t24, [nested PAR_5], τ, t26⟩` | Exact Token Match | $\ge$ 49 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, [nested PAR_1], t17, t21, t24, [nested PAR_5], t25⟩` | Exact Token Match | $\ge$ 57 | **31** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, [nested PAR_1], t17, t21, t24, [nested PAR_5], τ⟩` | Exact Token Match | $\ge$ 49 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, [nested PAR_1], t17, t21, t24, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 109 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, [nested PAR_1], t17, t21, t24⟩` | Exact Token Match | $\ge$ 109 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, [nested PAR_1], t17, t21⟩` | Exact Token Match | $\ge$ 246 | **169** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, [nested PAR_1], t17⟩` | Exact Token Match | $\ge$ 246 | **185** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t09, t10, [nested PAR_1], t17, t21, t24, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 41 | **36** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t09, t10, [nested PAR_1], t17, t21, t24⟩` | Exact Token Match | $\ge$ 41 | **36** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t09, t10, [nested PAR_1], t17, t21⟩` | Exact Token Match | $\ge$ 178 | **133** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t09, t10, [nested PAR_1], t17⟩` | Exact Token Match | $\ge$ 178 | **141** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t40, t34⟩` | Exact Token Match | $\ge$ 33 | **0** | ❌ **GHOST PATTERN** |
| `[ST]` | `⟨t39, t40, t43, t44⟩` | Exact Token Match | $\ge$ 44 | **0** | ❌ **GHOST PATTERN** |
| `[ST]` | `⟨t39, t40, t43⟩` | Exact Token Match | $\ge$ 44 | **0** | ❌ **GHOST PATTERN** |
| `[ST]` | `⟨t39, t40, t34⟩` | Exact Token Match | $\ge$ 33 | **0** | ❌ **GHOST PATTERN** |

## Audit Summary
- **Perfect Pattern Verifications:** 139
- **Frequency Discrepancies:** 99
- **Ghost Patterns (Fatal):** 4
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 8.75%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 5.19%
- **Tree Exposure (Local-Strict % of N):** 91.32% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 13.18%
- **Total Forced Volume (incl. unresolved AS, % of N):** 0.00%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 0.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 82.13%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 80.41%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 84.78%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 42.10%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 68.28%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 87.17%
- **Max Fractional Exposure (Worst-Case Normalized):** 9.11% (expected length: 259.34 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 84.22% (expected length: 28.07 events)
- **Mean Absolute Exposure Volume:** 4.56 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_2]`
- **Internal Structure:** `(t14 ∗ τ)`
- **Block Frequency:** 120

- **Max Loop Iterations:** `1`
- **Max Sub-Sequence Length:** `3` steps (if one case consumes all iterations)

![nested LOOP_2 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_2.png)

### `[nested LOOP_3]`
- **Internal Structure:** `(⟨[t05 │ τ], t15⟩ ∗ τ)`
- **Block Frequency:** 53

- **Max Loop Iterations:** `1`
- **Max Sub-Sequence Length:** `3` steps (if one case consumes all iterations)

![nested LOOP_3 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_3.png)

### `[nested XOR_4]`
- **Internal Structure:** `[t05 │ τ]`
- **Block Frequency:** 54



![nested XOR_4 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_XOR_4.png)

### `[nested PAR_1]`
- **Internal Structure:** `{[τ │ t13], ⟨[t19 │ ⟨[t11 │ τ], [(t14 ∗ τ) │ (⟨[t05 │ τ], t15⟩ ∗ τ)], [t16 │ τ]⟩], [t20 │ τ]⟩}`
- **Block Frequency:** 249



![nested PAR_1 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_PAR_1.png)

### `[nested PAR_5]`
- **Internal Structure:** `{t23, [t29 │ τ]}`
- **Block Frequency:** 112



![nested PAR_5 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_PAR_5.png)

### `[nested LOOP_6]`
- **Internal Structure:** `(t28 ∗ τ)`
- **Block Frequency:** 87

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_6 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_6.png)

### `[nested LOOP_7]`
- **Internal Structure:** `(t42 ∗ τ)`
- **Block Frequency:** 249

- **Max Loop Iterations:** `119`
- **Max Sub-Sequence Length:** `239` steps (if one case consumes all iterations)

![nested LOOP_7 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_7.png)

### `[nested LOOP_8]`
- **Internal Structure:** `(t44 ∗ τ)`
- **Block Frequency:** 115

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_8 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_8.png)

### `[nested LOOP_9]`
- **Internal Structure:** `(t36 ∗ τ)`
- **Block Frequency:** 204

- **Max Loop Iterations:** `234`
- **Max Sub-Sequence Length:** `469` steps (if one case consumes all iterations)

![nested LOOP_9 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_9.png)

### `[nested LOOP_11]`
- **Internal Structure:** `(t69 ∗ τ)`
- **Block Frequency:** 110

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_11 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_11.png)

### `[nested LOOP_12]`
- **Internal Structure:** `(t70 ∗ τ)`
- **Block Frequency:** 99

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_12 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_12.png)

### `[nested PAR_10]`
- **Internal Structure:** `{(t69 ∗ τ), [(t70 ∗ τ) │ τ]}`
- **Block Frequency:** 110



![nested PAR_10 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_PAR_10.png)

### `[nested LOOP_13]`
- **Internal Structure:** `(t46 ∗ τ)`
- **Block Frequency:** 204

- **Max Loop Iterations:** `129`
- **Max Sub-Sequence Length:** `259` steps (if one case consumes all iterations)

![nested LOOP_13 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_13.png)

### `[nested LOOP_15]`
- **Internal Structure:** `(t48 ∗ τ)`
- **Block Frequency:** 204

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_15 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_15.png)

### `[nested LOOP_17]`
- **Internal Structure:** `(t60 ∗ τ)`
- **Block Frequency:** 155

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_17 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_17.png)

### `[nested LOOP_19]`
- **Internal Structure:** `(t37 ∗ τ)`
- **Block Frequency:** 193

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_19 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_19.png)

### `[nested LOOP_20]`
- **Internal Structure:** `(t68 ∗ τ)`
- **Block Frequency:** 204

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_20 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_20.png)

### `[nested PAR_18]`
- **Internal Structure:** `{[(t37 ∗ τ) │ τ], (t68 ∗ τ)}`
- **Block Frequency:** 204



![nested PAR_18 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_PAR_18.png)

### `[nested PAR_16]`
- **Internal Structure:** `{[(t60 ∗ τ) │ τ], [(t37 ∗ τ) │ τ], (t68 ∗ τ)}`
- **Block Frequency:** 204



![nested PAR_16 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_PAR_16.png)

### `[nested PAR_14]`
- **Internal Structure:** `{(t48 ∗ τ), [(t60 ∗ τ) │ τ], [(t37 ∗ τ) │ τ], (t68 ∗ τ)}`
- **Block Frequency:** 204



![nested PAR_14 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_PAR_14.png)

### `[nested LOOP_21]`
- **Internal Structure:** `(t62 ∗ τ)`
- **Block Frequency:** 197

- **Max Loop Iterations:** `53`
- **Max Sub-Sequence Length:** `107` steps (if one case consumes all iterations)

![nested LOOP_21 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_21.png)

### `[nested LOOP_22]`
- **Internal Structure:** `(t64 ∗ τ)`
- **Block Frequency:** 182

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_22 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_22.png)

### `[nested LOOP_23]`
- **Internal Structure:** `(t65 ∗ τ)`
- **Block Frequency:** 197

- **Max Loop Iterations:** `144`
- **Max Sub-Sequence Length:** `289` steps (if one case consumes all iterations)

![nested LOOP_23 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_23.png)
