# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_0011012.xes` |
| **Noise Threshold** | `0.8` |
| **Fitness** | `0.6609264426582661` |
| **Precision** | `0.8792932628797886` |
| **Total Cases in Log** | `1000` |
| **Unique Activities** | `34` |
| **XOR Operators** | `32` |
| **LOOP Operators** | `1` |
| **SEQ Operators** | `26` |
| **PAR Operators** | `2` |
| **Binarization Additions** | `17` |
| **Tau Operators Added** | `27` |
| **Total Found Patterns** | `146` |
| **Verified Patterns** | `86` |
| **Discrepancy Patterns** | `13` |
| **Ghost Patterns** | `0` |
| **Nested LOOPs** | `1` |
| **Nested PARs** | `2` |
| **Tree Exposure (Strict, End-to-End % of N)** | `11.10%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `46.82%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `24.68%` |
| **Tree Exposure (Local-Strict % of N)** | `93.86%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `45.57%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `11.10%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `0.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `98.35%` |
| **Data Exposure, ST-only (% confirmed)** | `97.85%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `98.18%` |
| **Data Coverage, ST-only (% of real log)** | `78.89%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `98.77%` |
| **Data Coverage, Total (% of real log)** | `98.77%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `13.64%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `46.82%` |
| **Mean Absolute Exposure Volume (events/case)** | `1.53` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_0011012__noise0.8.png)


