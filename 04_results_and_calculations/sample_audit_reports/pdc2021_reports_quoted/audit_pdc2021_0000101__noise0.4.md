# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_0000101.xes` |
| **Noise Threshold** | `0.4` |
| **Fitness** | `0.9301438347705243` |
| **Precision** | `0.7076810176125244` |
| **Total Cases in Log** | `1000` |
| **Unique Activities** | `50` |
| **XOR Operators** | `38` |
| **LOOP Operators** | `13` |
| **SEQ Operators** | `33` |
| **PAR Operators** | `8` |
| **Binarization Additions** | `26` |
| **Tau Operators Added** | `29` |
| **Total Found Patterns** | `370` |
| **Verified Patterns** | `224` |
| **Discrepancy Patterns** | `35` |
| **Ghost Patterns** | `5` |
| **Nested LOOPs** | `13` |
| **Nested PARs** | `8` |
| **Tree Exposure (Strict, End-to-End % of N)** | `20.30%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `40.92%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `11.16%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `100.00%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `40.30%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `20.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `99.22%` |
| **Data Exposure, ST-only (% confirmed)** | `99.40%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `99.77%` |
| **Data Coverage, ST-only (% of real log)** | `39.07%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `99.25%` |
| **Data Coverage, Total (% of real log)** | `99.94%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `52.04%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `100.00%` |
| **Mean Absolute Exposure Volume (events/case)** | `7.53` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_0000101__noise0.4.png)


