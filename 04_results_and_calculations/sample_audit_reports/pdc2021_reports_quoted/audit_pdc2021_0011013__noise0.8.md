# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_0011013.xes` |
| **Noise Threshold** | `0.8` |
| **Fitness** | `0.8995972533101332` |
| **Precision** | `0.38499095446718545` |
| **Total Cases in Log** | `1000` |
| **Unique Activities** | `35` |
| **XOR Operators** | `27` |
| **LOOP Operators** | `2` |
| **SEQ Operators** | `13` |
| **PAR Operators** | `7` |
| **Binarization Additions** | `10` |
| **Tau Operators Added** | `24` |
| **Total Found Patterns** | `127` |
| **Verified Patterns** | `78` |
| **Discrepancy Patterns** | `4` |
| **Ghost Patterns** | `1` |
| **Nested LOOPs** | `2` |
| **Nested PARs** | `7` |
| **Tree Exposure (Strict, End-to-End % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `0.00%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `13.72%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `100.00%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `100.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `99.82%` |
| **Data Exposure, ST-only (% confirmed)** | `0.00%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `100.00%` |
| **Data Coverage, ST-only (% of real log)** | `0.00%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `42.13%` |
| **Data Coverage, Total (% of real log)** | `100.00%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `100.00%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `100.00%` |
| **Mean Absolute Exposure Volume (events/case)** | `10.23` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_0011013__noise0.8.png)


