# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_0011012.xes` |
| **Noise Threshold** | `0.4` |
| **Fitness** | `0.9183723690351041` |
| **Precision** | `0.6146331177958955` |
| **Total Cases in Log** | `1000` |
| **Unique Activities** | `35` |
| **XOR Operators** | `34` |
| **LOOP Operators** | `3` |
| **SEQ Operators** | `27` |
| **PAR Operators** | `3` |
| **Binarization Additions** | `14` |
| **Tau Operators Added** | `29` |
| **Total Found Patterns** | `230` |
| **Verified Patterns** | `123` |
| **Discrepancy Patterns** | `19` |
| **Ghost Patterns** | `0` |
| **Nested LOOPs** | `3` |
| **Nested PARs** | `3` |
| **Tree Exposure (Strict, End-to-End % of N)** | `11.10%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `46.62%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `24.54%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `100.00%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `11.10%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `0.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `99.65%` |
| **Data Exposure, ST-only (% confirmed)** | `99.79%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `99.74%` |
| **Data Coverage, ST-only (% of real log)** | `55.15%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `100.00%` |
| **Data Coverage, Total (% of real log)** | `100.00%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `13.64%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `46.62%` |
| **Mean Absolute Exposure Volume (events/case)** | `1.53` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_0011012__noise0.4.png)