```text
->( *( 't09', tau ), *( 't10', tau ), X( +( *( 't02', tau ), X( *( 't01', tau ), ->( *( 't06', tau ), *( 't04', tau ), X( 't03', +( *( 't08', tau ), *( 't05', tau ) ) ) ) ) ), ->( X( *( 't11', tau ), 't19' ), X( tau, ->( 't14', X( tau, 't16' ) ) ), 't20', 't17', X( tau, ->( 't15', 't13' ) ), 't21', +( *( 't36', tau ), ->( X( tau, ->( 't24', +( 't23', 't29' ), X( tau, 't25' ), 't26', 't27', X( tau, +( 't30', *( 't71', tau ) ) ), X( tau, 't28' ) ) ), X( tau, 't22' ), *( 't42', tau ), 't38', 't39', X( ->( 't43', 't44' ), 't40', 't34' ), 't33', 't46', X( 't69', 't70', ->( X( tau, 't47' ), +( *( 't62', tau ), 't45', ->( 't48', 't68' ), ->( 't37', 't60' ) ), 't64' ) ), 't65' ) ), 't66' ) ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_0000101__noise0.4.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST (in LOOP_1)]` | `t09` | Exact Token Match | $\ge$ 1003 | **1003** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_1]` | Exact Token Match | $\ge$ 1 | **985** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `t10` | Exact Token Match | $\ge$ 997 | **997** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10⟩` | Exact Token Match | $\ge$ 591 | **965** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_2]` | Exact Token Match | $\ge$ 1 | **981** | ✅ **VERIFIED** |
| `[ST (in LOOP_4)]` | `t02` | Exact Token Match | $\ge$ 513 | **513** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t02⟩` | Exact Token Match | $\ge$ 299 | **513** | ✅ **VERIFIED** |
| `[AS (in PAR_3)]` | `[nested LOOP_4]` | Exact Token Match | $\ge$ 1 | **513** | ✅ **VERIFIED** |
| `[ST (in LOOP_5)]` | `t01` | Exact Token Match | $\ge$ 215 | **215** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t01⟩` | Exact Token Match | $\ge$ 215 | **215** | ✅ **VERIFIED** |
| `[ST (in LOOP_6)]` | `t06` | Exact Token Match | $\ge$ 189 | **189** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t06⟩` | Exact Token Match | $\ge$ 189 | **189** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `t04` | Exact Token Match | $\ge$ 194 | **194** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t04⟩` | Exact Token Match | $\ge$ 188 | **194** | ✅ **VERIFIED** |
| `[AS (in PAR_3)]` | `[nested LOOP_7]` | Exact Token Match | $\ge$ 1 | **194** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `t03` | Exact Token Match | $\ge$ 92 | **92** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `t08` | Exact Token Match | $\ge$ 99 | **99** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨t08⟩` | Exact Token Match | $\ge$ 99 | **99** | ✅ **VERIFIED** |
| `[ST (in LOOP_10)]` | `t05` | Exact Token Match | $\ge$ 99 | **99** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨t05⟩` | Exact Token Match | $\ge$ 99 | **99** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t04, t03⟩` | Exact Token Match | $\ge$ 89 | **92** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t06, t04, t03⟩` | Exact Token Match | $\ge$ 87 | **88** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_3]` | Exact Token Match | $\ge$ 406 | **611** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `t11` | Exact Token Match | $\ge$ 195 | **195** | ✅ **VERIFIED** |
| `[ST]` | `t19` | Exact Token Match | $\ge$ 193 | **193** | ✅ **VERIFIED** |
| `[ST]` | `t14` | Exact Token Match | $\ge$ 194 | **194** | ✅ **VERIFIED** |
| `[ST]` | `t16` | Exact Token Match | $\ge$ 69 | **69** | ✅ **VERIFIED** |
| `[ST]` | `⟨t14, τ⟩` | Exact Token Match | $\ge$ 125 | **194** | ✅ **VERIFIED** |
| `[ST]` | `⟨t14, t16⟩` | Exact Token Match | $\ge$ 69 | **69** | ✅ **VERIFIED** |
| `[ST]` | `t20` | Exact Token Match | $\ge$ 328 | **328** | ✅ **VERIFIED** |
| `[ST]` | `t15` | Exact Token Match | $\ge$ 58 | **58** | ✅ **VERIFIED** |
| `[ST]` | `t13` | Exact Token Match | $\ge$ 58 | **58** | ✅ **VERIFIED** |
| `[ST]` | `⟨t15, t13⟩` | Exact Token Match | $\ge$ 58 | **58** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `t36` | Exact Token Match | $\ge$ 325 | **325** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t36⟩` | Exact Token Match | $\ge$ 325 | **325** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `t24` | Exact Token Match | $\ge$ 113 | **113** | ✅ **VERIFIED** |
| `[ST (in PAR_14)]` | `t23` | Exact Token Match | $\ge$ 112 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_14)]` | `t29` | Exact Token Match | $\ge$ 112 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `t25` | Exact Token Match | $\ge$ 57 | **57** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `t26` | Exact Token Match | $\ge$ 113 | **113** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `t27` | Exact Token Match | $\ge$ 113 | **113** | ✅ **VERIFIED** |
| `[ST (in PAR_15)]` | `t30` | Exact Token Match | $\ge$ 60 | **60** | ✅ **VERIFIED** |
| `[ST (in LOOP_16)]` | `t71` | Exact Token Match | $\ge$ 63 | **63** | ✅ **VERIFIED** |
| `[ST (in PAR_15)]` | `⟨t71⟩` | Exact Token Match | $\ge$ 57 | **63** | ✅ **VERIFIED** |
| `[AS (in PAR_15)]` | `[nested LOOP_16]` | Exact Token Match | $\ge$ 1 | **63** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `t28` | Exact Token Match | $\ge$ 52 | **52** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨[nested PAR_15], τ⟩` | Exact Token Match | $\ge$ 8 | **59** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t27, [nested PAR_15], τ⟩` | Exact Token Match | $\ge$ 8 | **58** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t27, τ⟩` | Exact Token Match | $\ge$ 53 | **113** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t26, t27, [nested PAR_15], τ⟩` | Exact Token Match | $\ge$ 8 | **58** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t26, t27, τ⟩` | Exact Token Match | $\ge$ 53 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨τ, t26, t27, [nested PAR_15]⟩` | Exact Token Match | $\ge$ 3 | **58** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨τ, t26, t27⟩` | Exact Token Match | $\ge$ 56 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨τ, t26⟩` | Exact Token Match | $\ge$ 56 | **113** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t25, t26, t27, [nested PAR_15]⟩` | Exact Token Match | $\ge$ 4 | **28** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t25, t26, t27⟩` | Exact Token Match | $\ge$ 57 | **57** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t25, t26⟩` | Exact Token Match | $\ge$ 57 | **57** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨[nested PAR_14], τ, t26, t27, [nested PAR_15]⟩` | Exact Token Match | $\ge$ 2 | **57** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨[nested PAR_14], τ, t26, t27⟩` | Exact Token Match | $\ge$ 55 | **110** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨[nested PAR_14], τ, t26⟩` | Exact Token Match | $\ge$ 55 | **111** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨[nested PAR_14], t25, t26, t27, [nested PAR_15]⟩` | Exact Token Match | $\ge$ 3 | **27** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨[nested PAR_14], τ⟩` | Exact Token Match | $\ge$ 55 | **111** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t24, [nested PAR_14], τ, t26, t27, [nested PAR_15]⟩` | Exact Token Match | $\ge$ 2 | **57** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t24, [nested PAR_14], τ, t26, t27⟩` | Exact Token Match | $\ge$ 55 | **110** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t24, [nested PAR_14], τ, t26⟩` | Exact Token Match | $\ge$ 55 | **111** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t24, [nested PAR_14], t25, t26, t27, [nested PAR_15]⟩` | Exact Token Match | $\ge$ 3 | **27** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t24, [nested PAR_14], τ⟩` | Exact Token Match | $\ge$ 55 | **111** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t24, τ⟩` | Exact Token Match | $\ge$ 1 | **113** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `t22` | Exact Token Match | $\ge$ 126 | **126** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `t42` | Exact Token Match | $\ge$ 326 | **326** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t42⟩` | Exact Token Match | $\ge$ 326 | **326** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `t38` | Exact Token Match | $\ge$ 324 | **324** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `t39` | Exact Token Match | $\ge$ 327 | **327** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `t43` | Exact Token Match | $\ge$ 91 | **91** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `t44` | Exact Token Match | $\ge$ 91 | **91** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t43, t44⟩` | Exact Token Match | $\ge$ 91 | **91** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `t40` | Exact Token Match | $\ge$ 82 | **82** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `t34` | Exact Token Match | $\ge$ 70 | **70** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `t33` | Exact Token Match | $\ge$ 325 | **325** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `t46` | Exact Token Match | $\ge$ 325 | **325** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `t69` | Exact Token Match | $\ge$ 88 | **88** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `t70` | Exact Token Match | $\ge$ 70 | **70** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `t47` | Exact Token Match | $\ge$ 81 | **81** | ✅ **VERIFIED** |
| `[ST (in LOOP_19)]` | `t62` | Exact Token Match | $\ge$ 168 | **168** | ✅ **VERIFIED** |
| `[ST (in PAR_18)]` | `⟨t62⟩` | Exact Token Match | $\ge$ 168 | **168** | ✅ **VERIFIED** |
| `[ST (in PAR_20)]` | `t45` | Exact Token Match | $\ge$ 165 | **165** | ✅ **VERIFIED** |
| `[ST (in PAR_21)]` | `t48` | Exact Token Match | $\ge$ 168 | **168** | ✅ **VERIFIED** |
| `[ST (in PAR_21)]` | `t68` | Exact Token Match | $\ge$ 167 | **167** | ✅ **VERIFIED** |
| `[ST (in PAR_21)]` | `⟨t48, τ⟩` | Exact Token Match | $\ge$ 1 | **168** | ✅ **VERIFIED** |
| `[ST (in PAR_21)]` | `t37` | Exact Token Match | $\ge$ 166 | **166** | ✅ **VERIFIED** |
| `[ST (in PAR_21)]` | `t60` | Exact Token Match | $\ge$ 167 | **167** | ✅ **VERIFIED** |
| `[ST (in PAR_21)]` | `⟨t37, t60⟩` | Exact Token Match | $\ge$ 166 | **166** | ✅ **VERIFIED** |
| `[ST (in PAR_21)]` | `⟨τ, t60⟩` | Exact Token Match | $\ge$ 1 | **167** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `t64` | Exact Token Match | $\ge$ 167 | **167** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨[nested PAR_18], τ⟩` | Exact Token Match | $\ge$ 1 | **162** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨τ, [nested PAR_18], t64⟩` | Exact Token Match | $\ge$ 86 | **161** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨τ, [nested PAR_18]⟩` | Exact Token Match | $\ge$ 87 | **162** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `t65` | Exact Token Match | $\ge$ 326 | **326** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t69, t65⟩` | Exact Token Match | $\ge$ 88 | **88** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t70, t65⟩` | Exact Token Match | $\ge$ 70 | **70** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨τ, [nested PAR_18], t64, t65⟩` | Exact Token Match | $\ge$ 86 | **161** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨[nested PAR_18], τ, t65⟩` | Exact Token Match | $\ge$ 1 | **162** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨τ, t65⟩` | Exact Token Match | $\ge$ 1 | **326** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t46, t69, t65⟩` | Exact Token Match | $\ge$ 87 | **87** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t46, t70, t65⟩` | Exact Token Match | $\ge$ 69 | **70** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t46, τ, [nested PAR_18], t64, t65⟩` | Exact Token Match | $\ge$ 85 | **160** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t46, t47, [nested PAR_18], t64, t65⟩` | Exact Token Match | $\ge$ 79 | **79** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t46, t69⟩` | Exact Token Match | $\ge$ 87 | **87** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t46, t70⟩` | Exact Token Match | $\ge$ 69 | **70** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t46, τ, [nested PAR_18], t64⟩` | Exact Token Match | $\ge$ 85 | **160** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t46, τ, [nested PAR_18]⟩` | Exact Token Match | $\ge$ 86 | **161** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t46, t47, [nested PAR_18], t64⟩` | Exact Token Match | $\ge$ 79 | **79** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t46, τ⟩` | Exact Token Match | $\ge$ 86 | **325** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t46, t47⟩` | Exact Token Match | $\ge$ 80 | **81** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t33, t46, t69, t65⟩` | Exact Token Match | $\ge$ 86 | **86** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t33, t46, t70, t65⟩` | Exact Token Match | $\ge$ 68 | **70** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t33, t46, τ, [nested PAR_18], t64, t65⟩` | Exact Token Match | $\ge$ 84 | **160** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t33, t46, t47, [nested PAR_18], t64, t65⟩` | Exact Token Match | $\ge$ 78 | **79** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t33, t46, t69⟩` | Exact Token Match | $\ge$ 86 | **86** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t33, t46, t70⟩` | Exact Token Match | $\ge$ 68 | **70** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t33, t46, τ, [nested PAR_18], t64⟩` | Exact Token Match | $\ge$ 84 | **160** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t33, t46, τ, [nested PAR_18]⟩` | Exact Token Match | $\ge$ 85 | **161** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t33, t46, t47, [nested PAR_18], t64⟩` | Exact Token Match | $\ge$ 78 | **79** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t33, t46, t47, [nested PAR_18]⟩` | Exact Token Match | $\ge$ 79 | **79** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t33, t46, τ⟩` | Exact Token Match | $\ge$ 85 | **323** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t33, t46, t47⟩` | Exact Token Match | $\ge$ 79 | **81** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t43, t44, t33, t46⟩` | Exact Token Match | $\ge$ 89 | **89** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t43, t44, t33⟩` | Exact Token Match | $\ge$ 90 | **91** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t40, t33, t46⟩` | Exact Token Match | $\ge$ 80 | **82** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t40, t33⟩` | Exact Token Match | $\ge$ 81 | **82** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t34, t33, t46⟩` | Exact Token Match | $\ge$ 68 | **70** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t34, t33⟩` | Exact Token Match | $\ge$ 69 | **70** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨τ, t33, t46⟩` | Exact Token Match | $\ge$ 81 | **323** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨τ, t33⟩` | Exact Token Match | $\ge$ 82 | **325** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t39, τ⟩` | Exact Token Match | $\ge$ 1 | **327** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t39, t43, t44, t33, t46⟩` | Exact Token Match | $\ge$ 89 | **89** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t39, t43, t44, t33⟩` | Exact Token Match | $\ge$ 90 | **91** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t39, t40, t33, t46⟩` | Exact Token Match | $\ge$ 80 | **82** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t39, t40, t33⟩` | Exact Token Match | $\ge$ 81 | **82** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t39, t34, t33, t46⟩` | Exact Token Match | $\ge$ 68 | **70** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t39, t34, t33⟩` | Exact Token Match | $\ge$ 69 | **70** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t39, τ, t33, t46⟩` | Exact Token Match | $\ge$ 81 | **323** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t39, τ, t33⟩` | Exact Token Match | $\ge$ 82 | **325** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t39, t43, t44⟩` | Exact Token Match | $\ge$ 91 | **91** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t39, t43⟩` | Exact Token Match | $\ge$ 91 | **91** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t39, t40⟩` | Exact Token Match | $\ge$ 82 | **82** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t39, t34⟩` | Exact Token Match | $\ge$ 70 | **70** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t39, τ⟩` | Exact Token Match | $\ge$ 83 | **327** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t38, t39, t43, t44, t33, t46⟩` | Exact Token Match | $\ge$ 86 | **89** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t38, t39, t43, t44, t33⟩` | Exact Token Match | $\ge$ 87 | **91** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t38, t39, t40, t33, t46⟩` | Exact Token Match | $\ge$ 77 | **80** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t38, t39, t40, t33⟩` | Exact Token Match | $\ge$ 78 | **80** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t38, t39, t34, t33, t46⟩` | Exact Token Match | $\ge$ 65 | **69** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t38, t39, t34, t33⟩` | Exact Token Match | $\ge$ 66 | **69** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t38, t39, τ, t33, t46⟩` | Exact Token Match | $\ge$ 78 | **320** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t38, t39, τ, t33⟩` | Exact Token Match | $\ge$ 79 | **322** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t38, t39, t43, t44⟩` | Exact Token Match | $\ge$ 88 | **91** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t38, t39, t43⟩` | Exact Token Match | $\ge$ 88 | **91** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t38, t39, t40⟩` | Exact Token Match | $\ge$ 79 | **80** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t38, t39, t34⟩` | Exact Token Match | $\ge$ 67 | **69** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t38, t39, τ⟩` | Exact Token Match | $\ge$ 80 | **323** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨τ, t39⟩` | Exact Token Match | $\ge$ 3 | **327** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t42, t38, t39, t43, t44, t33, t46⟩` | Exact Token Match | $\ge$ 85 | **88** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t42, t38, t39, t43, t44, t33⟩` | Exact Token Match | $\ge$ 86 | **90** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t42, t38, t39, t40, t33, t46⟩` | Exact Token Match | $\ge$ 76 | **80** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t42, t38, t39, t40, t33⟩` | Exact Token Match | $\ge$ 77 | **80** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t42, t38, t39, t34, t33, t46⟩` | Exact Token Match | $\ge$ 64 | **69** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t42, t38, t39, t34, t33⟩` | Exact Token Match | $\ge$ 65 | **69** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t42, t38, t39, τ, t33, t46⟩` | Exact Token Match | $\ge$ 77 | **319** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t42, t38, t39, τ, t33⟩` | Exact Token Match | $\ge$ 78 | **321** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t42, t38, t39, t43, t44⟩` | Exact Token Match | $\ge$ 87 | **90** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t42, t38, t39, t43⟩` | Exact Token Match | $\ge$ 87 | **90** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t42, t38, t39, t40⟩` | Exact Token Match | $\ge$ 78 | **80** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t42, t38, t39, t34⟩` | Exact Token Match | $\ge$ 66 | **69** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t42, t38, t39, τ⟩` | Exact Token Match | $\ge$ 79 | **322** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t42, τ, t39⟩` | Exact Token Match | $\ge$ 2 | **325** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t42, τ⟩` | Exact Token Match | $\ge$ 2 | **326** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨τ, t42, t38, t39⟩` | Exact Token Match | $\ge$ 197 | **322** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨τ, t42, t38⟩` | Exact Token Match | $\ge$ 197 | **322** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨τ, t42⟩` | Exact Token Match | $\ge$ 200 | **326** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t22, t42, t38, t39⟩` | Exact Token Match | $\ge$ 122 | **125** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t22, t42, t38⟩` | Exact Token Match | $\ge$ 122 | **125** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨t22, t42⟩` | Exact Token Match | $\ge$ 125 | **125** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨τ, τ, t42, t38, t39⟩` | Exact Token Match | $\ge$ 84 | **322** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨τ, τ, t42, t38⟩` | Exact Token Match | $\ge$ 84 | **322** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨τ, τ, t42⟩` | Exact Token Match | $\ge$ 87 | **326** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨τ, t22, t42, t38, t39⟩` | Exact Token Match | $\ge$ 9 | **125** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨τ, t22, t42, t38⟩` | Exact Token Match | $\ge$ 9 | **125** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨τ, t22, t42⟩` | Exact Token Match | $\ge$ 12 | **125** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨τ, t22⟩` | Exact Token Match | $\ge$ 13 | **126** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_12]` | Exact Token Match | $\ge$ 327 | **387** | ✅ **VERIFIED** |
| `[ST]` | `t66` | Exact Token Match | $\ge$ 386 | **386** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_12], t66⟩` | Exact Token Match | $\ge$ 327 | **385** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t66⟩` | Exact Token Match | $\ge$ 59 | **386** | ✅ **VERIFIED** |
| `[ST]` | `⟨t21, [nested PAR_12], t66⟩` | Exact Token Match | $\ge$ 326 | **372** | ✅ **VERIFIED** |
| `[ST]` | `⟨t21, τ, t66⟩` | Exact Token Match | $\ge$ 58 | **382** | ✅ **VERIFIED** |
| `[ST]` | `⟨t21, [nested PAR_12]⟩` | Exact Token Match | $\ge$ 326 | **374** | ✅ **VERIFIED** |
| `[ST]` | `⟨t21, τ⟩` | Exact Token Match | $\ge$ 58 | **383** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t21, [nested PAR_12], t66⟩` | Exact Token Match | $\ge$ 268 | **372** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t21, [nested PAR_12]⟩` | Exact Token Match | $\ge$ 268 | **374** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t21⟩` | Exact Token Match | $\ge$ 327 | **383** | ✅ **VERIFIED** |
| `[ST]` | `⟨t15, t13, t21⟩` | Exact Token Match | $\ge$ 57 | **57** | ✅ **VERIFIED** |
| `[ST]` | `⟨t17, τ, t21, [nested PAR_12], t66⟩` | Exact Token Match | $\ge$ 211 | **312** | ✅ **VERIFIED** |
| `[ST]` | `⟨t17, τ, t21, [nested PAR_12]⟩` | Exact Token Match | $\ge$ 211 | **313** | ✅ **VERIFIED** |
| `[ST]` | `⟨t17, τ, t21⟩` | Exact Token Match | $\ge$ 270 | **322** | ✅ **VERIFIED** |
| `[ST]` | `⟨t17, τ⟩` | Exact Token Match | $\ge$ 271 | **325** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, t17, τ, t21, [nested PAR_12], t66⟩` | Exact Token Match | $\ge$ 153 | **311** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, t17, τ, t21, [nested PAR_12]⟩` | Exact Token Match | $\ge$ 153 | **312** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, t17, τ, t21⟩` | Exact Token Match | $\ge$ 212 | **321** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, t17, τ⟩` | Exact Token Match | $\ge$ 213 | **324** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, t17⟩` | Exact Token Match | $\ge$ 271 | **324** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t17⟩` | Exact Token Match | $\ge$ 1 | **325** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t20, t17, τ, t21⟩` | Exact Token Match | $\ge$ 18 | **321** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t20, t17, τ⟩` | Exact Token Match | $\ge$ 19 | **324** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t20, t17⟩` | Exact Token Match | $\ge$ 77 | **324** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t20⟩` | Exact Token Match | $\ge$ 134 | **328** | ✅ **VERIFIED** |
| `[ST]` | `⟨t14, τ, t20, t17⟩` | Exact Token Match | $\ge$ 10 | **134** | ✅ **VERIFIED** |
| `[ST]` | `⟨t14, τ, t20⟩` | Exact Token Match | $\ge$ 67 | **136** | ✅ **VERIFIED** |
| `[ST]` | `⟨t14, t16, t20⟩` | Exact Token Match | $\ge$ 11 | **69** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, t14⟩` | Exact Token Match | $\ge$ 1 | **190** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, [nested PAR_3]⟩` | Exact Token Match | $\ge$ 203 | **560** | ✅ **VERIFIED** |
| `[ST]` | `⟨t09, t10, [nested PAR_3]⟩` | Exact Token Match | $\ge$ 200 | **525** | ✅ **VERIFIED** |
| `[ST]` | `⟨t09, τ⟩` | Exact Token Match | $\ge$ 203 | **967** | ✅ **VERIFIED** |
| `[ST]` | `⟨t09, t10⟩` | Exact Token Match | $\ge$ 588 | **924** | ✅ **VERIFIED** |
| `[ST]` | `⟨t09⟩` | Exact Token Match | $\ge$ 997 | **967** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_3)]` | `[nested PAR_8]` | Exact Token Match | $\ge$ 99 | **95** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_3)]` | `⟨t04, [nested PAR_8]⟩` | Exact Token Match | $\ge$ 96 | **94** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_3)]` | `⟨t06, t04, [nested PAR_8]⟩` | Exact Token Match | $\ge$ 94 | **93** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_3)]` | `⟨t06, t04⟩` | Exact Token Match | $\ge$ 186 | **185** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t11⟩` | Exact Token Match | $\ge$ 195 | **191** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t17` | Exact Token Match | $\ge$ 329 | **325** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t21` | Exact Token Match | $\ge$ 385 | **383** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_12)]` | `[nested PAR_14]` | Exact Token Match | $\ge$ 112 | **111** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_12)]` | `[nested PAR_15]` | Exact Token Match | $\ge$ 60 | **59** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_12)]` | `⟨t27, [nested PAR_15]⟩` | Exact Token Match | $\ge$ 60 | **58** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_12)]` | `⟨t26, t27, [nested PAR_15]⟩` | Exact Token Match | $\ge$ 60 | **58** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_12)]` | `⟨t26, t27⟩` | Exact Token Match | $\ge$ 113 | **112** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_12)]` | `⟨[nested PAR_14], t25, t26, t27⟩` | Exact Token Match | $\ge$ 56 | **55** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_12)]` | `⟨[nested PAR_14], t25, t26⟩` | Exact Token Match | $\ge$ 56 | **55** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_12)]` | `⟨[nested PAR_14], t25⟩` | Exact Token Match | $\ge$ 56 | **55** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_12)]` | `⟨t24, [nested PAR_14], t25, t26, t27⟩` | Exact Token Match | $\ge$ 56 | **55** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_12)]` | `⟨t24, [nested PAR_14], t25, t26⟩` | Exact Token Match | $\ge$ 56 | **55** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_12)]` | `⟨t24, [nested PAR_14], t25⟩` | Exact Token Match | $\ge$ 56 | **55** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_12)]` | `⟨t24, [nested PAR_14]⟩` | Exact Token Match | $\ge$ 112 | **111** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_21)]` | `⟨t48, t68⟩` | Exact Token Match | $\ge$ 167 | **165** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_20)]` | `[nested PAR_21]` | Exact Token Match | $\ge$ 168 | **164** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_18)]` | `[nested PAR_20]` | Exact Token Match | $\ge$ 168 | **162** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_12)]` | `[nested PAR_18]` | Exact Token Match | $\ge$ 168 | **162** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_12)]` | `⟨[nested PAR_18], t64⟩` | Exact Token Match | $\ge$ 167 | **161** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_12)]` | `⟨t47, [nested PAR_18], t64⟩` | Exact Token Match | $\ge$ 80 | **79** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_12)]` | `⟨t47, [nested PAR_18]⟩` | Exact Token Match | $\ge$ 81 | **79** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_12)]` | `⟨t47, [nested PAR_18], t64, t65⟩` | Exact Token Match | $\ge$ 80 | **79** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_12)]` | `⟨[nested PAR_18], t64, t65⟩` | Exact Token Match | $\ge$ 167 | **161** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_12)]` | `⟨t64, t65⟩` | Exact Token Match | $\ge$ 167 | **166** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_12)]` | `⟨t46, t47, [nested PAR_18]⟩` | Exact Token Match | $\ge$ 80 | **79** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_12)]` | `⟨t33, t46⟩` | Exact Token Match | $\ge$ 324 | **323** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_12)]` | `⟨t38, t39⟩` | Exact Token Match | $\ge$ 324 | **323** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_12)]` | `⟨t42, t38, t39⟩` | Exact Token Match | $\ge$ 323 | **322** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_12)]` | `⟨t42, t38⟩` | Exact Token Match | $\ge$ 323 | **322** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_12)]` | `⟨[nested PAR_15], t28⟩` | Exact Token Match | $\ge$ 52 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_12)]` | `⟨t27, [nested PAR_15], t28⟩` | Exact Token Match | $\ge$ 52 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_12)]` | `⟨t26, t27, [nested PAR_15], t28⟩` | Exact Token Match | $\ge$ 52 | **0** | ❌ **GHOST PATTERN** |
| `[ST]` | `⟨t17, t15, t13⟩` | Exact Token Match | $\ge$ 1 | **0** | ❌ **GHOST PATTERN** |
| `[ST]` | `⟨t17, t15⟩` | Exact Token Match | $\ge$ 1 | **0** | ❌ **GHOST PATTERN** |