```text
+( 't10', *( X( 't06', 't04', ->( X( 't15', 't55', ->( 't11', 't05' ), *( ->( X( tau, 't28' ), X( 't21', 't46', ->( 't48', 't68' ), ->( 't47', +( 't62', 't56' ) ), ->( 't16', +( 't20', 't24' ), +( 't17', 't23' ) ), ->( +( 't22', 't42', 't39' ), X( ->( 't43', 't44' ), ->( X( tau, 't37' ), 't40' ) ) ) ), X( 't36', ->( X( 't69', 't70' ), X( 't65', ->( 't34', +( 't27', 't26' ) ) ) ) ) ), tau ) ), X( tau, 't71' ) ) ), tau ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_0011013__noise0.8.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST (in PAR_1)]` | `t10` | Exact Token Match | $\ge$ 1000 | **1000** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `t06` | Exact Token Match | $\ge$ 485 | **485** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `t04` | Exact Token Match | $\ge$ 224 | **224** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `t15` | Exact Token Match | $\ge$ 502 | **502** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `t55` | Exact Token Match | $\ge$ 515 | **515** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `t11` | Exact Token Match | $\ge$ 271 | **271** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `t05` | Exact Token Match | $\ge$ 390 | **390** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `⟨t11, t05⟩` | Exact Token Match | $\ge$ 271 | **271** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `⟨τ, t05⟩` | Exact Token Match | $\ge$ 119 | **390** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t28` | Exact Token Match | $\ge$ 124 | **124** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t21` | Exact Token Match | $\ge$ 515 | **515** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t46` | Exact Token Match | $\ge$ 397 | **397** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t48` | Exact Token Match | $\ge$ 63 | **63** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t68` | Exact Token Match | $\ge$ 63 | **63** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨t48, t68⟩` | Exact Token Match | $\ge$ 63 | **63** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t47` | Exact Token Match | $\ge$ 138 | **138** | ✅ **VERIFIED** |
| `[ST (in PAR_4)]` | `t62` | Exact Token Match | $\ge$ 138 | **138** | ✅ **VERIFIED** |
| `[ST (in PAR_4)]` | `t56` | Exact Token Match | $\ge$ 138 | **138** | ✅ **VERIFIED** |
| `[AS (in LOOP_3)]` | `[nested PAR_4]` | Exact Token Match | $\ge$ 138 | **138** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨t47, [nested PAR_4]⟩` | Exact Token Match | $\ge$ 138 | **138** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t16` | Exact Token Match | $\ge$ 135 | **135** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t20` | Exact Token Match | $\ge$ 379 | **379** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t24` | Exact Token Match | $\ge$ 242 | **242** | ✅ **VERIFIED** |
| `[AS (in LOOP_3)]` | `[nested PAR_5]` | Exact Token Match | $\ge$ 379 | **443** | ✅ **VERIFIED** |
| `[ST (in PAR_6)]` | `t17` | Exact Token Match | $\ge$ 621 | **621** | ✅ **VERIFIED** |
| `[ST (in PAR_6)]` | `t23` | Exact Token Match | $\ge$ 242 | **242** | ✅ **VERIFIED** |
| `[AS (in LOOP_3)]` | `[nested PAR_6]` | Exact Token Match | $\ge$ 621 | **621** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨[nested PAR_5], [nested PAR_6]⟩` | Exact Token Match | $\ge$ 379 | **612** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨τ, [nested PAR_6]⟩` | Exact Token Match | $\ge$ 242 | **621** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨τ, [nested PAR_5], [nested PAR_6]⟩` | Exact Token Match | $\ge$ 244 | **612** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨τ, τ, [nested PAR_6]⟩` | Exact Token Match | $\ge$ 107 | **621** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨τ, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 244 | **443** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `t22` | Exact Token Match | $\ge$ 273 | **273** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `t42` | Exact Token Match | $\ge$ 397 | **397** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `t39` | Exact Token Match | $\ge$ 397 | **397** | ✅ **VERIFIED** |
| `[AS (in PAR_7)]` | `[nested PAR_8]` | Exact Token Match | $\ge$ 397 | **397** | ✅ **VERIFIED** |
| `[AS (in LOOP_3)]` | `[nested PAR_7]` | Exact Token Match | $\ge$ 397 | **397** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t43` | Exact Token Match | $\ge$ 141 | **141** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t44` | Exact Token Match | $\ge$ 141 | **141** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t37` | Exact Token Match | $\ge$ 74 | **74** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t40` | Exact Token Match | $\ge$ 199 | **199** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨τ, t40⟩` | Exact Token Match | $\ge$ 125 | **199** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨t37, t40⟩` | Exact Token Match | $\ge$ 74 | **74** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨[nested PAR_7], τ, t40⟩` | Exact Token Match | $\ge$ 125 | **167** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨[nested PAR_7], τ⟩` | Exact Token Match | $\ge$ 57 | **397** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨[nested PAR_7], t43⟩` | Exact Token Match | $\ge$ 141 | **141** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨[nested PAR_7], τ⟩` | Exact Token Match | $\ge$ 125 | **397** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨[nested PAR_7], t37⟩` | Exact Token Match | $\ge$ 74 | **74** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t36` | Exact Token Match | $\ge$ 397 | **397** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t69` | Exact Token Match | $\ge$ 119 | **119** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t70` | Exact Token Match | $\ge$ 140 | **140** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t65` | Exact Token Match | $\ge$ 397 | **397** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t34` | Exact Token Match | $\ge$ 373 | **373** | ✅ **VERIFIED** |
| `[ST (in PAR_9)]` | `t27` | Exact Token Match | $\ge$ 242 | **242** | ✅ **VERIFIED** |
| `[ST (in PAR_9)]` | `t26` | Exact Token Match | $\ge$ 242 | **242** | ✅ **VERIFIED** |
| `[AS (in LOOP_3)]` | `[nested PAR_9]` | Exact Token Match | $\ge$ 242 | **242** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨t34, τ⟩` | Exact Token Match | $\ge$ 131 | **373** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨τ, t65⟩` | Exact Token Match | $\ge$ 138 | **397** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨τ, t34⟩` | Exact Token Match | $\ge$ 114 | **373** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨τ, t21⟩` | Exact Token Match | $\ge$ 391 | **515** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨τ, t46⟩` | Exact Token Match | $\ge$ 273 | **397** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨τ, t47, [nested PAR_4]⟩` | Exact Token Match | $\ge$ 14 | **138** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨τ, t47⟩` | Exact Token Match | $\ge$ 14 | **138** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨τ, τ, [nested PAR_5], [nested PAR_6]⟩` | Exact Token Match | $\ge$ 120 | **612** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨τ, τ, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 120 | **443** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨τ, t16⟩` | Exact Token Match | $\ge$ 11 | **135** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨τ, [nested PAR_7], t43, t44⟩` | Exact Token Match | $\ge$ 17 | **140** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨τ, [nested PAR_7], t43⟩` | Exact Token Match | $\ge$ 17 | **141** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨τ, [nested PAR_7], τ, t40⟩` | Exact Token Match | $\ge$ 1 | **167** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨τ, [nested PAR_7], τ⟩` | Exact Token Match | $\ge$ 1 | **397** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨τ, [nested PAR_7]⟩` | Exact Token Match | $\ge$ 273 | **397** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `t71` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `⟨t15, τ⟩` | Exact Token Match | $\ge$ 384 | **502** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `⟨t55, τ⟩` | Exact Token Match | $\ge$ 397 | **515** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `⟨t11, t05, τ⟩` | Exact Token Match | $\ge$ 153 | **271** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `⟨τ, t05, τ⟩` | Exact Token Match | $\ge$ 1 | **390** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `⟨t05, τ⟩` | Exact Token Match | $\ge$ 272 | **390** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_1]` | Exact Token Match | $\ge$ 1000 | **1000** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `⟨t43, t44⟩` | Exact Token Match | $\ge$ 141 | **140** | ⚠️ **DISCREPANCY** |
| `[ST (in LOOP_3)]` | `⟨[nested PAR_7], t43, t44⟩` | Exact Token Match | $\ge$ 141 | **140** | ⚠️ **DISCREPANCY** |
| `[ST (in LOOP_3)]` | `⟨[nested PAR_7], t37, t40⟩` | Exact Token Match | $\ge$ 74 | **44** | ⚠️ **DISCREPANCY** |
| `[ST (in LOOP_3)]` | `⟨t34, [nested PAR_9]⟩` | Exact Token Match | $\ge$ 242 | **241** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_1)]` | `[nested LOOP_2]` | Exact Token Match | $\ge$ 1 | **0** | ❌ **GHOST PATTERN** |

## Audit Summary
- **Perfect Pattern Verifications:** 78
- **Frequency Discrepancies:** 4
- **Ghost Patterns (Fatal):** 1
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 0.00%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 13.72%
- **Total Forced Volume (incl. unresolved AS, % of N):** 100.00%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 100.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 99.82%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 0.00%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 100.00%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 0.00%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 42.13%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 100.00%
- **Max Fractional Exposure (Worst-Case Normalized):** 100.00% (expected length: 7061.40 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 100.00% (expected length: 10.23 events)
- **Mean Absolute Exposure Volume:** 10.23 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested PAR_4]`
- **Internal Structure:** `{t62, t56}`
- **Block Frequency:** 138



