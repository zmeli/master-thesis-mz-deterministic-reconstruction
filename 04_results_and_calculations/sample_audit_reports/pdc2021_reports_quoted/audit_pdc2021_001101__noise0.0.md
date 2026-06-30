# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_001101.xes` |
| **Noise Threshold** | `0.0` |
| **Fitness** | `1.0` |
| **Precision** | `0.13249651324965128` |
| **Total Cases in Log** | `250` |
| **Unique Activities** | `35` |
| **XOR Operators** | `37` |
| **LOOP Operators** | `19` |
| **SEQ Operators** | `18` |
| **PAR Operators** | `12` |
| **Binarization Additions** | `12` |
| **Tau Operators Added** | `26` |
| **Total Found Patterns** | `197` |
| **Verified Patterns** | `113` |
| **Discrepancy Patterns** | `17` |
| **Ghost Patterns** | `2` |
| **Nested LOOPs** | `19` |
| **Nested PARs** | `12` |
| **Tree Exposure (Strict, End-to-End % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `11.57%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `6.16%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `51.68%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `24.40%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `24.40%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `81.11%` |
| **Data Exposure, ST-only (% confirmed)** | `100.00%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `100.00%` |
| **Data Coverage, ST-only (% of real log)** | `9.50%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `60.71%` |
| **Data Coverage, Total (% of real log)** | `100.00%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `27.18%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `100.00%` |
| **Mean Absolute Exposure Volume (events/case)** | `25.29` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_001101__noise0.0.png)


```text
->( 't10', X( tau, ->( X( 't06', 't11' ), X( tau, +( X( tau, *( 't05', tau ) ), X( tau, *( 't15', tau ), *( 't04', tau ) ) ) ), X( tau, 't16' ) ) ), X( tau, ->( X( tau, 't20' ), +( X( tau, *( 't34', tau ) ), ->( *( ->( +( 't21', X( tau, +( X( tau, *( 't17', tau ) ), X( tau, ->( 't24', 't23' ) ) ) ) ), X( tau, 't22', ->( 't26', 't27', X( tau, 't28' ) ) ), X( tau, *( 't42', tau ) ) ), tau ), X( tau, 't71' ), +( X( tau, *( 't40', tau ) ), ->( X( tau, *( ->( 't39', X( tau, ->( 't43', 't44' ) ), *( 't36', tau ) ), tau ) ), *( ->( X( tau, ->( X( tau, 't46' ), +( X( tau, *( 't62', tau ) ), X( tau, *( 't47', tau ) ), X( tau, +( X( tau, *( 't37', tau ) ), X( tau, +( X( tau, *( 't69', tau ) ), X( tau, *( 't70', tau ) ), X( tau, *( 't48', tau ) ), X( tau, *( 't68', tau ) ), X( tau, *( 't56', tau ) ) ) ) ) ) ) ) ), X( 't65', 't55' ) ), tau ) ) ) ) ) ) ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_001101__noise0.0.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST]` | `t10` | Exact Token Match | $\ge$ 250 | **250** | ✅ **VERIFIED** |
| `[ST]` | `t06` | Exact Token Match | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[ST]` | `t11` | Exact Token Match | $\ge$ 133 | **133** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `t05` | Exact Token Match | $\ge$ 117 | **117** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t05⟩` | Exact Token Match | $\ge$ 117 | **117** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t15` | Exact Token Match | $\ge$ 77 | **77** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t15⟩` | Exact Token Match | $\ge$ 77 | **77** | ✅ **VERIFIED** |
| `[ST (in LOOP_4)]` | `t04` | Exact Token Match | $\ge$ 6 | **6** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t04⟩` | Exact Token Match | $\ge$ 6 | **6** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_1]` | Exact Token Match | $\ge$ 117 | **118** | ✅ **VERIFIED** |
| `[ST]` | `t16` | Exact Token Match | $\ge$ 64 | **64** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], τ⟩` | Exact Token Match | $\ge$ 53 | **118** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, [nested PAR_1], τ⟩` | Exact Token Match | $\ge$ 51 | **116** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, τ⟩` | Exact Token Match | $\ge$ 16 | **133** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 115 | **116** | ✅ **VERIFIED** |
| `[ST]` | `t20` | Exact Token Match | $\ge$ 192 | **192** | ✅ **VERIFIED** |
| `[ST (in LOOP_6)]` | `t34` | Exact Token Match | $\ge$ 144 | **144** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t34⟩` | Exact Token Match | $\ge$ 144 | **144** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `t21` | Exact Token Match | $\ge$ 273 | **273** | ✅ **VERIFIED** |
| `[ST (in LOOP_10)]` | `t17` | Exact Token Match | $\ge$ 266 | **266** | ✅ **VERIFIED** |
| `[ST (in PAR_9)]` | `⟨t17⟩` | Exact Token Match | $\ge$ 266 | **266** | ✅ **VERIFIED** |
| `[ST (in PAR_9)]` | `t24` | Exact Token Match | $\ge$ 110 | **110** | ✅ **VERIFIED** |
| `[ST (in PAR_9)]` | `t23` | Exact Token Match | $\ge$ 110 | **110** | ✅ **VERIFIED** |
| `[ST (in PAR_9)]` | `⟨t24, t23⟩` | Exact Token Match | $\ge$ 110 | **110** | ✅ **VERIFIED** |
| `[AS (in LOOP_7)]` | `[nested PAR_8]` | Exact Token Match | $\ge$ 273 | **327** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `t22` | Exact Token Match | $\ge$ 140 | **140** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `t26` | Exact Token Match | $\ge$ 110 | **110** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `t27` | Exact Token Match | $\ge$ 110 | **110** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `t28` | Exact Token Match | $\ge$ 72 | **72** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨t27, τ⟩` | Exact Token Match | $\ge$ 38 | **110** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨t27, t28⟩` | Exact Token Match | $\ge$ 72 | **72** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨t26, t27, τ⟩` | Exact Token Match | $\ge$ 38 | **110** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨t26, t27, t28⟩` | Exact Token Match | $\ge$ 72 | **72** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨t26, t27⟩` | Exact Token Match | $\ge$ 110 | **110** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `t42` | Exact Token Match | $\ge$ 316 | **316** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨t42⟩` | Exact Token Match | $\ge$ 316 | **316** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨τ, t42⟩` | Exact Token Match | $\ge$ 66 | **316** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨t22, t42⟩` | Exact Token Match | $\ge$ 140 | **140** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨t26, t27, τ, t42⟩` | Exact Token Match | $\ge$ 38 | **72** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨t26, t27, t28, t42⟩` | Exact Token Match | $\ge$ 72 | **72** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨t27, τ, t42⟩` | Exact Token Match | $\ge$ 38 | **72** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨t27, t28, t42⟩` | Exact Token Match | $\ge$ 72 | **72** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨τ, t42⟩` | Exact Token Match | $\ge$ 38 | **316** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨t28, t42⟩` | Exact Token Match | $\ge$ 72 | **72** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨[nested PAR_8], τ, t42⟩` | Exact Token Match | $\ge$ 23 | **235** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨[nested PAR_8], t22, t42⟩` | Exact Token Match | $\ge$ 97 | **140** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨[nested PAR_8], t26, t27, t28, t42⟩` | Exact Token Match | $\ge$ 29 | **72** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨[nested PAR_8], τ⟩` | Exact Token Match | $\ge$ 23 | **327** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨[nested PAR_8], t22⟩` | Exact Token Match | $\ge$ 97 | **140** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨[nested PAR_8], t26, t27, t28⟩` | Exact Token Match | $\ge$ 29 | **72** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨[nested PAR_8], t26, t27⟩` | Exact Token Match | $\ge$ 67 | **110** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨[nested PAR_8], t26⟩` | Exact Token Match | $\ge$ 67 | **110** | ✅ **VERIFIED** |
| `[AS (in PAR_5)]` | `[nested LOOP_7]` | Exact Token Match | $\ge$ 1 | **3** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t71` | Exact Token Match | $\ge$ 38 | **38** | ✅ **VERIFIED** |
| `[ST (in LOOP_16)]` | `t40` | Exact Token Match | $\ge$ 229 | **229** | ✅ **VERIFIED** |
| `[ST (in PAR_15)]` | `⟨t40⟩` | Exact Token Match | $\ge$ 229 | **229** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `t39` | Exact Token Match | $\ge$ 337 | **337** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `t43` | Exact Token Match | $\ge$ 154 | **154** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `t44` | Exact Token Match | $\ge$ 154 | **154** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨t43, t44⟩` | Exact Token Match | $\ge$ 154 | **154** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `t36` | Exact Token Match | $\ge$ 438 | **438** | ✅ **VERIFIED** |
| `[AS (in LOOP_17)]` | `[nested LOOP_18]` | Exact Token Match | $\ge$ 1 | **210** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨t43, t44, [nested LOOP_18]⟩` | Exact Token Match | $\ge$ 1 | **154** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨t44, [nested LOOP_18]⟩` | Exact Token Match | $\ge$ 1 | **154** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨t39, t43, t44, [nested LOOP_18]⟩` | Exact Token Match | $\ge$ 1 | **154** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨t39, τ⟩` | Exact Token Match | $\ge$ 183 | **337** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨t39, t43, t44⟩` | Exact Token Match | $\ge$ 154 | **154** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨t39, t43⟩` | Exact Token Match | $\ge$ 154 | **154** | ✅ **VERIFIED** |
| `[ST (in PAR_15)]` | `⟨t39, τ⟩` | Exact Token Match | $\ge$ 9 | **337** | ✅ **VERIFIED** |
| `[ST (in PAR_15)]` | `⟨t39, [nested XOR_19]⟩` | Exact Token Match | $\ge$ 154.0 | **154** | ✅ **VERIFIED** |
| `[AS (in PAR_15)]` | `[nested LOOP_17]` | Exact Token Match | $\ge$ 1 | **154** | ✅ **VERIFIED** |
| `[ST (in LOOP_20)]` | `t46` | Exact Token Match | $\ge$ 327 | **327** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `t62` | Exact Token Match | $\ge$ 264 | **264** | ✅ **VERIFIED** |
| `[ST (in PAR_21)]` | `⟨t62⟩` | Exact Token Match | $\ge$ 264 | **264** | ✅ **VERIFIED** |
| `[ST (in LOOP_24)]` | `t47` | Exact Token Match | $\ge$ 222 | **222** | ✅ **VERIFIED** |
| `[ST (in PAR_23)]` | `⟨t47⟩` | Exact Token Match | $\ge$ 222 | **222** | ✅ **VERIFIED** |
| `[ST (in LOOP_26)]` | `t37` | Exact Token Match | $\ge$ 192 | **192** | ✅ **VERIFIED** |
| `[ST (in PAR_25)]` | `⟨t37⟩` | Exact Token Match | $\ge$ 192 | **192** | ✅ **VERIFIED** |
| `[ST (in LOOP_28)]` | `t69` | Exact Token Match | $\ge$ 113 | **113** | ✅ **VERIFIED** |
| `[ST (in PAR_27)]` | `⟨t69⟩` | Exact Token Match | $\ge$ 113 | **113** | ✅ **VERIFIED** |
| `[ST (in LOOP_30)]` | `t70` | Exact Token Match | $\ge$ 93 | **93** | ✅ **VERIFIED** |
| `[ST (in PAR_29)]` | `⟨t70⟩` | Exact Token Match | $\ge$ 93 | **93** | ✅ **VERIFIED** |
| `[ST (in LOOP_32)]` | `t48` | Exact Token Match | $\ge$ 185 | **185** | ✅ **VERIFIED** |
| `[ST (in PAR_31)]` | `⟨t48⟩` | Exact Token Match | $\ge$ 185 | **185** | ✅ **VERIFIED** |
| `[ST (in LOOP_34)]` | `t68` | Exact Token Match | $\ge$ 185 | **185** | ✅ **VERIFIED** |
| `[ST (in PAR_33)]` | `⟨t68⟩` | Exact Token Match | $\ge$ 185 | **185** | ✅ **VERIFIED** |
| `[ST (in LOOP_35)]` | `t56` | Exact Token Match | $\ge$ 495 | **495** | ✅ **VERIFIED** |
| `[ST (in PAR_33)]` | `⟨t56⟩` | Exact Token Match | $\ge$ 495 | **495** | ✅ **VERIFIED** |
| `[ST (in LOOP_20)]` | `⟨τ, [nested PAR_21]⟩` | Exact Token Match | $\ge$ 168 | **245** | ✅ **VERIFIED** |
| `[ST (in LOOP_20)]` | `⟨t46, [nested PAR_21]⟩` | Exact Token Match | $\ge$ 327 | **327** | ✅ **VERIFIED** |
| `[ST (in LOOP_20)]` | `t65` | Exact Token Match | $\ge$ 366 | **366** | ✅ **VERIFIED** |
| `[ST (in LOOP_20)]` | `t55` | Exact Token Match | $\ge$ 465 | **465** | ✅ **VERIFIED** |
| `[ST (in LOOP_20)]` | `⟨[nested PAR_21], t65⟩` | Exact Token Match | $\ge$ 30 | **366** | ✅ **VERIFIED** |
| `[ST (in LOOP_20)]` | `⟨[nested PAR_21], t55⟩` | Exact Token Match | $\ge$ 129 | **462** | ✅ **VERIFIED** |
| `[AS (in PAR_15)]` | `[nested LOOP_20]` | Exact Token Match | $\ge$ 1 | **20** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 58 | **248** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 192 | **192** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t20, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 57 | **192** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, [nested PAR_1], t16, t20, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 4 | **53** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t20⟩` | Exact Token Match | $\ge$ 57 | **192** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, [nested PAR_1], t16, t20⟩` | Exact Token Match | $\ge$ 4 | **53** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], t16, t20, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 6 | **53** | ✅ **VERIFIED** |
| `[ST]` | `⟨t16, t20, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 6 | **64** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ, t20, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 57 | **192** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, [nested PAR_1], t16, t20, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 4 | **53** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ, t20⟩` | Exact Token Match | $\ge$ 57 | **192** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, [nested PAR_1], t16, t20⟩` | Exact Token Match | $\ge$ 4 | **53** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 115 | **250** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, [nested PAR_1], τ⟩` | Exact Token Match | $\ge$ 51 | **116** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 115 | **116** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, τ⟩` | Exact Token Match | $\ge$ 16 | **133** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06⟩` | Exact Token Match | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11⟩` | Exact Token Match | $\ge$ 133 | **133** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], t16⟩` | Exact Token Match | $\ge$ 64 | **53** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t11, [nested PAR_1], t16⟩` | Exact Token Match | $\ge$ 62 | **53** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_8)]` | `[nested PAR_9]` | Exact Token Match | $\ge$ 266 | **103** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨[nested PAR_8], [nested XOR_13], t42⟩` | Exact Token Match | $\ge$ 67.0 | **3** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨[nested PAR_8], [nested XOR_14], t42⟩` | Exact Token Match | $\ge$ 23.0 | **3** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_31)]` | `[nested PAR_33]` | Exact Token Match | $\ge$ 495 | **177** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_29)]` | `[nested PAR_31]` | Exact Token Match | $\ge$ 495 | **177** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_27)]` | `[nested PAR_29]` | Exact Token Match | $\ge$ 495 | **42** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_25)]` | `[nested PAR_27]` | Exact Token Match | $\ge$ 495 | **26** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_23)]` | `[nested PAR_25]` | Exact Token Match | $\ge$ 495 | **23** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_21)]` | `[nested PAR_23]` | Exact Token Match | $\ge$ 495 | **23** | ⚠️ **DISCREPANCY** |
| `[AS (in LOOP_20)]` | `[nested PAR_21]` | Exact Token Match | $\ge$ 495 | **245** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_5)]` | `[nested PAR_15]` | Exact Token Match | $\ge$ 250 | **6** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨τ, [nested PAR_15]⟩` | Exact Token Match | $\ge$ 212 | **6** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨[nested PAR_8], [nested XOR_13], t42, τ⟩` | Exact Token Match | $\ge$ 29.0 | **3** | ⚠️ **DISCREPANCY** |
| `[AS]` | `[nested PAR_5]` | Exact Token Match | $\ge$ 250 | **248** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, t11, [nested PAR_1], t16⟩` | Exact Token Match | $\ge$ 62 | **53** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_5)]` | `⟨t71, [nested PAR_15]⟩` | Exact Token Match | $\ge$ 38 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_5)]` | `⟨[nested PAR_8], [nested XOR_13], t42, τ, [nested PAR_15]⟩` | Exact Token Match | $\ge$ 29.0 | **0** | ❌ **GHOST PATTERN** |

## Audit Summary
- **Perfect Pattern Verifications:** 113
- **Frequency Discrepancies:** 17
- **Ghost Patterns (Fatal):** 2
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 11.57%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 6.16%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 51.68%
- **Total Forced Volume (incl. unresolved AS, % of N):** 24.40%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 24.40%
- **Data Exposure (Confirmed % of Claimed Volume):** 81.11%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 100.00%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 100.00%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 9.50%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 60.71%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 100.00%
- **Max Fractional Exposure (Worst-Case Normalized):** 27.18% (expected length: 2048.10 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 100.00% (expected length: 27.00 events)
- **Mean Absolute Exposure Volume:** 25.29 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_2]`
- **Internal Structure:** `(t05 ∗ τ)`
- **Block Frequency:** 117

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_2 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_2.png)

