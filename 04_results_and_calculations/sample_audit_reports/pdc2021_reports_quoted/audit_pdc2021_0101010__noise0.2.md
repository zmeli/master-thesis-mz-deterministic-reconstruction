# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_0101010.xes` |
| **Noise Threshold** | `0.2` |
| **Fitness** | `0.9845724728472475` |
| **Precision** | `0.3700390299521993` |
| **Total Cases in Log** | `1000` |
| **Unique Activities** | `39` |
| **XOR Operators** | `29` |
| **LOOP Operators** | `13` |
| **SEQ Operators** | `22` |
| **PAR Operators** | `8` |
| **Binarization Additions** | `13` |
| **Tau Operators Added** | `17` |
| **Total Found Patterns** | `173` |
| **Verified Patterns** | `101` |
| **Discrepancy Patterns** | `15` |
| **Ghost Patterns** | `2` |
| **Nested LOOPs** | `13` |
| **Nested PARs** | `8` |
| **Tree Exposure (Strict, End-to-End % of N)** | `25.50%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `38.33%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `7.68%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `35.08%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `25.50%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `0.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `92.59%` |
| **Data Exposure, ST-only (% confirmed)** | `95.68%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `98.21%` |
| **Data Coverage, ST-only (% of real log)** | `15.74%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `60.88%` |
| **Data Coverage, Total (% of real log)** | `100.00%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `26.47%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `100.00%` |
| **Mean Absolute Exposure Volume (events/case)** | `16.64` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_0101010__noise0.2.png)


