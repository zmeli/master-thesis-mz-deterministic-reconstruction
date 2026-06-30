# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_0011013.xes` |
| **Noise Threshold** | `0.0` |
| **Fitness** | `0.9925388945622851` |
| **Precision** | `0.15670356008731756` |
| **Total Cases in Log** | `1000` |
| **Unique Activities** | `35` |
| **XOR Operators** | `50` |
| **LOOP Operators** | `4` |
| **SEQ Operators** | `14` |
| **PAR Operators** | `9` |
| **Binarization Additions** | `12` |
| **Tau Operators Added** | `51` |
| **Total Found Patterns** | `117` |
| **Verified Patterns** | `62` |
| **Discrepancy Patterns** | `10` |
| **Ghost Patterns** | `2` |
| **Nested LOOPs** | `4` |
| **Nested PARs** | `9` |
| **Tree Exposure (Strict, End-to-End % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `0.00%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `11.55%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `100.00%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `100.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `88.69%` |
| **Data Exposure, ST-only (% confirmed)** | `0.00%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `97.26%` |
| **Data Coverage, ST-only (% of real log)** | `0.00%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `58.25%` |
| **Data Coverage, Total (% of real log)** | `100.00%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `100.00%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `100.00%` |
| **Mean Absolute Exposure Volume (events/case)** | `35.80` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_0011013__noise0.0.png)


