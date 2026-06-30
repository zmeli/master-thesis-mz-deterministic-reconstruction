# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_101010.xes` |
| **Noise Threshold** | `0.8` |
| **Fitness** | `0.8305016471611255` |
| **Precision** | `0.584271922767498` |
| **Total Cases in Log** | `250` |
| **Unique Activities** | `44` |
| **XOR Operators** | `30` |
| **LOOP Operators** | `15` |
| **SEQ Operators** | `30` |
| **PAR Operators** | `7` |
| **Binarization Additions** | `24` |
| **Tau Operators Added** | `21` |
| **Total Found Patterns** | `298` |
| **Verified Patterns** | `145` |
| **Discrepancy Patterns** | `80` |
| **Ghost Patterns** | `0` |
| **Nested LOOPs** | `15` |
| **Nested PARs** | `7` |
| **Tree Exposure (Strict, End-to-End % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `9.13%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `5.41%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `16.76%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `0.00%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `0.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `84.04%` |
| **Data Exposure, ST-only (% confirmed)** | `84.27%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `89.27%` |
| **Data Coverage, ST-only (% of real log)** | `41.02%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `75.56%` |
| **Data Coverage, Total (% of real log)** | `90.34%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `9.48%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `75.18%` |
| **Mean Absolute Exposure Volume (events/case)** | `4.32` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_101010__noise0.8__gt.png)


```text
->( 't09', 't10', X( ->( 't06', 't04', 't03', 't02' ), ->( +( X( tau, 't13' ), ->( X( 't19', ->( 't11', X( tau, *( 't14', tau ), *( 't05', tau ) ), 't16' ) ), 't20' ) ), X( tau, ->( X( tau, ->( 't17', 't21', X( 't22', ->( 't24', +( 't23', 't29' ), 't25', 't26', 't27', *( 't28', tau ) ) ), *( 't42', tau ), 't38', *( 't39', tau ), X( ->( 't43', *( 't44', tau ) ), 't40' ) ) ), *( 't36', tau ), X( ->( 't30', 't71' ), 't33' ), +( *( 't45', tau ), *( 't60', tau ), *( 't47', tau ), *( 't37', tau ), *( 't46', tau ) ), +( *( 't48', tau ), *( 't68', tau ) ), 't62', 't64' ) ), *( 't65', tau ), 't66' ) ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_101010__noise0.8__gt.png)



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
| `[ST (in LOOP_2)]` | `t14` | Exact Token Match | $\ge$ 121 | **121** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t14⟩` | Exact Token Match | $\ge$ 121 | **121** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t05` | Exact Token Match | $\ge$ 37 | **37** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t05⟩` | Exact Token Match | $\ge$ 37 | **37** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `t16` | Exact Token Match | $\ge$ 74 | **74** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t14, t16⟩` | Exact Token Match | $\ge$ 37 | **57** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t14, τ⟩` | Exact Token Match | $\ge$ 47 | **121** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t11, t14, t16⟩` | Exact Token Match | $\ge$ 20 | **57** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t11, t14, τ⟩` | Exact Token Match | $\ge$ 30 | **114** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t11, t14⟩` | Exact Token Match | $\ge$ 104 | **114** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t11, t05⟩` | Exact Token Match | $\ge$ 20 | **27** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `t20` | Exact Token Match | $\ge$ 212 | **212** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t19, t20⟩` | Exact Token Match | $\ge$ 54 | **77** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t11, t14, τ, t20⟩` | Exact Token Match | $\ge$ 7 | **82** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t14, t16, t20⟩` | Exact Token Match | $\ge$ 14 | **57** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t14, τ, t20⟩` | Exact Token Match | $\ge$ 24 | **82** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t16, t20⟩` | Exact Token Match | $\ge$ 51 | **74** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨τ, t20⟩` | Exact Token Match | $\ge$ 61 | **212** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_1]` | Exact Token Match | $\ge$ 235 | **249** | ✅ **VERIFIED** |
| `[ST (in PAR_4)]` | `t23` | Exact Token Match | $\ge$ 112 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_4)]` | `t29` | Exact Token Match | $\ge$ 78 | **78** | ✅ **VERIFIED** |
| `[ST (in LOOP_5)]` | `t28` | Exact Token Match | $\ge$ 87 | **87** | ✅ **VERIFIED** |
| `[ST]` | `⟨t27, τ⟩` | Exact Token Match | $\ge$ 25 | **95** | ✅ **VERIFIED** |
| `[ST]` | `⟨t26, t27, τ⟩` | Exact Token Match | $\ge$ 25 | **95** | ✅ **VERIFIED** |
| `[ST]` | `⟨t25, t26, t27, t28⟩` | Exact Token Match | $\ge$ 35 | **43** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t26, t27, t28⟩` | Exact Token Match | $\ge$ 27 | **73** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t26, t27⟩` | Exact Token Match | $\ge$ 52 | **95** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t26⟩` | Exact Token Match | $\ge$ 52 | **95** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_4], t25, t26, t27, t28⟩` | Exact Token Match | $\ge$ 35 | **43** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_4], τ, t26, t27, t28⟩` | Exact Token Match | $\ge$ 27 | **73** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_4], τ, t26, t27⟩` | Exact Token Match | $\ge$ 52 | **95** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_4], τ, t26⟩` | Exact Token Match | $\ge$ 52 | **95** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_4], τ⟩` | Exact Token Match | $\ge$ 52 | **103** | ✅ **VERIFIED** |
| `[ST]` | `⟨t24, [nested PAR_4], t25, t26, t27, t28⟩` | Exact Token Match | $\ge$ 35 | **43** | ✅ **VERIFIED** |
| `[ST]` | `⟨t24, [nested PAR_4], τ, t26, t27, t28⟩` | Exact Token Match | $\ge$ 27 | **73** | ✅ **VERIFIED** |
| `[ST]` | `⟨t24, [nested PAR_4], τ, t26, t27⟩` | Exact Token Match | $\ge$ 52 | **95** | ✅ **VERIFIED** |
| `[ST]` | `⟨t24, [nested PAR_4], τ, t26⟩` | Exact Token Match | $\ge$ 52 | **95** | ✅ **VERIFIED** |
| `[ST]` | `⟨t24, [nested PAR_4], τ⟩` | Exact Token Match | $\ge$ 52 | **95** | ✅ **VERIFIED** |
| `[ST (in LOOP_6)]` | `t42` | Exact Token Match | $\ge$ 368 | **368** | ✅ **VERIFIED** |
| `[ST]` | `⟨t42⟩` | Exact Token Match | $\ge$ 130 | **178** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_6]` | Exact Token Match | $\ge$ 1 | **233** | ✅ **VERIFIED** |
| `[ST]` | `t38` | Exact Token Match | $\ge$ 165 | **165** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `t39` | Exact Token Match | $\ge$ 337 | **337** | ✅ **VERIFIED** |
| `[ST]` | `⟨t39⟩` | Exact Token Match | $\ge$ 161 | **172** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_7]` | Exact Token Match | $\ge$ 1 | **224** | ✅ **VERIFIED** |
| `[ST (in LOOP_8)]` | `t44` | Exact Token Match | $\ge$ 115 | **115** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_8]` | Exact Token Match | $\ge$ 1 | **74** | ✅ **VERIFIED** |
| `[ST]` | `⟨t43, [nested LOOP_8]⟩` | Exact Token Match | $\ge$ 1 | **51** | ✅ **VERIFIED** |
| `[ST]` | `⟨t39, t43, t44⟩` | Exact Token Match | $\ge$ 15 | **28** | ✅ **VERIFIED** |
| `[ST]` | `⟨t39, t40⟩` | Exact Token Match | $\ge$ 52 | **69** | ✅ **VERIFIED** |
| `[ST]` | `⟨t39, t43⟩` | Exact Token Match | $\ge$ 21 | **28** | ✅ **VERIFIED** |
| `[ST]` | `⟨t38, t39⟩` | Exact Token Match | $\ge$ 77 | **140** | ✅ **VERIFIED** |
| `[ST]` | `⟨t42, t38⟩` | Exact Token Match | $\ge$ 46 | **145** | ✅ **VERIFIED** |
| `[ST]` | `⟨t22, t42⟩` | Exact Token Match | $\ge$ 2 | **81** | ✅ **VERIFIED** |
| `[ST]` | `⟨t21, t22, t42⟩` | Exact Token Match | $\ge$ 2 | **77** | ✅ **VERIFIED** |
| `[ST]` | `⟨t21, t24, [nested PAR_4], t25, t26, t27, t28⟩` | Exact Token Match | $\ge$ 35 | **38** | ✅ **VERIFIED** |
| `[ST]` | `⟨t21, t24, [nested PAR_4], τ, t26, t27, t28⟩` | Exact Token Match | $\ge$ 27 | **65** | ✅ **VERIFIED** |
| `[ST]` | `⟨t21, t24, [nested PAR_4], τ, t26, t27⟩` | Exact Token Match | $\ge$ 52 | **81** | ✅ **VERIFIED** |
| `[ST]` | `⟨t21, t24, [nested PAR_4], τ, t26⟩` | Exact Token Match | $\ge$ 52 | **81** | ✅ **VERIFIED** |
| `[ST]` | `⟨t21, t24, [nested PAR_4], τ⟩` | Exact Token Match | $\ge$ 52 | **81** | ✅ **VERIFIED** |
| `[ST]` | `⟨t21, τ⟩` | Exact Token Match | $\ge$ 16 | **223** | ✅ **VERIFIED** |
| `[ST]` | `⟨t17, t21, t24, [nested PAR_4], τ, t26, t27, t28⟩` | Exact Token Match | $\ge$ 24 | **35** | ✅ **VERIFIED** |
| `[ST]` | `⟨t17, t21, τ⟩` | Exact Token Match | $\ge$ 13 | **169** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t21⟩` | Exact Token Match | $\ge$ 3 | **223** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `t36` | Exact Token Match | $\ge$ 438 | **438** | ✅ **VERIFIED** |
| `[ST]` | `⟨t36⟩` | Exact Token Match | $\ge$ 60 | **163** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_9]` | Exact Token Match | $\ge$ 1 | **224** | ✅ **VERIFIED** |
| `[ST]` | `t30` | Exact Token Match | $\ge$ 36 | **36** | ✅ **VERIFIED** |
| `[ST]` | `t71` | Exact Token Match | $\ge$ 25 | **25** | ✅ **VERIFIED** |
| `[ST]` | `⟨t30, τ⟩` | Exact Token Match | $\ge$ 11 | **36** | ✅ **VERIFIED** |
| `[ST]` | `t33` | Exact Token Match | $\ge$ 145 | **145** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `t45` | Exact Token Match | $\ge$ 198 | **198** | ✅ **VERIFIED** |
| `[ST (in PAR_10)]` | `⟨t45⟩` | Exact Token Match | $\ge$ 198 | **198** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `t60` | Exact Token Match | $\ge$ 155 | **155** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t60⟩` | Exact Token Match | $\ge$ 155 | **155** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `t47` | Exact Token Match | $\ge$ 177 | **177** | ✅ **VERIFIED** |
| `[ST (in PAR_14)]` | `⟨t47⟩` | Exact Token Match | $\ge$ 177 | **177** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `t37` | Exact Token Match | $\ge$ 193 | **193** | ✅ **VERIFIED** |
| `[ST (in PAR_16)]` | `⟨t37⟩` | Exact Token Match | $\ge$ 193 | **193** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `t46` | Exact Token Match | $\ge$ 333 | **333** | ✅ **VERIFIED** |
| `[ST (in PAR_16)]` | `⟨t46⟩` | Exact Token Match | $\ge$ 165 | **333** | ✅ **VERIFIED** |
| `[AS (in PAR_16)]` | `[nested LOOP_18]` | Exact Token Match | $\ge$ 1 | **333** | ✅ **VERIFIED** |
| `[ST (in LOOP_20)]` | `t48` | Exact Token Match | $\ge$ 204 | **204** | ✅ **VERIFIED** |
| `[ST (in PAR_19)]` | `⟨t48⟩` | Exact Token Match | $\ge$ 204 | **204** | ✅ **VERIFIED** |
| `[ST (in LOOP_21)]` | `t68` | Exact Token Match | $\ge$ 204 | **204** | ✅ **VERIFIED** |
| `[ST (in PAR_19)]` | `⟨t68⟩` | Exact Token Match | $\ge$ 204 | **204** | ✅ **VERIFIED** |
| `[ST]` | `⟨t62, τ⟩` | Exact Token Match | $\ge$ 67 | **152** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_19], t62, τ⟩` | Exact Token Match | $\ge$ 22 | **72** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t62⟩` | Exact Token Match | $\ge$ 45 | **152** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_10], τ, t62⟩` | Exact Token Match | $\ge$ 45 | **93** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_10], τ⟩` | Exact Token Match | $\ge$ 45 | **239** | ✅ **VERIFIED** |
| `[ST]` | `⟨t30, τ, [nested PAR_10]⟩` | Exact Token Match | $\ge$ 11 | **28** | ✅ **VERIFIED** |
| `[ST]` | `⟨t33, [nested PAR_10]⟩` | Exact Token Match | $\ge$ 145 | **145** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_10], [nested PAR_19]⟩` | Exact Token Match | $\ge$ 23 | **35** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_10]⟩` | Exact Token Match | $\ge$ 68 | **239** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `t65` | Exact Token Match | $\ge$ 341 | **341** | ✅ **VERIFIED** |
| `[ST]` | `⟨t65⟩` | Exact Token Match | $\ge$ 53 | **192** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_22]` | Exact Token Match | $\ge$ 1 | **240** | ✅ **VERIFIED** |
| `[ST]` | `t66` | Exact Token Match | $\ge$ 197 | **197** | ✅ **VERIFIED** |
| `[ST]` | `⟨t65, t66⟩` | Exact Token Match | $\ge$ 53 | **160** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested LOOP_22], t66⟩` | Exact Token Match | $\ge$ 1 | **189** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], t17, t21, t24, [nested PAR_4], t25, t26, t27, t28⟩` | Exact Token Match | $\ge$ 18 | **26** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], t17, t21, t24, [nested PAR_4], τ, t26, t27, t28⟩` | Exact Token Match | $\ge$ 10 | **35** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], t17, t21, t24, [nested PAR_4], τ, t26, t27⟩` | Exact Token Match | $\ge$ 35 | **45** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], t17, t21, t24, [nested PAR_4], τ, t26⟩` | Exact Token Match | $\ge$ 35 | **45** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], t17, t21, t24, [nested PAR_4], τ⟩` | Exact Token Match | $\ge$ 35 | **45** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t17, t21⟩` | Exact Token Match | $\ge$ 11 | **169** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t17⟩` | Exact Token Match | $\ge$ 11 | **185** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06, t04, t03, t02⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06, t04, t03⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06, t04⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, [nested PAR_1], t17, t21, t24, [nested PAR_4], t25, t26, t27, t28⟩` | Exact Token Match | $\ge$ 18 | **26** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, [nested PAR_1], t17, t21, t24, [nested PAR_4], τ, t26, t27, t28⟩` | Exact Token Match | $\ge$ 10 | **35** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, [nested PAR_1], t17, t21, t24, [nested PAR_4], τ, t26, t27⟩` | Exact Token Match | $\ge$ 35 | **45** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, [nested PAR_1], t17, t21, t24, [nested PAR_4], τ, t26⟩` | Exact Token Match | $\ge$ 35 | **45** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, [nested PAR_1], t17, t21, t24, [nested PAR_4], τ⟩` | Exact Token Match | $\ge$ 35 | **45** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ, t17, t21⟩` | Exact Token Match | $\ge$ 11 | **169** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ, t17⟩` | Exact Token Match | $\ge$ 11 | **185** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 235 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 14 | **250** | ✅ **VERIFIED** |
| `[ST]` | `⟨t09, t10, [nested PAR_1], t17, t21, t22⟩` | Exact Token Match | $\ge$ 36 | **59** | ✅ **VERIFIED** |
| `[ST]` | `⟨t09, t10, [nested PAR_1], t17, t21, t24, [nested PAR_4]⟩` | Exact Token Match | $\ge$ 27 | **36** | ✅ **VERIFIED** |
| `[ST]` | `⟨t09, t10, [nested PAR_1], t17, t21, t24⟩` | Exact Token Match | $\ge$ 27 | **36** | ✅ **VERIFIED** |
| `[ST]` | `⟨t09, t10, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 167 | **181** | ✅ **VERIFIED** |
| `[ST]` | `⟨t09, t10⟩` | Exact Token Match | $\ge$ 182 | **182** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t10, [nested PAR_1], t17, t21⟩` | Exact Token Match | $\ge$ 50 | **169** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t10, [nested PAR_1], t17⟩` | Exact Token Match | $\ge$ 50 | **185** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t10, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 53 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t10⟩` | Exact Token Match | $\ge$ 68 | **250** | ✅ **VERIFIED** |
| `[ST]` | `t17` | Exact Token Match | $\ge$ 246 | **185** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t21` | Exact Token Match | $\ge$ 249 | **223** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t22` | Exact Token Match | $\ge$ 121 | **106** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t24` | Exact Token Match | $\ge$ 112 | **95** | ⚠️ **DISCREPANCY** |
| `[AS]` | `[nested PAR_4]` | Exact Token Match | $\ge$ 112 | **103** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t25` | Exact Token Match | $\ge$ 60 | **54** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t26` | Exact Token Match | $\ge$ 112 | **95** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t27` | Exact Token Match | $\ge$ 112 | **95** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t28⟩` | Exact Token Match | $\ge$ 87 | **76** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t27, t28⟩` | Exact Token Match | $\ge$ 87 | **73** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t26, t27, t28⟩` | Exact Token Match | $\ge$ 87 | **73** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t26, t27⟩` | Exact Token Match | $\ge$ 112 | **95** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t25, t26, t27⟩` | Exact Token Match | $\ge$ 60 | **53** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t25, t26⟩` | Exact Token Match | $\ge$ 60 | **53** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_4], t25, t26, t27⟩` | Exact Token Match | $\ge$ 60 | **53** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_4], t25, t26⟩` | Exact Token Match | $\ge$ 60 | **53** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_4], t25⟩` | Exact Token Match | $\ge$ 60 | **54** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t24, [nested PAR_4], t25, t26, t27⟩` | Exact Token Match | $\ge$ 60 | **53** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t24, [nested PAR_4], t25, t26⟩` | Exact Token Match | $\ge$ 60 | **53** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t24, [nested PAR_4], t25⟩` | Exact Token Match | $\ge$ 60 | **53** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t24, [nested PAR_4]⟩` | Exact Token Match | $\ge$ 112 | **95** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t43` | Exact Token Match | $\ge$ 109 | **51** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t44⟩` | Exact Token Match | $\ge$ 103 | **51** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t43, t44⟩` | Exact Token Match | $\ge$ 103 | **51** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t40` | Exact Token Match | $\ge$ 140 | **98** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t21, t22⟩` | Exact Token Match | $\ge$ 121 | **92** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t21, t24, [nested PAR_4], t25, t26, t27⟩` | Exact Token Match | $\ge$ 60 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t21, t24, [nested PAR_4], t25, t26⟩` | Exact Token Match | $\ge$ 60 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t21, t24, [nested PAR_4], t25⟩` | Exact Token Match | $\ge$ 60 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t21, t24, [nested PAR_4]⟩` | Exact Token Match | $\ge$ 112 | **81** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t21, t24⟩` | Exact Token Match | $\ge$ 112 | **81** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t17, t21, t22⟩` | Exact Token Match | $\ge$ 118 | **80** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t17, t21, t24, [nested PAR_4], t25, t26, t27, t28⟩` | Exact Token Match | $\ge$ 32 | **26** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t17, t21, t24, [nested PAR_4], t25, t26, t27⟩` | Exact Token Match | $\ge$ 57 | **31** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t17, t21, t24, [nested PAR_4], t25, t26⟩` | Exact Token Match | $\ge$ 57 | **31** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t17, t21, t24, [nested PAR_4], τ, t26, t27⟩` | Exact Token Match | $\ge$ 49 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t17, t21, t24, [nested PAR_4], τ, t26⟩` | Exact Token Match | $\ge$ 49 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t17, t21, t24, [nested PAR_4], t25⟩` | Exact Token Match | $\ge$ 57 | **31** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t17, t21, t24, [nested PAR_4], τ⟩` | Exact Token Match | $\ge$ 49 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t17, t21, t24, [nested PAR_4]⟩` | Exact Token Match | $\ge$ 109 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t17, t21, t24⟩` | Exact Token Match | $\ge$ 109 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t17, t21⟩` | Exact Token Match | $\ge$ 246 | **169** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t30, t71⟩` | Exact Token Match | $\ge$ 25 | **16** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_14)]` | `[nested PAR_16]` | Exact Token Match | $\ge$ 249 | **170** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_12)]` | `[nested PAR_14]` | Exact Token Match | $\ge$ 249 | **127** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_10)]` | `[nested PAR_12]` | Exact Token Match | $\ge$ 249 | **94** | ⚠️ **DISCREPANCY** |
| `[AS]` | `[nested PAR_10]` | Exact Token Match | $\ge$ 249 | **239** | ⚠️ **DISCREPANCY** |
| `[AS]` | `[nested PAR_19]` | Exact Token Match | $\ge$ 204 | **153** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t62` | Exact Token Match | $\ge$ 249 | **152** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t64` | Exact Token Match | $\ge$ 182 | **125** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t62, t64⟩` | Exact Token Match | $\ge$ 182 | **125** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_19], t62, t64⟩` | Exact Token Match | $\ge$ 137 | **62** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_19], t62⟩` | Exact Token Match | $\ge$ 204 | **72** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_10], [nested PAR_19], t62, t64⟩` | Exact Token Match | $\ge$ 137 | **10** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_10], [nested PAR_19], t62, τ⟩` | Exact Token Match | $\ge$ 22 | **14** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_10], [nested PAR_19], t62⟩` | Exact Token Match | $\ge$ 204 | **14** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_10], [nested PAR_19]⟩` | Exact Token Match | $\ge$ 204 | **35** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t33, [nested PAR_10], [nested PAR_19], t62, t64⟩` | Exact Token Match | $\ge$ 33 | **6** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t30, t71, [nested PAR_10]⟩` | Exact Token Match | $\ge$ 25 | **8** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t33, [nested PAR_10], [nested PAR_19], t62⟩` | Exact Token Match | $\ge$ 100 | **6** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t33, [nested PAR_10], [nested PAR_19]⟩` | Exact Token Match | $\ge$ 100 | **19** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨τ, [nested PAR_10], [nested PAR_19], t62⟩` | Exact Token Match | $\ge$ 23 | **14** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_1], t17, t21, t22⟩` | Exact Token Match | $\ge$ 104 | **80** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_1], t17, t21, t24, [nested PAR_4], t25, t26, t27⟩` | Exact Token Match | $\ge$ 43 | **31** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_1], t17, t21, t24, [nested PAR_4], t25, t26⟩` | Exact Token Match | $\ge$ 43 | **31** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_1], t17, t21, t24, [nested PAR_4], t25⟩` | Exact Token Match | $\ge$ 43 | **31** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_1], t17, t21, t24, [nested PAR_4]⟩` | Exact Token Match | $\ge$ 95 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_1], t17, t21, t24⟩` | Exact Token Match | $\ge$ 95 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_1], t17, t21⟩` | Exact Token Match | $\ge$ 232 | **169** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_1], t17⟩` | Exact Token Match | $\ge$ 232 | **185** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, [nested PAR_1], t17, t21, t22⟩` | Exact Token Match | $\ge$ 104 | **80** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, [nested PAR_1], t17, t21, t24, [nested PAR_4], t25, t26, t27⟩` | Exact Token Match | $\ge$ 43 | **31** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, [nested PAR_1], t17, t21, t24, [nested PAR_4], t25, t26⟩` | Exact Token Match | $\ge$ 43 | **31** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, [nested PAR_1], t17, t21, t24, [nested PAR_4], t25⟩` | Exact Token Match | $\ge$ 43 | **31** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, [nested PAR_1], t17, t21, t24, [nested PAR_4]⟩` | Exact Token Match | $\ge$ 95 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, [nested PAR_1], t17, t21, t24⟩` | Exact Token Match | $\ge$ 95 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, [nested PAR_1], t17, t21⟩` | Exact Token Match | $\ge$ 232 | **169** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, [nested PAR_1], t17⟩` | Exact Token Match | $\ge$ 232 | **185** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t09, t10, [nested PAR_1], t17, t21⟩` | Exact Token Match | $\ge$ 164 | **133** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t09, t10, [nested PAR_1], t17⟩` | Exact Token Match | $\ge$ 164 | **141** | ⚠️ **DISCREPANCY** |

## Audit Summary
- **Perfect Pattern Verifications:** 145
- **Frequency Discrepancies:** 80
- **Ghost Patterns (Fatal):** 0
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 9.13%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 5.41%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 16.76%
- **Total Forced Volume (incl. unresolved AS, % of N):** 0.00%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 0.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 84.04%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 84.27%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 89.27%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 41.02%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 75.56%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 90.34%
- **Max Fractional Exposure (Worst-Case Normalized):** 9.48% (expected length: 213.38 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 75.18% (expected length: 26.90 events)
- **Mean Absolute Exposure Volume:** 4.32 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_2]`
- **Internal Structure:** `(t14 ∗ τ)`
- **Block Frequency:** 121

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_2 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.8__gt_nested_LOOP_2.png)