```text
->( 't10', X( tau, ->( X( 't06', 't11' ), X( tau, +( X( tau, *( 't05', tau ) ), X( tau, *( 't04', 't07' ) ) ) ), X( tau, *( 't15', tau ) ), X( tau, 't16' ) ) ), X( tau, ->( 't20', +( *( 't17', tau ), 't21', X( tau, ->( 't24', 't23' ) ) ), X( tau, 't22' ), +( X( tau, *( 't34', tau ) ), ->( X( tau, ->( 't26', 't27' ) ), X( 't71', ->( X( tau, 't28' ), *( 't42', 't41' ) ) ), +( X( tau, *( 't40', tau ) ), ->( X( tau, *( ->( 't39', X( tau, ->( 't43', 't44' ) ), *( 't36', tau ) ), 't32' ) ), *( ->( 't46', X( 't69', 't70', 't47' ), X( tau, +( 't62', 't37', ->( 't48', 't68' ) ) ), 't65', +( *( 't55', tau ), X( tau, *( *( 't56', tau ), 't52' ) ) ) ), tau ) ) ) ) ) ) ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_0101010__noise0.2.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST]` | `t10` | Exact Token Match | $\ge$ 1000 | **1000** | ✅ **VERIFIED** |
| `[ST]` | `t06` | Exact Token Match | $\ge$ 496 | **496** | ✅ **VERIFIED** |
| `[ST]` | `t11` | Exact Token Match | $\ge$ 249 | **249** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `t05` | Exact Token Match | $\ge$ 504 | **504** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t05⟩` | Exact Token Match | $\ge$ 504 | **504** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t04` | Exact Token Match | $\ge$ 324 | **324** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t07` | Exact Token Match | $\ge$ 73 | **73** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t04⟩` | Exact Token Match | $\ge$ 178 | **324** | ✅ **VERIFIED** |
| `[AS (in PAR_1)]` | `[nested LOOP_3]` | Exact Token Match | $\ge$ 1 | **73** | ✅ **VERIFIED** |
| `[ST (in LOOP_4)]` | `t15` | Exact Token Match | $\ge$ 556 | **556** | ✅ **VERIFIED** |
| `[ST]` | `t16` | Exact Token Match | $\ge$ 171 | **171** | ✅ **VERIFIED** |
| `[ST]` | `⟨t15, τ⟩` | Exact Token Match | $\ge$ 385 | **487** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t15⟩` | Exact Token Match | $\ge$ 52 | **487** | ✅ **VERIFIED** |
| `[ST]` | `⟨t06, [nested PAR_1], t15, τ⟩` | Exact Token Match | $\ge$ 84 | **151** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, [nested PAR_1], t15⟩` | Exact Token Match | $\ge$ 8 | **57** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 8 | **249** | ✅ **VERIFIED** |
| `[ST]` | `t20` | Exact Token Match | $\ge$ 426 | **426** | ✅ **VERIFIED** |
| `[ST (in LOOP_6)]` | `t17` | Exact Token Match | $\ge$ 662 | **662** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t17⟩` | Exact Token Match | $\ge$ 346 | **662** | ✅ **VERIFIED** |
| `[AS (in PAR_5)]` | `[nested LOOP_6]` | Exact Token Match | $\ge$ 1 | **662** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `t21` | Exact Token Match | $\ge$ 504 | **504** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `t24` | Exact Token Match | $\ge$ 236 | **236** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `t23` | Exact Token Match | $\ge$ 236 | **236** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨t24, t23⟩` | Exact Token Match | $\ge$ 236 | **236** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_5]` | Exact Token Match | $\ge$ 504 | **504** | ✅ **VERIFIED** |
| `[ST]` | `t22` | Exact Token Match | $\ge$ 268 | **268** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `t34` | Exact Token Match | $\ge$ 506 | **506** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨t34⟩` | Exact Token Match | $\ge$ 506 | **506** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `t26` | Exact Token Match | $\ge$ 236 | **236** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `t27` | Exact Token Match | $\ge$ 236 | **236** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨t26, t27⟩` | Exact Token Match | $\ge$ 236 | **236** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `t71` | Exact Token Match | $\ge$ 129 | **129** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `t28` | Exact Token Match | $\ge$ 107 | **107** | ✅ **VERIFIED** |
| `[ST (in LOOP_10)]` | `t42` | Exact Token Match | $\ge$ 524 | **792** | ✅ **VERIFIED** |
| `[ST (in LOOP_10)]` | `t41` | Exact Token Match | $\ge$ 417 | **417** | ✅ **VERIFIED** |
| `[AS (in PAR_8)]` | `[nested LOOP_10]` | Exact Token Match | $\ge$ 1 | **417** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨t28, [nested LOOP_10]⟩` | Exact Token Match | $\ge$ 1 | **62** | ✅ **VERIFIED** |
| `[ST (in LOOP_12)]` | `t40` | Exact Token Match | $\ge$ 626 | **626** | ✅ **VERIFIED** |
| `[ST (in PAR_11)]` | `⟨t40⟩` | Exact Token Match | $\ge$ 626 | **626** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `t39` | Exact Token Match | $\ge$ 788 | **788** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `t43` | Exact Token Match | $\ge$ 248 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `t44` | Exact Token Match | $\ge$ 248 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `⟨t43, t44⟩` | Exact Token Match | $\ge$ 248 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_14)]` | `t36` | Exact Token Match | $\ge$ 1203 | **1203** | ✅ **VERIFIED** |
| `[AS (in LOOP_13)]` | `[nested LOOP_14]` | Exact Token Match | $\ge$ 1 | **375** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `⟨t43, t44, [nested LOOP_14]⟩` | Exact Token Match | $\ge$ 1 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `⟨t44, [nested LOOP_14]⟩` | Exact Token Match | $\ge$ 1 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `⟨t39, t43, t44, [nested LOOP_14]⟩` | Exact Token Match | $\ge$ 1 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `⟨t39, τ⟩` | Exact Token Match | $\ge$ 540 | **788** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `⟨t39, t43, t44⟩` | Exact Token Match | $\ge$ 248 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `⟨t39, t43⟩` | Exact Token Match | $\ge$ 248 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `t32` | Exact Token Match | $\ge$ 413 | **413** | ✅ **VERIFIED** |
| `[AS (in PAR_11)]` | `[nested LOOP_13]` | Exact Token Match | $\ge$ 1 | **184** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `t46` | Exact Token Match | $\ge$ 963 | **963** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `t69` | Exact Token Match | $\ge$ 305 | **305** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `t70` | Exact Token Match | $\ge$ 302 | **302** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `t47` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[ST (in PAR_16)]` | `t62` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[ST (in PAR_17)]` | `t37` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[ST (in PAR_17)]` | `t48` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[ST (in PAR_17)]` | `t68` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[ST (in PAR_17)]` | `⟨t48, t68⟩` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[AS (in PAR_16)]` | `[nested PAR_17]` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[AS (in LOOP_15)]` | `[nested PAR_16]` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `t65` | Exact Token Match | $\ge$ 963 | **963** | ✅ **VERIFIED** |
| `[ST (in LOOP_19)]` | `t55` | Exact Token Match | $\ge$ 1649 | **1649** | ✅ **VERIFIED** |
| `[ST (in PAR_18)]` | `⟨t55⟩` | Exact Token Match | $\ge$ 239 | **1649** | ✅ **VERIFIED** |
| `[AS (in PAR_18)]` | `[nested LOOP_19]` | Exact Token Match | $\ge$ 1 | **1649** | ✅ **VERIFIED** |
| `[ST (in LOOP_21)]` | `t56` | Exact Token Match | $\ge$ 1501 | **1501** | ✅ **VERIFIED** |
| `[ST (in LOOP_20)]` | `⟨t56⟩` | Exact Token Match | $\ge$ 1501 | **1501** | ✅ **VERIFIED** |
| `[ST (in LOOP_20)]` | `t52` | Exact Token Match | $\ge$ 557 | **557** | ✅ **VERIFIED** |
| `[ST (in PAR_18)]` | `⟨t56⟩` | Exact Token Match | $\ge$ 387 | **1501** | ✅ **VERIFIED** |
| `[AS (in PAR_18)]` | `[nested LOOP_20]` | Exact Token Match | $\ge$ 1 | **557** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨t65, [nested PAR_18]⟩` | Exact Token Match | $\ge$ 944 | **963** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨t65, τ⟩` | Exact Token Match | $\ge$ 19 | **963** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨τ, t65, [nested PAR_18]⟩` | Exact Token Match | $\ge$ 588 | **963** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨[nested PAR_16], t65, [nested PAR_18]⟩` | Exact Token Match | $\ge$ 337 | **356** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨τ, t65⟩` | Exact Token Match | $\ge$ 607 | **963** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨[nested PAR_16], t65⟩` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨t46, t69⟩` | Exact Token Match | $\ge$ 305 | **305** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨t46, t70⟩` | Exact Token Match | $\ge$ 302 | **302** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨t46, t47⟩` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[AS (in PAR_11)]` | `[nested LOOP_15]` | Exact Token Match | $\ge$ 1 | **63** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨t28, [nested LOOP_10], [nested PAR_11]⟩` | Exact Token Match | $\ge$ 1 | **4** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨[nested LOOP_10], [nested PAR_11]⟩` | Exact Token Match | $\ge$ 1 | **9** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_8]⟩` | Exact Token Match | $\ge$ 358 | **504** | ✅ **VERIFIED** |
| `[ST]` | `⟨t22, [nested PAR_8]⟩` | Exact Token Match | $\ge$ 268 | **268** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_5], τ, [nested PAR_8]⟩` | Exact Token Match | $\ge$ 236 | **504** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_5], t22, [nested PAR_8]⟩` | Exact Token Match | $\ge$ 146 | **268** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_5], τ⟩` | Exact Token Match | $\ge$ 236 | **504** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_5], t22⟩` | Exact Token Match | $\ge$ 146 | **268** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, [nested PAR_5], τ, [nested PAR_8]⟩` | Exact Token Match | $\ge$ 36 | **426** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, [nested PAR_5], τ⟩` | Exact Token Match | $\ge$ 36 | **426** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 304 | **426** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 78 | **504** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 255 | **1000** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06, [nested PAR_1], t15, τ⟩` | Exact Token Match | $\ge$ 84 | **151** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, [nested PAR_1], t15⟩` | Exact Token Match | $\ge$ 8 | **57** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 8 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06⟩` | Exact Token Match | $\ge$ 496 | **496** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11⟩` | Exact Token Match | $\ge$ 249 | **249** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_1]` | Exact Token Match | $\ge$ 504 | **500** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t15⟩` | Exact Token Match | $\ge$ 556 | **487** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t15, t16⟩` | Exact Token Match | $\ge$ 171 | **34** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_1], t15, τ⟩` | Exact Token Match | $\ge$ 333 | **208** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_1], t15⟩` | Exact Token Match | $\ge$ 504 | **208** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t06, [nested PAR_1], t15⟩` | Exact Token Match | $\ge$ 255 | **151** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t06, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 255 | **251** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_5)]` | `[nested PAR_7]` | Exact Token Match | $\ge$ 504 | **236** | ⚠️ **DISCREPANCY** |
| `[AS (in LOOP_15)]` | `[nested PAR_18]` | Exact Token Match | $\ge$ 944 | **504** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_8)]` | `[nested PAR_11]` | Exact Token Match | $\ge$ 626 | **21** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_8)]` | `⟨τ, [nested PAR_11]⟩` | Exact Token Match | $\ge$ 390 | **21** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_8)]` | `⟨τ, τ, [nested PAR_11]⟩` | Exact Token Match | $\ge$ 154 | **21** | ⚠️ **DISCREPANCY** |
| `[AS]` | `[nested PAR_8]` | Exact Token Match | $\ge$ 626 | **504** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, t06, [nested PAR_1], t15⟩` | Exact Token Match | $\ge$ 255 | **151** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, t06, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 255 | **251** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_1], t15, t16⟩` | Exact Token Match | $\ge$ 119 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_8)]` | `⟨t71, [nested PAR_11]⟩` | Exact Token Match | $\ge$ 129 | **0** | ❌ **GHOST PATTERN** |

