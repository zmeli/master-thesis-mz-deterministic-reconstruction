# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_001101.xes` |
| **Noise Threshold** | `0.2` |
| **Fitness** | `0.975943555603895` |
| **Precision** | `0.2804424614240565` |
| **Total Cases in Log** | `250` |
| **Unique Activities** | `35` |
| **XOR Operators** | `28` |
| **LOOP Operators** | `18` |
| **SEQ Operators** | `22` |
| **PAR Operators** | `7` |
| **Binarization Additions** | `13` |
| **Tau Operators Added** | `17` |
| **Total Found Patterns** | `170` |
| **Verified Patterns** | `103` |
| **Discrepancy Patterns** | `13` |
| **Ghost Patterns** | `1` |
| **Nested LOOPs** | `18` |
| **Nested PARs** | `7` |
| **Tree Exposure (Strict, End-to-End % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `12.58%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `7.17%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `52.93%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `0.00%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `0.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `93.79%` |
| **Data Exposure, ST-only (% confirmed)** | `99.26%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `99.79%` |
| **Data Coverage, ST-only (% of real log)** | `11.42%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `53.27%` |
| **Data Coverage, Total (% of real log)** | `99.85%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `2.53%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `100.00%` |
| **Mean Absolute Exposure Volume (events/case)** | `21.55` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_001101__noise0.2.png)


```text
->( 't10', X( tau, ->( X( 't06', 't11' ), +( *( 't05', tau ), X( tau, *( 't15', tau ), *( 't04', tau ) ) ), X( tau, 't16' ) ) ), X( tau, 't20' ), +( *( 't17', tau ), ->( *( 't21', tau ), X( tau, ->( 't24', 't23' ) ) ) ), X( tau, 't22' ), +( X( tau, *( 't34', tau ) ), ->( X( tau, ->( 't26', 't27', X( tau, 't28' ) ) ), *( 't42', tau ), X( tau, 't71' ), +( X( tau, *( 't40', tau ) ), ->( *( ->( 't39', X( tau, ->( 't43', 't44' ) ), *( 't36', tau ) ), tau ), *( ->( X( tau, ->( X( tau, 't46' ), X( *( 't69', tau ), *( 't70', tau ), +( X( tau, *( 't62', tau ) ), X( tau, *( 't37', tau ) ), *( 't56', tau ), X( tau, ->( *( 't47', tau ), X( tau, ->( 't48', *( 't68', tau ) ) ) ) ) ) ) ) ), X( 't65', 't55' ) ), tau ) ) ) ) ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_001101__noise0.2.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST]` | `t10` | Exact Token Match | $\ge$ 250 | **250** | ✅ **VERIFIED** |
| `[ST]` | `t06` | Exact Token Match | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[ST]` | `t11` | Exact Token Match | $\ge$ 133 | **133** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `t05` | Exact Token Match | $\ge$ 117 | **117** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t05⟩` | Exact Token Match | $\ge$ 49 | **117** | ✅ **VERIFIED** |
| `[AS (in PAR_1)]` | `[nested LOOP_2]` | Exact Token Match | $\ge$ 1 | **117** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t15` | Exact Token Match | $\ge$ 77 | **77** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t15⟩` | Exact Token Match | $\ge$ 77 | **77** | ✅ **VERIFIED** |
| `[ST (in LOOP_4)]` | `t04` | Exact Token Match | $\ge$ 6 | **6** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t04⟩` | Exact Token Match | $\ge$ 6 | **6** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_1]` | Exact Token Match | $\ge$ 83 | **118** | ✅ **VERIFIED** |
| `[ST]` | `t16` | Exact Token Match | $\ge$ 64 | **64** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], τ⟩` | Exact Token Match | $\ge$ 19 | **118** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, [nested PAR_1], τ⟩` | Exact Token Match | $\ge$ 17 | **116** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, τ⟩` | Exact Token Match | $\ge$ 50 | **133** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 81 | **116** | ✅ **VERIFIED** |
| `[ST]` | `t20` | Exact Token Match | $\ge$ 192 | **192** | ✅ **VERIFIED** |
| `[ST (in LOOP_6)]` | `t17` | Exact Token Match | $\ge$ 266 | **266** | ✅ **VERIFIED** |
| `[AS (in PAR_5)]` | `[nested LOOP_6]` | Exact Token Match | $\ge$ 1 | **266** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `t21` | Exact Token Match | $\ge$ 273 | **273** | ✅ **VERIFIED** |
| `[AS (in PAR_5)]` | `[nested LOOP_7]` | Exact Token Match | $\ge$ 1 | **273** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t24` | Exact Token Match | $\ge$ 110 | **110** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t23` | Exact Token Match | $\ge$ 110 | **110** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t24, t23⟩` | Exact Token Match | $\ge$ 110 | **110** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨[nested LOOP_7], t24, t23⟩` | Exact Token Match | $\ge$ 1 | **110** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨[nested LOOP_7], t24⟩` | Exact Token Match | $\ge$ 1 | **110** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_5]` | Exact Token Match | $\ge$ 110 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `t34` | Exact Token Match | $\ge$ 144 | **144** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨t34⟩` | Exact Token Match | $\ge$ 144 | **144** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `t26` | Exact Token Match | $\ge$ 110 | **110** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `t27` | Exact Token Match | $\ge$ 110 | **110** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `t28` | Exact Token Match | $\ge$ 72 | **72** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨t27, τ⟩` | Exact Token Match | $\ge$ 38 | **110** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨t27, t28⟩` | Exact Token Match | $\ge$ 72 | **72** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨t26, t27, τ⟩` | Exact Token Match | $\ge$ 38 | **110** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨t26, t27, t28⟩` | Exact Token Match | $\ge$ 72 | **72** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨t26, t27⟩` | Exact Token Match | $\ge$ 110 | **110** | ✅ **VERIFIED** |
| `[ST (in LOOP_10)]` | `t42` | Exact Token Match | $\ge$ 316 | **316** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨t42⟩` | Exact Token Match | $\ge$ 184 | **316** | ✅ **VERIFIED** |
| `[AS (in PAR_8)]` | `[nested LOOP_10]` | Exact Token Match | $\ge$ 1 | **316** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `t71` | Exact Token Match | $\ge$ 38 | **38** | ✅ **VERIFIED** |
| `[ST (in LOOP_12)]` | `t40` | Exact Token Match | $\ge$ 229 | **229** | ✅ **VERIFIED** |
| `[ST (in PAR_11)]` | `⟨t40⟩` | Exact Token Match | $\ge$ 229 | **229** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `t39` | Exact Token Match | $\ge$ 337 | **337** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `t43` | Exact Token Match | $\ge$ 154 | **154** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `t44` | Exact Token Match | $\ge$ 154 | **154** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `⟨t43, t44⟩` | Exact Token Match | $\ge$ 154 | **154** | ✅ **VERIFIED** |
| `[ST (in LOOP_14)]` | `t36` | Exact Token Match | $\ge$ 438 | **438** | ✅ **VERIFIED** |
| `[AS (in LOOP_13)]` | `[nested LOOP_14]` | Exact Token Match | $\ge$ 1 | **210** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `⟨t43, t44, [nested LOOP_14]⟩` | Exact Token Match | $\ge$ 1 | **154** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `⟨t44, [nested LOOP_14]⟩` | Exact Token Match | $\ge$ 1 | **154** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `⟨t39, t43, t44, [nested LOOP_14]⟩` | Exact Token Match | $\ge$ 1 | **154** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `⟨t39, τ⟩` | Exact Token Match | $\ge$ 183 | **337** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `⟨t39, t43, t44⟩` | Exact Token Match | $\ge$ 154 | **154** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `⟨t39, t43⟩` | Exact Token Match | $\ge$ 154 | **154** | ✅ **VERIFIED** |
| `[ST (in PAR_11)]` | `⟨t39, τ⟩` | Exact Token Match | $\ge$ 9 | **337** | ✅ **VERIFIED** |
| `[ST (in PAR_11)]` | `⟨t39, [nested XOR_15]⟩` | Exact Token Match | $\ge$ 154.0 | **154** | ✅ **VERIFIED** |
| `[AS (in PAR_11)]` | `[nested LOOP_13]` | Exact Token Match | $\ge$ 1 | **154** | ✅ **VERIFIED** |
| `[ST (in LOOP_16)]` | `t46` | Exact Token Match | $\ge$ 327 | **327** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `t69` | Exact Token Match | $\ge$ 113 | **113** | ✅ **VERIFIED** |
| `[ST (in LOOP_16)]` | `⟨t69⟩` | Exact Token Match | $\ge$ 113 | **113** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `t70` | Exact Token Match | $\ge$ 93 | **93** | ✅ **VERIFIED** |
| `[ST (in LOOP_16)]` | `⟨t70⟩` | Exact Token Match | $\ge$ 93 | **93** | ✅ **VERIFIED** |
| `[ST (in LOOP_20)]` | `t62` | Exact Token Match | $\ge$ 264 | **264** | ✅ **VERIFIED** |
| `[ST (in PAR_19)]` | `⟨t62⟩` | Exact Token Match | $\ge$ 264 | **264** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `t37` | Exact Token Match | $\ge$ 192 | **192** | ✅ **VERIFIED** |
| `[ST (in PAR_21)]` | `⟨t37⟩` | Exact Token Match | $\ge$ 192 | **192** | ✅ **VERIFIED** |
| `[ST (in LOOP_24)]` | `t56` | Exact Token Match | $\ge$ 495 | **495** | ✅ **VERIFIED** |
| `[AS (in PAR_23)]` | `[nested LOOP_24]` | Exact Token Match | $\ge$ 1 | **495** | ✅ **VERIFIED** |
| `[ST (in LOOP_25)]` | `t47` | Exact Token Match | $\ge$ 222 | **222** | ✅ **VERIFIED** |
| `[ST (in PAR_23)]` | `⟨t47⟩` | Exact Token Match | $\ge$ 148 | **222** | ✅ **VERIFIED** |
| `[AS (in PAR_23)]` | `[nested LOOP_25]` | Exact Token Match | $\ge$ 1 | **222** | ✅ **VERIFIED** |
| `[ST (in PAR_23)]` | `t48` | Exact Token Match | $\ge$ 185 | **185** | ✅ **VERIFIED** |
| `[ST (in LOOP_26)]` | `t68` | Exact Token Match | $\ge$ 185 | **185** | ✅ **VERIFIED** |
| `[ST (in PAR_23)]` | `⟨t68⟩` | Exact Token Match | $\ge$ 185 | **185** | ✅ **VERIFIED** |
| `[ST (in PAR_23)]` | `⟨t48, t68⟩` | Exact Token Match | $\ge$ 185 | **185** | ✅ **VERIFIED** |
| `[ST (in PAR_23)]` | `⟨t47, t48, t68⟩` | Exact Token Match | $\ge$ 148 | **167** | ✅ **VERIFIED** |
| `[ST (in PAR_23)]` | `⟨[nested LOOP_25], t48, t68⟩` | Exact Token Match | $\ge$ 1 | **167** | ✅ **VERIFIED** |
| `[ST (in PAR_23)]` | `⟨t47, t48⟩` | Exact Token Match | $\ge$ 148 | **167** | ✅ **VERIFIED** |
| `[ST (in PAR_23)]` | `⟨[nested LOOP_25], t48⟩` | Exact Token Match | $\ge$ 1 | **167** | ✅ **VERIFIED** |
| `[ST (in LOOP_16)]` | `⟨t46, [nested PAR_19]⟩` | Exact Token Match | $\ge$ 121 | **254** | ✅ **VERIFIED** |
| `[ST (in LOOP_16)]` | `t65` | Exact Token Match | $\ge$ 366 | **366** | ✅ **VERIFIED** |
| `[ST (in LOOP_16)]` | `t55` | Exact Token Match | $\ge$ 465 | **465** | ✅ **VERIFIED** |
| `[AS (in PAR_11)]` | `[nested LOOP_16]` | Exact Token Match | $\ge$ 1 | **20** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨t42, τ⟩` | Exact Token Match | $\ge$ 146 | **316** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨τ, t42, τ⟩` | Exact Token Match | $\ge$ 36 | **316** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨τ, t42⟩` | Exact Token Match | $\ge$ 74 | **316** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨t26, t27, t28, t42⟩` | Exact Token Match | $\ge$ 6 | **72** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_8]⟩` | Exact Token Match | $\ge$ 110 | **248** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t22, [nested PAR_8]⟩` | Exact Token Match | $\ge$ 30 | **127** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t22⟩` | Exact Token Match | $\ge$ 30 | **130** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 52 | **192** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, τ⟩` | Exact Token Match | $\ge$ 82 | **192** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t20⟩` | Exact Token Match | $\ge$ 57 | **192** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, [nested PAR_1], t16, t20⟩` | Exact Token Match | $\ge$ 4 | **53** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ, t20⟩` | Exact Token Match | $\ge$ 57 | **192** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, [nested PAR_1], t16, t20⟩` | Exact Token Match | $\ge$ 4 | **53** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 115 | **250** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, [nested PAR_1], τ⟩` | Exact Token Match | $\ge$ 17 | **116** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 81 | **116** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, τ⟩` | Exact Token Match | $\ge$ 50 | **133** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06⟩` | Exact Token Match | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11⟩` | Exact Token Match | $\ge$ 133 | **133** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], t16⟩` | Exact Token Match | $\ge$ 64 | **53** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t11, [nested PAR_1], t16⟩` | Exact Token Match | $\ge$ 62 | **53** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t22` | Exact Token Match | $\ge$ 140 | **130** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_21)]` | `[nested PAR_23]` | Exact Token Match | $\ge$ 185 | **162** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_19)]` | `[nested PAR_21]` | Exact Token Match | $\ge$ 192 | **139** | ⚠️ **DISCREPANCY** |
| `[AS (in LOOP_16)]` | `[nested PAR_19]` | Exact Token Match | $\ge$ 264 | **206** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_8)]` | `[nested PAR_11]` | Exact Token Match | $\ge$ 250 | **6** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_8)]` | `⟨τ, [nested PAR_11]⟩` | Exact Token Match | $\ge$ 212 | **6** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_8)]` | `⟨t42, τ, [nested PAR_11]⟩` | Exact Token Match | $\ge$ 146 | **5** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_8)]` | `⟨τ, t42, τ, [nested PAR_11]⟩` | Exact Token Match | $\ge$ 36 | **5** | ⚠️ **DISCREPANCY** |
| `[AS]` | `[nested PAR_8]` | Exact Token Match | $\ge$ 250 | **248** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t22, [nested PAR_8]⟩` | Exact Token Match | $\ge$ 140 | **127** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, t11, [nested PAR_1], t16⟩` | Exact Token Match | $\ge$ 62 | **53** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_8)]` | `⟨t71, [nested PAR_11]⟩` | Exact Token Match | $\ge$ 38 | **0** | ❌ **GHOST PATTERN** |

## Audit Summary
- **Perfect Pattern Verifications:** 103
- **Frequency Discrepancies:** 13
- **Ghost Patterns (Fatal):** 1
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 12.58%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 7.17%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 52.93%
- **Total Forced Volume (incl. unresolved AS, % of N):** 0.00%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 0.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 93.79%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 99.26%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 99.79%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 11.42%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 53.27%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 99.85%
- **Max Fractional Exposure (Worst-Case Normalized):** 2.53% (expected length: 1804.66 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 100.00% (expected length: 27.00 events)
- **Mean Absolute Exposure Volume:** 21.55 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_2]`
- **Internal Structure:** `(t05 ∗ τ)`
- **Block Frequency:** 83

