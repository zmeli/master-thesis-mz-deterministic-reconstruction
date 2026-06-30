# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_110101.xes` |
| **Noise Threshold** | `0.0` |
| **Fitness** | `1.0` |
| **Precision** | `0.12697417184560122` |
| **Total Cases in Log** | `250` |
| **Unique Activities** | `39` |
| **XOR Operators** | `40` |
| **LOOP Operators** | `15` |
| **SEQ Operators** | `20` |
| **PAR Operators** | `6` |
| **Binarization Additions** | `14` |
| **Tau Operators Added** | `29` |
| **Total Found Patterns** | `187` |
| **Verified Patterns** | `108` |
| **Discrepancy Patterns** | `10` |
| **Ghost Patterns** | `2` |
| **Nested LOOPs** | `15` |
| **Nested PARs** | `6` |
| **Tree Exposure (Strict, End-to-End % of N)** | `5.60%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `14.67%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `4.99%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `32.31%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `60.80%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `55.20%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `94.63%` |
| **Data Exposure, ST-only (% confirmed)** | `100.00%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `100.00%` |
| **Data Coverage, ST-only (% of real log)** | `8.26%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `26.10%` |
| **Data Coverage, Total (% of real log)** | `100.00%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `64.69%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `100.00%` |
| **Mean Absolute Exposure Volume (events/case)** | `28.39` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_110101__noise0.0__test.png)


