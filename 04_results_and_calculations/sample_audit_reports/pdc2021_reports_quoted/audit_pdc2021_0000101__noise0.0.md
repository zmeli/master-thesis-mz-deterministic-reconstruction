# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_0000101.xes` |
| **Noise Threshold** | `0.0` |
| **Fitness** | `0.9940101979002978` |
| **Precision** | `0.13960232396750738` |
| **Total Cases in Log** | `1000` |
| **Unique Activities** | `50` |
| **XOR Operators** | `61` |
| **LOOP Operators** | `10` |
| **SEQ Operators** | `23` |
| **PAR Operators** | `12` |
| **Binarization Additions** | `12` |
| **Tau Operators Added** | `60` |
| **Total Found Patterns** | `226` |
| **Verified Patterns** | `97` |
| **Discrepancy Patterns** | `13` |
| **Ghost Patterns** | `22` |
| **Nested LOOPs** | `10` |
| **Nested PARs** | `12` |
| **Tree Exposure (Strict, End-to-End % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `0.00%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `3.95%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `0.10%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `0.10%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `82.10%` |
| **Data Exposure, ST-only (% confirmed)** | `0.00%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `100.00%` |
| **Data Coverage, ST-only (% of real log)** | `0.00%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `54.21%` |
| **Data Coverage, Total (% of real log)** | `100.00%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `0.10%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `0.10%` |
| **Mean Absolute Exposure Volume (events/case)** | `0.09` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_0000101__noise0.0.png)