![nested PAR_4 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.8_nested_PAR_4.png)

### `[nested PAR_5]`
- **Internal Structure:** `{t20, [t24 │ τ]}`
- **Block Frequency:** 379



![nested PAR_5 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.8_nested_PAR_5.png)

### `[nested PAR_6]`
- **Internal Structure:** `{t17, [t23 │ τ]}`
- **Block Frequency:** 621



![nested PAR_6 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.8_nested_PAR_6.png)

### `[nested PAR_8]`
- **Internal Structure:** `{t42, t39}`
- **Block Frequency:** 397



![nested PAR_8 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.8_nested_PAR_8.png)

### `[nested PAR_7]`
- **Internal Structure:** `{[t22 │ τ], t42, t39}`
- **Block Frequency:** 397



![nested PAR_7 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.8_nested_PAR_7.png)

### `[nested PAR_9]`
- **Internal Structure:** `{t27, t26}`
- **Block Frequency:** 242



![nested PAR_9 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.8_nested_PAR_9.png)

### `[nested LOOP_3]`
- **Internal Structure:** `(⟨[τ │ t28], [t21 │ t46 │ ⟨t48, t68⟩ │ ⟨t47, {t62, t56}⟩ │ ⟨[t16 │ τ], [{t20, [t24 │ τ]} │ τ], {t17, [t23 │ τ]}⟩ │ ⟨{[t22 │ τ], t42, t39}, [⟨t43, t44⟩ │ ⟨[τ │ t37], t40⟩ │ τ]⟩], [t36 │ ⟨[t69 │ t70 │ τ], [t65 │ ⟨t34, [{t27, t26} │ τ]⟩]⟩ │ τ]⟩ ∗ τ)`
- **Block Frequency:** 2131

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_3 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.8_nested_LOOP_3.png)

### `[nested LOOP_2]`
- **Internal Structure:** `([t06 │ t04 │ ⟨[t15 │ t55 │ ⟨[t11 │ τ], t05⟩ │ (⟨[τ │ t28], [t21 │ t46 │ ⟨t48, t68⟩ │ ⟨t47, {t62, t56}⟩ │ ⟨[t16 │ τ], [{t20, [t24 │ τ]} │ τ], {t17, [t23 │ τ]}⟩ │ ⟨{[t22 │ τ], t42, t39}, [⟨t43, t44⟩ │ ⟨[τ │ t37], t40⟩ │ τ]⟩], [t36 │ ⟨[t69 │ t70 │ τ], [t65 │ ⟨t34, [{t27, t26} │ τ]⟩]⟩ │ τ]⟩ ∗ τ)], [τ │ t71]⟩] ∗ τ)`
- **Block Frequency:** 1000

- **Max Loop Iterations:** `3247`
- **Max Sub-Sequence Length:** `6495` steps (if one case consumes all iterations)

![nested LOOP_2 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.8_nested_LOOP_2.png)

### `[nested PAR_1]`
- **Internal Structure:** `{t10, ([t06 │ t04 │ ⟨[t15 │ t55 │ ⟨[t11 │ τ], t05⟩ │ (⟨[τ │ t28], [t21 │ t46 │ ⟨t48, t68⟩ │ ⟨t47, {t62, t56}⟩ │ ⟨[t16 │ τ], [{t20, [t24 │ τ]} │ τ], {t17, [t23 │ τ]}⟩ │ ⟨{[t22 │ τ], t42, t39}, [⟨t43, t44⟩ │ ⟨[τ │ t37], t40⟩ │ τ]⟩], [t36 │ ⟨[t69 │ t70 │ τ], [t65 │ ⟨t34, [{t27, t26} │ τ]⟩]⟩ │ τ]⟩ ∗ τ)], [τ │ t71]⟩] ∗ τ)}`
- **Block Frequency:** 1000



![nested PAR_1 Internal Diagram](images/nested_ref_audit_pdc2021_0011013__noise0.8_nested_PAR_1.png)
