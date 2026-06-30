# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_101010.xes` |
| **Noise Threshold** | `0.2` |
| **Fitness** | `0.9582939689101251` |
| **Precision** | `0.29968017057569296` |
| **Total Cases in Log** | `250` |
| **Unique Activities** | `46` |
| **XOR Operators** | `38` |
| **LOOP Operators** | `20` |
| **SEQ Operators** | `29` |
| **PAR Operators** | `12` |
| **Binarization Additions** | `20` |
| **Tau Operators Added** | `24` |
| **Total Found Patterns** | `292` |
| **Verified Patterns** | `161` |
| **Discrepancy Patterns** | `20` |
| **Ghost Patterns** | `6` |
| **Nested LOOPs** | `20` |
| **Nested PARs** | `12` |
| **Tree Exposure (Strict, End-to-End % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `8.66%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `5.14%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `60.09%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `45.60%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `45.60%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `92.88%` |
| **Data Exposure, ST-only (% confirmed)** | `100.00%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `99.87%` |
| **Data Coverage, ST-only (% of real log)** | `8.93%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `58.48%` |
| **Data Coverage, Total (% of real log)** | `100.00%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `51.06%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `100.00%` |
| **Mean Absolute Exposure Volume (events/case)** | `25.71` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_101010__noise0.2.png)


```text
->( X( tau, 't09' ), 't10', X( ->( 't06', 't04', 't03', 't02' ), ->( +( X( tau, 't13' ), ->( X( 't19', ->( 't11', 't14', X( tau, +( X( tau, *( 't15', tau ) ), X( tau, *( 't05', tau ) ) ) ), X( tau, 't16' ) ) ), 't20' ) ), +( X( tau, *( 't34', tau ) ), ->( +( *( 't17', tau ), ->( *( 't21', tau ), X( tau, ->( 't24', +( 't23', X( tau, 't29' ) ) ) ) ) ), X( tau, 't22', ->( X( tau, 't25' ), 't26', 't27', X( tau, *( 't28', tau ) ) ) ), *( 't42', tau ), X( tau, 't38' ), +( X( tau, *( 't40', tau ) ), ->( *( ->( 't39', X( tau, ->( 't43', 't44' ) ), *( 't36', tau ) ), tau ), X( tau, 't33' ), *( ->( 't46', X( +( X( tau, *( 't69', tau ) ), X( tau, *( 't70', tau ) ) ), ->( X( tau, 't47' ), +( *( 't62', tau ), *( 't45', tau ), *( 't48', tau ), X( tau, *( 't60', tau ) ), X( tau, *( 't37', tau ) ), *( 't68', tau ) ), X( tau, 't64' ) ) ), *( 't65', tau ) ), tau ) ) ) ) ), X( tau, 't66' ) ) ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_101010__noise0.2.png)



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
| `[ST (in LOOP_3)]` | `t15` | Exact Token Match | $\ge$ 54 | **54** | ✅ **VERIFIED** |
| `[ST (in PAR_2)]` | `⟨t15⟩` | Exact Token Match | $\ge$ 54 | **54** | ✅ **VERIFIED** |
| `[ST (in LOOP_4)]` | `t05` | Exact Token Match | $\ge$ 37 | **37** | ✅ **VERIFIED** |
| `[ST (in PAR_2)]` | `⟨t05⟩` | Exact Token Match | $\ge$ 37 | **37** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `t16` | Exact Token Match | $\ge$ 74 | **74** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨τ, t16⟩` | Exact Token Match | $\ge$ 20 | **74** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t14, τ, t16⟩` | Exact Token Match | $\ge$ 20 | **57** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t14, τ⟩` | Exact Token Match | $\ge$ 47 | **121** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t14, τ⟩` | Exact Token Match | $\ge$ 20 | **121** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t11, t14, τ, t16⟩` | Exact Token Match | $\ge$ 20 | **57** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t11, t14, τ⟩` | Exact Token Match | $\ge$ 47 | **114** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t11, τ⟩` | Exact Token Match | $\ge$ 20 | **141** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t11, t14, τ⟩` | Exact Token Match | $\ge$ 20 | **114** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `t20` | Exact Token Match | $\ge$ 212 | **212** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t19, t20⟩` | Exact Token Match | $\ge$ 71 | **77** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t11, t14, τ, t16, t20⟩` | Exact Token Match | $\ge$ 14 | **57** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t11, t14, τ, t20⟩` | Exact Token Match | $\ge$ 41 | **82** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t11, τ, t20⟩` | Exact Token Match | $\ge$ 14 | **104** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t14, τ, t16, t20⟩` | Exact Token Match | $\ge$ 14 | **57** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t14, τ, t20⟩` | Exact Token Match | $\ge$ 41 | **82** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨τ, t16, t20⟩` | Exact Token Match | $\ge$ 14 | **74** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t16, t20⟩` | Exact Token Match | $\ge$ 68 | **74** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨τ, t20⟩` | Exact Token Match | $\ge$ 41 | **212** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨τ, t20⟩` | Exact Token Match | $\ge$ 14 | **212** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_1]` | Exact Token Match | $\ge$ 218 | **249** | ✅ **VERIFIED** |
| `[ST (in LOOP_6)]` | `t34` | Exact Token Match | $\ge$ 104 | **104** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t34⟩` | Exact Token Match | $\ge$ 104 | **104** | ✅ **VERIFIED** |
| `[ST (in LOOP_8)]` | `t17` | Exact Token Match | $\ge$ 246 | **246** | ✅ **VERIFIED** |
| `[AS (in PAR_7)]` | `[nested LOOP_8]` | Exact Token Match | $\ge$ 1 | **246** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `t21` | Exact Token Match | $\ge$ 290 | **290** | ✅ **VERIFIED** |
| `[AS (in PAR_7)]` | `[nested LOOP_9]` | Exact Token Match | $\ge$ 1 | **290** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `t24` | Exact Token Match | $\ge$ 112 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_10)]` | `t23` | Exact Token Match | $\ge$ 112 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_10)]` | `t29` | Exact Token Match | $\ge$ 78 | **78** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨[nested LOOP_9], t24, [nested PAR_10]⟩` | Exact Token Match | $\ge$ 1 | **78** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨[nested LOOP_9], t24⟩` | Exact Token Match | $\ge$ 1 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t22` | Exact Token Match | $\ge$ 121 | **121** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t25` | Exact Token Match | $\ge$ 60 | **60** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t26` | Exact Token Match | $\ge$ 112 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t27` | Exact Token Match | $\ge$ 112 | **112** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `t28` | Exact Token Match | $\ge$ 87 | **87** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t28⟩` | Exact Token Match | $\ge$ 87 | **87** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t27, τ⟩` | Exact Token Match | $\ge$ 25 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t27, t28⟩` | Exact Token Match | $\ge$ 87 | **87** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t26, t27, τ⟩` | Exact Token Match | $\ge$ 25 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t26, t27, t28⟩` | Exact Token Match | $\ge$ 87 | **87** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t26, t27⟩` | Exact Token Match | $\ge$ 112 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, t26, t27, t28⟩` | Exact Token Match | $\ge$ 27 | **87** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t25, t26, t27, t28⟩` | Exact Token Match | $\ge$ 35 | **49** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, t26, t27⟩` | Exact Token Match | $\ge$ 52 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, t26⟩` | Exact Token Match | $\ge$ 52 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t25, t26, t27⟩` | Exact Token Match | $\ge$ 60 | **60** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t25, t26⟩` | Exact Token Match | $\ge$ 60 | **60** | ✅ **VERIFIED** |
| `[ST (in LOOP_12)]` | `t42` | Exact Token Match | $\ge$ 368 | **368** | ✅ **VERIFIED** |
| `[AS (in PAR_5)]` | `[nested LOOP_12]` | Exact Token Match | $\ge$ 1 | **368** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t38` | Exact Token Match | $\ge$ 165 | **165** | ✅ **VERIFIED** |
| `[ST (in LOOP_14)]` | `t40` | Exact Token Match | $\ge$ 148 | **148** | ✅ **VERIFIED** |
| `[ST (in PAR_13)]` | `⟨t40⟩` | Exact Token Match | $\ge$ 148 | **148** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `t39` | Exact Token Match | $\ge$ 337 | **337** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `t43` | Exact Token Match | $\ge$ 115 | **115** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `t44` | Exact Token Match | $\ge$ 115 | **115** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨t43, t44⟩` | Exact Token Match | $\ge$ 115 | **115** | ✅ **VERIFIED** |
| `[ST (in LOOP_16)]` | `t36` | Exact Token Match | $\ge$ 438 | **438** | ✅ **VERIFIED** |
| `[AS (in LOOP_15)]` | `[nested LOOP_16]` | Exact Token Match | $\ge$ 1 | **224** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨t43, t44, [nested LOOP_16]⟩` | Exact Token Match | $\ge$ 1 | **115** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨t44, [nested LOOP_16]⟩` | Exact Token Match | $\ge$ 1 | **115** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨t39, t43, t44, [nested LOOP_16]⟩` | Exact Token Match | $\ge$ 1 | **115** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨t39, τ⟩` | Exact Token Match | $\ge$ 222 | **337** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨t39, t43, t44⟩` | Exact Token Match | $\ge$ 115 | **115** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨t39, t43⟩` | Exact Token Match | $\ge$ 115 | **115** | ✅ **VERIFIED** |
| `[AS (in PAR_13)]` | `[nested LOOP_15]` | Exact Token Match | $\ge$ 1 | **115** | ✅ **VERIFIED** |
| `[ST (in PAR_13)]` | `t33` | Exact Token Match | $\ge$ 145 | **145** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `t46` | Exact Token Match | $\ge$ 333 | **333** | ✅ **VERIFIED** |
| `[ST (in LOOP_19)]` | `t69` | Exact Token Match | $\ge$ 110 | **110** | ✅ **VERIFIED** |
| `[ST (in PAR_18)]` | `⟨t69⟩` | Exact Token Match | $\ge$ 110 | **110** | ✅ **VERIFIED** |
| `[ST (in LOOP_20)]` | `t70` | Exact Token Match | $\ge$ 99 | **99** | ✅ **VERIFIED** |
| `[ST (in PAR_18)]` | `⟨t70⟩` | Exact Token Match | $\ge$ 99 | **99** | ✅ **VERIFIED** |
| `[AS (in LOOP_17)]` | `[nested PAR_18]` | Exact Token Match | $\ge$ 110 | **165** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `t47` | Exact Token Match | $\ge$ 177 | **177** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `t62` | Exact Token Match | $\ge$ 250 | **250** | ✅ **VERIFIED** |
| `[ST (in PAR_21)]` | `⟨t62⟩` | Exact Token Match | $\ge$ 136 | **250** | ✅ **VERIFIED** |
| `[AS (in PAR_21)]` | `[nested LOOP_22]` | Exact Token Match | $\ge$ 1 | **250** | ✅ **VERIFIED** |
| `[ST (in LOOP_24)]` | `t45` | Exact Token Match | $\ge$ 198 | **198** | ✅ **VERIFIED** |
| `[ST (in PAR_23)]` | `⟨t45⟩` | Exact Token Match | $\ge$ 188 | **198** | ✅ **VERIFIED** |
| `[AS (in PAR_23)]` | `[nested LOOP_24]` | Exact Token Match | $\ge$ 1 | **198** | ✅ **VERIFIED** |
| `[ST (in LOOP_26)]` | `t48` | Exact Token Match | $\ge$ 204 | **204** | ✅ **VERIFIED** |
| `[ST (in PAR_25)]` | `⟨t48⟩` | Exact Token Match | $\ge$ 182 | **204** | ✅ **VERIFIED** |
| `[AS (in PAR_25)]` | `[nested LOOP_26]` | Exact Token Match | $\ge$ 1 | **204** | ✅ **VERIFIED** |
| `[ST (in LOOP_28)]` | `t60` | Exact Token Match | $\ge$ 155 | **155** | ✅ **VERIFIED** |
| `[ST (in PAR_27)]` | `⟨t60⟩` | Exact Token Match | $\ge$ 155 | **155** | ✅ **VERIFIED** |
| `[ST (in LOOP_30)]` | `t37` | Exact Token Match | $\ge$ 193 | **193** | ✅ **VERIFIED** |
| `[ST (in PAR_29)]` | `⟨t37⟩` | Exact Token Match | $\ge$ 193 | **193** | ✅ **VERIFIED** |
| `[ST (in LOOP_31)]` | `t68` | Exact Token Match | $\ge$ 204 | **204** | ✅ **VERIFIED** |
| `[ST (in PAR_29)]` | `⟨t68⟩` | Exact Token Match | $\ge$ 182 | **204** | ✅ **VERIFIED** |
| `[AS (in PAR_29)]` | `[nested LOOP_31]` | Exact Token Match | $\ge$ 1 | **204** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `t64` | Exact Token Match | $\ge$ 182 | **182** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨[nested PAR_21], τ⟩` | Exact Token Match | $\ge$ 11 | **182** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨[nested PAR_21], t64⟩` | Exact Token Match | $\ge$ 182 | **182** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨τ, [nested PAR_21], t64⟩` | Exact Token Match | $\ge$ 5 | **182** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨τ, [nested PAR_21]⟩` | Exact Token Match | $\ge$ 16 | **182** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨t47, [nested PAR_21]⟩` | Exact Token Match | $\ge$ 177 | **177** | ✅ **VERIFIED** |
| `[ST (in LOOP_32)]` | `t65` | Exact Token Match | $\ge$ 341 | **341** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨t65⟩` | Exact Token Match | $\ge$ 265 | **341** | ✅ **VERIFIED** |
| `[AS (in LOOP_17)]` | `[nested LOOP_32]` | Exact Token Match | $\ge$ 1 | **240** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨[nested PAR_18], t65⟩` | Exact Token Match | $\ge$ 72 | **158** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨[nested PAR_21], t64, t65⟩` | Exact Token Match | $\ge$ 144 | **160** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨t64, t65⟩` | Exact Token Match | $\ge$ 144 | **160** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨t46, [nested PAR_18], t65⟩` | Exact Token Match | $\ge$ 72 | **121** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨t46, τ⟩` | Exact Token Match | $\ge$ 30 | **333** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨t46, [nested PAR_18]⟩` | Exact Token Match | $\ge$ 110 | **149** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨t46, τ, [nested PAR_21], t64⟩` | Exact Token Match | $\ge$ 5 | **160** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨t46, τ, [nested PAR_21]⟩` | Exact Token Match | $\ge$ 16 | **213** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨t46, τ⟩` | Exact Token Match | $\ge$ 16 | **333** | ✅ **VERIFIED** |
| `[AS (in PAR_13)]` | `[nested LOOP_17]` | Exact Token Match | $\ge$ 1 | **9** | ✅ **VERIFIED** |
| `[ST (in PAR_13)]` | `⟨t33, [nested LOOP_17]⟩` | Exact Token Match | $\ge$ 1 | **5** | ✅ **VERIFIED** |
| `[ST (in PAR_13)]` | `⟨[nested LOOP_15], t33⟩` | Exact Token Match | $\ge$ 1 | **32** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t38, τ⟩` | Exact Token Match | $\ge$ 17 | **165** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨[nested LOOP_12], t38⟩` | Exact Token Match | $\ge$ 1 | **165** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, t22⟩` | Exact Token Match | $\ge$ 9 | **121** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_5]` | Exact Token Match | $\ge$ 233 | **249** | ✅ **VERIFIED** |
| `[ST]` | `t66` | Exact Token Match | $\ge$ 197 | **197** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_5], τ⟩` | Exact Token Match | $\ge$ 36 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_5], t66⟩` | Exact Token Match | $\ge$ 197 | **197** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], [nested PAR_5], τ⟩` | Exact Token Match | $\ge$ 21 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], [nested PAR_5], t66⟩` | Exact Token Match | $\ge$ 182 | **197** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], [nested PAR_5]⟩` | Exact Token Match | $\ge$ 218 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 15 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06, t04, t03, t02⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, [nested PAR_1], [nested PAR_5], τ⟩` | Exact Token Match | $\ge$ 21 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, [nested PAR_1], [nested PAR_5], t66⟩` | Exact Token Match | $\ge$ 182 | **197** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 16 | **250** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06, t04, t03⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06, t04⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, [nested PAR_1], [nested PAR_5]⟩` | Exact Token Match | $\ge$ 218 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 15 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 218 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 15 | **250** | ✅ **VERIFIED** |
| `[ST]` | `⟨t09, t10, [nested PAR_1], [nested PAR_5], t66⟩` | Exact Token Match | $\ge$ 114 | **157** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t10, [nested PAR_1], [nested PAR_5]⟩` | Exact Token Match | $\ge$ 36 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t10, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 36 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t10⟩` | Exact Token Match | $\ge$ 68 | **250** | ✅ **VERIFIED** |
| `[ST]` | `⟨t09, t10, [nested PAR_1], [nested PAR_5]⟩` | Exact Token Match | $\ge$ 150 | **181** | ✅ **VERIFIED** |
| `[ST]` | `⟨t09, t10, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 150 | **181** | ✅ **VERIFIED** |
| `[ST]` | `⟨t09, t10⟩` | Exact Token Match | $\ge$ 182 | **182** | ✅ **VERIFIED** |
| `[AS (in PAR_1)]` | `[nested PAR_2]` | Exact Token Match | $\ge$ 54 | **15** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_1)]` | `⟨[nested PAR_2], t16⟩` | Exact Token Match | $\ge$ 54 | **4** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_1)]` | `⟨t11, t14⟩` | Exact Token Match | $\ge$ 121 | **114** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_1)]` | `⟨[nested PAR_2], t16, t20⟩` | Exact Token Match | $\ge$ 48 | **4** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_7)]` | `[nested PAR_10]` | Exact Token Match | $\ge$ 112 | **78** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_7)]` | `⟨t24, [nested PAR_10]⟩` | Exact Token Match | $\ge$ 112 | **78** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_5)]` | `[nested PAR_7]` | Exact Token Match | $\ge$ 112 | **56** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_27)]` | `[nested PAR_29]` | Exact Token Match | $\ge$ 193 | **176** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_25)]` | `[nested PAR_27]` | Exact Token Match | $\ge$ 193 | **140** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_23)]` | `[nested PAR_25]` | Exact Token Match | $\ge$ 193 | **140** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_21)]` | `[nested PAR_23]` | Exact Token Match | $\ge$ 193 | **140** | ⚠️ **DISCREPANCY** |
| `[AS (in LOOP_17)]` | `[nested PAR_21]` | Exact Token Match | $\ge$ 193 | **182** | ⚠️ **DISCREPANCY** |
| `[ST (in LOOP_17)]` | `⟨t47, [nested PAR_21], t64⟩` | Exact Token Match | $\ge$ 166 | **123** | ⚠️ **DISCREPANCY** |
| `[ST (in LOOP_17)]` | `⟨t47, [nested PAR_21], t64, t65⟩` | Exact Token Match | $\ge$ 128 | **107** | ⚠️ **DISCREPANCY** |
| `[ST (in LOOP_17)]` | `⟨t46, t47, [nested PAR_21], t64, t65⟩` | Exact Token Match | $\ge$ 128 | **98** | ⚠️ **DISCREPANCY** |
| `[ST (in LOOP_17)]` | `⟨t46, t47, [nested PAR_21], t64⟩` | Exact Token Match | $\ge$ 166 | **111** | ⚠️ **DISCREPANCY** |
| `[ST (in LOOP_17)]` | `⟨t46, t47, [nested PAR_21]⟩` | Exact Token Match | $\ge$ 177 | **153** | ⚠️ **DISCREPANCY** |
| `[ST (in LOOP_17)]` | `⟨t46, t47⟩` | Exact Token Match | $\ge$ 177 | **155** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_5)]` | `[nested PAR_13]` | Exact Token Match | $\ge$ 148 | **1** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨t38, [nested PAR_13]⟩` | Exact Token Match | $\ge$ 148 | **1** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_1)]` | `⟨t14, [nested PAR_2], t16⟩` | Exact Token Match | $\ge$ 54 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_1)]` | `⟨t14, [nested PAR_2]⟩` | Exact Token Match | $\ge$ 54 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_1)]` | `⟨t11, t14, [nested PAR_2], t16⟩` | Exact Token Match | $\ge$ 54 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_1)]` | `⟨t11, t14, [nested PAR_2]⟩` | Exact Token Match | $\ge$ 54 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_1)]` | `⟨t11, t14, [nested PAR_2], t16, t20⟩` | Exact Token Match | $\ge$ 48 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_1)]` | `⟨t14, [nested PAR_2], t16, t20⟩` | Exact Token Match | $\ge$ 48 | **0** | ❌ **GHOST PATTERN** |

