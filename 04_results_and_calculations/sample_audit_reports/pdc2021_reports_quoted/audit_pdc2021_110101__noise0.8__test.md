# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_110101.xes` |
| **Noise Threshold** | `0.8` |
| **Fitness** | `0.8290328677884488` |
| **Precision** | `0.803343949044586` |
| **Total Cases in Log** | `250` |
| **Unique Activities** | `37` |
| **XOR Operators** | `21` |
| **LOOP Operators** | `21` |
| **SEQ Operators** | `23` |
| **PAR Operators** | `6` |
| **Binarization Additions** | `17` |
| **Tau Operators Added** | `17` |
| **Total Found Patterns** | `165` |
| **Verified Patterns** | `100` |
| **Discrepancy Patterns** | `22` |
| **Ghost Patterns** | `3` |
| **Nested LOOPs** | `21` |
| **Nested PARs** | `6` |
| **Tree Exposure (Strict, End-to-End % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `14.86%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `9.02%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `30.65%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `0.00%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `0.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `87.98%` |
| **Data Exposure, ST-only (% confirmed)** | `91.88%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `94.97%` |
| **Data Coverage, ST-only (% of real log)** | `18.20%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `58.26%` |
| **Data Coverage, Total (% of real log)** | `97.73%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `1.79%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `100.00%` |
| **Mean Absolute Exposure Volume (events/case)** | `16.02` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_110101__noise0.8__test.png)


```text
->( 't10', X( 't06', 't11' ), X( tau, *( 't04', 't07' ) ), 't05', *( 't15', tau ), 't16', 't20', X( ->( 't34', 't26', 't27', *( 't28', tau ) ), ->( X( tau, ->( 't24', 't23' ) ), +( *( 't22', tau ), *( 't17', tau ), *( 't21', tau ) ) ) ), *( *( 't42', tau ), 't41' ), *( ->( *( 't39', tau ), 't43', *( 't44', tau ) ), 't32' ), X( tau, 't71' ), +( *( 't40', tau ), ->( *( 't36', tau ), *( ->( 't46', X( *( 't69', tau ), +( *( 't52', tau ), *( 't56', tau ), X( *( 't55', tau ), +( *( 't37', tau ), ->( *( 't47', tau ), 't48', *( 't68', tau ) ) ) ) ) ), 't65' ), tau ) ) ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_110101__noise0.8__test.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST]` | `t10` | Exact Token Match | $\ge$ 250 | **250** | ✅ **VERIFIED** |
| `[ST]` | `t06` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `t11` | Exact Token Match | $\ge$ 146 | **146** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `t04` | Exact Token Match | $\ge$ 3 | **3** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `t07` | Exact Token Match | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_1]` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `t15` | Exact Token Match | $\ge$ 82 | **82** | ✅ **VERIFIED** |
| `[ST]` | `t16` | Exact Token Match | $\ge$ 84 | **84** | ✅ **VERIFIED** |
| `[ST]` | `t20` | Exact Token Match | $\ge$ 205 | **205** | ✅ **VERIFIED** |
| `[ST]` | `t34` | Exact Token Match | $\ge$ 89 | **117** | ✅ **VERIFIED** |
| `[ST]` | `t26` | Exact Token Match | $\ge$ 89 | **107** | ✅ **VERIFIED** |
| `[ST]` | `t27` | Exact Token Match | $\ge$ 89 | **107** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t28` | Exact Token Match | $\ge$ 77 | **77** | ✅ **VERIFIED** |
| `[ST]` | `⟨t27, τ⟩` | Exact Token Match | $\ge$ 12 | **107** | ✅ **VERIFIED** |
| `[ST]` | `⟨t26, t27, τ⟩` | Exact Token Match | $\ge$ 12 | **107** | ✅ **VERIFIED** |
| `[ST]` | `⟨t26, t27⟩` | Exact Token Match | $\ge$ 89 | **107** | ✅ **VERIFIED** |
| `[ST]` | `⟨t34, t26, t27, τ⟩` | Exact Token Match | $\ge$ 12 | **58** | ✅ **VERIFIED** |
| `[ST (in LOOP_5)]` | `t22` | Exact Token Match | $\ge$ 145 | **145** | ✅ **VERIFIED** |
| `[ST (in PAR_4)]` | `⟨t22⟩` | Exact Token Match | $\ge$ 145 | **145** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `t17` | Exact Token Match | $\ge$ 295 | **295** | ✅ **VERIFIED** |
| `[ST (in PAR_6)]` | `⟨t17⟩` | Exact Token Match | $\ge$ 27 | **295** | ✅ **VERIFIED** |
| `[AS (in PAR_6)]` | `[nested LOOP_7]` | Exact Token Match | $\ge$ 1 | **295** | ✅ **VERIFIED** |
| `[ST (in LOOP_8)]` | `t21` | Exact Token Match | $\ge$ 293 | **293** | ✅ **VERIFIED** |
| `[ST (in PAR_6)]` | `⟨t21⟩` | Exact Token Match | $\ge$ 29 | **293** | ✅ **VERIFIED** |
| `[AS (in PAR_6)]` | `[nested LOOP_8]` | Exact Token Match | $\ge$ 1 | **293** | ✅ **VERIFIED** |
| `[AS (in PAR_4)]` | `[nested PAR_6]` | Exact Token Match | $\ge$ 161 | **233** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_4]` | Exact Token Match | $\ge$ 161 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_4]⟩` | Exact Token Match | $\ge$ 43 | **249** | ✅ **VERIFIED** |
| `[ST (in LOOP_10)]` | `t42` | Exact Token Match | $\ge$ 431 | **431** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `⟨t42⟩` | Exact Token Match | $\ge$ 427 | **431** | ✅ **VERIFIED** |
| `[AS (in LOOP_9)]` | `[nested LOOP_10]` | Exact Token Match | $\ge$ 1 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `t41` | Exact Token Match | $\ge$ 179 | **179** | ✅ **VERIFIED** |
| `[ST]` | `⟨t42⟩` | Exact Token Match | $\ge$ 69 | **116** | ✅ **VERIFIED** |
| `[AS]` | `⟨[nested LOOP_10]⟩` | Exact Token Match | $\ge$ 1 | **213** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_9]` | Exact Token Match | $\ge$ 1 | **213** | ✅ **VERIFIED** |
| `[ST (in LOOP_12)]` | `t39` | Exact Token Match | $\ge$ 391 | **391** | ✅ **VERIFIED** |
| `[AS (in LOOP_11)]` | `[nested LOOP_12]` | Exact Token Match | $\ge$ 1 | **208** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `t43` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `t44` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `⟨t44⟩` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `⟨t43, t44⟩` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `⟨[nested LOOP_12], t43, t44⟩` | Exact Token Match | $\ge$ 1 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `⟨[nested LOOP_12], t43⟩` | Exact Token Match | $\ge$ 1 | **190** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `t32` | Exact Token Match | $\ge$ 155 | **155** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_11]` | Exact Token Match | $\ge$ 1 | **208** | ✅ **VERIFIED** |
| `[ST]` | `t71` | Exact Token Match | $\ge$ 41 | **41** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `t40` | Exact Token Match | $\ge$ 221 | **221** | ✅ **VERIFIED** |
| `[ST (in PAR_14)]` | `⟨t40⟩` | Exact Token Match | $\ge$ 221 | **221** | ✅ **VERIFIED** |
| `[ST (in LOOP_16)]` | `t36` | Exact Token Match | $\ge$ 523 | **523** | ✅ **VERIFIED** |
| `[AS (in PAR_14)]` | `[nested LOOP_16]` | Exact Token Match | $\ge$ 1 | **523** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `t46` | Exact Token Match | $\ge$ 420 | **420** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `t69` | Exact Token Match | $\ge$ 170 | **170** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨t69⟩` | Exact Token Match | $\ge$ 170 | **170** | ✅ **VERIFIED** |
| `[ST (in LOOP_20)]` | `t52` | Exact Token Match | $\ge$ 248 | **248** | ✅ **VERIFIED** |
| `[ST (in PAR_19)]` | `⟨t52⟩` | Exact Token Match | $\ge$ 248 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `t56` | Exact Token Match | $\ge$ 606 | **606** | ✅ **VERIFIED** |
| `[ST (in PAR_21)]` | `⟨t56⟩` | Exact Token Match | $\ge$ 606 | **606** | ✅ **VERIFIED** |
| `[ST (in LOOP_23)]` | `t55` | Exact Token Match | $\ge$ 622 | **622** | ✅ **VERIFIED** |
| `[ST (in PAR_21)]` | `⟨t55⟩` | Exact Token Match | $\ge$ 622 | **622** | ✅ **VERIFIED** |
| `[ST (in LOOP_25)]` | `t37` | Exact Token Match | $\ge$ 180 | **180** | ✅ **VERIFIED** |
| `[ST (in PAR_24)]` | `⟨t37⟩` | Exact Token Match | $\ge$ 180 | **180** | ✅ **VERIFIED** |
| `[ST (in LOOP_26)]` | `t47` | Exact Token Match | $\ge$ 190 | **190** | ✅ **VERIFIED** |
| `[ST (in PAR_24)]` | `⟨t47⟩` | Exact Token Match | $\ge$ 186 | **190** | ✅ **VERIFIED** |
| `[AS (in PAR_24)]` | `[nested LOOP_26]` | Exact Token Match | $\ge$ 1 | **190** | ✅ **VERIFIED** |
| `[ST (in PAR_24)]` | `t48` | Exact Token Match | $\ge$ 188 | **188** | ✅ **VERIFIED** |
| `[ST (in LOOP_27)]` | `t68` | Exact Token Match | $\ge$ 188 | **188** | ✅ **VERIFIED** |
| `[ST (in PAR_24)]` | `⟨t68⟩` | Exact Token Match | $\ge$ 188 | **188** | ✅ **VERIFIED** |
| `[ST (in PAR_24)]` | `⟨t48, t68⟩` | Exact Token Match | $\ge$ 188 | **188** | ✅ **VERIFIED** |
| `[ST (in PAR_24)]` | `⟨[nested LOOP_26], t48, t68⟩` | Exact Token Match | $\ge$ 1 | **164** | ✅ **VERIFIED** |
| `[ST (in PAR_24)]` | `⟨[nested LOOP_26], t48⟩` | Exact Token Match | $\ge$ 1 | **164** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `t65` | Exact Token Match | $\ge$ 432 | **432** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨[nested PAR_19], t65⟩` | Exact Token Match | $\ge$ 262 | **333** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨t46, [nested PAR_19]⟩` | Exact Token Match | $\ge$ 250 | **400** | ✅ **VERIFIED** |
| `[AS (in PAR_14)]` | `[nested LOOP_17]` | Exact Token Match | $\ge$ 1 | **30** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_14]⟩` | Exact Token Match | $\ge$ 209 | **248** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, τ, [nested PAR_14]⟩` | Exact Token Match | $\ge$ 174 | **248** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t71, [nested PAR_14]⟩` | Exact Token Match | $\ge$ 6 | **40** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t71⟩` | Exact Token Match | $\ge$ 6 | **41** | ✅ **VERIFIED** |
| `[ST]` | `⟨t42, τ⟩` | Exact Token Match | $\ge$ 34 | **116** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, t34, t26, t27⟩` | Exact Token Match | $\ge$ 44 | **46** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, t34, t26⟩` | Exact Token Match | $\ge$ 44 | **46** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, t34⟩` | Exact Token Match | $\ge$ 44 | **102** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, t24, t23⟩` | Exact Token Match | $\ge$ 73 | **90** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, t24⟩` | Exact Token Match | $\ge$ 73 | **90** | ✅ **VERIFIED** |
| `[ST]` | `⟨t16, t20⟩` | Exact Token Match | $\ge$ 39 | **84** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t20⟩` | Exact Token Match | $\ge$ 121 | **205** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, τ, t20⟩` | Exact Token Match | $\ge$ 39 | **205** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t16⟩` | Exact Token Match | $\ge$ 2 | **84** | ✅ **VERIFIED** |
| `[ST]` | `⟨t05, τ⟩` | Exact Token Match | $\ge$ 62 | **89** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t05, τ⟩` | Exact Token Match | $\ge$ 61 | **89** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, τ, t05⟩` | Exact Token Match | $\ge$ 39 | **89** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, τ, τ⟩` | Exact Token Match | $\ge$ 1 | **146** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, τ⟩` | Exact Token Match | $\ge$ 145 | **146** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, τ, t05⟩` | Exact Token Match | $\ge$ 39 | **89** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, τ, τ⟩` | Exact Token Match | $\ge$ 1 | **146** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, τ⟩` | Exact Token Match | $\ge$ 145 | **146** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ, τ⟩` | Exact Token Match | $\ge$ 102 | **250** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06⟩` | Exact Token Match | $\ge$ 1 | **1** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11⟩` | Exact Token Match | $\ge$ 146 | **146** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 103 | **250** | ✅ **VERIFIED** |
| `[ST]` | `t05` | Exact Token Match | $\ge$ 144 | **89** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t15⟩` | Exact Token Match | $\ge$ 82 | **46** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t28⟩` | Exact Token Match | $\ge$ 77 | **71** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t27, t28⟩` | Exact Token Match | $\ge$ 77 | **69** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t26, t27, t28⟩` | Exact Token Match | $\ge$ 77 | **69** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t34, t26, t27, t28⟩` | Exact Token Match | $\ge$ 77 | **36** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t34, t26, t27⟩` | Exact Token Match | $\ge$ 89 | **58** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t34, t26⟩` | Exact Token Match | $\ge$ 89 | **58** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t24` | Exact Token Match | $\ge$ 118 | **107** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t23` | Exact Token Match | $\ge$ 118 | **107** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t24, t23⟩` | Exact Token Match | $\ge$ 118 | **107** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_24)]` | `⟨t47, t48, t68⟩` | Exact Token Match | $\ge$ 186 | **164** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_24)]` | `⟨t47, t48⟩` | Exact Token Match | $\ge$ 186 | **164** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_21)]` | `[nested PAR_24]` | Exact Token Match | $\ge$ 188 | **147** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_19)]` | `[nested PAR_21]` | Exact Token Match | $\ge$ 810 | **133** | ⚠️ **DISCREPANCY** |
| `[AS (in LOOP_17)]` | `[nested PAR_19]` | Exact Token Match | $\ge$ 810 | **239** | ⚠️ **DISCREPANCY** |
| `[ST (in LOOP_17)]` | `⟨[nested PAR_19], τ⟩` | Exact Token Match | $\ge$ 378 | **239** | ⚠️ **DISCREPANCY** |
| `[ST (in LOOP_17)]` | `⟨τ, [nested PAR_19]⟩` | Exact Token Match | $\ge$ 390 | **239** | ⚠️ **DISCREPANCY** |
| `[AS]` | `[nested PAR_14]` | Exact Token Match | $\ge$ 250 | **248** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t71, [nested PAR_14]⟩` | Exact Token Match | $\ge$ 41 | **40** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t20, t34, t26, t27, t28⟩` | Exact Token Match | $\ge$ 32 | **27** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨τ, t05⟩` | Exact Token Match | $\ge$ 143 | **89** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t24, t23, [nested PAR_4]⟩` | Exact Token Match | $\ge$ 118 | **0** | ❌ **GHOST PATTERN** |
| `[ST]` | `⟨t23, [nested PAR_4]⟩` | Exact Token Match | $\ge$ 118 | **0** | ❌ **GHOST PATTERN** |
| `[ST]` | `⟨t20, t24, t23, [nested PAR_4]⟩` | Exact Token Match | $\ge$ 73 | **0** | ❌ **GHOST PATTERN** |