### `[nested LOOP_3]`
- **Internal Structure:** `(t15 ∗ τ)`
- **Block Frequency:** 77

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_3 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_3.png)

### `[nested LOOP_4]`
- **Internal Structure:** `(t04 ∗ τ)`
- **Block Frequency:** 6

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_4 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_4.png)

### `[nested PAR_1]`
- **Internal Structure:** `{[τ │ (t05 ∗ τ)], [τ │ (t15 ∗ τ) │ (t04 ∗ τ)]}`
- **Block Frequency:** 117



![nested PAR_1 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_1.png)

### `[nested LOOP_6]`
- **Internal Structure:** `(t34 ∗ τ)`
- **Block Frequency:** 144

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_6 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_6.png)

### `[nested LOOP_10]`
- **Internal Structure:** `(t17 ∗ τ)`
- **Block Frequency:** 266

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_10 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_10.png)

### `[nested PAR_9]`
- **Internal Structure:** `{[τ │ (t17 ∗ τ)], [τ │ ⟨t24, t23⟩]}`
- **Block Frequency:** 266



![nested PAR_9 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_9.png)

### `[nested PAR_8]`
- **Internal Structure:** `{t21, [τ │ {[τ │ (t17 ∗ τ)], [τ │ ⟨t24, t23⟩]}]}`
- **Block Frequency:** 273



