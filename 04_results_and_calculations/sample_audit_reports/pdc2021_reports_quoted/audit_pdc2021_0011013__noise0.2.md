# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_0011013.xes` |
| **Noise Threshold** | `0.2` |
| **Fitness** | `0.9511513567528672` |
| **Precision** | `0.38495876008338625` |
| **Total Cases in Log** | `1000` |
| **Unique Activities** | `35` |
| **XOR Operators** | `31` |
| **LOOP Operators** | `3` |
| **SEQ Operators** | `21` |
| **PAR Operators** | `6` |
| **Binarization Additions** | `15` |
| **Tau Operators Added** | `19` |
| **Total Found Patterns** | `172` |
| **Verified Patterns** | `91` |
| **Discrepancy Patterns** | `23` |
| **Ghost Patterns** | `0` |
| **Nested LOOPs** | `3` |
| **Nested PARs** | `6` |
| **Tree Exposure (Strict, End-to-End % of N)** | `11.90%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `50.87%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `33.93%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `61.36%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `11.90%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `0.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `96.61%` |
| **Data Exposure, ST-only (% confirmed)** | `99.57%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `99.74%` |
| **Data Coverage, ST-only (% of real log)** | `43.69%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `82.65%` |
| **Data Coverage, Total (% of real log)** | `100.00%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `12.43%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `64.19%` |
| **Mean Absolute Exposure Volume (events/case)** | `2.50` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_0011013__noise0.2.png)


