# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_0011013.xes` |
| **Noise Threshold** | `0.4` |
| **Fitness** | `0.9039835372484369` |
| **Precision** | `0.6415406688003531` |
| **Total Cases in Log** | `1000` |
| **Unique Activities** | `35` |
| **XOR Operators** | `26` |
| **LOOP Operators** | `3` |
| **SEQ Operators** | `21` |
| **PAR Operators** | `6` |
| **Binarization Additions** | `15` |
| **Tau Operators Added** | `17` |
| **Total Found Patterns** | `145` |
| **Verified Patterns** | `82` |
| **Discrepancy Patterns** | `17` |
| **Ghost Patterns** | `0` |
| **Nested LOOPs** | `3` |
| **Nested PARs** | `6` |
| **Tree Exposure (Strict, End-to-End % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `27.35%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `17.44%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `55.20%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `0.00%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `0.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `96.70%` |
| **Data Exposure, ST-only (% confirmed)** | `99.89%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `99.95%` |
| **Data Coverage, ST-only (% of real log)** | `40.37%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `82.65%` |
| **Data Coverage, Total (% of real log)** | `100.00%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `0.60%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `59.72%` |
| **Mean Absolute Exposure Volume (events/case)** | `2.65` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_0011013__noise0.4.png)


```text
->( 't10', X( tau, 't11' ), +( 't06', X( tau, 't05' ), X( tau, 't04' ) ), X( 't15', ->( X( tau, 't16' ), 't20', +( *( 't17', tau ), X( tau, 't24' ), ->( 't21', X( tau, 't23' ) ) ), X( tau, 't22' ), *( X( 't34', ->( X( tau, ->( X( 't27', 't26' ), X( tau, 't28' ) ) ), X( 't42', 't39' ) ) ), tau ), X( 't71', ->( X( tau, 't43' ), X( tau, 't44' ), +( X( tau, *( 't40', tau ) ), ->( 't36', 't46', X( tau, 't47' ), X( tau, 't37' ) ) ), X( 't69', 't70', +( ->( 't56', 't62' ), X( tau, ->( 't48', 't68' ) ) ) ), 't65' ) ), 't55' ) ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_0011013__noise0.4.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST]` | `t10` | Exact Token Match | $\ge$ 1000 | **1000** | ✅ **VERIFIED** |
| `[ST]` | `t11` | Exact Token Match | $\ge$ 271 | **271** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `t06` | Exact Token Match | $\ge$ 485 | **485** | ✅ **VERIFIED** |
| `[ST (in PAR_2)]` | `t05` | Exact Token Match | $\ge$ 390 | **390** | ✅ **VERIFIED** |
| `[ST (in PAR_2)]` | `t04` | Exact Token Match | $\ge$ 224 | **224** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_1]` | Exact Token Match | $\ge$ 485 | **756** | ✅ **VERIFIED** |
| `[ST]` | `t15` | Exact Token Match | $\ge$ 494 | **502** | ✅ **VERIFIED** |
| `[ST]` | `t16` | Exact Token Match | $\ge$ 135 | **135** | ✅ **VERIFIED** |
| `[ST]` | `t20` | Exact Token Match | $\ge$ 379 | **379** | ✅ **VERIFIED** |
| `[ST (in LOOP_4)]` | `t17` | Exact Token Match | $\ge$ 621 | **621** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t17⟩` | Exact Token Match | $\ge$ 391 | **621** | ✅ **VERIFIED** |
| `[AS (in PAR_3)]` | `[nested LOOP_4]` | Exact Token Match | $\ge$ 1 | **621** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t24` | Exact Token Match | $\ge$ 242 | **242** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t21` | Exact Token Match | $\ge$ 506 | **515** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t23` | Exact Token Match | $\ge$ 242 | **242** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t21, τ⟩` | Exact Token Match | $\ge$ 264 | **515** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t21, t23⟩` | Exact Token Match | $\ge$ 242 | **242** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_3]` | Exact Token Match | $\ge$ 506 | **515** | ✅ **VERIFIED** |
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
| `[ST]` | `t71` | Exact Token Match | $\ge$ 116 | **118** | ✅ **VERIFIED** |
| `[ST]` | `t43` | Exact Token Match | $\ge$ 141 | **141** | ✅ **VERIFIED** |
| `[ST]` | `t44` | Exact Token Match | $\ge$ 141 | **141** | ✅ **VERIFIED** |
| `[ST (in LOOP_8)]` | `t40` | Exact Token Match | $\ge$ 199 | **199** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨t40⟩` | Exact Token Match | $\ge$ 199 | **199** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `t36` | Exact Token Match | $\ge$ 390 | **397** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `t46` | Exact Token Match | $\ge$ 390 | **397** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `t47` | Exact Token Match | $\ge$ 138 | **138** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `t37` | Exact Token Match | $\ge$ 74 | **74** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨t47, τ⟩` | Exact Token Match | $\ge$ 64 | **138** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨t47, t37⟩` | Exact Token Match | $\ge$ 74 | **74** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨t46, t47, τ⟩` | Exact Token Match | $\ge$ 64 | **138** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨t46, t47, t37⟩` | Exact Token Match | $\ge$ 74 | **74** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨t46, τ⟩` | Exact Token Match | $\ge$ 252 | **397** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨t46, t47⟩` | Exact Token Match | $\ge$ 138 | **138** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨t36, t46, t47, τ⟩` | Exact Token Match | $\ge$ 64 | **138** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨t36, t46, t47, t37⟩` | Exact Token Match | $\ge$ 74 | **74** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨t36, t46, τ⟩` | Exact Token Match | $\ge$ 252 | **397** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨t36, t46, t47⟩` | Exact Token Match | $\ge$ 138 | **138** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨t36, t46⟩` | Exact Token Match | $\ge$ 390 | **397** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_7]` | Exact Token Match | $\ge$ 390 | **397** | ✅ **VERIFIED** |
| `[ST]` | `t69` | Exact Token Match | $\ge$ 117 | **119** | ✅ **VERIFIED** |
| `[ST]` | `t70` | Exact Token Match | $\ge$ 137 | **140** | ✅ **VERIFIED** |
| `[ST (in PAR_9)]` | `t56` | Exact Token Match | $\ge$ 136 | **138** | ✅ **VERIFIED** |
| `[ST (in PAR_9)]` | `t62` | Exact Token Match | $\ge$ 136 | **138** | ✅ **VERIFIED** |
| `[ST (in PAR_9)]` | `⟨t56, t62⟩` | Exact Token Match | $\ge$ 136 | **138** | ✅ **VERIFIED** |
| `[ST (in PAR_9)]` | `t48` | Exact Token Match | $\ge$ 63 | **63** | ✅ **VERIFIED** |
| `[ST (in PAR_9)]` | `t68` | Exact Token Match | $\ge$ 63 | **63** | ✅ **VERIFIED** |
| `[ST (in PAR_9)]` | `⟨t48, t68⟩` | Exact Token Match | $\ge$ 63 | **63** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_9]` | Exact Token Match | $\ge$ 136 | **138** | ✅ **VERIFIED** |
| `[ST]` | `t65` | Exact Token Match | $\ge$ 390 | **397** | ✅ **VERIFIED** |
| `[ST]` | `⟨t70, t65⟩` | Exact Token Match | $\ge$ 137 | **139** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_9], t65⟩` | Exact Token Match | $\ge$ 136 | **137** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_7], t70, t65⟩` | Exact Token Match | $\ge$ 137 | **138** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_7], t70⟩` | Exact Token Match | $\ge$ 137 | **139** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_7]⟩` | Exact Token Match | $\ge$ 249 | **397** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, τ, [nested PAR_7]⟩` | Exact Token Match | $\ge$ 108 | **397** | ✅ **VERIFIED** |
| `[ST]` | `t55` | Exact Token Match | $\ge$ 506 | **515** | ✅ **VERIFIED** |
| `[ST]` | `⟨t70, t65, t55⟩` | Exact Token Match | $\ge$ 137 | **137** | ✅ **VERIFIED** |
| `[ST]` | `⟨t65, t55⟩` | Exact Token Match | $\ge$ 390 | **392** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_3], τ⟩` | Exact Token Match | $\ge$ 233 | **515** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, [nested PAR_3], τ⟩` | Exact Token Match | $\ge$ 106 | **373** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, [nested PAR_3], t22⟩` | Exact Token Match | $\ge$ 146 | **193** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_3]⟩` | Exact Token Match | $\ge$ 127 | **515** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t20, [nested PAR_3], t22⟩` | Exact Token Match | $\ge$ 11 | **193** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t20, [nested PAR_3]⟩` | Exact Token Match | $\ge$ 244 | **373** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t20⟩` | Exact Token Match | $\ge$ 244 | **379** | ✅ **VERIFIED** |
| `[ST]` | `⟨t16, t20, [nested PAR_3]⟩` | Exact Token Match | $\ge$ 8 | **132** | ✅ **VERIFIED** |
| `[ST]` | `⟨t16, t20⟩` | Exact Token Match | $\ge$ 8 | **135** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t15⟩` | Exact Token Match | $\ge$ 9 | **502** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 214 | **756** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ, [nested PAR_1]⟩` | Exact Token Match | $\ge$ 214 | **720** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ, τ⟩` | Exact Token Match | $\ge$ 244 | **1000** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 729 | **1000** | ✅ **VERIFIED** |
| `[AS (in PAR_1)]` | `[nested PAR_2]` | Exact Token Match | $\ge$ 390 | **119** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_3)]` | `[nested PAR_5]` | Exact Token Match | $\ge$ 506 | **242** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t69, t65⟩` | Exact Token Match | $\ge$ 117 | **116** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_7], t69, t65⟩` | Exact Token Match | $\ge$ 117 | **113** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_7], [nested PAR_9], t65⟩` | Exact Token Match | $\ge$ 136 | **83** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_7], t69⟩` | Exact Token Match | $\ge$ 117 | **116** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_7], [nested PAR_9]⟩` | Exact Token Match | $\ge$ 136 | **83** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t44, [nested PAR_7]⟩` | Exact Token Match | $\ge$ 141 | **139** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t71, t55⟩` | Exact Token Match | $\ge$ 116 | **114** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_7], t69, t65, t55⟩` | Exact Token Match | $\ge$ 117 | **112** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_7], t70, t65, t55⟩` | Exact Token Match | $\ge$ 137 | **136** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_7], [nested PAR_9], t65, t55⟩` | Exact Token Match | $\ge$ 136 | **82** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t69, t65, t55⟩` | Exact Token Match | $\ge$ 117 | **115** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_9], t65, t55⟩` | Exact Token Match | $\ge$ 136 | **135** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_3], t22⟩` | Exact Token Match | $\ge$ 273 | **266** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t20, [nested PAR_3]⟩` | Exact Token Match | $\ge$ 379 | **373** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t10, t11⟩` | Exact Token Match | $\ge$ 271 | **269** | ⚠️ **DISCREPANCY** |