![nested PAR_8 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_8.png)

### `[nested LOOP_11]`
- **Internal Structure:** `(t42 ∗ τ)`
- **Block Frequency:** 316

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_11 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_11.png)

### `[nested LOOP_7]`
- **Internal Structure:** `(⟨[{t21, [τ │ {[τ │ (t17 ∗ τ)], [τ │ ⟨t24, t23⟩]}]} │ τ], [τ │ t22 │ ⟨t26, t27, [τ │ t28]⟩], [τ │ (t42 ∗ τ)]⟩ ∗ τ)`
- **Block Frequency:** 250

- **Max Loop Iterations:** `66`
- **Max Sub-Sequence Length:** `133` steps (if one case consumes all iterations)

![nested LOOP_7 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_7.png)

### `[nested XOR_12]`
- **Internal Structure:** `[{t21, [τ │ {[τ │ (t17 ∗ τ)], [τ │ ⟨t24, t23⟩]}]} │ τ]`
- **Block Frequency:** 316



![nested XOR_12 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_XOR_12.png)

### `[nested XOR_13]`
- **Internal Structure:** `[t22 │ ⟨t26, t27, [τ │ t28]⟩]`
- **Block Frequency:** 250



![nested XOR_13 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_XOR_13.png)

### `[nested XOR_14]`
- **Internal Structure:** `[τ │ t22 │ ⟨t26, t27, [τ │ t28]⟩]`
- **Block Frequency:** 316