```text
->( 't10', X( tau, ->( X( tau, 't11' ), +( X( tau, 't06' ), X( tau, 't05' ), X( tau, 't04' ) ) ) ), X( 't15', ->( X( tau, 't16' ), 't20' ) ), X( tau, ->( +( *( 't17', tau ), X( tau, 't24' ), ->( 't21', X( tau, 't23' ) ) ), X( tau, 't22' ), *( X( 't34', ->( X( tau, ->( X( 't27', 't26' ), X( tau, 't28' ) ) ), X( tau, 't42', 't39' ) ) ), tau ), X( 't71', ->( X( tau, 't43' ), X( tau, 't44' ), +( X( tau, *( 't40', tau ) ), ->( 't36', 't46', X( tau, 't47' ), X( tau, +( X( tau, 't48' ), X( tau, 't37' ) ) ) ) ), X( tau, 't68' ), X( 't69', 't70', ->( 't56', 't62' ) ), 't65' ) ), 't55' ) ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_0011013__noise0.2.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST]` | `t10` | Exact Token Match | $\ge$ 1000 | **1000** | ✅ **VERIFIED** |
| `[ST]` | `t11` | Exact Token Match | $\ge$ 271 | **271** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `t06` | Exact Token Match | $\ge$ 485 | **485** | ✅ **VERIFIED** |
| `[ST (in PAR_2)]` | `t05` | Exact Token Match | $\ge$ 390 | **390** | ✅ **VERIFIED** |
| `[ST (in PAR_2)]` | `t04` | Exact Token Match | $\ge$ 224 | **224** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_1]` | Exact Token Match | $\ge$ 485 | **756** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 214 | **756** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 271 | **271** | ✅ **VERIFIED** |
| `[ST]` | `t15` | Exact Token Match | $\ge$ 502 | **502** | ✅ **VERIFIED** |
| `[ST]` | `t16` | Exact Token Match | $\ge$ 135 | **135** | ✅ **VERIFIED** |
| `[ST]` | `t20` | Exact Token Match | $\ge$ 379 | **379** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t20⟩` | Exact Token Match | $\ge$ 244 | **379** | ✅ **VERIFIED** |
| `[ST]` | `⟨t16, t20⟩` | Exact Token Match | $\ge$ 135 | **135** | ✅ **VERIFIED** |
| `[ST (in LOOP_4)]` | `t17` | Exact Token Match | $\ge$ 621 | **621** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t17⟩` | Exact Token Match | $\ge$ 409 | **621** | ✅ **VERIFIED** |
| `[AS (in PAR_3)]` | `[nested LOOP_4]` | Exact Token Match | $\ge$ 1 | **621** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t24` | Exact Token Match | $\ge$ 242 | **242** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t21` | Exact Token Match | $\ge$ 515 | **515** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t23` | Exact Token Match | $\ge$ 242 | **242** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t21, τ⟩` | Exact Token Match | $\ge$ 273 | **515** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t21, t23⟩` | Exact Token Match | $\ge$ 242 | **242** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_3]` | Exact Token Match | $\ge$ 515 | **515** | ✅ **VERIFIED** |
| `[ST]` | `t22` | Exact Token Match | $\ge$ 273 | **273** | ✅ **VERIFIED** |
| `[ST (in LOOP_6)]` | `t34` | Exact Token Match | $\ge$ 373 | **373** | ✅ **VERIFIED** |
| `[ST (in LOOP_6)]` | `t27` | Exact Token Match | $\ge$ 242 | **242** | ✅ **VERIFIED** |
| `[ST (in LOOP_6)]` | `t26` | Exact Token Match | $\ge$ 242 | **242** | ✅ **VERIFIED** |
| `[ST (in LOOP_6)]` | `t28` | Exact Token Match | $\ge$ 124 | **124** | ✅ **VERIFIED** |
| `[ST (in LOOP_6)]` | `⟨t27, τ⟩` | Exact Token Match | $\ge$ 118 | **242** | ✅ **VERIFIED** |
| `[ST (in LOOP_6)]` | `⟨t26, τ⟩` | Exact Token Match | $\ge$ 118 | **242** | ✅ **VERIFIED** |
| `[ST (in LOOP_6)]` | `t42` | Exact Token Match | $\ge$ 397 | **397** | ✅ **VERIFIED** |
| `[ST (in LOOP_6)]` | `t39` | Exact Token Match | $\ge$ 397 | **397** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_6]` | Exact Token Match | $\ge$ 1 | **515** | ✅ **VERIFIED** |
| `[ST]` | `t71` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[ST]` | `t43` | Exact Token Match | $\ge$ 141 | **141** | ✅ **VERIFIED** |
| `[ST]` | `t44` | Exact Token Match | $\ge$ 141 | **141** | ✅ **VERIFIED** |
| `[ST (in LOOP_8)]` | `t40` | Exact Token Match | $\ge$ 199 | **199** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨t40⟩` | Exact Token Match | $\ge$ 199 | **199** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `t36` | Exact Token Match | $\ge$ 397 | **397** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `t46` | Exact Token Match | $\ge$ 397 | **397** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `t47` | Exact Token Match | $\ge$ 138 | **138** | ✅ **VERIFIED** |
| `[ST (in PAR_9)]` | `t48` | Exact Token Match | $\ge$ 63 | **63** | ✅ **VERIFIED** |
| `[ST (in PAR_9)]` | `t37` | Exact Token Match | $\ge$ 74 | **74** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨t47, τ⟩` | Exact Token Match | $\ge$ 64 | **138** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨t46, t47, τ⟩` | Exact Token Match | $\ge$ 64 | **138** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨t46, τ⟩` | Exact Token Match | $\ge$ 259 | **397** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨t46, t47⟩` | Exact Token Match | $\ge$ 138 | **138** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨t36, t46, t47, τ⟩` | Exact Token Match | $\ge$ 64 | **138** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨t36, t46, τ⟩` | Exact Token Match | $\ge$ 259 | **397** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨t36, t46, t47⟩` | Exact Token Match | $\ge$ 138 | **138** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨t36, t46⟩` | Exact Token Match | $\ge$ 397 | **397** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_7]` | Exact Token Match | $\ge$ 397 | **397** | ✅ **VERIFIED** |
| `[ST]` | `t68` | Exact Token Match | $\ge$ 63 | **63** | ✅ **VERIFIED** |
| `[ST]` | `t69` | Exact Token Match | $\ge$ 119 | **119** | ✅ **VERIFIED** |
| `[ST]` | `t70` | Exact Token Match | $\ge$ 140 | **140** | ✅ **VERIFIED** |
| `[ST]` | `t56` | Exact Token Match | $\ge$ 138 | **138** | ✅ **VERIFIED** |
| `[ST]` | `t62` | Exact Token Match | $\ge$ 138 | **138** | ✅ **VERIFIED** |
| `[ST]` | `t65` | Exact Token Match | $\ge$ 397 | **397** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t69, t65⟩` | Exact Token Match | $\ge$ 56 | **116** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t70, t65⟩` | Exact Token Match | $\ge$ 77 | **139** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t56, t62, t65⟩` | Exact Token Match | $\ge$ 75 | **135** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t69⟩` | Exact Token Match | $\ge$ 56 | **119** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t70⟩` | Exact Token Match | $\ge$ 77 | **140** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t56, t62⟩` | Exact Token Match | $\ge$ 75 | **136** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t56⟩` | Exact Token Match | $\ge$ 75 | **138** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_7], τ, t69, t65⟩` | Exact Token Match | $\ge$ 56 | **113** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_7], τ, t70, t65⟩` | Exact Token Match | $\ge$ 77 | **138** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_7], τ, t56, t62, t65⟩` | Exact Token Match | $\ge$ 75 | **79** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_7], τ, t69⟩` | Exact Token Match | $\ge$ 56 | **116** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_7], τ, t70⟩` | Exact Token Match | $\ge$ 77 | **139** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_7], τ, t56, t62⟩` | Exact Token Match | $\ge$ 75 | **79** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_7], τ, t56⟩` | Exact Token Match | $\ge$ 75 | **79** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_7], τ⟩` | Exact Token Match | $\ge$ 334 | **397** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_7], τ⟩` | Exact Token Match | $\ge$ 193 | **397** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_7]⟩` | Exact Token Match | $\ge$ 256 | **397** | ✅ **VERIFIED** |
| `[ST]` | `⟨t44, [nested PAR_7], τ⟩` | Exact Token Match | $\ge$ 78 | **139** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, τ, [nested PAR_7], τ⟩` | Exact Token Match | $\ge$ 52 | **397** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, τ, [nested PAR_7]⟩` | Exact Token Match | $\ge$ 115 | **397** | ✅ **VERIFIED** |
| `[ST]` | `t55` | Exact Token Match | $\ge$ 515 | **515** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_7], τ, t69, t65, t55⟩` | Exact Token Match | $\ge$ 56 | **112** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_7], τ, t70, t65, t55⟩` | Exact Token Match | $\ge$ 77 | **136** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_7], τ, t56, t62, t65, t55⟩` | Exact Token Match | $\ge$ 75 | **78** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t69, t65, t55⟩` | Exact Token Match | $\ge$ 56 | **115** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t70, t65, t55⟩` | Exact Token Match | $\ge$ 77 | **137** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t56, t62, t65, t55⟩` | Exact Token Match | $\ge$ 75 | **133** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_3], τ⟩` | Exact Token Match | $\ge$ 242 | **515** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t15⟩` | Exact Token Match | $\ge$ 17 | **502** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 119 | **1000** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ, t15⟩` | Exact Token Match | $\ge$ 17 | **488** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 396 | **1000** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 214 | **720** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 214 | **1000** | ✅ **VERIFIED** |
| `[AS (in PAR_1)]` | `[nested PAR_2]` | Exact Token Match | $\ge$ 390 | **119** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_3)]` | `[nested PAR_5]` | Exact Token Match | $\ge$ 515 | **242** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_7)]` | `[nested PAR_9]` | Exact Token Match | $\ge$ 74 | **31** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_7)]` | `⟨t47, [nested PAR_9]⟩` | Exact Token Match | $\ge$ 74 | **31** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_7)]` | `⟨t46, t47, [nested PAR_9]⟩` | Exact Token Match | $\ge$ 74 | **31** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_7)]` | `⟨t36, t46, t47, [nested PAR_9]⟩` | Exact Token Match | $\ge$ 74 | **31** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t56, t62⟩` | Exact Token Match | $\ge$ 138 | **136** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t69, t65⟩` | Exact Token Match | $\ge$ 119 | **116** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t70, t65⟩` | Exact Token Match | $\ge$ 140 | **139** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t56, t62, t65⟩` | Exact Token Match | $\ge$ 138 | **135** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t62, t65⟩` | Exact Token Match | $\ge$ 138 | **137** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_7], t68⟩` | Exact Token Match | $\ge$ 63 | **49** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t44, [nested PAR_7]⟩` | Exact Token Match | $\ge$ 141 | **139** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t71, t55⟩` | Exact Token Match | $\ge$ 118 | **114** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t69, t65, t55⟩` | Exact Token Match | $\ge$ 119 | **115** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t70, t65, t55⟩` | Exact Token Match | $\ge$ 140 | **137** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t56, t62, t65, t55⟩` | Exact Token Match | $\ge$ 138 | **133** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t62, t65, t55⟩` | Exact Token Match | $\ge$ 138 | **135** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t65, t55⟩` | Exact Token Match | $\ge$ 397 | **392** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_3], t22⟩` | Exact Token Match | $\ge$ 273 | **266** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t15, [nested PAR_3]⟩` | Exact Token Match | $\ge$ 136 | **135** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, t11, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 271 | **269** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, t11⟩` | Exact Token Match | $\ge$ 271 | **269** | ⚠️ **DISCREPANCY** |