```text
->( 't10', X( tau, ->( X( 't06', 't11' ), X( tau, +( X( tau, *( 't05', tau ) ), X( tau, *( 't04', tau ) ), X( tau, *( 't15', tau ), *( 't07', tau ) ) ) ), X( tau, 't16' ) ) ), X( tau, ->( X( tau, 't20' ), +( X( tau, *( 't34', tau ) ), ->( *( ->( +( 't21', X( tau, +( X( tau, *( 't17', tau ) ), X( tau, ->( 't24', 't23' ) ) ) ) ), X( tau, 't22', ->( 't26', 't27', X( tau, 't28' ) ) ), X( tau, *( 't42', 't41' ) ) ), tau ), X( tau, 't71' ), X( tau, +( X( tau, *( 't40', tau ) ), ->( X( tau, *( *( ->( 't39', X( tau, ->( 't43', 't44' ) ), *( 't36', tau ) ), tau ), 't32' ) ), *( ->( X( tau, 't46' ), *( *( X( 't47', ->( X( 't69', 't70', 't55', ->( X( 't62', 't48', 't37', 't56' ), X( tau, 't68' ) ) ), X( tau, 't52' ) ) ), tau ), tau ), X( tau, 't65' ) ), tau ) ) ) ) ) ) ) ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_110101__noise0.0__test.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST]` | `t10` | Exact Token Match | $\ge$ 250 | **250** | ✅ **VERIFIED** |
| `[ST]` | `t06` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `t11` | Exact Token Match | $\ge$ 146 | **146** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `t05` | Exact Token Match | $\ge$ 144 | **144** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t05⟩` | Exact Token Match | $\ge$ 144 | **144** | ✅ **VERIFIED** |
| `[ST (in LOOP_4)]` | `t04` | Exact Token Match | $\ge$ 3 | **3** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t04⟩` | Exact Token Match | $\ge$ 3 | **3** | ✅ **VERIFIED** |
| `[ST (in LOOP_5)]` | `t15` | Exact Token Match | $\ge$ 82 | **82** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t15⟩` | Exact Token Match | $\ge$ 82 | **82** | ✅ **VERIFIED** |
| `[ST (in LOOP_6)]` | `t07` | Exact Token Match | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t07⟩` | Exact Token Match | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[ST]` | `t16` | Exact Token Match | $\ge$ 84 | **84** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], τ⟩` | Exact Token Match | $\ge$ 60 | **125** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, [nested PAR_1], τ⟩` | Exact Token Match | $\ge$ 59 | **124** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, τ⟩` | Exact Token Match | $\ge$ 2 | **146** | ✅ **VERIFIED** |
| `[ST]` | `t20` | Exact Token Match | $\ge$ 205 | **205** | ✅ **VERIFIED** |
| `[ST (in LOOP_8)]` | `t34` | Exact Token Match | $\ge$ 164 | **164** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨t34⟩` | Exact Token Match | $\ge$ 164 | **164** | ✅ **VERIFIED** |
| `[ST (in PAR_10)]` | `t21` | Exact Token Match | $\ge$ 293 | **293** | ✅ **VERIFIED** |
| `[ST (in LOOP_12)]` | `t17` | Exact Token Match | $\ge$ 295 | **295** | ✅ **VERIFIED** |
| `[ST (in PAR_11)]` | `⟨t17⟩` | Exact Token Match | $\ge$ 295 | **295** | ✅ **VERIFIED** |
| `[ST (in PAR_11)]` | `t24` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[ST (in PAR_11)]` | `t23` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[ST (in PAR_11)]` | `⟨t24, t23⟩` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[AS (in LOOP_9)]` | `[nested PAR_10]` | Exact Token Match | $\ge$ 295 | **355** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `t22` | Exact Token Match | $\ge$ 145 | **145** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `t26` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `t27` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `t28` | Exact Token Match | $\ge$ 77 | **77** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨t27, τ⟩` | Exact Token Match | $\ge$ 41 | **118** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨t27, t28⟩` | Exact Token Match | $\ge$ 77 | **77** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨t26, t27, τ⟩` | Exact Token Match | $\ge$ 41 | **118** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨t26, t27, t28⟩` | Exact Token Match | $\ge$ 77 | **77** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨t26, t27⟩` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `t42` | Exact Token Match | $\ge$ 431 | **431** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `t41` | Exact Token Match | $\ge$ 179 | **179** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨t42⟩` | Exact Token Match | $\ge$ 73 | **431** | ✅ **VERIFIED** |
| `[AS (in LOOP_9)]` | `[nested LOOP_13]` | Exact Token Match | $\ge$ 1 | **252** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨[nested PAR_10], τ⟩` | Exact Token Match | $\ge$ 32 | **355** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨[nested PAR_10], t22⟩` | Exact Token Match | $\ge$ 145 | **145** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨[nested PAR_10], t26, t27, τ⟩` | Exact Token Match | $\ge$ 41 | **118** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨[nested PAR_10], t26, t27, t28⟩` | Exact Token Match | $\ge$ 77 | **77** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨[nested PAR_10], t26, t27⟩` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨[nested PAR_10], t26⟩` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[AS (in PAR_7)]` | `[nested LOOP_9]` | Exact Token Match | $\ge$ 1 | **10** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `t71` | Exact Token Match | $\ge$ 41 | **41** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `t40` | Exact Token Match | $\ge$ 221 | **221** | ✅ **VERIFIED** |
| `[ST (in PAR_17)]` | `⟨t40⟩` | Exact Token Match | $\ge$ 221 | **221** | ✅ **VERIFIED** |
| `[ST (in LOOP_20)]` | `t39` | Exact Token Match | $\ge$ 391 | **391** | ✅ **VERIFIED** |
| `[ST (in LOOP_20)]` | `t43` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_20)]` | `t44` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_20)]` | `⟨t43, t44⟩` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_21)]` | `t36` | Exact Token Match | $\ge$ 523 | **523** | ✅ **VERIFIED** |
| `[AS (in LOOP_20)]` | `[nested LOOP_21]` | Exact Token Match | $\ge$ 1 | **208** | ✅ **VERIFIED** |
| `[ST (in LOOP_20)]` | `⟨t43, t44, [nested LOOP_21]⟩` | Exact Token Match | $\ge$ 1 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_20)]` | `⟨t44, [nested LOOP_21]⟩` | Exact Token Match | $\ge$ 1 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_20)]` | `⟨t39, t43, t44, [nested LOOP_21]⟩` | Exact Token Match | $\ge$ 1 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_20)]` | `⟨t39, τ⟩` | Exact Token Match | $\ge$ 201 | **391** | ✅ **VERIFIED** |
| `[ST (in LOOP_20)]` | `⟨t39, t43, t44⟩` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_20)]` | `⟨t39, t43⟩` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_19)]` | `t32` | Exact Token Match | $\ge$ 155 | **155** | ✅ **VERIFIED** |
| `[ST (in PAR_17)]` | `⟨t39, [nested XOR_22]⟩` | Exact Token Match | $\ge$ 81.0 | **190** | ✅ **VERIFIED** |
| `[AS (in PAR_17)]` | `[nested LOOP_19]` | Exact Token Match | $\ge$ 1 | **134** | ✅ **VERIFIED** |
| `[ST (in LOOP_23)]` | `t46` | Exact Token Match | $\ge$ 420 | **420** | ✅ **VERIFIED** |
| `[ST (in LOOP_25)]` | `t47` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_25)]` | `t69` | Exact Token Match | $\ge$ 170 | **170** | ✅ **VERIFIED** |
| `[ST (in LOOP_25)]` | `t70` | Exact Token Match | $\ge$ 150 | **150** | ✅ **VERIFIED** |
| `[ST (in LOOP_25)]` | `t55` | Exact Token Match | $\ge$ 622 | **622** | ✅ **VERIFIED** |
| `[ST (in LOOP_25)]` | `t62` | Exact Token Match | $\ge$ 225 | **225** | ✅ **VERIFIED** |
| `[ST (in LOOP_25)]` | `t48` | Exact Token Match | $\ge$ 188 | **188** | ✅ **VERIFIED** |
| `[ST (in LOOP_25)]` | `t37` | Exact Token Match | $\ge$ 180 | **180** | ✅ **VERIFIED** |
| `[ST (in LOOP_25)]` | `t56` | Exact Token Match | $\ge$ 606 | **606** | ✅ **VERIFIED** |
| `[ST (in LOOP_25)]` | `t68` | Exact Token Match | $\ge$ 188 | **188** | ✅ **VERIFIED** |
| `[ST (in LOOP_25)]` | `⟨t62, τ⟩` | Exact Token Match | $\ge$ 37 | **225** | ✅ **VERIFIED** |
| `[ST (in LOOP_25)]` | `⟨t56, τ⟩` | Exact Token Match | $\ge$ 418 | **606** | ✅ **VERIFIED** |
| `[ST (in LOOP_25)]` | `t52` | Exact Token Match | $\ge$ 248 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_25)]` | `⟨t55, τ⟩` | Exact Token Match | $\ge$ 374 | **622** | ✅ **VERIFIED** |
| `[ST (in LOOP_25)]` | `⟨t56, τ, τ⟩` | Exact Token Match | $\ge$ 170 | **606** | ✅ **VERIFIED** |
| `[ST (in LOOP_24)]` | `⟨t47⟩` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[AS (in LOOP_23)]` | `[nested LOOP_24]` | Exact Token Match | $\ge$ 1 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_23)]` | `t65` | Exact Token Match | $\ge$ 432 | **432** | ✅ **VERIFIED** |
| `[ST (in LOOP_23)]` | `⟨[nested LOOP_24], t65⟩` | Exact Token Match | $\ge$ 1 | **432** | ✅ **VERIFIED** |
| `[AS (in PAR_17)]` | `[nested LOOP_23]` | Exact Token Match | $\ge$ 1 | **16** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_7]` | Exact Token Match | $\ge$ 236 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_7]⟩` | Exact Token Match | $\ge$ 31 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, [nested PAR_7]⟩` | Exact Token Match | $\ge$ 205 | **205** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t20, [nested PAR_7]⟩` | Exact Token Match | $\ge$ 58 | **205** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, [nested PAR_1], τ, t20, [nested PAR_7]⟩` | Exact Token Match | $\ge$ 28 | **80** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, [nested PAR_1], t16, t20, [nested PAR_7]⟩` | Exact Token Match | $\ge$ 52 | **69** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t20⟩` | Exact Token Match | $\ge$ 58 | **205** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, [nested PAR_1], τ, t20⟩` | Exact Token Match | $\ge$ 28 | **80** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, [nested PAR_1], t16, t20⟩` | Exact Token Match | $\ge$ 52 | **69** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], τ, t20, [nested PAR_7]⟩` | Exact Token Match | $\ge$ 29 | **80** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], t16, t20, [nested PAR_7]⟩` | Exact Token Match | $\ge$ 53 | **69** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t20, [nested PAR_7]⟩` | Exact Token Match | $\ge$ 29 | **205** | ✅ **VERIFIED** |
| `[ST]` | `⟨t16, t20, [nested PAR_7]⟩` | Exact Token Match | $\ge$ 53 | **84** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ, t20, [nested PAR_7]⟩` | Exact Token Match | $\ge$ 58 | **205** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, [nested PAR_1], τ, t20, [nested PAR_7]⟩` | Exact Token Match | $\ge$ 28 | **80** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, [nested PAR_1], t16, t20, [nested PAR_7]⟩` | Exact Token Match | $\ge$ 52 | **69** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 14 | **250** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ, t20⟩` | Exact Token Match | $\ge$ 58 | **205** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, [nested PAR_1], τ, t20⟩` | Exact Token Match | $\ge$ 28 | **80** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, [nested PAR_1], t16, t20⟩` | Exact Token Match | $\ge$ 52 | **69** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 89 | **250** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, [nested PAR_1], τ⟩` | Exact Token Match | $\ge$ 59 | **124** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, τ⟩` | Exact Token Match | $\ge$ 2 | **146** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11⟩` | Exact Token Match | $\ge$ 146 | **146** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_1]` | Exact Token Match | $\ge$ 144 | **125** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_1], t16⟩` | Exact Token Match | $\ge$ 84 | **69** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t11, [nested PAR_1], t16⟩` | Exact Token Match | $\ge$ 83 | **69** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t11, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 143 | **124** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_10)]` | `[nested PAR_11]` | Exact Token Match | $\ge$ 295 | **112** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_7)]` | `⟨[nested PAR_10], [nested XOR_16]⟩` | Exact Token Match | $\ge$ 32.0 | **10** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_7)]` | `[nested PAR_17]` | Exact Token Match | $\ge$ 236 | **6** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_7)]` | `⟨τ, [nested PAR_17]⟩` | Exact Token Match | $\ge$ 195 | **6** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, t11, [nested PAR_1], t16⟩` | Exact Token Match | $\ge$ 83 | **69** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, t11, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 143 | **124** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_1)]` | `[nested PAR_3]` | Exact Token Match | $\ge$ 84 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_7)]` | `⟨t71, [nested PAR_17]⟩` | Exact Token Match | $\ge$ 41 | **0** | ❌ **GHOST PATTERN** |