- **Max Loop Iterations:** `34`
- **Max Sub-Sequence Length:** `69` steps (if one case consumes all iterations)

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
- **Internal Structure:** `{(t05 ∗ τ), [τ │ (t15 ∗ τ) │ (t04 ∗ τ)]}`
- **Block Frequency:** 83



![nested PAR_1 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_1.png)

### `[nested LOOP_6]`
- **Internal Structure:** `(t17 ∗ τ)`
- **Block Frequency:** 110

- **Max Loop Iterations:** `156`
- **Max Sub-Sequence Length:** `313` steps (if one case consumes all iterations)

![nested LOOP_6 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_6.png)

### `[nested LOOP_7]`
- **Internal Structure:** `(t21 ∗ τ)`
- **Block Frequency:** 110

- **Max Loop Iterations:** `163`
- **Max Sub-Sequence Length:** `327` steps (if one case consumes all iterations)

![nested LOOP_7 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_7.png)

### `[nested PAR_5]`
- **Internal Structure:** `{(t17 ∗ τ), ⟨(t21 ∗ τ), [τ │ ⟨t24, t23⟩]⟩}`
- **Block Frequency:** 110



![nested PAR_5 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_5.png)

### `[nested LOOP_9]`
- **Internal Structure:** `(t34 ∗ τ)`
- **Block Frequency:** 144

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_9 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_9.png)

