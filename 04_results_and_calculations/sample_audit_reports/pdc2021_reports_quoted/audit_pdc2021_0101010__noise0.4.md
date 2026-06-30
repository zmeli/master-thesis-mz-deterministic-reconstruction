# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_0101010.xes` |
| **Noise Threshold** | `0.4` |
| **Fitness** | `0.9505622289003718` |
| **Precision** | `0.7489872468117029` |
| **Total Cases in Log** | `1000` |
| **Unique Activities** | `39` |
| **XOR Operators** | `26` |
| **LOOP Operators** | `12` |
| **SEQ Operators** | `23` |
| **PAR Operators** | `7` |
| **Binarization Additions** | `15` |
| **Tau Operators Added** | `20` |
| **Total Found Patterns** | `147` |
| **Verified Patterns** | `92` |
| **Discrepancy Patterns** | `10` |
| **Ghost Patterns** | `1` |
| **Nested LOOPs** | `12` |
| **Nested PARs** | `7` |
| **Tree Exposure (Strict, End-to-End % of N)** | `3.70%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `20.18%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `10.20%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `37.61%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `3.70%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `0.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `90.19%` |
| **Data Exposure, ST-only (% confirmed)** | `95.25%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `97.56%` |
| **Data Coverage, ST-only (% of real log)** | `18.16%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `59.09%` |
| **Data Coverage, Total (% of real log)** | `98.88%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `6.61%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `100.00%` |
| **Mean Absolute Exposure Volume (events/case)** | `14.69` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_0101010__noise0.4.png)