## Audit Summary
- **Perfect Pattern Verifications:** 161
- **Frequency Discrepancies:** 20
- **Ghost Patterns (Fatal):** 6
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 8.66%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 5.14%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 60.09%
- **Total Forced Volume (incl. unresolved AS, % of N):** 45.60%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 45.60%
- **Data Exposure (Confirmed % of Claimed Volume):** 92.88%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 100.00%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 99.87%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 8.93%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 58.48%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 100.00%
- **Max Fractional Exposure (Worst-Case Normalized):** 51.06% (expected length: 1329.75 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 100.00% (expected length: 28.34 events)
- **Mean Absolute Exposure Volume:** 25.71 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_3]`
- **Internal Structure:** `(t15 ∗ τ)`
- **Block Frequency:** 54

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_3 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_3.png)

### `[nested LOOP_4]`
- **Internal Structure:** `(t05 ∗ τ)`
- **Block Frequency:** 37

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_4 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_4.png)

### `[nested PAR_2]`
- **Internal Structure:** `{[τ │ (t15 ∗ τ)], [τ │ (t05 ∗ τ)]}`
- **Block Frequency:** 54



![nested PAR_2 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_PAR_2.png)

### `[nested PAR_1]`
- **Internal Structure:** `{[τ │ t13], ⟨[t19 │ ⟨t11, [⟨t14, [⟨[τ │ {[τ │ (t15 ∗ τ)], [τ │ (t05 ∗ τ)]}], [τ │ t16]⟩ │ τ]⟩ │ τ]⟩], [t20 │ τ]⟩}`
- **Block Frequency:** 218



![nested PAR_1 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_PAR_1.png)

### `[nested LOOP_6]`
- **Internal Structure:** `(t34 ∗ τ)`
- **Block Frequency:** 104

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_6 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_6.png)

### `[nested LOOP_8]`
- **Internal Structure:** `(t17 ∗ τ)`
- **Block Frequency:** 112

- **Max Loop Iterations:** `134`
- **Max Sub-Sequence Length:** `269` steps (if one case consumes all iterations)

![nested LOOP_8 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_8.png)

### `[nested LOOP_9]`
- **Internal Structure:** `(t21 ∗ τ)`
- **Block Frequency:** 112

- **Max Loop Iterations:** `178`
- **Max Sub-Sequence Length:** `357` steps (if one case consumes all iterations)

![nested LOOP_9 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_9.png)

### `[nested PAR_10]`
- **Internal Structure:** `{t23, [τ │ t29]}`
- **Block Frequency:** 112



![nested PAR_10 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_PAR_10.png)

### `[nested PAR_7]`
- **Internal Structure:** `{(t17 ∗ τ), ⟨(t21 ∗ τ), [τ │ ⟨t24, {t23, [τ │ t29]}⟩]⟩}`
- **Block Frequency:** 112



![nested PAR_7 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_PAR_7.png)

### `[nested LOOP_11]`
- **Internal Structure:** `(t28 ∗ τ)`
- **Block Frequency:** 87

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_11 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_11.png)

### `[nested LOOP_12]`
- **Internal Structure:** `(t42 ∗ τ)`
- **Block Frequency:** 165

- **Max Loop Iterations:** `203`
- **Max Sub-Sequence Length:** `407` steps (if one case consumes all iterations)

![nested LOOP_12 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_12.png)

### `[nested LOOP_14]`
- **Internal Structure:** `(t40 ∗ τ)`
- **Block Frequency:** 148

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_14 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_14.png)

### `[nested LOOP_16]`
- **Internal Structure:** `(t36 ∗ τ)`
- **Block Frequency:** 115

- **Max Loop Iterations:** `323`
- **Max Sub-Sequence Length:** `647` steps (if one case consumes all iterations)

![nested LOOP_16 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_16.png)

### `[nested LOOP_15]`
- **Internal Structure:** `(⟨t39, [⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ τ)`
- **Block Frequency:** 145

- **Max Loop Iterations:** `192`
- **Max Sub-Sequence Length:** `385` steps (if one case consumes all iterations)

![nested LOOP_15 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_15.png)

### `[nested LOOP_19]`
- **Internal Structure:** `(t69 ∗ τ)`
- **Block Frequency:** 110

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_19 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_19.png)

### `[nested LOOP_20]`
- **Internal Structure:** `(t70 ∗ τ)`
- **Block Frequency:** 99

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_20 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_20.png)

### `[nested PAR_18]`
- **Internal Structure:** `{[τ │ (t69 ∗ τ)], [τ │ (t70 ∗ τ)]}`
- **Block Frequency:** 110



![nested PAR_18 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_PAR_18.png)

### `[nested LOOP_22]`
- **Internal Structure:** `(t62 ∗ τ)`
- **Block Frequency:** 193

- **Max Loop Iterations:** `57`
- **Max Sub-Sequence Length:** `115` steps (if one case consumes all iterations)

![nested LOOP_22 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_22.png)

### `[nested LOOP_24]`
- **Internal Structure:** `(t45 ∗ τ)`
- **Block Frequency:** 193

- **Max Loop Iterations:** `5`
- **Max Sub-Sequence Length:** `11` steps (if one case consumes all iterations)

![nested LOOP_24 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_24.png)

### `[nested LOOP_26]`
- **Internal Structure:** `(t48 ∗ τ)`
- **Block Frequency:** 193

- **Max Loop Iterations:** `11`
- **Max Sub-Sequence Length:** `23` steps (if one case consumes all iterations)

![nested LOOP_26 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_26.png)

### `[nested LOOP_28]`
- **Internal Structure:** `(t60 ∗ τ)`
- **Block Frequency:** 155

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_28 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_28.png)

### `[nested LOOP_30]`
- **Internal Structure:** `(t37 ∗ τ)`
- **Block Frequency:** 193

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_30 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_30.png)

### `[nested LOOP_31]`
- **Internal Structure:** `(t68 ∗ τ)`
- **Block Frequency:** 193

- **Max Loop Iterations:** `11`
- **Max Sub-Sequence Length:** `23` steps (if one case consumes all iterations)

![nested LOOP_31 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_31.png)

### `[nested PAR_29]`
- **Internal Structure:** `{[τ │ (t37 ∗ τ)], (t68 ∗ τ)}`
- **Block Frequency:** 193



![nested PAR_29 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_PAR_29.png)

### `[nested PAR_27]`
- **Internal Structure:** `{[τ │ (t60 ∗ τ)], [τ │ (t37 ∗ τ)], (t68 ∗ τ)}`
- **Block Frequency:** 193



![nested PAR_27 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_PAR_27.png)

### `[nested PAR_25]`
- **Internal Structure:** `{(t48 ∗ τ), [τ │ (t60 ∗ τ)], [τ │ (t37 ∗ τ)], (t68 ∗ τ)}`
- **Block Frequency:** 193



![nested PAR_25 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_PAR_25.png)

### `[nested PAR_23]`
- **Internal Structure:** `{(t45 ∗ τ), (t48 ∗ τ), [τ │ (t60 ∗ τ)], [τ │ (t37 ∗ τ)], (t68 ∗ τ)}`
- **Block Frequency:** 193



![nested PAR_23 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_PAR_23.png)

### `[nested PAR_21]`
- **Internal Structure:** `{(t62 ∗ τ), (t45 ∗ τ), (t48 ∗ τ), [τ │ (t60 ∗ τ)], [τ │ (t37 ∗ τ)], (t68 ∗ τ)}`
- **Block Frequency:** 193



![nested PAR_21 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_PAR_21.png)

### `[nested LOOP_32]`
- **Internal Structure:** `(t65 ∗ τ)`
- **Block Frequency:** 303

- **Max Loop Iterations:** `38`
- **Max Sub-Sequence Length:** `77` steps (if one case consumes all iterations)

![nested LOOP_32 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_32.png)

### `[nested LOOP_17]`
- **Internal Structure:** `(⟨t46, [⟨[{[τ │ (t69 ∗ τ)], [τ │ (t70 ∗ τ)]} │ ⟨[τ │ t47], {(t62 ∗ τ), (t45 ∗ τ), (t48 ∗ τ), [τ │ (t60 ∗ τ)], [τ │ (t37 ∗ τ)], (t68 ∗ τ)}, [τ │ t64]⟩], (t65 ∗ τ)⟩ │ τ]⟩ ∗ τ)`
- **Block Frequency:** 145

- **Max Loop Iterations:** `188`
- **Max Sub-Sequence Length:** `377` steps (if one case consumes all iterations)

![nested LOOP_17 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_LOOP_17.png)

### `[nested PAR_13]`
- **Internal Structure:** `{[τ │ (t40 ∗ τ)], [⟨(⟨t39, [⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ τ), [τ │ t33], (⟨t46, [⟨[{[τ │ (t69 ∗ τ)], [τ │ (t70 ∗ τ)]} │ ⟨[τ │ t47], {(t62 ∗ τ), (t45 ∗ τ), (t48 ∗ τ), [τ │ (t60 ∗ τ)], [τ │ (t37 ∗ τ)], (t68 ∗ τ)}, [τ │ t64]⟩], (t65 ∗ τ)⟩ │ τ]⟩ ∗ τ)⟩ │ τ]}`
- **Block Frequency:** 148



![nested PAR_13 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_PAR_13.png)

### `[nested PAR_5]`
- **Internal Structure:** `{[τ │ (t34 ∗ τ)], ⟨[{(t17 ∗ τ), ⟨(t21 ∗ τ), [τ │ ⟨t24, {t23, [τ │ t29]}⟩]⟩} │ τ], [τ │ t22 │ ⟨[τ │ t25], t26, t27, [τ │ (t28 ∗ τ)]⟩], [⟨(t42 ∗ τ), [τ │ t38], [{[τ │ (t40 ∗ τ)], [⟨(⟨t39, [⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ τ), [τ │ t33], (⟨t46, [⟨[{[τ │ (t69 ∗ τ)], [τ │ (t70 ∗ τ)]} │ ⟨[τ │ t47], {(t62 ∗ τ), (t45 ∗ τ), (t48 ∗ τ), [τ │ (t60 ∗ τ)], [τ │ (t37 ∗ τ)], (t68 ∗ τ)}, [τ │ t64]⟩], (t65 ∗ τ)⟩ │ τ]⟩ ∗ τ)⟩ │ τ]} │ τ]⟩ │ τ]⟩}`
- **Block Frequency:** 233



![nested PAR_5 Internal Diagram](images/nested_ref_audit_pdc2021_101010_nested_PAR_5.png)