### `[nested LOOP_10]`
- **Internal Structure:** `(t42 ∗ τ)`
- **Block Frequency:** 250

- **Max Loop Iterations:** `66`
- **Max Sub-Sequence Length:** `133` steps (if one case consumes all iterations)

![nested LOOP_10 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_10.png)

### `[nested LOOP_12]`
- **Internal Structure:** `(t40 ∗ τ)`
- **Block Frequency:** 229

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_12 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_12.png)

### `[nested LOOP_14]`
- **Internal Structure:** `(t36 ∗ τ)`
- **Block Frequency:** 154

- **Max Loop Iterations:** `284`
- **Max Sub-Sequence Length:** `569` steps (if one case consumes all iterations)

![nested LOOP_14 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_14.png)

### `[nested LOOP_13]`
- **Internal Structure:** `(⟨t39, [⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ τ)`
- **Block Frequency:** 250

- **Max Loop Iterations:** `87`
- **Max Sub-Sequence Length:** `175` steps (if one case consumes all iterations)

![nested LOOP_13 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_13.png)

### `[nested XOR_15]`
- **Internal Structure:** `[⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]`
- **Block Frequency:** 337



![nested XOR_15 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_XOR_15.png)

### `[nested LOOP_17]`
- **Internal Structure:** `(t69 ∗ τ)`
- **Block Frequency:** 113

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_17 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_17.png)

