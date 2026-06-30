# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_0101010.xes` |
| **Noise Threshold** | `0.0` |
| **Fitness** | `1.0` |
| **Precision** | `0.23909282930915188` |
| **Total Cases in Log** | `1000` |
| **Unique Activities** | `39` |
| **XOR Operators** | `33` |
| **LOOP Operators** | `13` |
| **SEQ Operators** | `22` |
| **PAR Operators** | `9` |
| **Binarization Additions** | `9` |
| **Tau Operators Added** | `19` |
| **Total Found Patterns** | `184` |
| **Verified Patterns** | `107` |
| **Discrepancy Patterns** | `8` |
| **Ghost Patterns** | `1` |
| **Nested LOOPs** | `13` |
| **Nested PARs** | `9` |
| **Tree Exposure (Strict, End-to-End % of N)** | `25.50%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `38.42%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `7.73%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `40.81%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `25.50%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `0.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `92.92%` |
| **Data Exposure, ST-only (% confirmed)** | `100.00%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `99.73%` |
| **Data Coverage, ST-only (% of real log)** | `13.27%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `63.13%` |
| **Data Coverage, Total (% of real log)** | `100.00%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `26.24%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `100.00%` |
| **Mean Absolute Exposure Volume (events/case)** | `16.99` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_0101010__noise0.0.png)