![nested XOR_14 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_XOR_14.png)

### `[nested LOOP_16]`
- **Internal Structure:** `(t40 ∗ τ)`
- **Block Frequency:** 229

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_16 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_16.png)

### `[nested LOOP_18]`
- **Internal Structure:** `(t36 ∗ τ)`
- **Block Frequency:** 154

- **Max Loop Iterations:** `284`
- **Max Sub-Sequence Length:** `569` steps (if one case consumes all iterations)

![nested LOOP_18 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_18.png)

### `[nested LOOP_17]`
- **Internal Structure:** `(⟨t39, [⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ τ)`
- **Block Frequency:** 250

- **Max Loop Iterations:** `87`
- **Max Sub-Sequence Length:** `175` steps (if one case consumes all iterations)

![nested LOOP_17 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_17.png)

### `[nested XOR_19]`
- **Internal Structure:** `[⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]`
- **Block Frequency:** 337



![nested XOR_19 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_XOR_19.png)

### `[nested LOOP_22]`
- **Internal Structure:** `(t62 ∗ τ)`
- **Block Frequency:** 264

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_22 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_22.png)

### `[nested LOOP_24]`
- **Internal Structure:** `(t47 ∗ τ)`
- **Block Frequency:** 222

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_24 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_24.png)

### `[nested LOOP_26]`
- **Internal Structure:** `(t37 ∗ τ)`
- **Block Frequency:** 192

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_26 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_26.png)

