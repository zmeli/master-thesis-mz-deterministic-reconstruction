# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_101010.xes` |
| **Noise Threshold** | `0.0` |
| **Fitness** | `1.0` |
| **Precision** | `0.12463620117436813` |
| **Total Cases in Log** | `250` |
| **Unique Activities** | `48` |
| **XOR Operators** | `50` |
| **LOOP Operators** | `13` |
| **SEQ Operators** | `26` |
| **PAR Operators** | `9` |
| **Binarization Additions** | `18` |
| **Tau Operators Added** | `29` |
| **Total Found Patterns** | `257` |
| **Verified Patterns** | `139` |
| **Discrepancy Patterns** | `6` |
| **Ghost Patterns** | `13` |
| **Nested LOOPs** | `13` |
| **Nested PARs** | `9` |
| **Tree Exposure (Strict, End-to-End % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `8.59%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `5.09%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `59.35%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `38.80%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `38.80%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `89.50%` |
| **Data Exposure, ST-only (% confirmed)** | `100.00%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `100.00%` |
| **Data Coverage, ST-only (% of real log)** | `8.86%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `39.68%` |
| **Data Coverage, Total (% of real log)** | `100.00%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `42.50%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `100.00%` |
| **Mean Absolute Exposure Volume (events/case)** | `30.46` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_101010__noise0.0.png)


```text
->( X( tau, 't09' ), 't10', X( ->( 't06', 't04', 't03', 't02' ), ->( +( X( tau, 't13' ), ->( X( tau, 't19', ->( 't11', +( X( tau, +( X( tau, *( 't14', tau ) ), X( tau, *( 't15', tau ) ) ) ), X( tau, *( 't05', tau ) ) ), X( tau, 't16' ) ) ), X( tau, 't20' ) ) ), +( X( tau, *( 't34', tau ) ), ->( *( ->( +( 't21', X( tau, +( X( tau, *( 't17', tau ) ), X( tau, ->( 't24', +( 't23', X( tau, 't29' ) ) ) ) ) ) ), X( tau, 't22', ->( X( tau, 't25' ), 't26', 't27', X( tau, 't28' ) ) ), X( tau, *( 't42', tau ) ) ), tau ), X( tau, 't38' ), +( X( tau, 't30' ), ->( X( tau, 't71' ), X( tau, +( X( tau, *( 't40', tau ) ), ->( X( tau, ->( *( ->( 't39', X( tau, ->( 't43', 't44' ) ), *( 't36', tau ) ), tau ), X( tau, 't33' ) ) ), *( *( ->( X( 't69', 't45', 't48', 't47', 't46' ), X( tau, *( X( 't65', 't70', ->( X( 't62', 't60', 't37', 't68' ), X( tau, 't64' ) ) ), tau ) ) ), tau ), tau ) ) ) ) ) ) ) ), X( tau, 't66' ) ) ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_101010__noise0.0.png)



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
| `[ST (in LOOP_4)]` | `t14` | Exact Token Match | $\ge$ 121 | **121** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t14⟩` | Exact Token Match | $\ge$ 121 | **121** | ✅ **VERIFIED** |
| `[ST (in LOOP_5)]` | `t15` | Exact Token Match | $\ge$ 54 | **54** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t15⟩` | Exact Token Match | $\ge$ 54 | **54** | ✅ **VERIFIED** |
| `[ST (in LOOP_6)]` | `t05` | Exact Token Match | $\ge$ 37 | **37** | ✅ **VERIFIED** |
| `[ST (in PAR_2)]` | `⟨t05⟩` | Exact Token Match | $\ge$ 37 | **37** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `t16` | Exact Token Match | $\ge$ 74 | **74** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t11, τ⟩` | Exact Token Match | $\ge$ 20 | **141** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `t20` | Exact Token Match | $\ge$ 212 | **212** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t19, t20⟩` | Exact Token Match | $\ge$ 71 | **77** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t11, τ, t20⟩` | Exact Token Match | $\ge$ 14 | **104** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨τ, t20⟩` | Exact Token Match | $\ge$ 41 | **212** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t16, t20⟩` | Exact Token Match | $\ge$ 68 | **74** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨τ, t20⟩` | Exact Token Match | $\ge$ 14 | **212** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_1]` | Exact Token Match | $\ge$ 218 | **249** | ✅ **VERIFIED** |
| `[ST (in LOOP_8)]` | `t34` | Exact Token Match | $\ge$ 104 | **104** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨t34⟩` | Exact Token Match | $\ge$ 104 | **104** | ✅ **VERIFIED** |
| `[ST (in PAR_10)]` | `t21` | Exact Token Match | $\ge$ 290 | **290** | ✅ **VERIFIED** |
| `[ST (in LOOP_12)]` | `t17` | Exact Token Match | $\ge$ 246 | **246** | ✅ **VERIFIED** |
| `[ST (in PAR_11)]` | `⟨t17⟩` | Exact Token Match | $\ge$ 246 | **246** | ✅ **VERIFIED** |
| `[ST (in PAR_11)]` | `t24` | Exact Token Match | $\ge$ 112 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_13)]` | `t23` | Exact Token Match | $\ge$ 112 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_13)]` | `t29` | Exact Token Match | $\ge$ 78 | **78** | ✅ **VERIFIED** |
| `[AS (in LOOP_9)]` | `[nested PAR_10]` | Exact Token Match | $\ge$ 290 | **311** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `t22` | Exact Token Match | $\ge$ 121 | **121** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `t25` | Exact Token Match | $\ge$ 60 | **60** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `t26` | Exact Token Match | $\ge$ 112 | **112** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `t27` | Exact Token Match | $\ge$ 112 | **112** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `t28` | Exact Token Match | $\ge$ 87 | **87** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨t27, τ⟩` | Exact Token Match | $\ge$ 25 | **112** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨t27, t28⟩` | Exact Token Match | $\ge$ 87 | **87** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨t26, t27, τ⟩` | Exact Token Match | $\ge$ 25 | **112** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨t26, t27, t28⟩` | Exact Token Match | $\ge$ 87 | **87** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨t26, t27⟩` | Exact Token Match | $\ge$ 112 | **112** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨τ, t26, t27, t28⟩` | Exact Token Match | $\ge$ 27 | **87** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨t25, t26, t27, t28⟩` | Exact Token Match | $\ge$ 35 | **48** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨τ, t26, t27⟩` | Exact Token Match | $\ge$ 52 | **112** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨τ, t26⟩` | Exact Token Match | $\ge$ 52 | **112** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨t25, t26, t27⟩` | Exact Token Match | $\ge$ 60 | **60** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨t25, t26⟩` | Exact Token Match | $\ge$ 60 | **60** | ✅ **VERIFIED** |
| `[ST (in LOOP_14)]` | `t42` | Exact Token Match | $\ge$ 368 | **368** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨t42⟩` | Exact Token Match | $\ge$ 368 | **368** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨τ, t42⟩` | Exact Token Match | $\ge$ 135 | **368** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨t22, t42⟩` | Exact Token Match | $\ge$ 121 | **121** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨τ, t26, t27, t28, t42⟩` | Exact Token Match | $\ge$ 27 | **87** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨t25, t26, t27, t28, t42⟩` | Exact Token Match | $\ge$ 35 | **48** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨t26, t27, τ, t42⟩` | Exact Token Match | $\ge$ 25 | **87** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨t26, t27, t28, t42⟩` | Exact Token Match | $\ge$ 87 | **87** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨t27, τ, t42⟩` | Exact Token Match | $\ge$ 25 | **87** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨t27, t28, t42⟩` | Exact Token Match | $\ge$ 87 | **87** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨τ, t42⟩` | Exact Token Match | $\ge$ 25 | **368** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨t28, t42⟩` | Exact Token Match | $\ge$ 87 | **87** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨[nested PAR_10], τ, t42⟩` | Exact Token Match | $\ge$ 57 | **265** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨[nested PAR_10], t22, t42⟩` | Exact Token Match | $\ge$ 43 | **121** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨[nested PAR_10], τ⟩` | Exact Token Match | $\ge$ 57 | **311** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨[nested PAR_10], t22⟩` | Exact Token Match | $\ge$ 43 | **121** | ✅ **VERIFIED** |
| `[AS (in PAR_7)]` | `[nested LOOP_9]` | Exact Token Match | $\ge$ 1 | **7** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `t38` | Exact Token Match | $\ge$ 165 | **165** | ✅ **VERIFIED** |
| `[ST (in PAR_15)]` | `t30` | Exact Token Match | $\ge$ 36 | **36** | ✅ **VERIFIED** |
| `[ST (in PAR_15)]` | `t71` | Exact Token Match | $\ge$ 25 | **25** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `t40` | Exact Token Match | $\ge$ 148 | **148** | ✅ **VERIFIED** |
| `[ST (in PAR_16)]` | `⟨t40⟩` | Exact Token Match | $\ge$ 148 | **148** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `t39` | Exact Token Match | $\ge$ 337 | **337** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `t43` | Exact Token Match | $\ge$ 115 | **115** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `t44` | Exact Token Match | $\ge$ 115 | **115** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `⟨t43, t44⟩` | Exact Token Match | $\ge$ 115 | **115** | ✅ **VERIFIED** |
| `[ST (in LOOP_19)]` | `t36` | Exact Token Match | $\ge$ 438 | **438** | ✅ **VERIFIED** |
| `[AS (in LOOP_18)]` | `[nested LOOP_19]` | Exact Token Match | $\ge$ 1 | **224** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `⟨t43, t44, [nested LOOP_19]⟩` | Exact Token Match | $\ge$ 1 | **115** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `⟨t44, [nested LOOP_19]⟩` | Exact Token Match | $\ge$ 1 | **115** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `⟨t39, t43, t44, [nested LOOP_19]⟩` | Exact Token Match | $\ge$ 1 | **115** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `⟨t39, τ⟩` | Exact Token Match | $\ge$ 222 | **337** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `⟨t39, t43, t44⟩` | Exact Token Match | $\ge$ 115 | **115** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `⟨t39, t43⟩` | Exact Token Match | $\ge$ 115 | **115** | ✅ **VERIFIED** |
| `[AS (in PAR_16)]` | `[nested LOOP_18]` | Exact Token Match | $\ge$ 1 | **115** | ✅ **VERIFIED** |
| `[ST (in PAR_16)]` | `t33` | Exact Token Match | $\ge$ 145 | **145** | ✅ **VERIFIED** |
| `[ST (in PAR_16)]` | `⟨[nested LOOP_18], t33⟩` | Exact Token Match | $\ge$ 1 | **32** | ✅ **VERIFIED** |
| `[ST (in LOOP_21)]` | `t69` | Exact Token Match | $\ge$ 110 | **110** | ✅ **VERIFIED** |
| `[ST (in LOOP_21)]` | `t45` | Exact Token Match | $\ge$ 198 | **198** | ✅ **VERIFIED** |
| `[ST (in LOOP_21)]` | `t48` | Exact Token Match | $\ge$ 204 | **204** | ✅ **VERIFIED** |
| `[ST (in LOOP_21)]` | `t47` | Exact Token Match | $\ge$ 177 | **177** | ✅ **VERIFIED** |
| `[ST (in LOOP_21)]` | `t46` | Exact Token Match | $\ge$ 333 | **333** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `t65` | Exact Token Match | $\ge$ 341 | **341** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `t70` | Exact Token Match | $\ge$ 99 | **99** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `t62` | Exact Token Match | $\ge$ 250 | **250** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `t60` | Exact Token Match | $\ge$ 155 | **155** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `t37` | Exact Token Match | $\ge$ 193 | **193** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `t68` | Exact Token Match | $\ge$ 204 | **204** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `t64` | Exact Token Match | $\ge$ 182 | **182** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `⟨t62, τ⟩` | Exact Token Match | $\ge$ 68 | **250** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `⟨t37, τ⟩` | Exact Token Match | $\ge$ 11 | **193** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `⟨t68, τ⟩` | Exact Token Match | $\ge$ 22 | **204** | ✅ **VERIFIED** |
| `[ST (in LOOP_21)]` | `⟨t65⟩` | Exact Token Match | $\ge$ 341 | **341** | ✅ **VERIFIED** |
| `[ST (in LOOP_21)]` | `⟨t70⟩` | Exact Token Match | $\ge$ 99 | **99** | ✅ **VERIFIED** |
| `[AS (in PAR_16)]` | `[nested LOOP_20]` | Exact Token Match | $\ge$ 1 | **9** | ✅ **VERIFIED** |
| `[ST (in PAR_16)]` | `⟨t33, [nested LOOP_20]⟩` | Exact Token Match | $\ge$ 1 | **5** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨t38, τ⟩` | Exact Token Match | $\ge$ 17 | **165** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨[nested LOOP_9], t38⟩` | Exact Token Match | $\ge$ 1 | **3** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_7]` | Exact Token Match | $\ge$ 165 | **249** | ✅ **VERIFIED** |
| `[ST]` | `t66` | Exact Token Match | $\ge$ 197 | **197** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_7], t66⟩` | Exact Token Match | $\ge$ 165 | **197** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t66⟩` | Exact Token Match | $\ge$ 32 | **197** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], [nested PAR_7], t66⟩` | Exact Token Match | $\ge$ 165 | **197** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], τ, t66⟩` | Exact Token Match | $\ge$ 32 | **197** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], τ⟩` | Exact Token Match | $\ge$ 21 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], [nested PAR_7]⟩` | Exact Token Match | $\ge$ 165 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], τ⟩` | Exact Token Match | $\ge$ 32 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06, t04, t03, t02⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, [nested PAR_1], [nested PAR_7], t66⟩` | Exact Token Match | $\ge$ 165 | **197** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, [nested PAR_1], τ, t66⟩` | Exact Token Match | $\ge$ 32 | **197** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, [nested PAR_1], τ⟩` | Exact Token Match | $\ge$ 21 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 31 | **250** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06, t04, t03⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06, t04⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, [nested PAR_1], [nested PAR_7]⟩` | Exact Token Match | $\ge$ 165 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, [nested PAR_1], τ⟩` | Exact Token Match | $\ge$ 32 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 218 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨t09, t10, [nested PAR_1], [nested PAR_7], t66⟩` | Exact Token Match | $\ge$ 97 | **157** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t10, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 36 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t10⟩` | Exact Token Match | $\ge$ 68 | **250** | ✅ **VERIFIED** |
| `[ST]` | `⟨t09, t10, [nested PAR_1], [nested PAR_7]⟩` | Exact Token Match | $\ge$ 97 | **181** | ✅ **VERIFIED** |
| `[ST]` | `⟨t09, t10, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 150 | **181** | ✅ **VERIFIED** |
| `[ST]` | `⟨t09, t10⟩` | Exact Token Match | $\ge$ 182 | **182** | ✅ **VERIFIED** |
| `[AS (in PAR_2)]` | `[nested PAR_3]` | Exact Token Match | $\ge$ 121 | **39** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_11)]` | `[nested PAR_13]` | Exact Token Match | $\ge$ 112 | **78** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_11)]` | `⟨t24, [nested PAR_13]⟩` | Exact Token Match | $\ge$ 112 | **78** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_10)]` | `[nested PAR_11]` | Exact Token Match | $\ge$ 246 | **56** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_15)]` | `[nested PAR_16]` | Exact Token Match | $\ge$ 148 | **1** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_15)]` | `⟨τ, [nested PAR_16]⟩` | Exact Token Match | $\ge$ 123 | **1** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_1)]` | `[nested PAR_2]` | Exact Token Match | $\ge$ 121 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_1)]` | `⟨[nested PAR_2], τ⟩` | Exact Token Match | $\ge$ 47 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_1)]` | `⟨[nested PAR_2], t16⟩` | Exact Token Match | $\ge$ 74 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_1)]` | `⟨t11, [nested PAR_2], τ⟩` | Exact Token Match | $\ge$ 47 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_1)]` | `⟨t11, [nested PAR_2], t16⟩` | Exact Token Match | $\ge$ 74 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_1)]` | `⟨t11, [nested PAR_2]⟩` | Exact Token Match | $\ge$ 121 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_1)]` | `⟨t11, [nested PAR_2], τ, t20⟩` | Exact Token Match | $\ge$ 41 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_1)]` | `⟨t11, [nested PAR_2], t16, t20⟩` | Exact Token Match | $\ge$ 68 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_1)]` | `⟨[nested PAR_2], τ, t20⟩` | Exact Token Match | $\ge$ 41 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_1)]` | `⟨[nested PAR_2], t16, t20⟩` | Exact Token Match | $\ge$ 68 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_15)]` | `⟨t71, [nested PAR_16]⟩` | Exact Token Match | $\ge$ 25 | **0** | ❌ **GHOST PATTERN** |
| `[AS (in PAR_7)]` | `[nested PAR_15]` | Exact Token Match | $\ge$ 148 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_7)]` | `⟨t38, [nested PAR_15]⟩` | Exact Token Match | $\ge$ 148 | **0** | ❌ **GHOST PATTERN** |

## Audit Summary
- **Perfect Pattern Verifications:** 139
- **Frequency Discrepancies:** 6
- **Ghost Patterns (Fatal):** 13
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 8.59%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 5.09%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 59.35%
- **Total Forced Volume (incl. unresolved AS, % of N):** 38.80%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 38.80%
- **Data Exposure (Confirmed % of Claimed Volume):** 89.50%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 100.00%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 100.00%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 8.86%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 39.68%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 100.00%
- **Max Fractional Exposure (Worst-Case Normalized):** 42.50% (expected length: 2173.79 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 100.00% (expected length: 28.59 events)
- **Mean Absolute Exposure Volume:** 30.46 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_4]`
- **Internal Structure:** `(t14 ∗ τ)`
- **Block Frequency:** 121

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_4 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_4.png)