```text
->( 't10', X( tau, ->( X( 't06', 't11' ), +( X( tau, *( 't05', tau ) ), X( tau, *( 't04', tau ) ), X( tau, ->( X( tau, *( 't07', tau ) ), X( tau, *( 't15', tau ) ) ) ) ), X( tau, 't16' ) ) ), X( tau, ->( X( tau, 't20' ), +( 't21', X( tau, +( *( 't17', tau ), X( tau, ->( 't24', 't23' ) ) ) ) ), X( tau, 't22' ), +( X( tau, *( 't34', tau ) ), ->( X( tau, ->( 't26', 't27' ) ), X( 't71', ->( X( tau, 't28' ), *( 't42', 't41' ) ) ), +( X( tau, *( 't40', tau ) ), ->( X( tau, *( ->( 't39', X( tau, ->( 't43', 't44' ) ), *( 't36', tau ) ), 't32' ) ), *( ->( X( tau, ->( 't46', X( 't69', 't70', 't47' ) ) ), +( X( tau, *( 't56', tau ) ), ->( X( tau, ->( X( tau, +( 't62', 't37', ->( 't48', 't68' ) ) ), 't65' ) ), *( 't55', 't52' ) ) ) ), tau ) ) ) ) ) ) ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_0101010__noise0.0.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST]` | `t10` | Exact Token Match | $\ge$ 1000 | **1000** | ✅ **VERIFIED** |
| `[ST]` | `t06` | Exact Token Match | $\ge$ 496 | **496** | ✅ **VERIFIED** |
| `[ST]` | `t11` | Exact Token Match | $\ge$ 249 | **249** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `t05` | Exact Token Match | $\ge$ 504 | **504** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t05⟩` | Exact Token Match | $\ge$ 504 | **504** | ✅ **VERIFIED** |
| `[ST (in LOOP_4)]` | `t04` | Exact Token Match | $\ge$ 324 | **324** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t04⟩` | Exact Token Match | $\ge$ 324 | **324** | ✅ **VERIFIED** |
| `[ST (in LOOP_5)]` | `t07` | Exact Token Match | $\ge$ 73 | **73** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t07⟩` | Exact Token Match | $\ge$ 73 | **73** | ✅ **VERIFIED** |
| `[ST (in LOOP_6)]` | `t15` | Exact Token Match | $\ge$ 556 | **556** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t15⟩` | Exact Token Match | $\ge$ 556 | **556** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨τ, t15⟩` | Exact Token Match | $\ge$ 483 | **556** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_1]` | Exact Token Match | $\ge$ 556 | **745** | ✅ **VERIFIED** |
| `[ST]` | `t16` | Exact Token Match | $\ge$ 171 | **171** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], τ⟩` | Exact Token Match | $\ge$ 385 | **745** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], t16⟩` | Exact Token Match | $\ge$ 171 | **171** | ✅ **VERIFIED** |
| `[ST]` | `⟨t06, [nested PAR_1], τ⟩` | Exact Token Match | $\ge$ 136 | **496** | ✅ **VERIFIED** |
| `[ST]` | `⟨t06, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 307 | **496** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 60 | **249** | ✅ **VERIFIED** |
| `[ST]` | `t20` | Exact Token Match | $\ge$ 426 | **426** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `t21` | Exact Token Match | $\ge$ 504 | **504** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `t17` | Exact Token Match | $\ge$ 662 | **662** | ✅ **VERIFIED** |
| `[AS (in PAR_8)]` | `[nested LOOP_9]` | Exact Token Match | $\ge$ 1 | **662** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `t24` | Exact Token Match | $\ge$ 236 | **236** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `t23` | Exact Token Match | $\ge$ 236 | **236** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨t24, t23⟩` | Exact Token Match | $\ge$ 236 | **236** | ✅ **VERIFIED** |
| `[AS (in PAR_7)]` | `[nested PAR_8]` | Exact Token Match | $\ge$ 236 | **236** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_7]` | Exact Token Match | $\ge$ 504 | **504** | ✅ **VERIFIED** |
| `[ST]` | `t22` | Exact Token Match | $\ge$ 268 | **268** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `t34` | Exact Token Match | $\ge$ 506 | **506** | ✅ **VERIFIED** |
| `[ST (in PAR_10)]` | `⟨t34⟩` | Exact Token Match | $\ge$ 506 | **506** | ✅ **VERIFIED** |
| `[ST (in PAR_10)]` | `t26` | Exact Token Match | $\ge$ 236 | **236** | ✅ **VERIFIED** |
| `[ST (in PAR_10)]` | `t27` | Exact Token Match | $\ge$ 236 | **236** | ✅ **VERIFIED** |
| `[ST (in PAR_10)]` | `⟨t26, t27⟩` | Exact Token Match | $\ge$ 236 | **236** | ✅ **VERIFIED** |
| `[ST (in PAR_10)]` | `t71` | Exact Token Match | $\ge$ 129 | **129** | ✅ **VERIFIED** |
| `[ST (in PAR_10)]` | `t28` | Exact Token Match | $\ge$ 107 | **107** | ✅ **VERIFIED** |
| `[ST (in LOOP_12)]` | `t42` | Exact Token Match | $\ge$ 524 | **792** | ✅ **VERIFIED** |
| `[ST (in LOOP_12)]` | `t41` | Exact Token Match | $\ge$ 417 | **417** | ✅ **VERIFIED** |
| `[AS (in PAR_10)]` | `[nested LOOP_12]` | Exact Token Match | $\ge$ 1 | **417** | ✅ **VERIFIED** |
| `[ST (in PAR_10)]` | `⟨t28, [nested LOOP_12]⟩` | Exact Token Match | $\ge$ 1 | **62** | ✅ **VERIFIED** |
| `[ST (in LOOP_14)]` | `t40` | Exact Token Match | $\ge$ 626 | **626** | ✅ **VERIFIED** |
| `[ST (in PAR_13)]` | `⟨t40⟩` | Exact Token Match | $\ge$ 626 | **626** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `t39` | Exact Token Match | $\ge$ 788 | **788** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `t43` | Exact Token Match | $\ge$ 248 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `t44` | Exact Token Match | $\ge$ 248 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨t43, t44⟩` | Exact Token Match | $\ge$ 248 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_16)]` | `t36` | Exact Token Match | $\ge$ 1203 | **1203** | ✅ **VERIFIED** |
| `[AS (in LOOP_15)]` | `[nested LOOP_16]` | Exact Token Match | $\ge$ 1 | **375** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨t43, t44, [nested LOOP_16]⟩` | Exact Token Match | $\ge$ 1 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨t44, [nested LOOP_16]⟩` | Exact Token Match | $\ge$ 1 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨t39, t43, t44, [nested LOOP_16]⟩` | Exact Token Match | $\ge$ 1 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨t39, τ⟩` | Exact Token Match | $\ge$ 540 | **788** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨t39, t43, t44⟩` | Exact Token Match | $\ge$ 248 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨t39, t43⟩` | Exact Token Match | $\ge$ 248 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `t32` | Exact Token Match | $\ge$ 413 | **413** | ✅ **VERIFIED** |
| `[AS (in PAR_13)]` | `[nested LOOP_15]` | Exact Token Match | $\ge$ 1 | **184** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `t46` | Exact Token Match | $\ge$ 963 | **963** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `t69` | Exact Token Match | $\ge$ 305 | **305** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `t70` | Exact Token Match | $\ge$ 302 | **302** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `t47` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨t46, t69⟩` | Exact Token Match | $\ge$ 305 | **305** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨t46, t70⟩` | Exact Token Match | $\ge$ 302 | **302** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨t46, t47⟩` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[ST (in LOOP_19)]` | `t56` | Exact Token Match | $\ge$ 1501 | **1501** | ✅ **VERIFIED** |
| `[ST (in PAR_18)]` | `⟨t56⟩` | Exact Token Match | $\ge$ 1501 | **1501** | ✅ **VERIFIED** |
| `[ST (in PAR_20)]` | `t62` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[ST (in PAR_21)]` | `t37` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[ST (in PAR_21)]` | `t48` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[ST (in PAR_21)]` | `t68` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[ST (in PAR_21)]` | `⟨t48, t68⟩` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[AS (in PAR_20)]` | `[nested PAR_21]` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[AS (in PAR_18)]` | `[nested PAR_20]` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[ST (in PAR_18)]` | `t65` | Exact Token Match | $\ge$ 963 | **963** | ✅ **VERIFIED** |
| `[ST (in PAR_18)]` | `⟨τ, t65⟩` | Exact Token Match | $\ge$ 607 | **963** | ✅ **VERIFIED** |
| `[ST (in PAR_18)]` | `⟨[nested PAR_20], t65⟩` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `t55` | Exact Token Match | $\ge$ 1520 | **1649** | ✅ **VERIFIED** |
| `[ST (in LOOP_22)]` | `t52` | Exact Token Match | $\ge$ 557 | **557** | ✅ **VERIFIED** |
| `[ST (in PAR_18)]` | `⟨t55⟩` | Exact Token Match | $\ge$ 406 | **1649** | ✅ **VERIFIED** |
| `[AS (in PAR_18)]` | `[nested LOOP_22]` | Exact Token Match | $\ge$ 1 | **557** | ✅ **VERIFIED** |
| `[ST (in PAR_18)]` | `⟨τ, t65, t55⟩` | Exact Token Match | $\ge$ 50 | **963** | ✅ **VERIFIED** |
| `[ST (in PAR_18)]` | `⟨t65, t55⟩` | Exact Token Match | $\ge$ 406 | **963** | ✅ **VERIFIED** |
| `[ST (in PAR_18)]` | `⟨t65, [nested LOOP_22]⟩` | Exact Token Match | $\ge$ 1 | **448** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨t46, t69, [nested PAR_18]⟩` | Exact Token Match | $\ge$ 305 | **305** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨t46, t70, [nested PAR_18]⟩` | Exact Token Match | $\ge$ 302 | **302** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨t46, t47, [nested PAR_18]⟩` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨t69, [nested PAR_18]⟩` | Exact Token Match | $\ge$ 305 | **305** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨t70, [nested PAR_18]⟩` | Exact Token Match | $\ge$ 302 | **302** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `⟨t47, [nested PAR_18]⟩` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[AS (in PAR_13)]` | `[nested LOOP_17]` | Exact Token Match | $\ge$ 1 | **63** | ✅ **VERIFIED** |
| `[ST (in PAR_10)]` | `⟨t28, [nested LOOP_12], [nested PAR_13]⟩` | Exact Token Match | $\ge$ 1 | **4** | ✅ **VERIFIED** |
| `[ST (in PAR_10)]` | `⟨[nested LOOP_12], [nested PAR_13]⟩` | Exact Token Match | $\ge$ 1 | **9** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_10]⟩` | Exact Token Match | $\ge$ 358 | **504** | ✅ **VERIFIED** |
| `[ST]` | `⟨t22, [nested PAR_10]⟩` | Exact Token Match | $\ge$ 268 | **268** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_7], τ, [nested PAR_10]⟩` | Exact Token Match | $\ge$ 236 | **504** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_7], t22, [nested PAR_10]⟩` | Exact Token Match | $\ge$ 146 | **268** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_7], τ⟩` | Exact Token Match | $\ge$ 236 | **504** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_7], t22⟩` | Exact Token Match | $\ge$ 146 | **268** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, [nested PAR_7], τ, [nested PAR_10]⟩` | Exact Token Match | $\ge$ 36 | **426** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_7]⟩` | Exact Token Match | $\ge$ 78 | **504** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, [nested PAR_7], τ⟩` | Exact Token Match | $\ge$ 36 | **426** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, [nested PAR_7]⟩` | Exact Token Match | $\ge$ 304 | **426** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 255 | **1000** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06, [nested PAR_1], τ⟩` | Exact Token Match | $\ge$ 136 | **496** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 307 | **496** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 60 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06⟩` | Exact Token Match | $\ge$ 496 | **496** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11⟩` | Exact Token Match | $\ge$ 249 | **249** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t07, t15⟩` | Exact Token Match | $\ge$ 73 | **34** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_1)]` | `[nested PAR_3]` | Exact Token Match | $\ge$ 556 | **34** | ⚠️ **DISCREPANCY** |
| `[AS (in LOOP_17)]` | `[nested PAR_18]` | Exact Token Match | $\ge$ 1501 | **504** | ⚠️ **DISCREPANCY** |
| `[ST (in LOOP_17)]` | `⟨τ, [nested PAR_18]⟩` | Exact Token Match | $\ge$ 538 | **504** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_10)]` | `[nested PAR_13]` | Exact Token Match | $\ge$ 626 | **21** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_10)]` | `⟨τ, [nested PAR_13]⟩` | Exact Token Match | $\ge$ 390 | **21** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_10)]` | `⟨τ, τ, [nested PAR_13]⟩` | Exact Token Match | $\ge$ 154 | **21** | ⚠️ **DISCREPANCY** |
| `[AS]` | `[nested PAR_10]` | Exact Token Match | $\ge$ 626 | **504** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_10)]` | `⟨t71, [nested PAR_13]⟩` | Exact Token Match | $\ge$ 129 | **0** | ❌ **GHOST PATTERN** |