```text
+( 't10', *( X( 't06', 't04', ->( *( ->( X( tau, 't28', 't15' ), X( tau, +( X( tau, 't27' ), ->( *( ->( X( tau, +( X( tau, 't20' ), X( tau, ->( X( tau, *( X( 't69', 't70', ->( X( 't42', 't39' ), X( tau, 't43' ) ), ->( X( tau, 't22', 't47' ), X( tau, +( X( tau, 't44' ), X( tau, ->( X( tau, 't46' ), X( tau, +( X( tau, 't37' ), X( tau, ->( X( tau, 't48' ), X( tau, 't68' ) ) ), X( tau, +( X( tau, ->( X( tau, 't56' ), X( tau, 't62' ) ) ), X( tau, 't40' ) ) ) ) ) ) ) ) ), X( tau, 't36', 't11' ) ) ), tau ) ), X( tau, +( X( tau, 't16' ), X( tau, ->( X( tau, 't05' ), X( tau, 't17' ) ) ) ) ) ) ) ) ), X( tau, 't55', 't24', 't21' ), X( tau, 't23' ), X( tau, +( X( tau, 't65' ), X( tau, 't34' ) ) ) ), tau ), X( tau, 't26' ) ) ) ) ), tau ), X( tau, 't71' ) ) ), tau ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_0011013__noise0.0.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST (in PAR_1)]` | `t10` | Exact Token Match | $\ge$ 1000 | **1000** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `t06` | Exact Token Match | $\ge$ 485 | **485** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `t04` | Exact Token Match | $\ge$ 224 | **224** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t28` | Exact Token Match | $\ge$ 124 | **124** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t15` | Exact Token Match | $\ge$ 502 | **502** | ✅ **VERIFIED** |
| `[ST (in PAR_4)]` | `t27` | Exact Token Match | $\ge$ 242 | **242** | ✅ **VERIFIED** |
| `[ST (in PAR_6)]` | `t20` | Exact Token Match | $\ge$ 379 | **379** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `t69` | Exact Token Match | $\ge$ 119 | **119** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `t70` | Exact Token Match | $\ge$ 140 | **140** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `t42` | Exact Token Match | $\ge$ 397 | **397** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `t39` | Exact Token Match | $\ge$ 397 | **397** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `t43` | Exact Token Match | $\ge$ 141 | **141** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨t42, τ⟩` | Exact Token Match | $\ge$ 256 | **397** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨t39, τ⟩` | Exact Token Match | $\ge$ 256 | **397** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `t22` | Exact Token Match | $\ge$ 273 | **273** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `t47` | Exact Token Match | $\ge$ 138 | **138** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `t44` | Exact Token Match | $\ge$ 141 | **141** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `t46` | Exact Token Match | $\ge$ 397 | **397** | ✅ **VERIFIED** |
| `[ST (in PAR_9)]` | `t37` | Exact Token Match | $\ge$ 74 | **74** | ✅ **VERIFIED** |
| `[ST (in PAR_10)]` | `t48` | Exact Token Match | $\ge$ 63 | **63** | ✅ **VERIFIED** |
| `[ST (in PAR_10)]` | `t68` | Exact Token Match | $\ge$ 63 | **63** | ✅ **VERIFIED** |
| `[ST (in PAR_10)]` | `⟨t48, t68⟩` | Exact Token Match | $\ge$ 63 | **63** | ✅ **VERIFIED** |
| `[ST (in PAR_11)]` | `t56` | Exact Token Match | $\ge$ 138 | **138** | ✅ **VERIFIED** |
| `[ST (in PAR_11)]` | `t62` | Exact Token Match | $\ge$ 138 | **138** | ✅ **VERIFIED** |
| `[ST (in PAR_11)]` | `⟨t56, t62⟩` | Exact Token Match | $\ge$ 138 | **138** | ✅ **VERIFIED** |
| `[ST (in PAR_11)]` | `t40` | Exact Token Match | $\ge$ 199 | **199** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨t46, τ⟩` | Exact Token Match | $\ge$ 198 | **397** | ✅ **VERIFIED** |
| `[AS (in LOOP_7)]` | `[nested PAR_8]` | Exact Token Match | $\ge$ 397 | **397** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `t36` | Exact Token Match | $\ge$ 397 | **397** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `t11` | Exact Token Match | $\ge$ 271 | **271** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨[nested PAR_8], t36⟩` | Exact Token Match | $\ge$ 126 | **265** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `⟨t22, [nested PAR_8]⟩` | Exact Token Match | $\ge$ 2 | **272** | ✅ **VERIFIED** |
| `[ST (in PAR_6)]` | `⟨t69⟩` | Exact Token Match | $\ge$ 119 | **119** | ✅ **VERIFIED** |
| `[ST (in PAR_6)]` | `⟨t70⟩` | Exact Token Match | $\ge$ 140 | **140** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `t16` | Exact Token Match | $\ge$ 135 | **135** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `t05` | Exact Token Match | $\ge$ 390 | **390** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `t17` | Exact Token Match | $\ge$ 621 | **621** | ✅ **VERIFIED** |
| `[ST (in PAR_12)]` | `⟨τ, t17⟩` | Exact Token Match | $\ge$ 231 | **621** | ✅ **VERIFIED** |
| `[ST (in LOOP_5)]` | `t55` | Exact Token Match | $\ge$ 515 | **515** | ✅ **VERIFIED** |
| `[ST (in LOOP_5)]` | `t24` | Exact Token Match | $\ge$ 242 | **242** | ✅ **VERIFIED** |
| `[ST (in LOOP_5)]` | `t21` | Exact Token Match | $\ge$ 515 | **515** | ✅ **VERIFIED** |
| `[ST (in LOOP_5)]` | `t23` | Exact Token Match | $\ge$ 242 | **242** | ✅ **VERIFIED** |
| `[ST (in PAR_13)]` | `t65` | Exact Token Match | $\ge$ 397 | **397** | ✅ **VERIFIED** |
| `[ST (in PAR_13)]` | `t34` | Exact Token Match | $\ge$ 373 | **373** | ✅ **VERIFIED** |
| `[AS (in LOOP_5)]` | `[nested PAR_13]` | Exact Token Match | $\ge$ 397 | **557** | ✅ **VERIFIED** |
| `[ST (in LOOP_5)]` | `⟨τ, [nested PAR_13]⟩` | Exact Token Match | $\ge$ 155 | **557** | ✅ **VERIFIED** |
| `[ST (in LOOP_5)]` | `⟨t23, [nested PAR_13]⟩` | Exact Token Match | $\ge$ 242 | **242** | ✅ **VERIFIED** |
| `[ST (in LOOP_5)]` | `⟨t55, τ⟩` | Exact Token Match | $\ge$ 118 | **515** | ✅ **VERIFIED** |
| `[ST (in LOOP_5)]` | `⟨t21, τ⟩` | Exact Token Match | $\ge$ 118 | **515** | ✅ **VERIFIED** |
| `[ST (in LOOP_5)]` | `⟨[nested PAR_6], t55, τ⟩` | Exact Token Match | $\ge$ 118 | **513** | ✅ **VERIFIED** |
| `[ST (in LOOP_5)]` | `⟨[nested PAR_6], t21, τ⟩` | Exact Token Match | $\ge$ 118 | **514** | ✅ **VERIFIED** |
| `[ST (in LOOP_5)]` | `⟨[nested PAR_6], τ⟩` | Exact Token Match | $\ge$ 449 | **634** | ✅ **VERIFIED** |
| `[ST (in PAR_4)]` | `t26` | Exact Token Match | $\ge$ 242 | **242** | ✅ **VERIFIED** |
| `[AS (in LOOP_3)]` | `[nested PAR_4]` | Exact Token Match | $\ge$ 242 | **634** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨t15, τ⟩` | Exact Token Match | $\ge$ 260 | **502** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨t15, [nested PAR_4]⟩` | Exact Token Match | $\ge$ 118 | **136** | ✅ **VERIFIED** |
| `[AS (in LOOP_2)]` | `[nested LOOP_3]` | Exact Token Match | $\ge$ 1 | **1000** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `t71` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `⟨[nested LOOP_3], t71⟩` | Exact Token Match | $\ge$ 1 | **118** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t06⟩` | Exact Token Match | $\ge$ 485 | **485** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t04⟩` | Exact Token Match | $\ge$ 224 | **224** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_1]` | Exact Token Match | $\ge$ 1000 | **1000** | ✅ **VERIFIED** |
| `[AS (in PAR_10)]` | `[nested PAR_11]` | Exact Token Match | $\ge$ 199 | **93** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_9)]` | `[nested PAR_10]` | Exact Token Match | $\ge$ 199 | **36** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_8)]` | `[nested PAR_9]` | Exact Token Match | $\ge$ 199 | **31** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_8)]` | `⟨t46, [nested PAR_9]⟩` | Exact Token Match | $\ge$ 199 | **31** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_12)]` | `⟨t05, t17⟩` | Exact Token Match | $\ge$ 390 | **199** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_6)]` | `[nested PAR_12]` | Exact Token Match | $\ge$ 621 | **135** | ⚠️ **DISCREPANCY** |
| `[AS (in LOOP_5)]` | `[nested PAR_6]` | Exact Token Match | $\ge$ 1721 | **634** | ⚠️ **DISCREPANCY** |
| `[ST (in LOOP_5)]` | `⟨[nested PAR_6], t55⟩` | Exact Token Match | $\ge$ 515 | **513** | ⚠️ **DISCREPANCY** |
| `[ST (in LOOP_5)]` | `⟨[nested PAR_6], t24⟩` | Exact Token Match | $\ge$ 242 | **241** | ⚠️ **DISCREPANCY** |
| `[ST (in LOOP_5)]` | `⟨[nested PAR_6], t21⟩` | Exact Token Match | $\ge$ 515 | **514** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_4)]` | `[nested LOOP_5]` | Exact Token Match | $\ge$ 1 | **0** | ❌ **GHOST PATTERN** |
| `[ST (in PAR_4)]` | `⟨[nested LOOP_5], t26⟩` | Exact Token Match | $\ge$ 1 | **0** | ❌ **GHOST PATTERN** |

## Audit Summary
- **Perfect Pattern Verifications:** 62
- **Frequency Discrepancies:** 10
- **Ghost Patterns (Fatal):** 2
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 0.00%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 11.55%
- **Total Forced Volume (incl. unresolved AS, % of N):** 100.00%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 100.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 88.69%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 0.00%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 97.26%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 0.00%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 58.25%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 100.00%
- **Max Fractional Exposure (Worst-Case Normalized):** 100.00% (expected length: 6271.44 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 100.00% (expected length: 10.23 events)
- **Mean Absolute Exposure Volume:** 35.80 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested PAR_11]`
- **Internal Structure:** `{[τ │ ⟨[τ │ t56], [τ │ t62]⟩], [τ │ t40]}`
- **Block Frequency:** 199