### `[nested LOOP_28]`
- **Internal Structure:** `(t69 ∗ τ)`
- **Block Frequency:** 113

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_28 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_28.png)

### `[nested LOOP_30]`
- **Internal Structure:** `(t70 ∗ τ)`
- **Block Frequency:** 93

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_30 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_30.png)

### `[nested LOOP_32]`
- **Internal Structure:** `(t48 ∗ τ)`
- **Block Frequency:** 185

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_32 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_32.png)

### `[nested LOOP_34]`
- **Internal Structure:** `(t68 ∗ τ)`
- **Block Frequency:** 185

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_34 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_34.png)

### `[nested LOOP_35]`
- **Internal Structure:** `(t56 ∗ τ)`
- **Block Frequency:** 495

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_35 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_35.png)

### `[nested PAR_33]`
- **Internal Structure:** `{[τ │ (t68 ∗ τ)], [τ │ (t56 ∗ τ)]}`
- **Block Frequency:** 495



![nested PAR_33 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_33.png)

### `[nested PAR_31]`
- **Internal Structure:** `{[τ │ (t48 ∗ τ)], [τ │ (t68 ∗ τ)], [τ │ (t56 ∗ τ)]}`
- **Block Frequency:** 495



![nested PAR_31 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_31.png)

### `[nested PAR_29]`
- **Internal Structure:** `{[τ │ (t70 ∗ τ)], [τ │ (t48 ∗ τ)], [τ │ (t68 ∗ τ)], [τ │ (t56 ∗ τ)]}`
- **Block Frequency:** 495