### `[nested LOOP_3]`
- **Internal Structure:** `(t05 ∗ τ)`
- **Block Frequency:** 37

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_3 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.8__gt_nested_LOOP_3.png)

### `[nested PAR_1]`
- **Internal Structure:** `{[τ │ t13], ⟨[t19 │ ⟨[t11 │ τ], [τ │ (t14 ∗ τ) │ (t05 ∗ τ)], [t16 │ τ]⟩], [t20 │ τ]⟩}`
- **Block Frequency:** 235



![nested PAR_1 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.8__gt_nested_PAR_1.png)

### `[nested PAR_4]`
- **Internal Structure:** `{t23, [t29 │ τ]}`
- **Block Frequency:** 112



![nested PAR_4 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.8__gt_nested_PAR_4.png)

### `[nested LOOP_5]`
- **Internal Structure:** `(t28 ∗ τ)`
- **Block Frequency:** 87

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_5 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.8__gt_nested_LOOP_5.png)

### `[nested LOOP_6]`
- **Internal Structure:** `(t42 ∗ τ)`
- **Block Frequency:** 249

- **Max Loop Iterations:** `119`
- **Max Sub-Sequence Length:** `239` steps (if one case consumes all iterations)

![nested LOOP_6 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.8__gt_nested_LOOP_6.png)