```text
->( 't10', X( 't06', 't11' ), X( tau, *( 't04', 't07' ) ), X( tau, 't05' ), *( 't15', tau ), X( tau, 't16' ), X( tau, ->( 't20', +( *( 't17', tau ), 't21', X( tau, ->( 't24', 't23' ) ) ), X( tau, 't22' ), +( *( 't34', tau ), ->( X( tau, ->( 't26', 't27' ) ), X( 't71', ->( X( tau, 't28' ), *( 't42', 't41' ) ) ), +( *( 't40', tau ), ->( *( ->( 't39', X( tau, ->( 't43', 't44' ) ), *( 't36', tau ) ), 't32' ), *( ->( 't46', X( 't69', 't70', 't47' ), X( tau, +( 't62', 't37', ->( 't48', 't68' ) ) ), 't65', +( *( 't55', tau ), X( tau, *( *( 't56', tau ), 't52' ) ) ) ), tau ) ) ) ) ) ) ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_0101010__noise0.4.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST]` | `t10` | Exact Token Match | $\ge$ 1000 | **1000** | ✅ **VERIFIED** |
| `[ST]` | `t06` | Exact Token Match | $\ge$ 496 | **496** | ✅ **VERIFIED** |
| `[ST]` | `t11` | Exact Token Match | $\ge$ 249 | **249** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `t04` | Exact Token Match | $\ge$ 324 | **324** | ✅ **VERIFIED** |
| `[ST (in LOOP_1)]` | `t07` | Exact Token Match | $\ge$ 73 | **73** | ✅ **VERIFIED** |
| `[ST]` | `⟨t04⟩` | Exact Token Match | $\ge$ 178 | **192** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_1]` | Exact Token Match | $\ge$ 1 | **251** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `t15` | Exact Token Match | $\ge$ 556 | **556** | ✅ **VERIFIED** |
| `[ST]` | `t16` | Exact Token Match | $\ge$ 171 | **171** | ✅ **VERIFIED** |
| `[ST]` | `t20` | Exact Token Match | $\ge$ 426 | **426** | ✅ **VERIFIED** |
| `[ST (in LOOP_4)]` | `t17` | Exact Token Match | $\ge$ 662 | **662** | ✅ **VERIFIED** |
| `[ST (in PAR_3)]` | `⟨t17⟩` | Exact Token Match | $\ge$ 346 | **662** | ✅ **VERIFIED** |
| `[AS (in PAR_3)]` | `[nested LOOP_4]` | Exact Token Match | $\ge$ 1 | **662** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t21` | Exact Token Match | $\ge$ 504 | **504** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t24` | Exact Token Match | $\ge$ 236 | **236** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `t23` | Exact Token Match | $\ge$ 236 | **236** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t24, t23⟩` | Exact Token Match | $\ge$ 236 | **236** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_3]` | Exact Token Match | $\ge$ 504 | **504** | ✅ **VERIFIED** |
| `[ST]` | `t22` | Exact Token Match | $\ge$ 268 | **268** | ✅ **VERIFIED** |
| `[ST (in LOOP_7)]` | `t34` | Exact Token Match | $\ge$ 506 | **506** | ✅ **VERIFIED** |
| `[ST (in PAR_6)]` | `⟨t34⟩` | Exact Token Match | $\ge$ 506 | **506** | ✅ **VERIFIED** |
| `[ST (in PAR_6)]` | `t26` | Exact Token Match | $\ge$ 236 | **236** | ✅ **VERIFIED** |
| `[ST (in PAR_6)]` | `t27` | Exact Token Match | $\ge$ 236 | **236** | ✅ **VERIFIED** |
| `[ST (in PAR_6)]` | `⟨t26, t27⟩` | Exact Token Match | $\ge$ 236 | **236** | ✅ **VERIFIED** |
| `[ST (in PAR_6)]` | `t71` | Exact Token Match | $\ge$ 129 | **129** | ✅ **VERIFIED** |
| `[ST (in PAR_6)]` | `t28` | Exact Token Match | $\ge$ 107 | **107** | ✅ **VERIFIED** |
| `[ST (in LOOP_8)]` | `t42` | Exact Token Match | $\ge$ 524 | **792** | ✅ **VERIFIED** |
| `[ST (in LOOP_8)]` | `t41` | Exact Token Match | $\ge$ 417 | **417** | ✅ **VERIFIED** |
| `[AS (in PAR_6)]` | `[nested LOOP_8]` | Exact Token Match | $\ge$ 1 | **417** | ✅ **VERIFIED** |
| `[ST (in PAR_6)]` | `⟨t28, [nested LOOP_8]⟩` | Exact Token Match | $\ge$ 1 | **62** | ✅ **VERIFIED** |
| `[ST (in LOOP_10)]` | `t40` | Exact Token Match | $\ge$ 626 | **626** | ✅ **VERIFIED** |
| `[ST (in PAR_9)]` | `⟨t40⟩` | Exact Token Match | $\ge$ 626 | **626** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `t39` | Exact Token Match | $\ge$ 788 | **788** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `t43` | Exact Token Match | $\ge$ 248 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `t44` | Exact Token Match | $\ge$ 248 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `⟨t43, t44⟩` | Exact Token Match | $\ge$ 248 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_12)]` | `t36` | Exact Token Match | $\ge$ 1203 | **1203** | ✅ **VERIFIED** |
| `[AS (in LOOP_11)]` | `[nested LOOP_12]` | Exact Token Match | $\ge$ 1 | **375** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `⟨t43, t44, [nested LOOP_12]⟩` | Exact Token Match | $\ge$ 1 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `⟨t44, [nested LOOP_12]⟩` | Exact Token Match | $\ge$ 1 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `⟨t39, t43, t44, [nested LOOP_12]⟩` | Exact Token Match | $\ge$ 1 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `⟨t39, τ⟩` | Exact Token Match | $\ge$ 540 | **788** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `⟨t39, t43, t44⟩` | Exact Token Match | $\ge$ 248 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `⟨t39, t43⟩` | Exact Token Match | $\ge$ 248 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `t32` | Exact Token Match | $\ge$ 413 | **413** | ✅ **VERIFIED** |
| `[AS (in PAR_9)]` | `[nested LOOP_11]` | Exact Token Match | $\ge$ 1 | **184** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `t46` | Exact Token Match | $\ge$ 963 | **963** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `t69` | Exact Token Match | $\ge$ 305 | **305** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `t70` | Exact Token Match | $\ge$ 302 | **302** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `t47` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[ST (in PAR_14)]` | `t62` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[ST (in PAR_15)]` | `t37` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[ST (in PAR_15)]` | `t48` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[ST (in PAR_15)]` | `t68` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[ST (in PAR_15)]` | `⟨t48, t68⟩` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[AS (in PAR_14)]` | `[nested PAR_15]` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[AS (in LOOP_13)]` | `[nested PAR_14]` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `t65` | Exact Token Match | $\ge$ 963 | **963** | ✅ **VERIFIED** |
| `[ST (in LOOP_17)]` | `t55` | Exact Token Match | $\ge$ 1649 | **1649** | ✅ **VERIFIED** |
| `[ST (in PAR_16)]` | `⟨t55⟩` | Exact Token Match | $\ge$ 239 | **1649** | ✅ **VERIFIED** |
| `[AS (in PAR_16)]` | `[nested LOOP_17]` | Exact Token Match | $\ge$ 1 | **1649** | ✅ **VERIFIED** |
| `[ST (in LOOP_19)]` | `t56` | Exact Token Match | $\ge$ 1501 | **1501** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `⟨t56⟩` | Exact Token Match | $\ge$ 1501 | **1501** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `t52` | Exact Token Match | $\ge$ 557 | **557** | ✅ **VERIFIED** |
| `[ST (in PAR_16)]` | `⟨t56⟩` | Exact Token Match | $\ge$ 387 | **1501** | ✅ **VERIFIED** |
| `[AS (in PAR_16)]` | `[nested LOOP_18]` | Exact Token Match | $\ge$ 1 | **557** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `⟨t65, [nested PAR_16]⟩` | Exact Token Match | $\ge$ 944 | **963** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `⟨t65, τ⟩` | Exact Token Match | $\ge$ 19 | **963** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `⟨τ, t65, [nested PAR_16]⟩` | Exact Token Match | $\ge$ 588 | **963** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `⟨[nested PAR_14], t65, [nested PAR_16]⟩` | Exact Token Match | $\ge$ 337 | **356** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `⟨τ, t65⟩` | Exact Token Match | $\ge$ 607 | **963** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `⟨[nested PAR_14], t65⟩` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `⟨t46, t69⟩` | Exact Token Match | $\ge$ 305 | **305** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `⟨t46, t70⟩` | Exact Token Match | $\ge$ 302 | **302** | ✅ **VERIFIED** |
| `[ST (in LOOP_13)]` | `⟨t46, t47⟩` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[ST (in PAR_6)]` | `⟨t28, [nested LOOP_8], [nested PAR_9]⟩` | Exact Token Match | $\ge$ 1 | **4** | ✅ **VERIFIED** |
| `[ST (in PAR_6)]` | `⟨[nested LOOP_8], [nested PAR_9]⟩` | Exact Token Match | $\ge$ 1 | **9** | ✅ **VERIFIED** |
| `[ST]` | `⟨t22, [nested PAR_6]⟩` | Exact Token Match | $\ge$ 268 | **268** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_3], τ, [nested PAR_6]⟩` | Exact Token Match | $\ge$ 236 | **504** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, τ, [nested PAR_6]⟩` | Exact Token Match | $\ge$ 191 | **504** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_3], τ⟩` | Exact Token Match | $\ge$ 236 | **504** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_3]⟩` | Exact Token Match | $\ge$ 78 | **504** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t20⟩` | Exact Token Match | $\ge$ 255 | **426** | ✅ **VERIFIED** |
| `[ST]` | `⟨t15, τ⟩` | Exact Token Match | $\ge$ 385 | **487** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t15⟩` | Exact Token Match | $\ge$ 52 | **487** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t05⟩` | Exact Token Match | $\ge$ 253 | **284** | ✅ **VERIFIED** |
| `[ST]` | `⟨t06, τ⟩` | Exact Token Match | $\ge$ 245 | **496** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 37 | **1000** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06, τ⟩` | Exact Token Match | $\ge$ 245 | **496** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06⟩` | Exact Token Match | $\ge$ 496 | **496** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11⟩` | Exact Token Match | $\ge$ 249 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 218 | **1000** | ✅ **VERIFIED** |
| `[ST]` | `t05` | Exact Token Match | $\ge$ 504 | **284** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t15⟩` | Exact Token Match | $\ge$ 556 | **487** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_3)]` | `[nested PAR_5]` | Exact Token Match | $\ge$ 504 | **236** | ⚠️ **DISCREPANCY** |
| `[AS (in LOOP_13)]` | `[nested PAR_16]` | Exact Token Match | $\ge$ 944 | **504** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_6)]` | `[nested PAR_9]` | Exact Token Match | $\ge$ 963 | **21** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_6)]` | `⟨τ, [nested PAR_9]⟩` | Exact Token Match | $\ge$ 727 | **21** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_6)]` | `⟨τ, τ, [nested PAR_9]⟩` | Exact Token Match | $\ge$ 491 | **21** | ⚠️ **DISCREPANCY** |
| `[AS]` | `[nested PAR_6]` | Exact Token Match | $\ge$ 963 | **504** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨τ, [nested PAR_6]⟩` | Exact Token Match | $\ge$ 695 | **504** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t05, t15⟩` | Exact Token Match | $\ge$ 97 | **83** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_6)]` | `⟨t71, [nested PAR_9]⟩` | Exact Token Match | $\ge$ 129 | **0** | ❌ **GHOST PATTERN** |