### `[nested LOOP_5]`
- **Internal Structure:** `(t15 ∗ τ)`
- **Block Frequency:** 54

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_5 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_5.png)

### `[nested PAR_3]`
- **Internal Structure:** `{[τ │ (t14 ∗ τ)], [τ │ (t15 ∗ τ)]}`
- **Block Frequency:** 121



![nested PAR_3 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_PAR_3.png)

### `[nested LOOP_6]`
- **Internal Structure:** `(t05 ∗ τ)`
- **Block Frequency:** 37

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_6 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_6.png)

### `[nested PAR_2]`
- **Internal Structure:** `{[τ │ {[τ │ (t14 ∗ τ)], [τ │ (t15 ∗ τ)]}], [τ │ (t05 ∗ τ)]}`
- **Block Frequency:** 121



![nested PAR_2 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_PAR_2.png)

### `[nested PAR_1]`
- **Internal Structure:** `{[τ │ t13], ⟨[τ │ t19 │ ⟨t11, [⟨{[τ │ {[τ │ (t14 ∗ τ)], [τ │ (t15 ∗ τ)]}], [τ │ (t05 ∗ τ)]}, [τ │ t16]⟩ │ τ]⟩], [τ │ t20]⟩}`
- **Block Frequency:** 218



![nested PAR_1 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_PAR_1.png)