### `[nested LOOP_7]`
- **Internal Structure:** `(t39 ∗ τ)`
- **Block Frequency:** 249

- **Max Loop Iterations:** `88`
- **Max Sub-Sequence Length:** `177` steps (if one case consumes all iterations)

![nested LOOP_7 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.8__gt_nested_LOOP_7.png)

### `[nested LOOP_8]`
- **Internal Structure:** `(t44 ∗ τ)`
- **Block Frequency:** 109

- **Max Loop Iterations:** `6`
- **Max Sub-Sequence Length:** `13` steps (if one case consumes all iterations)

![nested LOOP_8 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.8__gt_nested_LOOP_8.png)

### `[nested LOOP_9]`
- **Internal Structure:** `(t36 ∗ τ)`
- **Block Frequency:** 249

- **Max Loop Iterations:** `189`
- **Max Sub-Sequence Length:** `379` steps (if one case consumes all iterations)

![nested LOOP_9 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.8__gt_nested_LOOP_9.png)

### `[nested LOOP_11]`
- **Internal Structure:** `(t45 ∗ τ)`
- **Block Frequency:** 198

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_11 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.8__gt_nested_LOOP_11.png)

### `[nested LOOP_13]`
- **Internal Structure:** `(t60 ∗ τ)`
- **Block Frequency:** 155

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_13 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.8__gt_nested_LOOP_13.png)