```text
*( X( 't01', ->( X( tau, 't06' ), X( 't02', ->( X( tau, 't04', *( ->( X( 't30', 't11', 't09', 't10' ), X( tau, +( X( tau, 't14' ), ->( X( tau, ->( 't15', 't13' ) ), *( ->( X( tau, ->( X( tau, 't16' ), +( X( tau, 't21' ), ->( X( tau, 't22', 't19', ->( +( X( tau, *( 't27', tau ) ), ->( X( tau, 't24' ), +( X( tau, 't71' ), X( tau, 't23' ), X( tau, 't29' ) ), X( tau, ->( X( tau, 't25' ), 't26' ) ) ) ), X( tau, 't28' ) ) ), X( tau, +( X( tau, 't36' ), ->( +( X( tau, 't62' ), ->( X( tau, ->( *( ->( X( tau, 't20' ), +( X( tau, 't17' ), X( tau, ->( X( tau, *( 't42', tau ) ), X( 't38', ->( X( tau, 't39' ), X( tau, 't43' ) ) ) ) ) ) ), tau ), X( tau, 't44', 't34' ) ) ), X( tau, ->( X( tau, 't33' ), +( X( tau, 't46' ), X( tau, ->( X( tau, 't69', 't70' ), +( X( tau, *( 't68', tau ) ), ->( X( tau, *( ->( X( tau, 't47' ), X( tau, +( X( tau, 't45' ), X( tau, 't37' ) ) ), X( 't48', 't60', 't64' ) ), tau ) ), X( tau, 't65' ) ) ) ) ) ) ) ) ) ), X( tau, 't40' ) ) ) ) ) ) ) ), X( tau, 't66' ) ), tau ) ) ) ) ), tau ) ), X( tau, 't03', +( X( tau, *( 't08', tau ) ), X( tau, *( 't05', tau ) ) ) ) ) ) ) ), tau )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_0000101__noise0.0.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST (in LOOP_1)]` | `t01` | Exact Token Match | $\ge$ 215 | **215** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `t06` | Exact Token Match | $\ge$ 189 | **189** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `t02` | Exact Token Match | $\ge$ 513 | **513** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `t04` | Exact Token Match | $\ge$ 194 | **194** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `t30` | Exact Token Match | $\ge$ 60 | **60** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `t11` | Exact Token Match | $\ge$ 195 | **195** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `t09` | Exact Token Match | $\ge$ 1003 | **1003** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `t10` | Exact Token Match | $\ge$ 997 | **997** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `t14` | Exact Token Match | $\ge$ 194 | **194** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `t15` | Exact Token Match | $\ge$ 58 | **58** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `t13` | Exact Token Match | $\ge$ 58 | **58** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t15, t13⟩` | Exact Token Match | $\ge$ 58 | **58** | ✅ **VERIFIED** |
| `[ST (in LOOP_4)]` | `t16` | Exact Token Match | $\ge$ 69 | **69** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t21` | Exact Token Match | $\ge$ 385 | **385** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t22` | Exact Token Match | $\ge$ 126 | **126** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t19` | Exact Token Match | $\ge$ 193 | **193** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `t27` | Exact Token Match | $\ge$ 113 | **113** | ✅ **VERIFIED** |
| `[ST (in PAR_6)]` | `⟨t27⟩` | Exact Token Match | $\ge$ 113 | **113** | ✅ **VERIFIED** |
| `[ST (in PAR_6)]` | `t24` | Exact Token Match | $\ge$ 113 | **113** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `t71` | Exact Token Match | $\ge$ 63 | **63** | ✅ **VERIFIED** |
| `[ST (in PAR_9)]` | `t23` | Exact Token Match | $\ge$ 112 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_9)]` | `t29` | Exact Token Match | $\ge$ 112 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_6)]` | `t25` | Exact Token Match | $\ge$ 57 | **57** | ✅ **VERIFIED** |
| `[ST (in PAR_6)]` | `t26` | Exact Token Match | $\ge$ 113 | **113** | ✅ **VERIFIED** |
| `[ST (in PAR_6)]` | `⟨τ, t26⟩` | Exact Token Match | $\ge$ 56 | **113** | ✅ **VERIFIED** |
| `[ST (in PAR_6)]` | `⟨t25, t26⟩` | Exact Token Match | $\ge$ 57 | **57** | ✅ **VERIFIED** |
| `[ST (in PAR_6)]` | `⟨[nested PAR_8], τ, t26⟩` | Exact Token Match | $\ge$ 55 | **60** | ✅ **VERIFIED** |
| `[ST (in PAR_6)]` | `⟨[nested PAR_8], τ⟩` | Exact Token Match | $\ge$ 55 | **60** | ✅ **VERIFIED** |
| `[ST (in PAR_6)]` | `⟨t24, [nested PAR_8], τ, t26⟩` | Exact Token Match | $\ge$ 55 | **60** | ✅ **VERIFIED** |
| `[ST (in PAR_6)]` | `⟨t24, [nested PAR_8], τ⟩` | Exact Token Match | $\ge$ 55 | **60** | ✅ **VERIFIED** |
| `[ST (in PAR_6)]` | `⟨t24, τ⟩` | Exact Token Match | $\ge$ 1 | **113** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t28` | Exact Token Match | $\ge$ 52 | **52** | ✅ **VERIFIED** |
| `[ST (in PAR_10)]` | `t36` | Exact Token Match | $\ge$ 325 | **325** | ✅ **VERIFIED** |
| `[ST (in PAR_11)]` | `t62` | Exact Token Match | $\ge$ 168 | **168** | ✅ **VERIFIED** |
| `[ST (in LOOP_12)]` | `t20` | Exact Token Match | $\ge$ 328 | **328** | ✅ **VERIFIED** |
| `[ST (in PAR_13)]` | `t17` | Exact Token Match | $\ge$ 329 | **329** | ✅ **VERIFIED** |
| `[ST (in LOOP_14)]` | `t42` | Exact Token Match | $\ge$ 326 | **326** | ✅ **VERIFIED** |
| `[ST (in PAR_13)]` | `⟨t42⟩` | Exact Token Match | $\ge$ 326 | **326** | ✅ **VERIFIED** |
| `[ST (in PAR_13)]` | `t38` | Exact Token Match | $\ge$ 324 | **324** | ✅ **VERIFIED** |
| `[ST (in PAR_13)]` | `t39` | Exact Token Match | $\ge$ 327 | **327** | ✅ **VERIFIED** |
| `[ST (in PAR_13)]` | `t43` | Exact Token Match | $\ge$ 91 | **91** | ✅ **VERIFIED** |
| `[ST (in PAR_13)]` | `⟨t39, τ⟩` | Exact Token Match | $\ge$ 236 | **327** | ✅ **VERIFIED** |
| `[ST (in PAR_13)]` | `⟨t39, t43⟩` | Exact Token Match | $\ge$ 91 | **91** | ✅ **VERIFIED** |
| `[ST (in PAR_13)]` | `⟨τ, t39⟩` | Exact Token Match | $\ge$ 1 | **327** | ✅ **VERIFIED** |
| `[ST (in PAR_13)]` | `⟨t42, t39⟩` | Exact Token Match | $\ge$ 2 | **325** | ✅ **VERIFIED** |
| `[AS (in LOOP_12)]` | `[nested PAR_13]` | Exact Token Match | $\ge$ 651 | **703** | ✅ **VERIFIED** |
| `[ST (in LOOP_12)]` | `⟨τ, [nested PAR_13]⟩` | Exact Token Match | $\ge$ 323 | **703** | ✅ **VERIFIED** |
| `[ST (in LOOP_12)]` | `⟨t20, [nested PAR_13]⟩` | Exact Token Match | $\ge$ 328 | **328** | ✅ **VERIFIED** |
| `[AS (in PAR_11)]` | `[nested LOOP_12]` | Exact Token Match | $\ge$ 1 | **73** | ✅ **VERIFIED** |
| `[ST (in PAR_11)]` | `t44` | Exact Token Match | $\ge$ 91 | **91** | ✅ **VERIFIED** |
| `[ST (in PAR_11)]` | `t34` | Exact Token Match | $\ge$ 70 | **70** | ✅ **VERIFIED** |
| `[ST (in PAR_11)]` | `t33` | Exact Token Match | $\ge$ 325 | **325** | ✅ **VERIFIED** |
| `[ST (in PAR_15)]` | `t46` | Exact Token Match | $\ge$ 325 | **325** | ✅ **VERIFIED** |
| `[ST (in PAR_15)]` | `t69` | Exact Token Match | $\ge$ 88 | **88** | ✅ **VERIFIED** |
| `[ST (in PAR_15)]` | `t70` | Exact Token Match | $\ge$ 70 | **70** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `t68` | Exact Token Match | $\ge$ 167 | **167** | ✅ **VERIFIED** |
| `[ST (in PAR_16)]` | `⟨t68⟩` | Exact Token Match | $\ge$ 167 | **167** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `t47` | Exact Token Match | $\ge$ 81 | **81** | ✅ **VERIFIED** |
| `[ST (in PAR_19)]` | `t45` | Exact Token Match | $\ge$ 165 | **165** | ✅ **VERIFIED** |
| `[ST (in PAR_19)]` | `t37` | Exact Token Match | $\ge$ 166 | **166** | ✅ **VERIFIED** |
| `[AS (in LOOP_18)]` | `[nested PAR_19]` | Exact Token Match | $\ge$ 166 | **167** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `t48` | Exact Token Match | $\ge$ 168 | **168** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `t60` | Exact Token Match | $\ge$ 167 | **167** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `t64` | Exact Token Match | $\ge$ 167 | **167** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `⟨τ, t48⟩` | Exact Token Match | $\ge$ 2 | **168** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `⟨τ, t60⟩` | Exact Token Match | $\ge$ 1 | **167** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `⟨τ, t64⟩` | Exact Token Match | $\ge$ 1 | **167** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `⟨τ, [nested PAR_19]⟩` | Exact Token Match | $\ge$ 85 | **167** | ✅ **VERIFIED** |
| `[ST (in PAR_16)]` | `t65` | Exact Token Match | $\ge$ 326 | **326** | ✅ **VERIFIED** |
| `[ST (in PAR_11)]` | `⟨τ, t33⟩` | Exact Token Match | $\ge$ 164 | **325** | ✅ **VERIFIED** |
| `[ST (in PAR_10)]` | `t40` | Exact Token Match | $\ge$ 82 | **82** | ✅ **VERIFIED** |
| `[ST (in LOOP_4)]` | `⟨t16, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 69 | **69** | ✅ **VERIFIED** |
| `[ST (in LOOP_4)]` | `t66` | Exact Token Match | $\ge$ 386 | **386** | ✅ **VERIFIED** |
| `[ST (in LOOP_4)]` | `⟨τ, [nested PAR_5], τ⟩` | Exact Token Match | $\ge$ 47 | **387** | ✅ **VERIFIED** |
| `[ST (in LOOP_4)]` | `⟨τ, [nested PAR_5], t66⟩` | Exact Token Match | $\ge$ 317 | **386** | ✅ **VERIFIED** |
| `[ST (in LOOP_4)]` | `⟨[nested PAR_5], τ⟩` | Exact Token Match | $\ge$ 116 | **387** | ✅ **VERIFIED** |
| `[ST (in LOOP_4)]` | `⟨[nested PAR_5], t66⟩` | Exact Token Match | $\ge$ 386 | **386** | ✅ **VERIFIED** |
| `[AS (in LOOP_2)]` | `[nested PAR_3]` | Exact Token Match | $\ge$ 194 | **387** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `⟨t11, τ⟩` | Exact Token Match | $\ge$ 1 | **195** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `⟨t09, τ⟩` | Exact Token Match | $\ge$ 809 | **1003** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 803 | **997** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `t03` | Exact Token Match | $\ge$ 92 | **92** | ✅ **VERIFIED** |
| `[ST (in LOOP_21)]` | `t08` | Exact Token Match | $\ge$ 99 | **99** | ✅ **VERIFIED** |
| `[ST (in PAR_20)]` | `⟨t08⟩` | Exact Token Match | $\ge$ 99 | **99** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `t05` | Exact Token Match | $\ge$ 99 | **99** | ✅ **VERIFIED** |
| `[ST (in PAR_20)]` | `⟨t05⟩` | Exact Token Match | $\ge$ 99 | **99** | ✅ **VERIFIED** |
| `[AS (in LOOP_1)]` | `[nested PAR_20]` | Exact Token Match | $\ge$ 99 | **103** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `⟨t04, τ⟩` | Exact Token Match | $\ge$ 3 | **194** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `⟨t09, τ, τ⟩` | Exact Token Match | $\ge$ 618 | **1003** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `⟨t10, τ, τ⟩` | Exact Token Match | $\ge$ 612 | **997** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `⟨τ, t02⟩` | Exact Token Match | $\ge$ 324 | **513** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `⟨τ, t09, τ, τ⟩` | Exact Token Match | $\ge$ 429 | **1003** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `⟨τ, t10, τ, τ⟩` | Exact Token Match | $\ge$ 423 | **997** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `⟨τ, t04⟩` | Exact Token Match | $\ge$ 5 | **194** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `⟨τ, t09, τ⟩` | Exact Token Match | $\ge$ 620 | **1003** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `⟨τ, t10, τ⟩` | Exact Token Match | $\ge$ 614 | **997** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_1]` | Exact Token Match | $\ge$ 1 | **1000** | ✅ **VERIFIED** |
| `[AS (in PAR_8)]` | `[nested PAR_9]` | Exact Token Match | $\ge$ 112 | **111** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_6)]` | `[nested PAR_8]` | Exact Token Match | $\ge$ 112 | **60** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_6)]` | `⟨[nested PAR_8], t25, t26⟩` | Exact Token Match | $\ge$ 56 | **27** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_6)]` | `⟨[nested PAR_8], t25⟩` | Exact Token Match | $\ge$ 56 | **27** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_6)]` | `⟨t24, [nested PAR_8], t25, t26⟩` | Exact Token Match | $\ge$ 56 | **27** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_6)]` | `⟨t24, [nested PAR_8], t25⟩` | Exact Token Match | $\ge$ 56 | **27** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_6)]` | `⟨t24, [nested PAR_8]⟩` | Exact Token Match | $\ge$ 112 | **60** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_5)]` | `[nested PAR_6]` | Exact Token Match | $\ge$ 113 | **27** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨[nested PAR_6], τ⟩` | Exact Token Match | $\ge$ 61 | **27** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_15)]` | `[nested PAR_16]` | Exact Token Match | $\ge$ 502 | **79** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_15)]` | `⟨τ, [nested PAR_16]⟩` | Exact Token Match | $\ge$ 344 | **79** | ⚠️ **DISCREPANCY** |
| `[AS (in LOOP_4)]` | `[nested PAR_5]` | Exact Token Match | $\ge$ 502 | **387** | ⚠️ **DISCREPANCY** |
| `[ST (in LOOP_4)]` | `⟨τ, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 433 | **387** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨[nested PAR_6], t28⟩` | Exact Token Match | $\ge$ 52 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_15)]` | `⟨t69, [nested PAR_16]⟩` | Exact Token Match | $\ge$ 88 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_15)]` | `⟨t70, [nested PAR_16]⟩` | Exact Token Match | $\ge$ 70 | **0** | ❌ **GHOST PATTERN** |
| `[AS (in PAR_11)]` | `[nested PAR_15]` | Exact Token Match | $\ge$ 502 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_11)]` | `⟨τ, [nested PAR_15]⟩` | Exact Token Match | $\ge$ 177 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_11)]` | `⟨t33, [nested PAR_15]⟩` | Exact Token Match | $\ge$ 325 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_11)]` | `⟨τ, τ, [nested PAR_15]⟩` | Exact Token Match | $\ge$ 16 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_11)]` | `⟨τ, t33, [nested PAR_15]⟩` | Exact Token Match | $\ge$ 164 | **0** | ❌ **GHOST PATTERN** |
| `[AS (in PAR_10)]` | `[nested PAR_11]` | Exact Token Match | $\ge$ 502 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_10)]` | `⟨[nested PAR_11], τ⟩` | Exact Token Match | $\ge$ 420 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_10)]` | `⟨[nested PAR_11], t40⟩` | Exact Token Match | $\ge$ 82 | **0** | ❌ **GHOST PATTERN** |
| `[AS (in PAR_5)]` | `[nested PAR_10]` | Exact Token Match | $\ge$ 502 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_5)]` | `⟨τ, [nested PAR_10]⟩` | Exact Token Match | $\ge$ 70 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_5)]` | `⟨t22, [nested PAR_10]⟩` | Exact Token Match | $\ge$ 126 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_5)]` | `⟨t19, [nested PAR_10]⟩` | Exact Token Match | $\ge$ 193 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_5)]` | `⟨[nested PAR_6], τ, [nested PAR_10]⟩` | Exact Token Match | $\ge$ 61 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_5)]` | `⟨[nested PAR_6], t28, [nested PAR_10]⟩` | Exact Token Match | $\ge$ 52 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_5)]` | `⟨τ, [nested PAR_10]⟩` | Exact Token Match | $\ge$ 61 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_5)]` | `⟨t28, [nested PAR_10]⟩` | Exact Token Match | $\ge$ 52 | **0** | ❌ **GHOST PATTERN** |
| `[AS (in PAR_3)]` | `[nested LOOP_4]` | Exact Token Match | $\ge$ 1 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_3)]` | `⟨t15, t13, [nested LOOP_4]⟩` | Exact Token Match | $\ge$ 1 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_3)]` | `⟨t13, [nested LOOP_4]⟩` | Exact Token Match | $\ge$ 1 | **0** | ❌ **GHOST PATTERN** |