## Audit Summary
- **Perfect Pattern Verifications:** 108
- **Frequency Discrepancies:** 10
- **Ghost Patterns (Fatal):** 2
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 5.60%
- **Tree Exposure (Strict, Fragment-Level % of N):** 14.67%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 4.99%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 32.31%
- **Total Forced Volume (incl. unresolved AS, % of N):** 60.80%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 55.20%
- **Data Exposure (Confirmed % of Claimed Volume):** 94.63%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 100.00%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 100.00%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 8.26%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 26.10%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 100.00%
- **Max Fractional Exposure (Worst-Case Normalized):** 64.69% (expected length: 2269.78 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 100.00% (expected length: 33.21 events)
- **Mean Absolute Exposure Volume:** 28.39 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_2]`
- **Internal Structure:** `(t05 ∗ τ)`
- **Block Frequency:** 144

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_2 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.0__test_nested_LOOP_2.png)

### `[nested LOOP_4]`
- **Internal Structure:** `(t04 ∗ τ)`
- **Block Frequency:** 3

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_4 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.0__test_nested_LOOP_4.png)

### `[nested LOOP_5]`
- **Internal Structure:** `(t15 ∗ τ)`
- **Block Frequency:** 82

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_5 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.0__test_nested_LOOP_5.png)

### `[nested LOOP_6]`
- **Internal Structure:** `(t07 ∗ τ)`
- **Block Frequency:** 2

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_6 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.0__test_nested_LOOP_6.png)

### `[nested PAR_3]`
- **Internal Structure:** `{[τ │ (t04 ∗ τ)], [τ │ (t15 ∗ τ) │ (t07 ∗ τ)]}`
- **Block Frequency:** 84



![nested PAR_3 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.0__test_nested_PAR_3.png)

### `[nested PAR_1]`
- **Internal Structure:** `{[τ │ (t05 ∗ τ)], [{[τ │ (t04 ∗ τ)], [τ │ (t15 ∗ τ) │ (t07 ∗ τ)]} │ τ]}`
- **Block Frequency:** 144



![nested PAR_1 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.0__test_nested_PAR_1.png)

### `[nested LOOP_8]`
- **Internal Structure:** `(t34 ∗ τ)`
- **Block Frequency:** 164

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_8 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.0__test_nested_LOOP_8.png)

### `[nested LOOP_12]`
- **Internal Structure:** `(t17 ∗ τ)`
- **Block Frequency:** 295

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_12 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.0__test_nested_LOOP_12.png)

### `[nested PAR_11]`
- **Internal Structure:** `{[τ │ (t17 ∗ τ)], [τ │ ⟨t24, t23⟩]}`
- **Block Frequency:** 295



![nested PAR_11 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.0__test_nested_PAR_11.png)

### `[nested PAR_10]`
- **Internal Structure:** `{[t21 │ τ], [τ │ {[τ │ (t17 ∗ τ)], [τ │ ⟨t24, t23⟩]}]}`
- **Block Frequency:** 295



![nested PAR_10 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.0__test_nested_PAR_10.png)

### `[nested LOOP_13]`
- **Internal Structure:** `(t42 ∗ t41)`
- **Block Frequency:** 252

- **Max Loop Iterations:** `179`
- **Max Sub-Sequence Length:** `359` steps (if one case consumes all iterations)

![nested LOOP_13 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.0__test_nested_LOOP_13.png)

### `[nested LOOP_9]`
- **Internal Structure:** `(⟨{[t21 │ τ], [τ │ {[τ │ (t17 ∗ τ)], [τ │ ⟨t24, t23⟩]}]}, [⟨[τ │ t22 │ ⟨t26, t27, [τ │ t28]⟩], [τ │ (t42 ∗ t41)]⟩ │ τ]⟩ ∗ τ)`
- **Block Frequency:** 236

- **Max Loop Iterations:** `59`
- **Max Sub-Sequence Length:** `119` steps (if one case consumes all iterations)

![nested LOOP_9 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.0__test_nested_LOOP_9.png)

### `[nested XOR_14]`
- **Internal Structure:** `[t22 │ ⟨t26, t27, [τ │ t28]⟩]`
- **Block Frequency:** 263



![nested XOR_14 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.0__test_nested_XOR_14.png)

### `[nested XOR_15]`
- **Internal Structure:** `[τ │ (t42 ∗ t41)]`
- **Block Frequency:** 263



![nested XOR_15 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.0__test_nested_XOR_15.png)

### `[nested XOR_16]`
- **Internal Structure:** `[⟨[τ │ t22 │ ⟨t26, t27, [τ │ t28]⟩], [τ │ (t42 ∗ t41)]⟩ │ τ]`
- **Block Frequency:** 295



![nested XOR_16 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.0__test_nested_XOR_16.png)

### `[nested LOOP_18]`
- **Internal Structure:** `(t40 ∗ τ)`
- **Block Frequency:** 221

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_18 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.0__test_nested_LOOP_18.png)

### `[nested LOOP_21]`
- **Internal Structure:** `(t36 ∗ τ)`
- **Block Frequency:** 190

- **Max Loop Iterations:** `333`
- **Max Sub-Sequence Length:** `667` steps (if one case consumes all iterations)

![nested LOOP_21 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.0__test_nested_LOOP_21.png)

### `[nested LOOP_20]`
- **Internal Structure:** `(⟨t39, [⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ τ)`
- **Block Frequency:** 391

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_20 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.0__test_nested_LOOP_20.png)

### `[nested LOOP_19]`
- **Internal Structure:** `((⟨t39, [⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ τ) ∗ t32)`
- **Block Frequency:** 236

- **Max Loop Iterations:** `155`
- **Max Sub-Sequence Length:** `311` steps (if one case consumes all iterations)

![nested LOOP_19 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.0__test_nested_LOOP_19.png)

### `[nested XOR_22]`
- **Internal Structure:** `[⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]`
- **Block Frequency:** 391



![nested XOR_22 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.0__test_nested_XOR_22.png)

### `[nested LOOP_25]`
- **Internal Structure:** `([t47 │ ⟨[t69 │ t70 │ t55 │ ⟨[t62 │ t48 │ t37 │ t56], [τ │ t68]⟩], [τ │ t52]⟩] ∗ τ)`
- **Block Frequency:** 2331

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_25 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.0__test_nested_LOOP_25.png)

### `[nested LOOP_24]`
- **Internal Structure:** `(([t47 │ ⟨[t69 │ t70 │ t55 │ ⟨[t62 │ t48 │ t37 │ t56], [τ │ t68]⟩], [τ │ t52]⟩] ∗ τ) ∗ τ)`
- **Block Frequency:** 432

- **Max Loop Iterations:** `1899`
- **Max Sub-Sequence Length:** `3799` steps (if one case consumes all iterations)

![nested LOOP_24 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.0__test_nested_LOOP_24.png)

### `[nested LOOP_23]`
- **Internal Structure:** `(⟨[τ │ t46], (([t47 │ ⟨[t69 │ t70 │ t55 │ ⟨[t62 │ t48 │ t37 │ t56], [τ │ t68]⟩], [τ │ t52]⟩] ∗ τ) ∗ τ), [τ │ t65]⟩ ∗ τ)`
- **Block Frequency:** 236

- **Max Loop Iterations:** `196`
- **Max Sub-Sequence Length:** `393` steps (if one case consumes all iterations)

![nested LOOP_23 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.0__test_nested_LOOP_23.png)

### `[nested XOR_26]`
- **Internal Structure:** `[τ │ t46]`
- **Block Frequency:** 432



![nested XOR_26 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.0__test_nested_XOR_26.png)

### `[nested PAR_17]`
- **Internal Structure:** `{[τ │ (t40 ∗ τ)], ⟨[τ │ ((⟨t39, [⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ τ) ∗ t32)], (⟨[τ │ t46], (([t47 │ ⟨[t69 │ t70 │ t55 │ ⟨[t62 │ t48 │ t37 │ t56], [τ │ t68]⟩], [τ │ t52]⟩] ∗ τ) ∗ τ), [τ │ t65]⟩ ∗ τ)⟩}`
- **Block Frequency:** 236



![nested PAR_17 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.0__test_nested_PAR_17.png)

### `[nested PAR_7]`
- **Internal Structure:** `{[τ │ (t34 ∗ τ)], ⟨(⟨{[t21 │ τ], [τ │ {[τ │ (t17 ∗ τ)], [τ │ ⟨t24, t23⟩]}]}, [⟨[τ │ t22 │ ⟨t26, t27, [τ │ t28]⟩], [τ │ (t42 ∗ t41)]⟩ │ τ]⟩ ∗ τ), [τ │ t71], [τ │ {[τ │ (t40 ∗ τ)], ⟨[τ │ ((⟨t39, [⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ τ) ∗ t32)], (⟨[τ │ t46], (([t47 │ ⟨[t69 │ t70 │ t55 │ ⟨[t62 │ t48 │ t37 │ t56], [τ │ t68]⟩], [τ │ t52]⟩] ∗ τ) ∗ τ), [τ │ t65]⟩ ∗ τ)⟩}]⟩}`
- **Block Frequency:** 236



![nested PAR_7 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.0__test_nested_PAR_7.png)