## Audit Summary
- **Perfect Pattern Verifications:** 224
- **Frequency Discrepancies:** 35
- **Ghost Patterns (Fatal):** 5
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 20.30%
- **Tree Exposure (Strict, Fragment-Level % of N):** 40.92%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 11.16%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 100.00%
- **Total Forced Volume (incl. unresolved AS, % of N):** 40.30%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 20.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 99.22%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 99.40%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 99.77%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 39.07%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 99.25%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 99.94%
- **Max Fractional Exposure (Worst-Case Normalized):** 52.04% (expected length: 213.22 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 100.00% (expected length: 10.54 events)
- **Mean Absolute Exposure Volume:** 7.53 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_1]`
- **Internal Structure:** `(t09 ∗ τ)`
- **Block Frequency:** 1000

- **Max Loop Iterations:** `3`
- **Max Sub-Sequence Length:** `7` steps (if one case consumes all iterations)

![nested LOOP_1 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_1.png)

### `[nested LOOP_2]`
- **Internal Structure:** `(t10 ∗ τ)`
- **Block Frequency:** 794

- **Max Loop Iterations:** `203`
- **Max Sub-Sequence Length:** `407` steps (if one case consumes all iterations)

![nested LOOP_2 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_2.png)

### `[nested LOOP_4]`
- **Internal Structure:** `(t02 ∗ τ)`
- **Block Frequency:** 406

- **Max Loop Iterations:** `107`
- **Max Sub-Sequence Length:** `215` steps (if one case consumes all iterations)

![nested LOOP_4 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_4.png)

### `[nested LOOP_5]`
- **Internal Structure:** `(t01 ∗ τ)`
- **Block Frequency:** 215

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_5 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_5.png)

### `[nested LOOP_6]`
- **Internal Structure:** `(t06 ∗ τ)`
- **Block Frequency:** 189

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_6 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_6.png)

### `[nested LOOP_7]`
- **Internal Structure:** `(t04 ∗ τ)`
- **Block Frequency:** 191

- **Max Loop Iterations:** `3`
- **Max Sub-Sequence Length:** `7` steps (if one case consumes all iterations)

![nested LOOP_7 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_7.png)

### `[nested LOOP_9]`
- **Internal Structure:** `(t08 ∗ τ)`
- **Block Frequency:** 99

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_9 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_9.png)

### `[nested LOOP_10]`
- **Internal Structure:** `(t05 ∗ τ)`
- **Block Frequency:** 99

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_10 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_10.png)

### `[nested PAR_8]`
- **Internal Structure:** `{(t08 ∗ τ), (t05 ∗ τ)}`
- **Block Frequency:** 99



![nested PAR_8 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_PAR_8.png)

### `[nested PAR_3]`
- **Internal Structure:** `{(t02 ∗ τ), [(t01 ∗ τ) │ ⟨[(t06 ∗ τ) │ τ], (t04 ∗ τ), [t03 │ {(t08 ∗ τ), (t05 ∗ τ)}]⟩]}`
- **Block Frequency:** 406



![nested PAR_3 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_PAR_3.png)

### `[nested LOOP_11]`
- **Internal Structure:** `(t11 ∗ τ)`
- **Block Frequency:** 195

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_11 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_11.png)

### `[nested LOOP_13]`
- **Internal Structure:** `(t36 ∗ τ)`
- **Block Frequency:** 325

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_13 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_13.png)

### `[nested PAR_14]`
- **Internal Structure:** `{t23, t29}`
- **Block Frequency:** 112



![nested PAR_14 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_PAR_14.png)

### `[nested LOOP_16]`
- **Internal Structure:** `(t71 ∗ τ)`
- **Block Frequency:** 60

- **Max Loop Iterations:** `3`
- **Max Sub-Sequence Length:** `7` steps (if one case consumes all iterations)

![nested LOOP_16 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_16.png)

### `[nested PAR_15]`
- **Internal Structure:** `{t30, (t71 ∗ τ)}`
- **Block Frequency:** 60



![nested PAR_15 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_PAR_15.png)

### `[nested LOOP_17]`
- **Internal Structure:** `(t42 ∗ τ)`
- **Block Frequency:** 326

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_17 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_17.png)

### `[nested LOOP_19]`
- **Internal Structure:** `(t62 ∗ τ)`
- **Block Frequency:** 168

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_19 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_LOOP_19.png)

### `[nested PAR_21]`
- **Internal Structure:** `{⟨t48, [t68 │ τ]⟩, [⟨[t37 │ τ], t60⟩ │ τ]}`
- **Block Frequency:** 168



![nested PAR_21 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_PAR_21.png)

### `[nested PAR_20]`
- **Internal Structure:** `{[t45 │ τ], ⟨t48, [t68 │ τ]⟩, [⟨[t37 │ τ], t60⟩ │ τ]}`
- **Block Frequency:** 168



![nested PAR_20 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_PAR_20.png)

### `[nested PAR_18]`
- **Internal Structure:** `{(t62 ∗ τ), [t45 │ τ], ⟨t48, [t68 │ τ]⟩, [⟨[t37 │ τ], t60⟩ │ τ]}`
- **Block Frequency:** 168



![nested PAR_18 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_PAR_18.png)

### `[nested PAR_12]`
- **Internal Structure:** `{[(t36 ∗ τ) │ τ], ⟨[τ │ ⟨t24, [{t23, t29} │ τ], [τ │ t25], t26, t27, [⟨[τ │ {t30, (t71 ∗ τ)}], [τ │ t28]⟩ │ τ]⟩], [τ │ t22], [(t42 ∗ τ) │ τ], [t38 │ τ], t39, [⟨[⟨t43, t44⟩ │ t40 │ t34 │ τ], [t33 │ τ], [t46 │ τ], [t69 │ t70 │ ⟨[τ │ t47], {(t62 ∗ τ), [t45 │ τ], ⟨t48, [t68 │ τ]⟩, [⟨[t37 │ τ], t60⟩ │ τ]}, [t64 │ τ]⟩], t65⟩ │ τ]⟩}`
- **Block Frequency:** 327



![nested PAR_12 Internal Diagram](images/nested_ref_audit_pdc2021_0000101_nested_PAR_12.png)