### `[nested LOOP_8]`
- **Internal Structure:** `(t34 ∗ τ)`
- **Block Frequency:** 104

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_8 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_8.png)

### `[nested LOOP_12]`
- **Internal Structure:** `(t17 ∗ τ)`
- **Block Frequency:** 246

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_12 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_12.png)

### `[nested PAR_13]`
- **Internal Structure:** `{t23, [τ │ t29]}`
- **Block Frequency:** 112



![nested PAR_13 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_PAR_13.png)

### `[nested PAR_11]`
- **Internal Structure:** `{[τ │ (t17 ∗ τ)], [τ │ ⟨t24, {t23, [τ │ t29]}⟩]}`
- **Block Frequency:** 246



![nested PAR_11 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_PAR_11.png)

### `[nested PAR_10]`
- **Internal Structure:** `{t21, [τ │ {[τ │ (t17 ∗ τ)], [τ │ ⟨t24, {t23, [τ │ t29]}⟩]}]}`
- **Block Frequency:** 290



![nested PAR_10 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_PAR_10.png)

### `[nested LOOP_14]`
- **Internal Structure:** `(t42 ∗ τ)`
- **Block Frequency:** 368

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_14 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_14.png)

### `[nested LOOP_9]`
- **Internal Structure:** `(⟨[{t21, [τ │ {[τ │ (t17 ∗ τ)], [τ │ ⟨t24, {t23, [τ │ t29]}⟩]}]} │ τ], [τ │ t22 │ ⟨[τ │ t25], t26, t27, [τ │ t28]⟩], [τ │ (t42 ∗ τ)]⟩ ∗ τ)`
- **Block Frequency:** 165