![nested PAR_11 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.0_nested_PAR_11.png)

### `[nested PAR_10]`
- **Internal Structure:** `{[τ │ ⟨[τ │ t48], [τ │ t68]⟩], [τ │ {[τ │ ⟨[τ │ t56], [τ │ t62]⟩], [τ │ t40]}]}`
- **Block Frequency:** 199



![nested PAR_10 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.0_nested_PAR_10.png)

### `[nested PAR_9]`
- **Internal Structure:** `{[τ │ t37], [τ │ ⟨[τ │ t48], [τ │ t68]⟩], [τ │ {[τ │ ⟨[τ │ t56], [τ │ t62]⟩], [τ │ t40]}]}`
- **Block Frequency:** 199



![nested PAR_9 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.0_nested_PAR_9.png)

### `[nested PAR_8]`
- **Internal Structure:** `{[τ │ t44], [τ │ ⟨[τ │ t46], [τ │ {[τ │ t37], [τ │ ⟨[τ │ t48], [τ │ t68]⟩], [τ │ {[τ │ ⟨[τ │ t56], [τ │ t62]⟩], [τ │ t40]}]}]⟩]}`
- **Block Frequency:** 397



![nested PAR_8 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.0_nested_PAR_8.png)

### `[nested LOOP_7]`
- **Internal Structure:** `([t69 │ t70 │ ⟨[t42 │ t39], [τ │ t43]⟩ │ ⟨[τ │ t22 │ t47], [τ │ {[τ │ t44], [τ │ ⟨[τ │ t46], [τ │ {[τ │ t37], [τ │ ⟨[τ │ t48], [τ │ t68]⟩], [τ │ {[τ │ ⟨[τ │ t56], [τ │ t62]⟩], [τ │ t40]}]}]⟩]}], [τ │ t36 │ t11]⟩] ∗ τ)`
- **Block Frequency:** 1721

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_7 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.0_nested_LOOP_7.png)