```text
->( 't10', X( 't11', ->( 't06', 't04' ) ), 't05', X( 't15', ->( 't16', 't20' ) ), +( *( 't17', tau ), ->( 't21', 't24', 't23' ) ), 't22', 't34', 't26', 't27', 't28', 't42', 't39', X( 't71', ->( 't43', 't44', X( ->( 't40', 't36', 't46' ), ->( 't47', +( ->( 't56', 't62' ), ->( 't48', 't68' ) ) ) ), X( 't69', 't70' ), 't65' ) ), 't55' )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_0011012__noise0.8.png)



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
| `[ST]` | `t26` | Exact Token Match | $\ge$ 236 | **236** | ✅ **VERIFIED** |
| `[ST]` | `t27` | Exact Token Match | $\ge$ 235 | **235** | ✅ **VERIFIED** |
| `[ST]` | `t28` | Exact Token Match | $\ge$ 126 | **126** | ✅ **VERIFIED** |
| `[ST]` | `t42` | Exact Token Match | $\ge$ 357 | **357** | ✅ **VERIFIED** |
| `[ST]` | `t39` | Exact Token Match | $\ge$ 357 | **357** | ✅ **VERIFIED** |
| `[ST]` | `t71` | Exact Token Match | $\ge$ 109 | **109** | ✅ **VERIFIED** |
| `[ST]` | `t43` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[ST]` | `t44` | Exact Token Match | $\ge$ 119 | **119** | ✅ **VERIFIED** |
| `[ST]` | `t36` | Exact Token Match | $\ge$ 358 | **358** | ✅ **VERIFIED** |
| `[ST]` | `t46` | Exact Token Match | $\ge$ 360 | **360** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t46⟩` | Exact Token Match | $\ge$ 2 | **360** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t36, t46⟩` | Exact Token Match | $\ge$ 184 | **356** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t36⟩` | Exact Token Match | $\ge$ 184 | **358** | ✅ **VERIFIED** |
| `[ST]` | `t47` | Exact Token Match | $\ge$ 115 | **115** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `t56` | Exact Token Match | $\ge$ 115 | **115** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `t62` | Exact Token Match | $\ge$ 112 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t56, t62⟩` | Exact Token Match | $\ge$ 112 | **112** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t56, τ⟩` | Exact Token Match | $\ge$ 3 | **115** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `t48` | Exact Token Match | $\ge$ 63 | **63** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `t68` | Exact Token Match | $\ge$ 61 | **61** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t48, t68⟩` | Exact Token Match | $\ge$ 61 | **61** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t48, τ⟩` | Exact Token Match | $\ge$ 2 | **63** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_3]` | Exact Token Match | $\ge$ 115 | **115** | ✅ **VERIFIED** |
| `[ST]` | `⟨t47, [nested PAR_3]⟩` | Exact Token Match | $\ge$ 115 | **115** | ✅ **VERIFIED** |
| `[ST]` | `t69` | Exact Token Match | $\ge$ 144 | **144** | ✅ **VERIFIED** |
| `[ST]` | `t70` | Exact Token Match | $\ge$ 99 | **99** | ✅ **VERIFIED** |
| `[ST]` | `t65` | Exact Token Match | $\ge$ 359 | **359** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t65⟩` | Exact Token Match | $\ge$ 116 | **359** | ✅ **VERIFIED** |
| `[ST]` | `⟨t36, t46, t69, t65⟩` | Exact Token Match | $\ge$ 27 | **140** | ✅ **VERIFIED** |
| `[ST]` | `⟨t46, t69, t65⟩` | Exact Token Match | $\ge$ 29 | **140** | ✅ **VERIFIED** |
| `[ST]` | `⟨t46, τ, t65⟩` | Exact Token Match | $\ge$ 1 | **357** | ✅ **VERIFIED** |
| `[ST]` | `⟨t46, τ⟩` | Exact Token Match | $\ge$ 1 | **360** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t40, t36, t46⟩` | Exact Token Match | $\ge$ 53 | **101** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t40, t36⟩` | Exact Token Match | $\ge$ 53 | **101** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, τ, t36, t46⟩` | Exact Token Match | $\ge$ 65 | **356** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, τ, t36⟩` | Exact Token Match | $\ge$ 65 | **358** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t40⟩` | Exact Token Match | $\ge$ 55 | **136** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t44⟩` | Exact Token Match | $\ge$ 1 | **119** | ✅ **VERIFIED** |
| `[ST]` | `t55` | Exact Token Match | $\ge$ 471 | **471** | ✅ **VERIFIED** |
| `[ST]` | `⟨t69, t65, t55⟩` | Exact Token Match | $\ge$ 31 | **142** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t65, t55⟩` | Exact Token Match | $\ge$ 3 | **358** | ✅ **VERIFIED** |
| `[ST]` | `⟨t65, t55⟩` | Exact Token Match | $\ge$ 246 | **358** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t55⟩` | Exact Token Match | $\ge$ 3 | **471** | ✅ **VERIFIED** |
| `[ST]` | `⟨t39, τ, τ⟩` | Exact Token Match | $\ge$ 11 | **357** | ✅ **VERIFIED** |
| `[ST]` | `⟨t39, τ⟩` | Exact Token Match | $\ge$ 130 | **357** | ✅ **VERIFIED** |
| `[ST]` | `⟨t42, t39⟩` | Exact Token Match | $\ge$ 130 | **352** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t42, t39⟩` | Exact Token Match | $\ge$ 4 | **352** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t42⟩` | Exact Token Match | $\ge$ 231 | **357** | ✅ **VERIFIED** |
| `[ST]` | `⟨t27, τ⟩` | Exact Token Match | $\ge$ 109 | **235** | ✅ **VERIFIED** |
| `[ST]` | `⟨t26, τ⟩` | Exact Token Match | $\ge$ 1 | **236** | ✅ **VERIFIED** |
| `[ST]` | `⟨t34, t26⟩` | Exact Token Match | $\ge$ 8 | **196** | ✅ **VERIFIED** |
| `[ST]` | `⟨t34, τ⟩` | Exact Token Match | $\ge$ 120 | **278** | ✅ **VERIFIED** |
| `[ST]` | `⟨t22, t34⟩` | Exact Token Match | $\ge$ 5 | **81** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t34⟩` | Exact Token Match | $\ge$ 123 | **278** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], τ, t34⟩` | Exact Token Match | $\ge$ 5 | **278** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], t22⟩` | Exact Token Match | $\ge$ 115 | **233** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], τ⟩` | Exact Token Match | $\ge$ 233 | **472** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t15⟩` | Exact Token Match | $\ge$ 160 | **497** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 111 | **959** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11⟩` | Exact Token Match | $\ge$ 183 | **222** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06, t04⟩` | Exact Token Match | $\ge$ 196 | **222** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06, τ⟩` | Exact Token Match | $\ge$ 224 | **468** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06⟩` | Exact Token Match | $\ge$ 461 | **468** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 81 | **959** | ✅ **VERIFIED** |
| `[ST]` | `⟨t06, t04⟩` | Exact Token Match | $\ge$ 237 | **229** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t16, t20⟩` | Exact Token Match | $\ge$ 113 | **110** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_1)]` | `⟨t24, t23⟩` | Exact Token Match | $\ge$ 230 | **229** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_1)]` | `⟨t21, t24, t23⟩` | Exact Token Match | $\ge$ 230 | **226** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_1)]` | `⟨t21, t24⟩` | Exact Token Match | $\ge$ 230 | **227** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t34` | Exact Token Match | $\ge$ 356 | **278** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t40` | Exact Token Match | $\ge$ 174 | **136** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t36, t46⟩` | Exact Token Match | $\ge$ 358 | **356** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t40, t36, t46⟩` | Exact Token Match | $\ge$ 172 | **101** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t40, t36⟩` | Exact Token Match | $\ge$ 172 | **101** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t69, t65⟩` | Exact Token Match | $\ge$ 144 | **142** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t70, t65⟩` | Exact Token Match | $\ge$ 99 | **98** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t15, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 115 | **113** | ⚠️ **DISCREPANCY** |

## Audit Summary
- **Perfect Pattern Verifications:** 86
- **Frequency Discrepancies:** 13
- **Ghost Patterns (Fatal):** 0
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 11.10%
- **Tree Exposure (Strict, Fragment-Level % of N):** 46.82%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 24.68%
- **Tree Exposure (Local-Strict % of N):** 93.86% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 45.57%
- **Total Forced Volume (incl. unresolved AS, % of N):** 11.10%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 0.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 98.35%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 97.85%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 98.18%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 78.89%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 98.77%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 98.77%
- **Max Fractional Exposure (Worst-Case Normalized):** 13.64% (expected length: 132.29 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 46.82% (expected length: 9.42 events)
- **Mean Absolute Exposure Volume:** 1.53 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_2]`
- **Internal Structure:** `(t17 ∗ τ)`
- **Block Frequency:** 466

- **Max Loop Iterations:** `123`
- **Max Sub-Sequence Length:** `247` steps (if one case consumes all iterations)

![nested LOOP_2 Internal Diagram](images/nested_ref_audit_pdc2021_0011012__noise0.8_nested_LOOP_2.png)

### `[nested PAR_1]`
- **Internal Structure:** `{(t17 ∗ τ), ⟨t21, [⟨[t24 │ τ], t23⟩ │ τ]⟩}`
- **Block Frequency:** 466



![nested PAR_1 Internal Diagram](images/nested_ref_audit_pdc2021_0011012__noise0.8_nested_PAR_1.png)

### `[nested PAR_3]`
- **Internal Structure:** `{⟨t56, [t62 │ τ]⟩, [⟨t48, [t68 │ τ]⟩ │ τ]}`
- **Block Frequency:** 115



![nested PAR_3 Internal Diagram](images/nested_ref_audit_pdc2021_0011012__noise0.8_nested_PAR_3.png)