- **Max Loop Iterations:** `203`
- **Max Sub-Sequence Length:** `407` steps (if one case consumes all iterations)

![nested LOOP_9 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_9.png)

### `[nested LOOP_17]`
- **Internal Structure:** `(t40 ∗ τ)`
- **Block Frequency:** 148

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_17 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_17.png)

### `[nested LOOP_19]`
- **Internal Structure:** `(t36 ∗ τ)`
- **Block Frequency:** 115

- **Max Loop Iterations:** `323`
- **Max Sub-Sequence Length:** `647` steps (if one case consumes all iterations)

![nested LOOP_19 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_19.png)

### `[nested LOOP_18]`
- **Internal Structure:** `(⟨t39, [⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ τ)`
- **Block Frequency:** 145

- **Max Loop Iterations:** `192`
- **Max Sub-Sequence Length:** `385` steps (if one case consumes all iterations)

![nested LOOP_18 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_18.png)

### `[nested LOOP_22]`
- **Internal Structure:** `([t65 │ t70 │ ⟨[t62 │ t60 │ t37 │ t68], [τ │ t64]⟩] ∗ τ)`
- **Block Frequency:** 1242

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_22 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_22.png)

### `[nested LOOP_21]`
- **Internal Structure:** `(⟨[t69 │ t45 │ t48 │ t47 │ t46 │ τ], [τ │ ([t65 │ t70 │ ⟨[t62 │ t60 │ t37 │ t68], [τ │ t64]⟩] ∗ τ)]⟩ ∗ τ)`
- **Block Frequency:** 1242

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_21 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_21.png)