![nested PAR_29 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_29.png)

### `[nested PAR_27]`
- **Internal Structure:** `{[τ │ (t69 ∗ τ)], [τ │ (t70 ∗ τ)], [τ │ (t48 ∗ τ)], [τ │ (t68 ∗ τ)], [τ │ (t56 ∗ τ)]}`
- **Block Frequency:** 495



![nested PAR_27 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_27.png)

### `[nested PAR_25]`
- **Internal Structure:** `{[τ │ (t37 ∗ τ)], [τ │ {[τ │ (t69 ∗ τ)], [τ │ (t70 ∗ τ)], [τ │ (t48 ∗ τ)], [τ │ (t68 ∗ τ)], [τ │ (t56 ∗ τ)]}]}`
- **Block Frequency:** 495



![nested PAR_25 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_25.png)

### `[nested PAR_23]`
- **Internal Structure:** `{[τ │ (t47 ∗ τ)], [τ │ {[τ │ (t37 ∗ τ)], [τ │ {[τ │ (t69 ∗ τ)], [τ │ (t70 ∗ τ)], [τ │ (t48 ∗ τ)], [τ │ (t68 ∗ τ)], [τ │ (t56 ∗ τ)]}]}]}`
- **Block Frequency:** 495



![nested PAR_23 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_23.png)