## Audit Summary
- **Perfect Pattern Verifications:** 97
- **Frequency Discrepancies:** 13
- **Ghost Patterns (Fatal):** 22
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 0.00%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 3.95%
- **Total Forced Volume (incl. unresolved AS, % of N):** 0.10%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 0.10%
- **Data Exposure (Confirmed % of Claimed Volume):** 82.10%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 0.00%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 100.00%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 0.00%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 54.21%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 100.00%
- **Max Fractional Exposure (Worst-Case Normalized):** 0.10% (expected length: 4663.98 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 0.10% (expected length: 10.54 events)
- **Mean Absolute Exposure Volume:** 0.09 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_7]`
- **Internal Structure:** `(t27 ∗ τ)`
- **Block Frequency:** 113

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_7 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_7.png)

### `[nested PAR_9]`
- **Internal Structure:** `{[τ │ t23], [τ │ t29]}`
- **Block Frequency:** 112



![nested PAR_9 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_PAR_9.png)

### `[nested PAR_8]`
- **Internal Structure:** `{[τ │ t71], [τ │ t23], [τ │ t29]}`
- **Block Frequency:** 112



![nested PAR_8 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_PAR_8.png)

### `[nested PAR_6]`
- **Internal Structure:** `{[τ │ (t27 ∗ τ)], ⟨[τ │ t24], [{[τ │ t71], [τ │ t23], [τ │ t29]} │ τ], [τ │ ⟨[τ │ t25], t26⟩]⟩}`
- **Block Frequency:** 113



![nested PAR_6 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_PAR_6.png)

### `[nested LOOP_14]`
- **Internal Structure:** `(t42 ∗ τ)`
- **Block Frequency:** 326

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_14 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_14.png)

### `[nested PAR_13]`
- **Internal Structure:** `{[τ │ t17], [τ │ ⟨[τ │ (t42 ∗ τ)], [t38 │ ⟨[τ │ t39], [τ │ t43]⟩]⟩]}`
- **Block Frequency:** 651



![nested PAR_13 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_PAR_13.png)

### `[nested LOOP_12]`
- **Internal Structure:** `(⟨[τ │ t20], {[τ │ t17], [τ │ ⟨[τ │ (t42 ∗ τ)], [t38 │ ⟨[τ │ t39], [τ │ t43]⟩]⟩]}⟩ ∗ τ)`
- **Block Frequency:** 161

- **Max Loop Iterations:** `490`
- **Max Sub-Sequence Length:** `981` steps (if one case consumes all iterations)

![nested LOOP_12 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_12.png)

### `[nested LOOP_17]`
- **Internal Structure:** `(t68 ∗ τ)`
- **Block Frequency:** 167

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_17 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_17.png)

### `[nested PAR_19]`
- **Internal Structure:** `{[τ │ t45], [τ │ t37]}`
- **Block Frequency:** 166



![nested PAR_19 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_PAR_19.png)

### `[nested LOOP_18]`
- **Internal Structure:** `(⟨[τ │ t47], [τ │ {[τ │ t45], [τ │ t37]}], [t48 │ t60 │ t64]⟩ ∗ τ)`
- **Block Frequency:** 502

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_18 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_18.png)

### `[nested PAR_16]`
- **Internal Structure:** `{[τ │ (t68 ∗ τ)], ⟨[τ │ (⟨[τ │ t47], [τ │ {[τ │ t45], [τ │ t37]}], [t48 │ t60 │ t64]⟩ ∗ τ)], [τ │ t65]⟩}`
- **Block Frequency:** 502



![nested PAR_16 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_PAR_16.png)

### `[nested PAR_15]`
- **Internal Structure:** `{[τ │ t46], [τ │ ⟨[τ │ t69 │ t70], {[τ │ (t68 ∗ τ)], ⟨[τ │ (⟨[τ │ t47], [τ │ {[τ │ t45], [τ │ t37]}], [t48 │ t60 │ t64]⟩ ∗ τ)], [τ │ t65]⟩}⟩]}`
- **Block Frequency:** 502



![nested PAR_15 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_PAR_15.png)

### `[nested PAR_11]`
- **Internal Structure:** `{[τ │ t62], ⟨[τ │ ⟨(⟨[τ │ t20], {[τ │ t17], [τ │ ⟨[τ │ (t42 ∗ τ)], [t38 │ ⟨[τ │ t39], [τ │ t43]⟩]⟩]}⟩ ∗ τ), [τ │ t44 │ t34]⟩], [τ │ ⟨[τ │ t33], {[τ │ t46], [τ │ ⟨[τ │ t69 │ t70], {[τ │ (t68 ∗ τ)], ⟨[τ │ (⟨[τ │ t47], [τ │ {[τ │ t45], [τ │ t37]}], [t48 │ t60 │ t64]⟩ ∗ τ)], [τ │ t65]⟩}⟩]}⟩]⟩}`
- **Block Frequency:** 502



![nested PAR_11 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_PAR_11.png)

### `[nested PAR_10]`
- **Internal Structure:** `{[τ │ t36], ⟨{[τ │ t62], ⟨[τ │ ⟨(⟨[τ │ t20], {[τ │ t17], [τ │ ⟨[τ │ (t42 ∗ τ)], [t38 │ ⟨[τ │ t39], [τ │ t43]⟩]⟩]}⟩ ∗ τ), [τ │ t44 │ t34]⟩], [τ │ ⟨[τ │ t33], {[τ │ t46], [τ │ ⟨[τ │ t69 │ t70], {[τ │ (t68 ∗ τ)], ⟨[τ │ (⟨[τ │ t47], [τ │ {[τ │ t45], [τ │ t37]}], [t48 │ t60 │ t64]⟩ ∗ τ)], [τ │ t65]⟩}⟩]}⟩]⟩}, [τ │ t40]⟩}`
- **Block Frequency:** 502



![nested PAR_10 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_PAR_10.png)

### `[nested PAR_5]`
- **Internal Structure:** `{[τ │ t21], ⟨[τ │ t22 │ t19 │ ⟨{[τ │ (t27 ∗ τ)], ⟨[τ │ t24], [{[τ │ t71], [τ │ t23], [τ │ t29]} │ τ], [τ │ ⟨[τ │ t25], t26⟩]⟩}, [τ │ t28]⟩], [τ │ {[τ │ t36], ⟨{[τ │ t62], ⟨[τ │ ⟨(⟨[τ │ t20], {[τ │ t17], [τ │ ⟨[τ │ (t42 ∗ τ)], [t38 │ ⟨[τ │ t39], [τ │ t43]⟩]⟩]}⟩ ∗ τ), [τ │ t44 │ t34]⟩], [τ │ ⟨[τ │ t33], {[τ │ t46], [τ │ ⟨[τ │ t69 │ t70], {[τ │ (t68 ∗ τ)], ⟨[τ │ (⟨[τ │ t47], [τ │ {[τ │ t45], [τ │ t37]}], [t48 │ t60 │ t64]⟩ ∗ τ)], [τ │ t65]⟩}⟩]}⟩]⟩}, [τ │ t40]⟩}]⟩}`
- **Block Frequency:** 502



![nested PAR_5 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_PAR_5.png)

### `[nested LOOP_4]`
- **Internal Structure:** `(⟨[τ │ ⟨[τ │ t16], {[τ │ t21], ⟨[τ │ t22 │ t19 │ ⟨{[τ │ (t27 ∗ τ)], ⟨[τ │ t24], [{[τ │ t71], [τ │ t23], [τ │ t29]} │ τ], [τ │ ⟨[τ │ t25], t26⟩]⟩}, [τ │ t28]⟩], [τ │ {[τ │ t36], ⟨{[τ │ t62], ⟨[τ │ ⟨(⟨[τ │ t20], {[τ │ t17], [τ │ ⟨[τ │ (t42 ∗ τ)], [t38 │ ⟨[τ │ t39], [τ │ t43]⟩]⟩]}⟩ ∗ τ), [τ │ t44 │ t34]⟩], [τ │ ⟨[τ │ t33], {[τ │ t46], [τ │ ⟨[τ │ t69 │ t70], {[τ │ (t68 ∗ τ)], ⟨[τ │ (⟨[τ │ t47], [τ │ {[τ │ t45], [τ │ t37]}], [t48 │ t60 │ t64]⟩ ∗ τ)], [τ │ t65]⟩}⟩]}⟩]⟩}, [τ │ t40]⟩}]⟩}⟩], [τ │ t66]⟩ ∗ τ)`
- **Block Frequency:** 58

- **Max Loop Iterations:** `444`
- **Max Sub-Sequence Length:** `889` steps (if one case consumes all iterations)

![nested LOOP_4 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_4.png)

### `[nested PAR_3]`
- **Internal Structure:** `{[τ │ t14], [⟨[τ │ ⟨t15, t13⟩], (⟨[τ │ ⟨[τ │ t16], {[τ │ t21], ⟨[τ │ t22 │ t19 │ ⟨{[τ │ (t27 ∗ τ)], ⟨[τ │ t24], [{[τ │ t71], [τ │ t23], [τ │ t29]} │ τ], [τ │ ⟨[τ │ t25], t26⟩]⟩}, [τ │ t28]⟩], [τ │ {[τ │ t36], ⟨{[τ │ t62], ⟨[τ │ ⟨(⟨[τ │ t20], {[τ │ t17], [τ │ ⟨[τ │ (t42 ∗ τ)], [t38 │ ⟨[τ │ t39], [τ │ t43]⟩]⟩]}⟩ ∗ τ), [τ │ t44 │ t34]⟩], [τ │ ⟨[τ │ t33], {[τ │ t46], [τ │ ⟨[τ │ t69 │ t70], {[τ │ (t68 ∗ τ)], ⟨[τ │ (⟨[τ │ t47], [τ │ {[τ │ t45], [τ │ t37]}], [t48 │ t60 │ t64]⟩ ∗ τ)], [τ │ t65]⟩}⟩]}⟩]⟩}, [τ │ t40]⟩}]⟩}⟩], [τ │ t66]⟩ ∗ τ)⟩ │ τ]}`
- **Block Frequency:** 194



![nested PAR_3 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_PAR_3.png)

### `[nested LOOP_2]`
- **Internal Structure:** `(⟨[t30 │ t11 │ t09 │ t10], [τ │ {[τ │ t14], [⟨[τ │ ⟨t15, t13⟩], (⟨[τ │ ⟨[τ │ t16], {[τ │ t21], ⟨[τ │ t22 │ t19 │ ⟨{[τ │ (t27 ∗ τ)], ⟨[τ │ t24], [{[τ │ t71], [τ │ t23], [τ │ t29]} │ τ], [τ │ ⟨[τ │ t25], t26⟩]⟩}, [τ │ t28]⟩], [τ │ {[τ │ t36], ⟨{[τ │ t62], ⟨[τ │ ⟨(⟨[τ │ t20], {[τ │ t17], [τ │ ⟨[τ │ (t42 ∗ τ)], [t38 │ ⟨[τ │ t39], [τ │ t43]⟩]⟩]}⟩ ∗ τ), [τ │ t44 │ t34]⟩], [τ │ ⟨[τ │ t33], {[τ │ t46], [τ │ ⟨[τ │ t69 │ t70], {[τ │ (t68 ∗ τ)], ⟨[τ │ (⟨[τ │ t47], [τ │ {[τ │ t45], [τ │ t37]}], [t48 │ t60 │ t64]⟩ ∗ τ)], [τ │ t65]⟩}⟩]}⟩]⟩}, [τ │ t40]⟩}]⟩}⟩], [τ │ t66]⟩ ∗ τ)⟩ │ τ]}]⟩ ∗ τ)`
- **Block Frequency:** 2255

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_2 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_2.png)

### `[nested LOOP_21]`
- **Internal Structure:** `(t08 ∗ τ)`
- **Block Frequency:** 99

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_21 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_21.png)

### `[nested LOOP_22]`
- **Internal Structure:** `(t05 ∗ τ)`
- **Block Frequency:** 99

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_22 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_22.png)

### `[nested PAR_20]`
- **Internal Structure:** `{[τ │ (t08 ∗ τ)], [τ │ (t05 ∗ τ)]}`
- **Block Frequency:** 99



![nested PAR_20 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_PAR_20.png)

### `[nested LOOP_1]`
- **Internal Structure:** `([t01 │ ⟨[τ │ t06], [t02 │ ⟨[τ │ t04 │ (⟨[t30 │ t11 │ t09 │ t10], [τ │ {[τ │ t14], [⟨[τ │ ⟨t15, t13⟩], (⟨[τ │ ⟨[τ │ t16], {[τ │ t21], ⟨[τ │ t22 │ t19 │ ⟨{[τ │ (t27 ∗ τ)], ⟨[τ │ t24], [{[τ │ t71], [τ │ t23], [τ │ t29]} │ τ], [τ │ ⟨[τ │ t25], t26⟩]⟩}, [τ │ t28]⟩], [τ │ {[τ │ t36], ⟨{[τ │ t62], ⟨[τ │ ⟨(⟨[τ │ t20], {[τ │ t17], [τ │ ⟨[τ │ (t42 ∗ τ)], [t38 │ ⟨[τ │ t39], [τ │ t43]⟩]⟩]}⟩ ∗ τ), [τ │ t44 │ t34]⟩], [τ │ ⟨[τ │ t33], {[τ │ t46], [τ │ ⟨[τ │ t69 │ t70], {[τ │ (t68 ∗ τ)], ⟨[τ │ (⟨[τ │ t47], [τ │ {[τ │ t45], [τ │ t37]}], [t48 │ t60 │ t64]⟩ ∗ τ)], [τ │ t65]⟩}⟩]}⟩]⟩}, [τ │ t40]⟩}]⟩}⟩], [τ │ t66]⟩ ∗ τ)⟩ │ τ]}]⟩ ∗ τ)], [τ │ t03 │ {[τ │ (t08 ∗ τ)], [τ │ (t05 ∗ τ)]}]⟩]⟩] ∗ τ)`
- **Block Frequency:** 1000

- **Max Loop Iterations:** `2177`
- **Max Sub-Sequence Length:** `4355` steps (if one case consumes all iterations)

![nested LOOP_1 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_1.png)