```text
->( 't10', X( 't11', ->( 't06', X( tau, 't04' ) ) ), X( tau, 't05' ), X( 't15', ->( X( tau, 't16' ), 't20' ) ), X( tau, ->( +( *( 't17', tau ), ->( 't21', X( tau, 't24' ), X( tau, 't23' ) ) ), X( tau, 't22' ), +( *( 't34', tau ), ->( X( tau, 't26' ), X( tau, ->( 't27', X( tau, 't28' ) ) ), 't42', 't39' ) ), X( 't71', ->( X( tau, ->( 't43', 't44' ) ), +( X( tau, *( 't40', tau ) ), ->( 't36', 't46', X( tau, ->( 't47', X( tau, 't37' ) ) ) ) ), X( tau, ->( 't48', X( tau, 't68' ) ) ), X( tau, ->( 't56', 't62' ) ), X( 't69', 't70' ), 't65' ) ), 't55' ) ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_0011012__noise0.4.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST]` | `t10` | Exact Token Match | $\ge$ 959 | **959** | ✅ **VERIFIED** |
| `[ST]` | `t11` | Exact Token Match | $\ge$ 224 | **224** | ✅ **VERIFIED** |
| `[ST]` | `t06` | Exact Token Match | $\ge$ 502 | **502** | ✅ **VERIFIED** |
| `[ST]` | `t04` | Exact Token Match | $\ge$ 237 | **237** | ✅ **VERIFIED** |
| `[ST]` | `⟨t06, τ⟩` | Exact Token Match | $\ge$ 265 | **502** | ✅ **VERIFIED** |
| `[ST]` | `t05` | Exact Token Match | $\ge$ 337 | **337** | ✅ **VERIFIED** |
| `[ST]` | `t15` | Exact Token Match | $\ge$ 497 | **497** | ✅ **VERIFIED** |
| `[ST]` | `t16` | Exact Token Match | $\ge$ 113 | **113** | ✅ **VERIFIED** |
| `[ST]` | `t20` | Exact Token Match | $\ge$ 351 | **351** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t20⟩` | Exact Token Match | $\ge$ 238 | **351** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `t17` | Exact Token Match | $\ge$ 589 | **589** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t17⟩` | Exact Token Match | $\ge$ 343 | **589** | ✅ **VERIFIED** |
| `[AS (in PAR_1)]` | `[nested LOOP_2]` | Exact Token Match | $\ge$ 1 | **589** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `t21` | Exact Token Match | $\ge$ 466 | **466** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `t24` | Exact Token Match | $\ge$ 230 | **230** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `t23` | Exact Token Match | $\ge$ 236 | **236** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨τ, t23⟩` | Exact Token Match | $\ge$ 6 | **236** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t21, τ, t23⟩` | Exact Token Match | $\ge$ 6 | **233** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t21, τ⟩` | Exact Token Match | $\ge$ 230 | **466** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t21, τ⟩` | Exact Token Match | $\ge$ 6 | **466** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_1]` | Exact Token Match | $\ge$ 466 | **472** | ✅ **VERIFIED** |
| `[ST]` | `t22` | Exact Token Match | $\ge$ 233 | **233** | ✅ **VERIFIED** |
| `[ST (in LOOP_4)]` | `t34` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t34⟩` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `t26` | Exact Token Match | $\ge$ 236 | **236** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `t27` | Exact Token Match | $\ge$ 235 | **235** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `t28` | Exact Token Match | $\ge$ 126 | **126** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t27, τ⟩` | Exact Token Match | $\ge$ 109 | **235** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t27, t28⟩` | Exact Token Match | $\ge$ 126 | **126** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `t42` | Exact Token Match | $\ge$ 357 | **357** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `t39` | Exact Token Match | $\ge$ 357 | **357** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨τ, t42, t39⟩` | Exact Token Match | $\ge$ 122 | **352** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t27, τ, t42, t39⟩` | Exact Token Match | $\ge$ 109 | **123** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨τ, t42⟩` | Exact Token Match | $\ge$ 122 | **357** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t27, τ, t42⟩` | Exact Token Match | $\ge$ 109 | **125** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨τ, t42, t39⟩` | Exact Token Match | $\ge$ 109 | **352** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t26, τ, t42, t39⟩` | Exact Token Match | $\ge$ 1 | **123** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t26, t27, t28, t42, t39⟩` | Exact Token Match | $\ge$ 5 | **122** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t26, τ, t42⟩` | Exact Token Match | $\ge$ 1 | **125** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t26, t27, t28, t42⟩` | Exact Token Match | $\ge$ 5 | **124** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t26, τ⟩` | Exact Token Match | $\ge$ 1 | **236** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t26, t27, t28⟩` | Exact Token Match | $\ge$ 5 | **126** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t26, t27⟩` | Exact Token Match | $\ge$ 114 | **234** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_3]` | Exact Token Match | $\ge$ 357 | **472** | ✅ **VERIFIED** |
| `[ST]` | `t71` | Exact Token Match | $\ge$ 109 | **109** | ✅ **VERIFIED** |
| `[ST]` | `t43` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[ST]` | `t44` | Exact Token Match | $\ge$ 119 | **119** | ✅ **VERIFIED** |
| `[ST]` | `⟨t43, t44⟩` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t44⟩` | Exact Token Match | $\ge$ 1 | **119** | ✅ **VERIFIED** |
| `[ST (in LOOP_6)]` | `t40` | Exact Token Match | $\ge$ 174 | **174** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t40⟩` | Exact Token Match | $\ge$ 174 | **174** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t36` | Exact Token Match | $\ge$ 358 | **358** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t46` | Exact Token Match | $\ge$ 360 | **360** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t47` | Exact Token Match | $\ge$ 115 | **115** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t37` | Exact Token Match | $\ge$ 53 | **53** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t47, τ⟩` | Exact Token Match | $\ge$ 62 | **115** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t47, t37⟩` | Exact Token Match | $\ge$ 53 | **53** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t46, τ⟩` | Exact Token Match | $\ge$ 245 | **360** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t46, t47, τ⟩` | Exact Token Match | $\ge$ 62 | **115** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t46, t47, t37⟩` | Exact Token Match | $\ge$ 53 | **53** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t46, t47⟩` | Exact Token Match | $\ge$ 115 | **115** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t36, t46, τ⟩` | Exact Token Match | $\ge$ 243 | **356** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t36, t46, t47, τ⟩` | Exact Token Match | $\ge$ 60 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t36, t46, t47, t37⟩` | Exact Token Match | $\ge$ 51 | **52** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨τ, t46⟩` | Exact Token Match | $\ge$ 2 | **360** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_5]` | Exact Token Match | $\ge$ 360 | **362** | ✅ **VERIFIED** |
| `[ST]` | `t48` | Exact Token Match | $\ge$ 63 | **63** | ✅ **VERIFIED** |
| `[ST]` | `t68` | Exact Token Match | $\ge$ 61 | **61** | ✅ **VERIFIED** |
| `[ST]` | `⟨t48, τ⟩` | Exact Token Match | $\ge$ 2 | **63** | ✅ **VERIFIED** |
| `[ST]` | `⟨t48, t68⟩` | Exact Token Match | $\ge$ 61 | **61** | ✅ **VERIFIED** |
| `[ST]` | `t56` | Exact Token Match | $\ge$ 115 | **115** | ✅ **VERIFIED** |
| `[ST]` | `t62` | Exact Token Match | $\ge$ 112 | **112** | ✅ **VERIFIED** |
| `[ST]` | `⟨t56, t62⟩` | Exact Token Match | $\ge$ 112 | **112** | ✅ **VERIFIED** |
| `[ST]` | `⟨t56, τ⟩` | Exact Token Match | $\ge$ 3 | **115** | ✅ **VERIFIED** |
| `[ST]` | `t69` | Exact Token Match | $\ge$ 144 | **144** | ✅ **VERIFIED** |
| `[ST]` | `t70` | Exact Token Match | $\ge$ 99 | **99** | ✅ **VERIFIED** |
| `[ST]` | `t65` | Exact Token Match | $\ge$ 359 | **359** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t65⟩` | Exact Token Match | $\ge$ 116 | **359** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t69, t65⟩` | Exact Token Match | $\ge$ 29 | **142** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, τ, t65⟩` | Exact Token Match | $\ge$ 1 | **359** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t69⟩` | Exact Token Match | $\ge$ 29 | **144** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t56, t62⟩` | Exact Token Match | $\ge$ 49 | **112** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t56⟩` | Exact Token Match | $\ge$ 52 | **115** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_5], τ⟩` | Exact Token Match | $\ge$ 1 | **362** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_5], τ, τ⟩` | Exact Token Match | $\ge$ 181 | **362** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_5], τ, t56, t62⟩` | Exact Token Match | $\ge$ 49 | **79** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_5], τ, t56⟩` | Exact Token Match | $\ge$ 52 | **81** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_5], τ⟩` | Exact Token Match | $\ge$ 296 | **362** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_5], t48, τ⟩` | Exact Token Match | $\ge$ 2 | **47** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_5], τ, τ⟩` | Exact Token Match | $\ge$ 62 | **362** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_5], τ⟩` | Exact Token Match | $\ge$ 177 | **362** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 241 | **362** | ✅ **VERIFIED** |
| `[ST]` | `⟨t43, t44, [nested PAR_5], τ⟩` | Exact Token Match | $\ge$ 54 | **118** | ✅ **VERIFIED** |
| `[ST]` | `⟨t43, t44, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t44, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 1 | **119** | ✅ **VERIFIED** |
| `[ST]` | `t55` | Exact Token Match | $\ge$ 471 | **471** | ✅ **VERIFIED** |
| `[ST]` | `⟨t71, t55⟩` | Exact Token Match | $\ge$ 109 | **109** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t55⟩` | Exact Token Match | $\ge$ 2 | **471** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_5], τ, t55⟩` | Exact Token Match | $\ge$ 1 | **361** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t69, t65, t55⟩` | Exact Token Match | $\ge$ 29 | **142** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, τ, t65, t55⟩` | Exact Token Match | $\ge$ 1 | **358** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t65, t55⟩` | Exact Token Match | $\ge$ 116 | **358** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t55⟩` | Exact Token Match | $\ge$ 1 | **471** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_3], τ, [nested PAR_5], τ⟩` | Exact Token Match | $\ge$ 63 | **362** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_3], τ, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 127 | **362** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_3], t43, t44, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 4 | **118** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_3], τ⟩` | Exact Token Match | $\ge$ 127 | **472** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_3], t43, t44⟩` | Exact Token Match | $\ge$ 4 | **118** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_3], t43⟩` | Exact Token Match | $\ge$ 4 | **118** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_3]⟩` | Exact Token Match | $\ge$ 124 | **472** | ✅ **VERIFIED** |
| `[ST]` | `⟨t22, [nested PAR_3]⟩` | Exact Token Match | $\ge$ 119 | **233** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], τ, [nested PAR_3]⟩` | Exact Token Match | $\ge$ 119 | **472** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], t22, [nested PAR_3]⟩` | Exact Token Match | $\ge$ 114 | **233** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], τ⟩` | Exact Token Match | $\ge$ 233 | **472** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], t22⟩` | Exact Token Match | $\ge$ 228 | **233** | ✅ **VERIFIED** |
| `[ST]` | `⟨t15, τ⟩` | Exact Token Match | $\ge$ 26 | **497** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t15⟩` | Exact Token Match | $\ge$ 160 | **497** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 111 | **959** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11⟩` | Exact Token Match | $\ge$ 183 | **222** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06, τ⟩` | Exact Token Match | $\ge$ 224 | **468** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06, t04⟩` | Exact Token Match | $\ge$ 196 | **222** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06⟩` | Exact Token Match | $\ge$ 461 | **468** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 81 | **959** | ✅ **VERIFIED** |
| `[ST]` | `⟨t06, t04⟩` | Exact Token Match | $\ge$ 237 | **229** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t16, t20⟩` | Exact Token Match | $\ge$ 113 | **110** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_1)]` | `⟨t24, t23⟩` | Exact Token Match | $\ge$ 230 | **229** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_1)]` | `⟨t21, t24, t23⟩` | Exact Token Match | $\ge$ 230 | **226** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_1)]` | `⟨t21, t24⟩` | Exact Token Match | $\ge$ 230 | **227** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_3)]` | `⟨t42, t39⟩` | Exact Token Match | $\ge$ 357 | **352** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_3)]` | `⟨t27, t28, t42, t39⟩` | Exact Token Match | $\ge$ 126 | **122** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_3)]` | `⟨t27, t28, t42⟩` | Exact Token Match | $\ge$ 126 | **124** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_3)]` | `⟨t28, t42, t39⟩` | Exact Token Match | $\ge$ 126 | **122** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨t36, t46, t47⟩` | Exact Token Match | $\ge$ 113 | **112** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨t36, t46⟩` | Exact Token Match | $\ge$ 358 | **356** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t69, t65⟩` | Exact Token Match | $\ge$ 144 | **142** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t70, t65⟩` | Exact Token Match | $\ge$ 99 | **98** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_5], t48, t68⟩` | Exact Token Match | $\ge$ 61 | **45** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_5], t48⟩` | Exact Token Match | $\ge$ 63 | **47** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t69, t65, t55⟩` | Exact Token Match | $\ge$ 144 | **142** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t70, t65, t55⟩` | Exact Token Match | $\ge$ 99 | **97** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t65, t55⟩` | Exact Token Match | $\ge$ 359 | **358** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t15, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 115 | **113** | ⚠️ **DISCREPANCY** |

## Audit Summary
- **Perfect Pattern Verifications:** 123
- **Frequency Discrepancies:** 19
- **Ghost Patterns (Fatal):** 0
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 11.10%
- **Tree Exposure (Strict, Fragment-Level % of N):** 46.62%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 24.54%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 100.00%
- **Total Forced Volume (incl. unresolved AS, % of N):** 11.10%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 0.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 99.65%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 99.79%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 99.74%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 55.15%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 100.00%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 100.00%
- **Max Fractional Exposure (Worst-Case Normalized):** 13.64% (expected length: 132.35 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 46.62% (expected length: 9.47 events)
- **Mean Absolute Exposure Volume:** 1.53 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_2]`
- **Internal Structure:** `(t17 ∗ τ)`
- **Block Frequency:** 466