### `[nested PAR_21]`
- **Internal Structure:** `{[τ │ (t62 ∗ τ)], [τ │ (t47 ∗ τ)], [τ │ {[τ │ (t37 ∗ τ)], [τ │ {[τ │ (t69 ∗ τ)], [τ │ (t70 ∗ τ)], [τ │ (t48 ∗ τ)], [τ │ (t68 ∗ τ)], [τ │ (t56 ∗ τ)]}]}]}`
- **Block Frequency:** 495



![nested PAR_21 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_21.png)

### `[nested LOOP_20]`
- **Internal Structure:** `(⟨[τ │ ⟨[τ │ t46], {[τ │ (t62 ∗ τ)], [τ │ (t47 ∗ τ)], [τ │ {[τ │ (t37 ∗ τ)], [τ │ {[τ │ (t69 ∗ τ)], [τ │ (t70 ∗ τ)], [τ │ (t48 ∗ τ)], [τ │ (t68 ∗ τ)], [τ │ (t56 ∗ τ)]}]}]}⟩], [t65 │ t55]⟩ ∗ τ)`
- **Block Frequency:** 250

- **Max Loop Iterations:** `581`
- **Max Sub-Sequence Length:** `1163` steps (if one case consumes all iterations)

![nested LOOP_20 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_20.png)

### `[nested PAR_15]`
- **Internal Structure:** `{[τ │ (t40 ∗ τ)], ⟨[τ │ (⟨t39, [⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ τ)], (⟨[τ │ ⟨[τ │ t46], {[τ │ (t62 ∗ τ)], [τ │ (t47 ∗ τ)], [τ │ {[τ │ (t37 ∗ τ)], [τ │ {[τ │ (t69 ∗ τ)], [τ │ (t70 ∗ τ)], [τ │ (t48 ∗ τ)], [τ │ (t68 ∗ τ)], [τ │ (t56 ∗ τ)]}]}]}⟩], [t65 │ t55]⟩ ∗ τ)⟩}`
- **Block Frequency:** 250



![nested PAR_15 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_15.png)

### `[nested PAR_5]`
- **Internal Structure:** `{[τ │ (t34 ∗ τ)], ⟨(⟨[{t21, [τ │ {[τ │ (t17 ∗ τ)], [τ │ ⟨t24, t23⟩]}]} │ τ], [τ │ t22 │ ⟨t26, t27, [τ │ t28]⟩], [τ │ (t42 ∗ τ)]⟩ ∗ τ), [τ │ t71], {[τ │ (t40 ∗ τ)], ⟨[τ │ (⟨t39, [⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ τ)], (⟨[τ │ ⟨[τ │ t46], {[τ │ (t62 ∗ τ)], [τ │ (t47 ∗ τ)], [τ │ {[τ │ (t37 ∗ τ)], [τ │ {[τ │ (t69 ∗ τ)], [τ │ (t70 ∗ τ)], [τ │ (t48 ∗ τ)], [τ │ (t68 ∗ τ)], [τ │ (t56 ∗ τ)]}]}]}⟩], [t65 │ t55]⟩ ∗ τ)⟩}⟩}`
- **Block Frequency:** 250



![nested PAR_5 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_5.png)