### `[nested LOOP_18]`
- **Internal Structure:** `(t70 ∗ τ)`
- **Block Frequency:** 93

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_18 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_18.png)

### `[nested LOOP_20]`
- **Internal Structure:** `(t62 ∗ τ)`
- **Block Frequency:** 264

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_20 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_20.png)

### `[nested LOOP_22]`
- **Internal Structure:** `(t37 ∗ τ)`
- **Block Frequency:** 192

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_22 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_22.png)

### `[nested LOOP_24]`
- **Internal Structure:** `(t56 ∗ τ)`
- **Block Frequency:** 185

- **Max Loop Iterations:** `310`
- **Max Sub-Sequence Length:** `621` steps (if one case consumes all iterations)

![nested LOOP_24 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_24.png)

### `[nested LOOP_25]`
- **Internal Structure:** `(t47 ∗ τ)`
- **Block Frequency:** 185

- **Max Loop Iterations:** `37`
- **Max Sub-Sequence Length:** `75` steps (if one case consumes all iterations)

![nested LOOP_25 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_25.png)

### `[nested LOOP_26]`
- **Internal Structure:** `(t68 ∗ τ)`
- **Block Frequency:** 185

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_26 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_26.png)

### `[nested PAR_23]`
- **Internal Structure:** `{(t56 ∗ τ), [τ │ ⟨(t47 ∗ τ), [τ │ ⟨t48, (t68 ∗ τ)⟩]⟩]}`
- **Block Frequency:** 185