### `[nested LOOP_15]`
- **Internal Structure:** `(t47 ∗ τ)`
- **Block Frequency:** 177

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_15 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.8__gt_nested_LOOP_15.png)

### `[nested LOOP_17]`
- **Internal Structure:** `(t37 ∗ τ)`
- **Block Frequency:** 193

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_17 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.8__gt_nested_LOOP_17.png)

### `[nested LOOP_18]`
- **Internal Structure:** `(t46 ∗ τ)`
- **Block Frequency:** 249

- **Max Loop Iterations:** `84`
- **Max Sub-Sequence Length:** `169` steps (if one case consumes all iterations)

![nested LOOP_18 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.8__gt_nested_LOOP_18.png)

### `[nested PAR_16]`
- **Internal Structure:** `{[(t37 ∗ τ) │ τ], (t46 ∗ τ)}`
- **Block Frequency:** 249



![nested PAR_16 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.8__gt_nested_PAR_16.png)

### `[nested PAR_14]`
- **Internal Structure:** `{[(t47 ∗ τ) │ τ], [(t37 ∗ τ) │ τ], (t46 ∗ τ)}`
- **Block Frequency:** 249



![nested PAR_14 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.8__gt_nested_PAR_14.png)

### `[nested PAR_12]`
- **Internal Structure:** `{[(t60 ∗ τ) │ τ], [(t47 ∗ τ) │ τ], [(t37 ∗ τ) │ τ], (t46 ∗ τ)}`
- **Block Frequency:** 249