## Audit Summary
- **Perfect Pattern Verifications:** 91
- **Frequency Discrepancies:** 23
- **Ghost Patterns (Fatal):** 0
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 11.90%
- **Tree Exposure (Strict, Fragment-Level % of N):** 50.87%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 33.93%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 61.36%
- **Total Forced Volume (incl. unresolved AS, % of N):** 11.90%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 0.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 96.61%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 99.57%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 99.74%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 43.69%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 82.65%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 100.00%
- **Max Fractional Exposure (Worst-Case Normalized):** 12.43% (expected length: 1000.82 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 64.19% (expected length: 10.23 events)
- **Mean Absolute Exposure Volume:** 2.50 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested PAR_2]`
- **Internal Structure:** `{[τ │ t05], [τ │ t04]}`
- **Block Frequency:** 390



![nested PAR_2 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.2_nested_PAR_2.png)

### `[nested PAR_1]`
- **Internal Structure:** `{[τ │ t06], [{[τ │ t05], [τ │ t04]} │ τ]}`
- **Block Frequency:** 485



![nested PAR_1 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.2_nested_PAR_1.png)

### `[nested LOOP_4]`
- **Internal Structure:** `(t17 ∗ τ)`
- **Block Frequency:** 515

- **Max Loop Iterations:** `106`
- **Max Sub-Sequence Length:** `213` steps (if one case consumes all iterations)

![nested LOOP_4 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.2_nested_LOOP_4.png)

### `[nested PAR_5]`
- **Internal Structure:** `{[τ │ t24], ⟨t21, [τ │ t23]⟩}`
- **Block Frequency:** 515



![nested PAR_5 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.2_nested_PAR_5.png)

### `[nested PAR_3]`
- **Internal Structure:** `{(t17 ∗ τ), [τ │ t24], ⟨t21, [τ │ t23]⟩}`
- **Block Frequency:** 515



![nested PAR_3 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.2_nested_PAR_3.png)

### `[nested LOOP_6]`
- **Internal Structure:** `([t34 │ ⟨[τ │ ⟨[t27 │ t26], [τ │ t28]⟩], [τ │ t42 │ t39]⟩] ∗ τ)`
- **Block Frequency:** 515

- **Max Loop Iterations:** `652`
- **Max Sub-Sequence Length:** `1305` steps (if one case consumes all iterations)

![nested LOOP_6 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.2_nested_LOOP_6.png)

### `[nested LOOP_8]`
- **Internal Structure:** `(t40 ∗ τ)`
- **Block Frequency:** 199

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_8 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.2_nested_LOOP_8.png)

### `[nested PAR_9]`
- **Internal Structure:** `{[τ │ t48], [τ │ t37]}`
- **Block Frequency:** 74



![nested PAR_9 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.2_nested_PAR_9.png)

### `[nested PAR_7]`
- **Internal Structure:** `{[τ │ (t40 ∗ τ)], ⟨t36, t46, [⟨[τ │ t47], [τ │ {[τ │ t48], [τ │ t37]}]⟩ │ τ]⟩}`
- **Block Frequency:** 397



![nested PAR_7 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.2_nested_PAR_7.png)