## Audit Summary
- **Perfect Pattern Verifications:** 107
- **Frequency Discrepancies:** 8
- **Ghost Patterns (Fatal):** 1
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 25.50%
- **Tree Exposure (Strict, Fragment-Level % of N):** 38.42%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 7.73%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 40.81%
- **Total Forced Volume (incl. unresolved AS, % of N):** 25.50%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 0.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 92.92%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 100.00%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 99.73%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 13.27%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 63.13%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 100.00%
- **Max Fractional Exposure (Worst-Case Normalized):** 26.24% (expected length: 5093.53 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 100.00% (expected length: 19.28 events)
- **Mean Absolute Exposure Volume:** 16.99 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_2]`
- **Internal Structure:** `(t05 ∗ τ)`
- **Block Frequency:** 504

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_2 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.0_nested_LOOP_2.png)

### `[nested LOOP_4]`
- **Internal Structure:** `(t04 ∗ τ)`
- **Block Frequency:** 324

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_4 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.0_nested_LOOP_4.png)

### `[nested LOOP_5]`
- **Internal Structure:** `(t07 ∗ τ)`
- **Block Frequency:** 73

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_5 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.0_nested_LOOP_5.png)

### `[nested LOOP_6]`
- **Internal Structure:** `(t15 ∗ τ)`
- **Block Frequency:** 556

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_6 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.0_nested_LOOP_6.png)

### `[nested PAR_3]`
- **Internal Structure:** `{[τ │ (t04 ∗ τ)], [τ │ ⟨[τ │ (t07 ∗ τ)], [τ │ (t15 ∗ τ)]⟩]}`
- **Block Frequency:** 556



![nested PAR_3 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.0_nested_PAR_3.png)

### `[nested PAR_1]`
- **Internal Structure:** `{[τ │ (t05 ∗ τ)], [τ │ (t04 ∗ τ)], [τ │ ⟨[τ │ (t07 ∗ τ)], [τ │ (t15 ∗ τ)]⟩]}`
- **Block Frequency:** 556



![nested PAR_1 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.0_nested_PAR_1.png)

### `[nested LOOP_9]`
- **Internal Structure:** `(t17 ∗ τ)`
- **Block Frequency:** 236

- **Max Loop Iterations:** `426`
- **Max Sub-Sequence Length:** `853` steps (if one case consumes all iterations)

![nested LOOP_9 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.0_nested_LOOP_9.png)

### `[nested PAR_8]`
- **Internal Structure:** `{(t17 ∗ τ), [τ │ ⟨t24, t23⟩]}`
- **Block Frequency:** 236



![nested PAR_8 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.0_nested_PAR_8.png)

### `[nested PAR_7]`
- **Internal Structure:** `{t21, [τ │ {(t17 ∗ τ), [τ │ ⟨t24, t23⟩]}]}`
- **Block Frequency:** 504



![nested PAR_7 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.0_nested_PAR_7.png)

### `[nested LOOP_11]`
- **Internal Structure:** `(t34 ∗ τ)`
- **Block Frequency:** 506

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_11 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.0_nested_LOOP_11.png)

### `[nested LOOP_12]`
- **Internal Structure:** `(t42 ∗ t41)`
- **Block Frequency:** 107

- **Max Loop Iterations:** `417`
- **Max Sub-Sequence Length:** `835` steps (if one case consumes all iterations)

![nested LOOP_12 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.0_nested_LOOP_12.png)

### `[nested LOOP_14]`
- **Internal Structure:** `(t40 ∗ τ)`
- **Block Frequency:** 626

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_14 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.0_nested_LOOP_14.png)

### `[nested LOOP_16]`
- **Internal Structure:** `(t36 ∗ τ)`
- **Block Frequency:** 248

- **Max Loop Iterations:** `955`
- **Max Sub-Sequence Length:** `1911` steps (if one case consumes all iterations)

![nested LOOP_16 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.0_nested_LOOP_16.png)

### `[nested LOOP_15]`
- **Internal Structure:** `(⟨t39, [⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ t32)`
- **Block Frequency:** 375

- **Max Loop Iterations:** `413`
- **Max Sub-Sequence Length:** `827` steps (if one case consumes all iterations)

![nested LOOP_15 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.0_nested_LOOP_15.png)

### `[nested LOOP_19]`
- **Internal Structure:** `(t56 ∗ τ)`
- **Block Frequency:** 1501

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_19 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.0_nested_LOOP_19.png)

### `[nested PAR_21]`
- **Internal Structure:** `{t37, ⟨t48, t68⟩}`
- **Block Frequency:** 356



![nested PAR_21 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.0_nested_PAR_21.png)

### `[nested PAR_20]`
- **Internal Structure:** `{t62, t37, ⟨t48, t68⟩}`
- **Block Frequency:** 356



![nested PAR_20 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.0_nested_PAR_20.png)

### `[nested LOOP_22]`
- **Internal Structure:** `(t55 ∗ t52)`
- **Block Frequency:** 963

- **Max Loop Iterations:** `557`
- **Max Sub-Sequence Length:** `1115` steps (if one case consumes all iterations)

![nested LOOP_22 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.0_nested_LOOP_22.png)

### `[nested PAR_18]`
- **Internal Structure:** `{[τ │ (t56 ∗ τ)], [⟨[τ │ ⟨[τ │ {t62, t37, ⟨t48, t68⟩}], t65⟩], (t55 ∗ t52)⟩ │ τ]}`
- **Block Frequency:** 1501



![nested PAR_18 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.0_nested_PAR_18.png)

### `[nested LOOP_17]`
- **Internal Structure:** `(⟨[τ │ ⟨t46, [t69 │ t70 │ t47]⟩], {[τ │ (t56 ∗ τ)], [⟨[τ │ ⟨[τ │ {t62, t37, ⟨t48, t68⟩}], t65⟩], (t55 ∗ t52)⟩ │ τ]}⟩ ∗ τ)`
- **Block Frequency:** 375

- **Max Loop Iterations:** `1126`
- **Max Sub-Sequence Length:** `2253` steps (if one case consumes all iterations)

![nested LOOP_17 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.0_nested_LOOP_17.png)

### `[nested PAR_13]`
- **Internal Structure:** `{[τ │ (t40 ∗ τ)], [⟨[τ │ (⟨t39, [⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ t32)], (⟨[τ │ ⟨t46, [t69 │ t70 │ t47]⟩], {[τ │ (t56 ∗ τ)], [⟨[τ │ ⟨[τ │ {t62, t37, ⟨t48, t68⟩}], t65⟩], (t55 ∗ t52)⟩ │ τ]}⟩ ∗ τ)⟩ │ τ]}`
- **Block Frequency:** 626



![nested PAR_13 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.0_nested_PAR_13.png)

### `[nested PAR_10]`
- **Internal Structure:** `{[τ │ (t34 ∗ τ)], ⟨[τ │ ⟨t26, t27⟩], [t71 │ ⟨[τ │ t28], (t42 ∗ t41)⟩ │ τ], {[τ │ (t40 ∗ τ)], [⟨[τ │ (⟨t39, [⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ t32)], (⟨[τ │ ⟨t46, [t69 │ t70 │ t47]⟩], {[τ │ (t56 ∗ τ)], [⟨[τ │ ⟨[τ │ {t62, t37, ⟨t48, t68⟩}], t65⟩], (t55 ∗ t52)⟩ │ τ]}⟩ ∗ τ)⟩ │ τ]}⟩}`
- **Block Frequency:** 626



![nested PAR_10 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.0_nested_PAR_10.png)