## Audit Summary
- **Perfect Pattern Verifications:** 100
- **Frequency Discrepancies:** 22
- **Ghost Patterns (Fatal):** 3
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 14.86%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 9.02%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 30.65%
- **Total Forced Volume (incl. unresolved AS, % of N):** 0.00%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 0.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 87.98%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 91.88%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 94.97%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 18.20%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 58.26%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 97.73%
- **Max Fractional Exposure (Worst-Case Normalized):** 1.79% (expected length: 2429.58 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 100.00% (expected length: 31.18 events)
- **Mean Absolute Exposure Volume:** 16.02 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_1]`
- **Internal Structure:** `(t04 ∗ t07)`
- **Block Frequency:** 1

- **Max Loop Iterations:** `2`
- **Max Sub-Sequence Length:** `5` steps (if one case consumes all iterations)

![nested LOOP_1 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.8__test_nested_LOOP_1.png)

### `[nested LOOP_2]`
- **Internal Structure:** `(t15 ∗ τ)`
- **Block Frequency:** 82

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_2 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.8__test_nested_LOOP_2.png)

### `[nested LOOP_3]`
- **Internal Structure:** `(t28 ∗ τ)`
- **Block Frequency:** 77

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_3 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.8__test_nested_LOOP_3.png)

### `[nested LOOP_5]`
- **Internal Structure:** `(t22 ∗ τ)`
- **Block Frequency:** 145

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_5 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.8__test_nested_LOOP_5.png)

### `[nested LOOP_7]`
- **Internal Structure:** `(t17 ∗ τ)`
- **Block Frequency:** 161

- **Max Loop Iterations:** `134`
- **Max Sub-Sequence Length:** `269` steps (if one case consumes all iterations)

![nested LOOP_7 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.8__test_nested_LOOP_7.png)

### `[nested LOOP_8]`
- **Internal Structure:** `(t21 ∗ τ)`
- **Block Frequency:** 161

- **Max Loop Iterations:** `132`
- **Max Sub-Sequence Length:** `265` steps (if one case consumes all iterations)

![nested LOOP_8 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.8__test_nested_LOOP_8.png)

### `[nested PAR_6]`
- **Internal Structure:** `{(t17 ∗ τ), (t21 ∗ τ)}`
- **Block Frequency:** 161



![nested PAR_6 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.8__test_nested_PAR_6.png)

### `[nested PAR_4]`
- **Internal Structure:** `{[(t22 ∗ τ) │ τ], (t17 ∗ τ), (t21 ∗ τ)}`
- **Block Frequency:** 161



![nested PAR_4 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.8__test_nested_PAR_4.png)

### `[nested LOOP_10]`
- **Internal Structure:** `(t42 ∗ τ)`
- **Block Frequency:** 429

- **Max Loop Iterations:** `2`
- **Max Sub-Sequence Length:** `5` steps (if one case consumes all iterations)

![nested LOOP_10 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.8__test_nested_LOOP_10.png)

### `[nested LOOP_9]`
- **Internal Structure:** `((t42 ∗ τ) ∗ t41)`
- **Block Frequency:** 250

- **Max Loop Iterations:** `179`
- **Max Sub-Sequence Length:** `359` steps (if one case consumes all iterations)

![nested LOOP_9 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.8__test_nested_LOOP_9.png)

### `[nested LOOP_12]`
- **Internal Structure:** `(t39 ∗ τ)`
- **Block Frequency:** 190

- **Max Loop Iterations:** `201`
- **Max Sub-Sequence Length:** `403` steps (if one case consumes all iterations)

![nested LOOP_12 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.8__test_nested_LOOP_12.png)

### `[nested LOOP_13]`
- **Internal Structure:** `(t44 ∗ τ)`
- **Block Frequency:** 190

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_13 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.8__test_nested_LOOP_13.png)

### `[nested LOOP_11]`
- **Internal Structure:** `(⟨(t39 ∗ τ), t43, (t44 ∗ τ)⟩ ∗ t32)`
- **Block Frequency:** 35

- **Max Loop Iterations:** `155`
- **Max Sub-Sequence Length:** `311` steps (if one case consumes all iterations)

![nested LOOP_11 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.8__test_nested_LOOP_11.png)

### `[nested LOOP_15]`
- **Internal Structure:** `(t40 ∗ τ)`
- **Block Frequency:** 221

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_15 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.8__test_nested_LOOP_15.png)

### `[nested LOOP_16]`
- **Internal Structure:** `(t36 ∗ τ)`
- **Block Frequency:** 250

- **Max Loop Iterations:** `273`
- **Max Sub-Sequence Length:** `547` steps (if one case consumes all iterations)

![nested LOOP_16 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.8__test_nested_LOOP_16.png)

### `[nested LOOP_18]`
- **Internal Structure:** `(t69 ∗ τ)`
- **Block Frequency:** 170

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_18 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.8__test_nested_LOOP_18.png)

### `[nested LOOP_20]`
- **Internal Structure:** `(t52 ∗ τ)`
- **Block Frequency:** 248

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_20 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.8__test_nested_LOOP_20.png)

### `[nested LOOP_22]`
- **Internal Structure:** `(t56 ∗ τ)`
- **Block Frequency:** 606

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_22 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.8__test_nested_LOOP_22.png)

### `[nested LOOP_23]`
- **Internal Structure:** `(t55 ∗ τ)`
- **Block Frequency:** 622

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_23 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.8__test_nested_LOOP_23.png)

### `[nested LOOP_25]`
- **Internal Structure:** `(t37 ∗ τ)`
- **Block Frequency:** 180

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_25 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.8__test_nested_LOOP_25.png)

### `[nested LOOP_26]`
- **Internal Structure:** `(t47 ∗ τ)`
- **Block Frequency:** 188

- **Max Loop Iterations:** `2`
- **Max Sub-Sequence Length:** `5` steps (if one case consumes all iterations)

![nested LOOP_26 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.8__test_nested_LOOP_26.png)

### `[nested LOOP_27]`
- **Internal Structure:** `(t68 ∗ τ)`
- **Block Frequency:** 188

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_27 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.8__test_nested_LOOP_27.png)

### `[nested PAR_24]`
- **Internal Structure:** `{[(t37 ∗ τ) │ τ], ⟨(t47 ∗ τ), t48, (t68 ∗ τ)⟩}`
- **Block Frequency:** 188



![nested PAR_24 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.8__test_nested_PAR_24.png)

### `[nested PAR_21]`
- **Internal Structure:** `{[(t56 ∗ τ) │ τ], [(t55 ∗ τ) │ {[(t37 ∗ τ) │ τ], ⟨(t47 ∗ τ), t48, (t68 ∗ τ)⟩}]}`
- **Block Frequency:** 810



![nested PAR_21 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.8__test_nested_PAR_21.png)

### `[nested PAR_19]`
- **Internal Structure:** `{[(t52 ∗ τ) │ τ], [(t56 ∗ τ) │ τ], [(t55 ∗ τ) │ {[(t37 ∗ τ) │ τ], ⟨(t47 ∗ τ), t48, (t68 ∗ τ)⟩}]}`
- **Block Frequency:** 810



![nested PAR_19 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.8__test_nested_PAR_19.png)

### `[nested LOOP_17]`
- **Internal Structure:** `(⟨[t46 │ τ], [(t69 ∗ τ) │ {[(t52 ∗ τ) │ τ], [(t56 ∗ τ) │ τ], [(t55 ∗ τ) │ {[(t37 ∗ τ) │ τ], ⟨(t47 ∗ τ), t48, (t68 ∗ τ)⟩}]}], [t65 │ τ]⟩ ∗ τ)`
- **Block Frequency:** 250

- **Max Loop Iterations:** `730`
- **Max Sub-Sequence Length:** `1461` steps (if one case consumes all iterations)

![nested LOOP_17 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.8__test_nested_LOOP_17.png)

### `[nested PAR_14]`
- **Internal Structure:** `{[(t40 ∗ τ) │ τ], ⟨(t36 ∗ τ), (⟨[t46 │ τ], [(t69 ∗ τ) │ {[(t52 ∗ τ) │ τ], [(t56 ∗ τ) │ τ], [(t55 ∗ τ) │ {[(t37 ∗ τ) │ τ], ⟨(t47 ∗ τ), t48, (t68 ∗ τ)⟩}]}], [t65 │ τ]⟩ ∗ τ)⟩}`
- **Block Frequency:** 250



![nested PAR_14 Internal Diagram](images/nested_ref_audit_pdc2021_110101__noise0.8__test_nested_PAR_14.png)