### `[nested PAR_12]`
- **Internal Structure:** `{[τ │ t16], [τ │ ⟨[τ │ t05], [τ │ t17]⟩]}`
- **Block Frequency:** 621



![nested PAR_12 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.0_nested_PAR_12.png)

### `[nested PAR_6]`
- **Internal Structure:** `{[τ │ t20], [τ │ ⟨[τ │ ([t69 │ t70 │ ⟨[t42 │ t39], [τ │ t43]⟩ │ ⟨[τ │ t22 │ t47], [τ │ {[τ │ t44], [τ │ ⟨[τ │ t46], [τ │ {[τ │ t37], [τ │ ⟨[τ │ t48], [τ │ t68]⟩], [τ │ {[τ │ ⟨[τ │ t56], [τ │ t62]⟩], [τ │ t40]}]}]⟩]}], [τ │ t36 │ t11]⟩] ∗ τ)], [τ │ {[τ │ t16], [τ │ ⟨[τ │ t05], [τ │ t17]⟩]}]⟩]}`
- **Block Frequency:** 1721



![nested PAR_6 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.0_nested_PAR_6.png)

### `[nested PAR_13]`
- **Internal Structure:** `{[τ │ t65], [τ │ t34]}`
- **Block Frequency:** 397



![nested PAR_13 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.0_nested_PAR_13.png)

### `[nested LOOP_5]`
- **Internal Structure:** `(⟨[τ │ {[τ │ t20], [τ │ ⟨[τ │ ([t69 │ t70 │ ⟨[t42 │ t39], [τ │ t43]⟩ │ ⟨[τ │ t22 │ t47], [τ │ {[τ │ t44], [τ │ ⟨[τ │ t46], [τ │ {[τ │ t37], [τ │ ⟨[τ │ t48], [τ │ t68]⟩], [τ │ {[τ │ ⟨[τ │ t56], [τ │ t62]⟩], [τ │ t40]}]}]⟩]}], [τ │ t36 │ t11]⟩] ∗ τ)], [τ │ {[τ │ t16], [τ │ ⟨[τ │ t05], [τ │ t17]⟩]}]⟩]}], [⟨[τ │ t55 │ t24 │ t21], [⟨[τ │ t23], [τ │ {[τ │ t65], [τ │ t34]}]⟩ │ τ]⟩ │ τ]⟩ ∗ τ)`
- **Block Frequency:** 242

- **Max Loop Iterations:** `1479`
- **Max Sub-Sequence Length:** `2959` steps (if one case consumes all iterations)

![nested LOOP_5 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.0_nested_LOOP_5.png)

### `[nested PAR_4]`
- **Internal Structure:** `{[τ │ t27], ⟨(⟨[τ │ {[τ │ t20], [τ │ ⟨[τ │ ([t69 │ t70 │ ⟨[t42 │ t39], [τ │ t43]⟩ │ ⟨[τ │ t22 │ t47], [τ │ {[τ │ t44], [τ │ ⟨[τ │ t46], [τ │ {[τ │ t37], [τ │ ⟨[τ │ t48], [τ │ t68]⟩], [τ │ {[τ │ ⟨[τ │ t56], [τ │ t62]⟩], [τ │ t40]}]}]⟩]}], [τ │ t36 │ t11]⟩] ∗ τ)], [τ │ {[τ │ t16], [τ │ ⟨[τ │ t05], [τ │ t17]⟩]}]⟩]}], [⟨[τ │ t55 │ t24 │ t21], [⟨[τ │ t23], [τ │ {[τ │ t65], [τ │ t34]}]⟩ │ τ]⟩ │ τ]⟩ ∗ τ), [τ │ t26]⟩}`
- **Block Frequency:** 242