## Audit Summary
- **Perfect Pattern Verifications:** 82
- **Frequency Discrepancies:** 17
- **Ghost Patterns (Fatal):** 0
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 27.35%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 17.44%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 55.20%
- **Total Forced Volume (incl. unresolved AS, % of N):** 0.00%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 0.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 96.70%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 99.89%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 99.95%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 40.37%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 82.65%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 100.00%
- **Max Fractional Exposure (Worst-Case Normalized):** 0.60% (expected length: 1014.43 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 59.72% (expected length: 10.17 events)
- **Mean Absolute Exposure Volume:** 2.65 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested PAR_2]`
- **Internal Structure:** `{[τ │ t05], [τ │ t04]}`
- **Block Frequency:** 390



![nested PAR_2 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.4_nested_PAR_2.png)

### `[nested PAR_1]`
- **Internal Structure:** `{t06, [{[τ │ t05], [τ │ t04]} │ τ]}`
- **Block Frequency:** 485



![nested PAR_1 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.4_nested_PAR_1.png)

### `[nested LOOP_4]`
- **Internal Structure:** `(t17 ∗ τ)`
- **Block Frequency:** 506

- **Max Loop Iterations:** `115`
- **Max Sub-Sequence Length:** `231` steps (if one case consumes all iterations)

![nested LOOP_4 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.4_nested_LOOP_4.png)

### `[nested PAR_5]`
- **Internal Structure:** `{[τ │ t24], ⟨t21, [τ │ t23]⟩}`
- **Block Frequency:** 506



![nested PAR_5 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.4_nested_PAR_5.png)

### `[nested PAR_3]`
- **Internal Structure:** `{(t17 ∗ τ), [τ │ t24], ⟨t21, [τ │ t23]⟩}`
- **Block Frequency:** 506



![nested PAR_3 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.4_nested_PAR_3.png)

### `[nested LOOP_6]`
- **Internal Structure:** `([t34 │ ⟨[τ │ ⟨[t27 │ t26], [τ │ t28]⟩], [t42 │ t39]⟩] ∗ τ)`
- **Block Frequency:** 506

- **Max Loop Iterations:** `661`
- **Max Sub-Sequence Length:** `1323` steps (if one case consumes all iterations)

![nested LOOP_6 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.4_nested_LOOP_6.png)

### `[nested LOOP_8]`
- **Internal Structure:** `(t40 ∗ τ)`
- **Block Frequency:** 199

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_8 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.4_nested_LOOP_8.png)

### `[nested PAR_7]`
- **Internal Structure:** `{[τ │ (t40 ∗ τ)], ⟨t36, t46, [⟨[τ │ t47], [τ │ t37]⟩ │ τ]⟩}`
- **Block Frequency:** 390



![nested PAR_7 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.4_nested_PAR_7.png)

### `[nested PAR_9]`
- **Internal Structure:** `{⟨t56, t62⟩, [τ │ ⟨t48, t68⟩]}`
- **Block Frequency:** 136



![nested PAR_9 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.4_nested_PAR_9.png)