![nested PAR_12 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.8__gt_nested_PAR_12.png)

### `[nested PAR_10]`
- **Internal Structure:** `{[(t45 ∗ τ) │ τ], [(t60 ∗ τ) │ τ], [(t47 ∗ τ) │ τ], [(t37 ∗ τ) │ τ], (t46 ∗ τ)}`
- **Block Frequency:** 249



![nested PAR_10 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.8__gt_nested_PAR_10.png)

### `[nested LOOP_20]`
- **Internal Structure:** `(t48 ∗ τ)`
- **Block Frequency:** 204

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_20 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.8__gt_nested_LOOP_20.png)

### `[nested LOOP_21]`
- **Internal Structure:** `(t68 ∗ τ)`
- **Block Frequency:** 204

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_21 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.8__gt_nested_LOOP_21.png)

### `[nested PAR_19]`
- **Internal Structure:** `{(t48 ∗ τ), (t68 ∗ τ)}`
- **Block Frequency:** 204



![nested PAR_19 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.8__gt_nested_PAR_19.png)

### `[nested LOOP_22]`
- **Internal Structure:** `(t65 ∗ τ)`
- **Block Frequency:** 197

- **Max Loop Iterations:** `144`
- **Max Sub-Sequence Length:** `289` steps (if one case consumes all iterations)

![nested LOOP_22 Internal Diagram](images/nested_ref_audit_pdc2021_101010__noise0.8__gt_nested_LOOP_22.png)