### `[nested LOOP_20]`
- **Internal Structure:** `((⟨[t69 │ t45 │ t48 │ t47 │ t46 │ τ], [τ │ ([t65 │ t70 │ ⟨[t62 │ t60 │ t37 │ t68], [τ │ t64]⟩] ∗ τ)]⟩ ∗ τ) ∗ τ)`
- **Block Frequency:** 145

- **Max Loop Iterations:** `1097`
- **Max Sub-Sequence Length:** `2195` steps (if one case consumes all iterations)

![nested LOOP_20 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_20.png)

### `[nested PAR_16]`
- **Internal Structure:** `{[τ │ (t40 ∗ τ)], [⟨[τ │ ⟨(⟨t39, [⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ τ), [τ │ t33]⟩], ((⟨[t69 │ t45 │ t48 │ t47 │ t46 │ τ], [τ │ ([t65 │ t70 │ ⟨[t62 │ t60 │ t37 │ t68], [τ │ t64]⟩] ∗ τ)]⟩ ∗ τ) ∗ τ)⟩ │ τ]}`
- **Block Frequency:** 148



![nested PAR_16 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_PAR_16.png)

### `[nested PAR_15]`
- **Internal Structure:** `{[τ │ t30], ⟨[τ │ t71], [τ │ {[τ │ (t40 ∗ τ)], [⟨[τ │ ⟨(⟨t39, [⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ τ), [τ │ t33]⟩], ((⟨[t69 │ t45 │ t48 │ t47 │ t46 │ τ], [τ │ ([t65 │ t70 │ ⟨[t62 │ t60 │ t37 │ t68], [τ │ t64]⟩] ∗ τ)]⟩ ∗ τ) ∗ τ)⟩ │ τ]}]⟩}`
- **Block Frequency:** 148



![nested PAR_15 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_PAR_15.png)

### `[nested PAR_7]`
- **Internal Structure:** `{[τ │ (t34 ∗ τ)], ⟨(⟨[{t21, [τ │ {[τ │ (t17 ∗ τ)], [τ │ ⟨t24, {t23, [τ │ t29]}⟩]}]} │ τ], [τ │ t22 │ ⟨[τ │ t25], t26, t27, [τ │ t28]⟩], [τ │ (t42 ∗ τ)]⟩ ∗ τ), [τ │ t38], [{[τ │ t30], ⟨[τ │ t71], [τ │ {[τ │ (t40 ∗ τ)], [⟨[τ │ ⟨(⟨t39, [⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ τ), [τ │ t33]⟩], ((⟨[t69 │ t45 │ t48 │ t47 │ t46 │ τ], [τ │ ([t65 │ t70 │ ⟨[t62 │ t60 │ t37 │ t68], [τ │ t64]⟩] ∗ τ)]⟩ ∗ τ) ∗ τ)⟩ │ τ]}]⟩} │ τ]⟩}`
- **Block Frequency:** 165



![nested PAR_7 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_PAR_7.png)