![nested PAR_4 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.0_nested_PAR_4.png)

### `[nested LOOP_3]`
- **Internal Structure:** `(⟨[τ │ t28 │ t15], [τ │ {[τ │ t27], ⟨(⟨[τ │ {[τ │ t20], [τ │ ⟨[τ │ ([t69 │ t70 │ ⟨[t42 │ t39], [τ │ t43]⟩ │ ⟨[τ │ t22 │ t47], [τ │ {[τ │ t44], [τ │ ⟨[τ │ t46], [τ │ {[τ │ t37], [τ │ ⟨[τ │ t48], [τ │ t68]⟩], [τ │ {[τ │ ⟨[τ │ t56], [τ │ t62]⟩], [τ │ t40]}]}]⟩]}], [τ │ t36 │ t11]⟩] ∗ τ)], [τ │ {[τ │ t16], [τ │ ⟨[τ │ t05], [τ │ t17]⟩]}]⟩]}], [⟨[τ │ t55 │ t24 │ t21], [⟨[τ │ t23], [τ │ {[τ │ t65], [τ │ t34]}]⟩ │ τ]⟩ │ τ]⟩ ∗ τ), [τ │ t26]⟩}]⟩ ∗ τ)`
- **Block Frequency:** 118

- **Max Loop Iterations:** `508`
- **Max Sub-Sequence Length:** `1017` steps (if one case consumes all iterations)

![nested LOOP_3 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.0_nested_LOOP_3.png)

### `[nested LOOP_2]`
- **Internal Structure:** `([t06 │ t04 │ ⟨(⟨[τ │ t28 │ t15], [τ │ {[τ │ t27], ⟨(⟨[τ │ {[τ │ t20], [τ │ ⟨[τ │ ([t69 │ t70 │ ⟨[t42 │ t39], [τ │ t43]⟩ │ ⟨[τ │ t22 │ t47], [τ │ {[τ │ t44], [τ │ ⟨[τ │ t46], [τ │ {[τ │ t37], [τ │ ⟨[τ │ t48], [τ │ t68]⟩], [τ │ {[τ │ ⟨[τ │ t56], [τ │ t62]⟩], [τ │ t40]}]}]⟩]}], [τ │ t36 │ t11]⟩] ∗ τ)], [τ │ {[τ │ t16], [τ │ ⟨[τ │ t05], [τ │ t17]⟩]}]⟩]}], [⟨[τ │ t55 │ t24 │ t21], [⟨[τ │ t23], [τ │ {[τ │ t65], [τ │ t34]}]⟩ │ τ]⟩ │ τ]⟩ ∗ τ), [τ │ t26]⟩}]⟩ ∗ τ), [τ │ t71]⟩] ∗ τ)`
- **Block Frequency:** 827

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_2 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.0_nested_LOOP_2.png)

### `[nested PAR_1]`
- **Internal Structure:** `{t10, [([t06 │ t04 │ ⟨(⟨[τ │ t28 │ t15], [τ │ {[τ │ t27], ⟨(⟨[τ │ {[τ │ t20], [τ │ ⟨[τ │ ([t69 │ t70 │ ⟨[t42 │ t39], [τ │ t43]⟩ │ ⟨[τ │ t22 │ t47], [τ │ {[τ │ t44], [τ │ ⟨[τ │ t46], [τ │ {[τ │ t37], [τ │ ⟨[τ │ t48], [τ │ t68]⟩], [τ │ {[τ │ ⟨[τ │ t56], [τ │ t62]⟩], [τ │ t40]}]}]⟩]}], [τ │ t36 │ t11]⟩] ∗ τ)], [τ │ {[τ │ t16], [τ │ ⟨[τ │ t05], [τ │ t17]⟩]}]⟩]}], [⟨[τ │ t55 │ t24 │ t21], [⟨[τ │ t23], [τ │ {[τ │ t65], [τ │ t34]}]⟩ │ τ]⟩ │ τ]⟩ ∗ τ), [τ │ t26]⟩}]⟩ ∗ τ), [τ │ t71]⟩] ∗ τ) │ τ]}`
- **Block Frequency:** 1000



![nested PAR_1 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.0_nested_PAR_1.png)