## Audit Summary
- **Perfect Pattern Verifications:** 101
- **Frequency Discrepancies:** 15
- **Ghost Patterns (Fatal):** 2
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 25.50%
- **Tree Exposure (Strict, Fragment-Level % of N):** 38.33%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 7.68%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 35.08%
- **Total Forced Volume (incl. unresolved AS, % of N):** 25.50%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 0.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 92.59%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 95.68%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 98.21%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 15.74%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 60.88%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 100.00%
- **Max Fractional Exposure (Worst-Case Normalized):** 26.47% (expected length: 3796.77 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 100.00% (expected length: 19.41 events)
- **Mean Absolute Exposure Volume:** 16.64 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_2]`
- **Internal Structure:** `(t05 ∗ τ)`
- **Block Frequency:** 504

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_2 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.2_nested_LOOP_2.png)

### `[nested LOOP_3]`
- **Internal Structure:** `(t04 ∗ t07)`
- **Block Frequency:** 251

- **Max Loop Iterations:** `73`
- **Max Sub-Sequence Length:** `147` steps (if one case consumes all iterations)

![nested LOOP_3 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.2_nested_LOOP_3.png)

### `[nested PAR_1]`
- **Internal Structure:** `{[τ │ (t05 ∗ τ)], [τ │ (t04 ∗ t07)]}`
- **Block Frequency:** 504



![nested PAR_1 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.2_nested_PAR_1.png)

### `[nested LOOP_4]`
- **Internal Structure:** `(t15 ∗ τ)`
- **Block Frequency:** 556

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_4 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.2_nested_LOOP_4.png)

### `[nested LOOP_6]`
- **Internal Structure:** `(t17 ∗ τ)`
- **Block Frequency:** 504

- **Max Loop Iterations:** `158`
- **Max Sub-Sequence Length:** `317` steps (if one case consumes all iterations)

![nested LOOP_6 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.2_nested_LOOP_6.png)

### `[nested PAR_7]`
- **Internal Structure:** `{t21, [τ │ ⟨t24, t23⟩]}`
- **Block Frequency:** 504



![nested PAR_7 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.2_nested_PAR_7.png)

### `[nested PAR_5]`
- **Internal Structure:** `{(t17 ∗ τ), t21, [τ │ ⟨t24, t23⟩]}`
- **Block Frequency:** 504



![nested PAR_5 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.2_nested_PAR_5.png)

### `[nested LOOP_9]`
- **Internal Structure:** `(t34 ∗ τ)`
- **Block Frequency:** 506

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_9 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.2_nested_LOOP_9.png)

### `[nested LOOP_10]`
- **Internal Structure:** `(t42 ∗ t41)`
- **Block Frequency:** 107

- **Max Loop Iterations:** `417`
- **Max Sub-Sequence Length:** `835` steps (if one case consumes all iterations)

![nested LOOP_10 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.2_nested_LOOP_10.png)

### `[nested LOOP_12]`
- **Internal Structure:** `(t40 ∗ τ)`
- **Block Frequency:** 626

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_12 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.2_nested_LOOP_12.png)

### `[nested LOOP_14]`
- **Internal Structure:** `(t36 ∗ τ)`
- **Block Frequency:** 248

- **Max Loop Iterations:** `955`
- **Max Sub-Sequence Length:** `1911` steps (if one case consumes all iterations)

![nested LOOP_14 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.2_nested_LOOP_14.png)

### `[nested LOOP_13]`
- **Internal Structure:** `(⟨t39, [⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ t32)`
- **Block Frequency:** 375

- **Max Loop Iterations:** `413`
- **Max Sub-Sequence Length:** `827` steps (if one case consumes all iterations)

![nested LOOP_13 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.2_nested_LOOP_13.png)

### `[nested PAR_17]`
- **Internal Structure:** `{t37, ⟨t48, t68⟩}`
- **Block Frequency:** 356



![nested PAR_17 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.2_nested_PAR_17.png)

### `[nested PAR_16]`
- **Internal Structure:** `{t62, t37, ⟨t48, t68⟩}`
- **Block Frequency:** 356



![nested PAR_16 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.2_nested_PAR_16.png)

### `[nested LOOP_19]`
- **Internal Structure:** `(t55 ∗ τ)`
- **Block Frequency:** 944

- **Max Loop Iterations:** `705`
- **Max Sub-Sequence Length:** `1411` steps (if one case consumes all iterations)

![nested LOOP_19 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.2_nested_LOOP_19.png)

### `[nested LOOP_21]`
- **Internal Structure:** `(t56 ∗ τ)`
- **Block Frequency:** 1501

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_21 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.2_nested_LOOP_21.png)

### `[nested LOOP_20]`
- **Internal Structure:** `((t56 ∗ τ) ∗ t52)`
- **Block Frequency:** 944

- **Max Loop Iterations:** `557`
- **Max Sub-Sequence Length:** `1115` steps (if one case consumes all iterations)

![nested LOOP_20 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.2_nested_LOOP_20.png)

### `[nested PAR_18]`
- **Internal Structure:** `{(t55 ∗ τ), [τ │ ((t56 ∗ τ) ∗ t52)]}`
- **Block Frequency:** 944



![nested PAR_18 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.2_nested_PAR_18.png)

### `[nested LOOP_15]`
- **Internal Structure:** `(⟨t46, [t69 │ t70 │ t47], [τ │ {t62, t37, ⟨t48, t68⟩}], t65, [{(t55 ∗ τ), [τ │ ((t56 ∗ τ) ∗ t52)]} │ τ]⟩ ∗ τ)`
- **Block Frequency:** 375

- **Max Loop Iterations:** `588`
- **Max Sub-Sequence Length:** `1177` steps (if one case consumes all iterations)

![nested LOOP_15 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.2_nested_LOOP_15.png)

### `[nested PAR_11]`
- **Internal Structure:** `{[τ │ (t40 ∗ τ)], [⟨[τ │ (⟨t39, [⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ t32)], (⟨t46, [t69 │ t70 │ t47], [τ │ {t62, t37, ⟨t48, t68⟩}], t65, [{(t55 ∗ τ), [τ │ ((t56 ∗ τ) ∗ t52)]} │ τ]⟩ ∗ τ)⟩ │ τ]}`
- **Block Frequency:** 626



![nested PAR_11 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.2_nested_PAR_11.png)

### `[nested PAR_8]`
- **Internal Structure:** `{[τ │ (t34 ∗ τ)], ⟨[τ │ ⟨t26, t27⟩], [t71 │ ⟨[τ │ t28], (t42 ∗ t41)⟩ │ τ], {[τ │ (t40 ∗ τ)], [⟨[τ │ (⟨t39, [⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ t32)], (⟨t46, [t69 │ t70 │ t47], [τ │ {t62, t37, ⟨t48, t68⟩}], t65, [{(t55 ∗ τ), [τ │ ((t56 ∗ τ) ∗ t52)]} │ τ]⟩ ∗ τ)⟩ │ τ]}⟩}`
- **Block Frequency:** 626



![nested PAR_8 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.2_nested_PAR_8.png)