## Audit Summary
- **Perfect Pattern Verifications:** 92
- **Frequency Discrepancies:** 10
- **Ghost Patterns (Fatal):** 1
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 3.70%
- **Tree Exposure (Strict, Fragment-Level % of N):** 20.18%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 10.20%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 37.61%
- **Total Forced Volume (incl. unresolved AS, % of N):** 3.70%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 0.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 90.19%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 95.25%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 97.56%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 18.16%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 59.09%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 98.88%
- **Max Fractional Exposure (Worst-Case Normalized):** 6.61% (expected length: 1230.22 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 100.00% (expected length: 19.41 events)
- **Mean Absolute Exposure Volume:** 14.69 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_1]`
- **Internal Structure:** `(t04 ∗ t07)`
- **Block Frequency:** 251

- **Max Loop Iterations:** `73`
- **Max Sub-Sequence Length:** `147` steps (if one case consumes all iterations)

![nested LOOP_1 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.4_nested_LOOP_1.png)

### `[nested LOOP_2]`
- **Internal Structure:** `(t15 ∗ τ)`
- **Block Frequency:** 556

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_2 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.4_nested_LOOP_2.png)

### `[nested LOOP_4]`
- **Internal Structure:** `(t17 ∗ τ)`
- **Block Frequency:** 504

- **Max Loop Iterations:** `158`
- **Max Sub-Sequence Length:** `317` steps (if one case consumes all iterations)

![nested LOOP_4 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.4_nested_LOOP_4.png)

### `[nested PAR_5]`
- **Internal Structure:** `{t21, [τ │ ⟨t24, t23⟩]}`
- **Block Frequency:** 504



![nested PAR_5 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.4_nested_PAR_5.png)

### `[nested PAR_3]`
- **Internal Structure:** `{(t17 ∗ τ), t21, [τ │ ⟨t24, t23⟩]}`
- **Block Frequency:** 504



![nested PAR_3 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.4_nested_PAR_3.png)

### `[nested LOOP_7]`
- **Internal Structure:** `(t34 ∗ τ)`
- **Block Frequency:** 506

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_7 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.4_nested_LOOP_7.png)

### `[nested LOOP_8]`
- **Internal Structure:** `(t42 ∗ t41)`
- **Block Frequency:** 107

- **Max Loop Iterations:** `417`
- **Max Sub-Sequence Length:** `835` steps (if one case consumes all iterations)

![nested LOOP_8 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.4_nested_LOOP_8.png)

### `[nested LOOP_10]`
- **Internal Structure:** `(t40 ∗ τ)`
- **Block Frequency:** 626

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_10 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.4_nested_LOOP_10.png)

### `[nested LOOP_12]`
- **Internal Structure:** `(t36 ∗ τ)`
- **Block Frequency:** 248

- **Max Loop Iterations:** `955`
- **Max Sub-Sequence Length:** `1911` steps (if one case consumes all iterations)

![nested LOOP_12 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.4_nested_LOOP_12.png)

### `[nested LOOP_11]`
- **Internal Structure:** `(⟨t39, [⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ t32)`
- **Block Frequency:** 375

- **Max Loop Iterations:** `413`
- **Max Sub-Sequence Length:** `827` steps (if one case consumes all iterations)

![nested LOOP_11 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.4_nested_LOOP_11.png)

### `[nested PAR_15]`
- **Internal Structure:** `{t37, ⟨t48, t68⟩}`
- **Block Frequency:** 356



![nested PAR_15 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.4_nested_PAR_15.png)

### `[nested PAR_14]`
- **Internal Structure:** `{t62, t37, ⟨t48, t68⟩}`
- **Block Frequency:** 356



![nested PAR_14 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.4_nested_PAR_14.png)

### `[nested LOOP_17]`
- **Internal Structure:** `(t55 ∗ τ)`
- **Block Frequency:** 944

- **Max Loop Iterations:** `705`
- **Max Sub-Sequence Length:** `1411` steps (if one case consumes all iterations)

![nested LOOP_17 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.4_nested_LOOP_17.png)

### `[nested LOOP_19]`
- **Internal Structure:** `(t56 ∗ τ)`
- **Block Frequency:** 1501

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_19 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.4_nested_LOOP_19.png)

### `[nested LOOP_18]`
- **Internal Structure:** `((t56 ∗ τ) ∗ t52)`
- **Block Frequency:** 944

- **Max Loop Iterations:** `557`
- **Max Sub-Sequence Length:** `1115` steps (if one case consumes all iterations)

![nested LOOP_18 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.4_nested_LOOP_18.png)

### `[nested PAR_16]`
- **Internal Structure:** `{(t55 ∗ τ), [τ │ ((t56 ∗ τ) ∗ t52)]}`
- **Block Frequency:** 944



![nested PAR_16 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.4_nested_PAR_16.png)

### `[nested LOOP_13]`
- **Internal Structure:** `(⟨t46, [t69 │ t70 │ t47], [τ │ {t62, t37, ⟨t48, t68⟩}], t65, [{(t55 ∗ τ), [τ │ ((t56 ∗ τ) ∗ t52)]} │ τ]⟩ ∗ τ)`
- **Block Frequency:** 963

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_13 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.4_nested_LOOP_13.png)

### `[nested PAR_9]`
- **Internal Structure:** `{[(t40 ∗ τ) │ τ], ⟨[(⟨t39, [⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ t32) │ τ], (⟨t46, [t69 │ t70 │ t47], [τ │ {t62, t37, ⟨t48, t68⟩}], t65, [{(t55 ∗ τ), [τ │ ((t56 ∗ τ) ∗ t52)]} │ τ]⟩ ∗ τ)⟩}`
- **Block Frequency:** 963



![nested PAR_9 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.4_nested_PAR_9.png)

### `[nested PAR_6]`
- **Internal Structure:** `{[(t34 ∗ τ) │ τ], ⟨[τ │ ⟨t26, t27⟩], [t71 │ ⟨[τ │ t28], (t42 ∗ t41)⟩ │ τ], {[(t40 ∗ τ) │ τ], ⟨[(⟨t39, [⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ t32) │ τ], (⟨t46, [t69 │ t70 │ t47], [τ │ {t62, t37, ⟨t48, t68⟩}], t65, [{(t55 ∗ τ), [τ │ ((t56 ∗ τ) ∗ t52)]} │ τ]⟩ ∗ τ)⟩}⟩}`
- **Block Frequency:** 963



![nested PAR_6 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.4_nested_PAR_6.png)