- **Max Loop Iterations:** `123`
- **Max Sub-Sequence Length:** `247` steps (if one case consumes all iterations)

![nested LOOP_2 Internal Diagram](images/nested_ref_audit_pdc2021_0011012__noise0.4_nested_LOOP_2.png)

### `[nested PAR_1]`
- **Internal Structure:** `{(t17 ∗ τ), ⟨t21, [⟨[τ │ t24], [τ │ t23]⟩ │ τ]⟩}`
- **Block Frequency:** 466



![nested PAR_1 Internal Diagram](images/nested_ref_audit_pdc2021_0011012__noise0.4_nested_PAR_1.png)

### `[nested LOOP_4]`
- **Internal Structure:** `(t34 ∗ τ)`
- **Block Frequency:** 356

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_4 Internal Diagram](images/nested_ref_audit_pdc2021_0011012__noise0.4_nested_LOOP_4.png)

### `[nested PAR_3]`
- **Internal Structure:** `{[(t34 ∗ τ) │ τ], ⟨[τ │ t26], [τ │ ⟨t27, [τ │ t28]⟩], t42, t39⟩}`
- **Block Frequency:** 357



![nested PAR_3 Internal Diagram](images/nested_ref_audit_pdc2021_0011012__noise0.4_nested_PAR_3.png)

### `[nested LOOP_6]`
- **Internal Structure:** `(t40 ∗ τ)`
- **Block Frequency:** 174

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_6 Internal Diagram](images/nested_ref_audit_pdc2021_0011012__noise0.4_nested_LOOP_6.png)

### `[nested PAR_5]`
- **Internal Structure:** `{[τ │ (t40 ∗ τ)], ⟨[t36 │ τ], t46, [τ │ ⟨t47, [τ │ t37]⟩]⟩}`
- **Block Frequency:** 360



![nested PAR_5 Internal Diagram](images/nested_ref_audit_pdc2021_0011012__noise0.4_nested_PAR_5.png)