![nested PAR_23 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_23.png)

### `[nested PAR_21]`
- **Internal Structure:** `{[τ │ (t37 ∗ τ)], [{(t56 ∗ τ), [τ │ ⟨(t47 ∗ τ), [τ │ ⟨t48, (t68 ∗ τ)⟩]⟩]} │ τ]}`
- **Block Frequency:** 192



![nested PAR_21 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_21.png)

### `[nested PAR_19]`
- **Internal Structure:** `{[τ │ (t62 ∗ τ)], [{[τ │ (t37 ∗ τ)], [{(t56 ∗ τ), [τ │ ⟨(t47 ∗ τ), [τ │ ⟨t48, (t68 ∗ τ)⟩]⟩]} │ τ]} │ τ]}`
- **Block Frequency:** 264



![nested PAR_19 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_19.png)

### `[nested LOOP_16]`
- **Internal Structure:** `(⟨[τ │ ⟨[τ │ t46], [(t69 ∗ τ) │ (t70 ∗ τ) │ {[τ │ (t62 ∗ τ)], [{[τ │ (t37 ∗ τ)], [{(t56 ∗ τ), [τ │ ⟨(t47 ∗ τ), [τ │ ⟨t48, (t68 ∗ τ)⟩]⟩]} │ τ]} │ τ]}]⟩], [t65 │ t55]⟩ ∗ τ)`
- **Block Frequency:** 250

- **Max Loop Iterations:** `581`
- **Max Sub-Sequence Length:** `1163` steps (if one case consumes all iterations)

![nested LOOP_16 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_16.png)

### `[nested PAR_11]`
- **Internal Structure:** `{[τ │ (t40 ∗ τ)], ⟨(⟨t39, [⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ τ), (⟨[τ │ ⟨[τ │ t46], [(t69 ∗ τ) │ (t70 ∗ τ) │ {[τ │ (t62 ∗ τ)], [{[τ │ (t37 ∗ τ)], [{(t56 ∗ τ), [τ │ ⟨(t47 ∗ τ), [τ │ ⟨t48, (t68 ∗ τ)⟩]⟩]} │ τ]} │ τ]}]⟩], [t65 │ t55]⟩ ∗ τ)⟩}`
- **Block Frequency:** 250



![nested PAR_11 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_11.png)

### `[nested PAR_8]`
- **Internal Structure:** `{[τ │ (t34 ∗ τ)], ⟨[τ │ ⟨t26, t27, [τ │ t28]⟩], (t42 ∗ τ), [τ │ t71], {[τ │ (t40 ∗ τ)], ⟨(⟨t39, [⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ τ), (⟨[τ │ ⟨[τ │ t46], [(t69 ∗ τ) │ (t70 ∗ τ) │ {[τ │ (t62 ∗ τ)], [{[τ │ (t37 ∗ τ)], [{(t56 ∗ τ), [τ │ ⟨(t47 ∗ τ), [τ │ ⟨t48, (t68 ∗ τ)⟩]⟩]} │ τ]} │ τ]}]⟩], [t65 │ t55]⟩ ∗ τ)⟩}⟩}`
- **Block Frequency:** 250



![nested PAR_8 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_8.png)
