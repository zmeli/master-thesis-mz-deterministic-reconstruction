# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_0101010.xes` |
| **Noise Threshold** | `0.6` |
| **Fitness** | `0.8229238093856741` |
| **Precision** | `0.6859616573902287` |
| **Total Cases in Log** | `1000` |
| **Unique Activities** | `38` |
| **XOR Operators** | `26` |
| **LOOP Operators** | `11` |
| **SEQ Operators** | `23` |
| **PAR Operators** | `7` |
| **Binarization Additions** | `17` |
| **Tau Operators Added** | `21` |
| **Total Found Patterns** | `153` |
| **Verified Patterns** | `90` |
| **Discrepancy Patterns** | `12` |
| **Ghost Patterns** | `1` |
| **Nested LOOPs** | `11` |
| **Nested PARs** | `7` |
| **Tree Exposure (Strict, End-to-End % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `17.18%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `10.50%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `81.79%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `0.00%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `0.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `88.82%` |
| **Data Exposure, ST-only (% confirmed)** | `100.00%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `100.00%` |
| **Data Coverage, ST-only (% of real log)** | `14.66%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `45.84%` |
| **Data Coverage, Total (% of real log)** | `100.00%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `1.41%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `100.00%` |
| **Mean Absolute Exposure Volume (events/case)** | `14.00` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_0101010__noise0.6.png)


```text
->( 't10', X( 't06', 't11' ), X( tau, *( 't04', 't07' ) ), +( *( 't15', tau ), *( 't05', tau ) ), X( tau, 't16' ), 't20', +( *( 't17', tau ), 't21', ->( 't24', 't23' ) ), 't22', +( *( 't34', tau ), ->( 't26', 't27', X( 't71', ->( X( tau, 't28' ), *( 't42', 't41' ) ) ), +( *( 't40', tau ), ->( *( ->( 't39', X( tau, ->( 't43', 't44' ) ), *( 't36', tau ) ), 't32' ), *( ->( 't46', X( 't69', 't70', 't47' ), X( tau, +( 't62', 't37', ->( 't48', 't68' ) ) ), 't65', 't56', *( 't55', tau ) ), tau ) ) ) ) ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_0101010__noise0.6.png)



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
| `[ST (in LOOP_3)]` | `t15` | Exact Token Match | $\ge$ 556 | **556** | ✅ **VERIFIED** |
| `[ST (in PAR_2)]` | `⟨t15⟩` | Exact Token Match | $\ge$ 556 | **556** | ✅ **VERIFIED** |
| `[ST (in LOOP_4)]` | `t05` | Exact Token Match | $\ge$ 504 | **504** | ✅ **VERIFIED** |
| `[ST (in PAR_2)]` | `⟨t05⟩` | Exact Token Match | $\ge$ 504 | **504** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_2]` | Exact Token Match | $\ge$ 556 | **745** | ✅ **VERIFIED** |
| `[ST]` | `t16` | Exact Token Match | $\ge$ 171 | **171** | ✅ **VERIFIED** |
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
| `[ST (in LOOP_15)]` | `t56` | Exact Token Match | $\ge$ 1501 | **1501** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `t55` | Exact Token Match | $\ge$ 1649 | **1649** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨t55⟩` | Exact Token Match | $\ge$ 1353 | **1649** | ✅ **VERIFIED** |
| `[AS (in LOOP_15)]` | `[nested LOOP_18]` | Exact Token Match | $\ge$ 1 | **504** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨t56, [nested LOOP_18]⟩` | Exact Token Match | $\ge$ 1 | **1317** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨τ, t56, t55⟩` | Exact Token Match | $\ge$ 390 | **1317** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨τ, t56⟩` | Exact Token Match | $\ge$ 538 | **1501** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨τ, t65, t56, t55⟩` | Exact Token Match | $\ge$ 459 | **521** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨τ, τ, t56, t55⟩` | Exact Token Match | $\ge$ 34 | **1317** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨τ, τ, t56⟩` | Exact Token Match | $\ge$ 182 | **1501** | ✅ **VERIFIED** |
| `[ST (in LOOP_15)]` | `⟨τ, t65⟩` | Exact Token Match | $\ge$ 607 | **963** | ✅ **VERIFIED** |
| `[AS (in PAR_11)]` | `[nested LOOP_15]` | Exact Token Match | $\ge$ 1 | **68** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨t28, [nested LOOP_10], [nested PAR_11]⟩` | Exact Token Match | $\ge$ 1 | **4** | ✅ **VERIFIED** |
| `[ST (in PAR_8)]` | `⟨[nested LOOP_10], [nested PAR_11]⟩` | Exact Token Match | $\ge$ 1 | **9** | ✅ **VERIFIED** |
| `[ST]` | `⟨t22, [nested PAR_8]⟩` | Exact Token Match | $\ge$ 268 | **268** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_5], τ, [nested PAR_8]⟩` | Exact Token Match | $\ge$ 236 | **504** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, τ, [nested PAR_8]⟩` | Exact Token Match | $\ge$ 228 | **504** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_5], τ⟩` | Exact Token Match | $\ge$ 236 | **504** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 78 | **504** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t20⟩` | Exact Token Match | $\ge$ 255 | **426** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_2], τ⟩` | Exact Token Match | $\ge$ 385 | **745** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_2], τ⟩` | Exact Token Match | $\ge$ 134 | **745** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_2]⟩` | Exact Token Match | $\ge$ 305 | **745** | ✅ **VERIFIED** |
| `[ST]` | `⟨t06, τ⟩` | Exact Token Match | $\ge$ 245 | **496** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06, τ⟩` | Exact Token Match | $\ge$ 245 | **496** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ, τ⟩` | Exact Token Match | $\ge$ 4 | **1000** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06⟩` | Exact Token Match | $\ge$ 496 | **496** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11⟩` | Exact Token Match | $\ge$ 249 | **249** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 255 | **1000** | ✅ **VERIFIED** |
| `[AS (in PAR_5)]` | `[nested PAR_7]` | Exact Token Match | $\ge$ 504 | **236** | ⚠️ **DISCREPANCY** |
| `[ST (in LOOP_15)]` | `⟨t56, t55⟩` | Exact Token Match | $\ge$ 1353 | **1317** | ⚠️ **DISCREPANCY** |
| `[ST (in LOOP_15)]` | `⟨t65, t56, t55⟩` | Exact Token Match | $\ge$ 815 | **521** | ⚠️ **DISCREPANCY** |
| `[ST (in LOOP_15)]` | `⟨t65, t56⟩` | Exact Token Match | $\ge$ 963 | **521** | ⚠️ **DISCREPANCY** |
| `[ST (in LOOP_15)]` | `⟨τ, t65, t56⟩` | Exact Token Match | $\ge$ 607 | **521** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_11)]` | `⟨[nested XOR_19], [nested XOR_20], [nested XOR_21], [nested XOR_22], t56, t55⟩` | Exact Token Match | $\ge$ 208.0 | **68** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_8)]` | `[nested PAR_11]` | Exact Token Match | $\ge$ 1000 | **21** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_8)]` | `⟨τ, [nested PAR_11]⟩` | Exact Token Match | $\ge$ 764 | **21** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_8)]` | `⟨τ, τ, [nested PAR_11]⟩` | Exact Token Match | $\ge$ 528 | **21** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_8)]` | `⟨τ, τ, τ, [nested PAR_11]⟩` | Exact Token Match | $\ge$ 292 | **21** | ⚠️ **DISCREPANCY** |
| `[AS]` | `[nested PAR_8]` | Exact Token Match | $\ge$ 1000 | **504** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨τ, [nested PAR_8]⟩` | Exact Token Match | $\ge$ 732 | **504** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_8)]` | `⟨t71, [nested PAR_11]⟩` | Exact Token Match | $\ge$ 129 | **0** | ❌ **GHOST PATTERN** |

## Audit Summary
- **Perfect Pattern Verifications:** 90
- **Frequency Discrepancies:** 12
- **Ghost Patterns (Fatal):** 1
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 17.18%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 10.50%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 81.79%
- **Total Forced Volume (incl. unresolved AS, % of N):** 0.00%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 0.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 88.82%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 100.00%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 100.00%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 14.66%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 45.84%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 100.00%
- **Max Fractional Exposure (Worst-Case Normalized):** 1.41% (expected length: 2454.53 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 100.00% (expected length: 18.85 events)
- **Mean Absolute Exposure Volume:** 14.00 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_1]`
- **Internal Structure:** `(t04 ∗ t07)`
- **Block Frequency:** 251

- **Max Loop Iterations:** `73`
- **Max Sub-Sequence Length:** `147` steps (if one case consumes all iterations)

![nested LOOP_1 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.6_nested_LOOP_1.png)

### `[nested LOOP_3]`
- **Internal Structure:** `(t15 ∗ τ)`
- **Block Frequency:** 556

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_3 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.6_nested_LOOP_3.png)

### `[nested LOOP_4]`
- **Internal Structure:** `(t05 ∗ τ)`
- **Block Frequency:** 504

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_4 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.6_nested_LOOP_4.png)

### `[nested PAR_2]`
- **Internal Structure:** `{(t15 ∗ τ), [(t05 ∗ τ) │ τ]}`
- **Block Frequency:** 556



![nested PAR_2 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.6_nested_PAR_2.png)

### `[nested LOOP_6]`
- **Internal Structure:** `(t17 ∗ τ)`
- **Block Frequency:** 504

- **Max Loop Iterations:** `158`
- **Max Sub-Sequence Length:** `317` steps (if one case consumes all iterations)

![nested LOOP_6 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.6_nested_LOOP_6.png)

### `[nested PAR_7]`
- **Internal Structure:** `{t21, [⟨t24, t23⟩ │ τ]}`
- **Block Frequency:** 504



![nested PAR_7 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.6_nested_PAR_7.png)

### `[nested PAR_5]`
- **Internal Structure:** `{(t17 ∗ τ), t21, [⟨t24, t23⟩ │ τ]}`
- **Block Frequency:** 504



![nested PAR_5 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.6_nested_PAR_5.png)

### `[nested LOOP_9]`
- **Internal Structure:** `(t34 ∗ τ)`
- **Block Frequency:** 506

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_9 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.6_nested_LOOP_9.png)

### `[nested LOOP_10]`
- **Internal Structure:** `(t42 ∗ t41)`
- **Block Frequency:** 107

- **Max Loop Iterations:** `417`
- **Max Sub-Sequence Length:** `835` steps (if one case consumes all iterations)

![nested LOOP_10 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.6_nested_LOOP_10.png)

### `[nested LOOP_12]`
- **Internal Structure:** `(t40 ∗ τ)`
- **Block Frequency:** 626

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_12 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.6_nested_LOOP_12.png)

### `[nested LOOP_14]`
- **Internal Structure:** `(t36 ∗ τ)`
- **Block Frequency:** 248

- **Max Loop Iterations:** `955`
- **Max Sub-Sequence Length:** `1911` steps (if one case consumes all iterations)

![nested LOOP_14 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.6_nested_LOOP_14.png)

### `[nested LOOP_13]`
- **Internal Structure:** `(⟨t39, [⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ t32)`
- **Block Frequency:** 375

- **Max Loop Iterations:** `413`
- **Max Sub-Sequence Length:** `827` steps (if one case consumes all iterations)

![nested LOOP_13 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.6_nested_LOOP_13.png)

### `[nested PAR_17]`
- **Internal Structure:** `{t37, ⟨t48, t68⟩}`
- **Block Frequency:** 356



![nested PAR_17 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.6_nested_PAR_17.png)

### `[nested PAR_16]`
- **Internal Structure:** `{t62, t37, ⟨t48, t68⟩}`
- **Block Frequency:** 356



![nested PAR_16 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.6_nested_PAR_16.png)

### `[nested LOOP_18]`
- **Internal Structure:** `(t55 ∗ τ)`
- **Block Frequency:** 1501

- **Max Loop Iterations:** `148`
- **Max Sub-Sequence Length:** `297` steps (if one case consumes all iterations)

![nested LOOP_18 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.6_nested_LOOP_18.png)

### `[nested LOOP_15]`
- **Internal Structure:** `(⟨[t46 │ τ], [t69 │ t70 │ t47 │ τ], [τ │ {t62, t37, ⟨t48, t68⟩}], [t65 │ τ], t56, (t55 ∗ τ)⟩ ∗ τ)`
- **Block Frequency:** 1000

- **Max Loop Iterations:** `501`
- **Max Sub-Sequence Length:** `1003` steps (if one case consumes all iterations)

![nested LOOP_15 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.6_nested_LOOP_15.png)

### `[nested XOR_19]`
- **Internal Structure:** `[t46 │ τ]`
- **Block Frequency:** 1501



![nested XOR_19 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.6_nested_XOR_19.png)

### `[nested XOR_20]`
- **Internal Structure:** `[t69 │ t70 │ t47 │ τ]`
- **Block Frequency:** 1501



![nested XOR_20 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.6_nested_XOR_20.png)

### `[nested XOR_21]`
- **Internal Structure:** `[τ │ {t62, t37, ⟨t48, t68⟩}]`
- **Block Frequency:** 1501



![nested XOR_21 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.6_nested_XOR_21.png)

### `[nested XOR_22]`
- **Internal Structure:** `[t65 │ τ]`
- **Block Frequency:** 1501



![nested XOR_22 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.6_nested_XOR_22.png)

### `[nested PAR_11]`
- **Internal Structure:** `{[(t40 ∗ τ) │ τ], ⟨[(⟨t39, [⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ t32) │ τ], (⟨[t46 │ τ], [t69 │ t70 │ t47 │ τ], [τ │ {t62, t37, ⟨t48, t68⟩}], [t65 │ τ], t56, (t55 ∗ τ)⟩ ∗ τ)⟩}`
- **Block Frequency:** 1000



![nested PAR_11 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.6_nested_PAR_11.png)

### `[nested PAR_8]`
- **Internal Structure:** `{[(t34 ∗ τ) │ τ], ⟨[t26 │ τ], [t27 │ τ], [t71 │ ⟨[τ │ t28], (t42 ∗ t41)⟩ │ τ], {[(t40 ∗ τ) │ τ], ⟨[(⟨t39, [⟨[τ │ ⟨t43, t44⟩], (t36 ∗ τ)⟩ │ τ]⟩ ∗ t32) │ τ], (⟨[t46 │ τ], [t69 │ t70 │ t47 │ τ], [τ │ {t62, t37, ⟨t48, t68⟩}], [t65 │ τ], t56, (t55 ∗ τ)⟩ ∗ τ)⟩}⟩}`
- **Block Frequency:** 1000



![nested PAR_8 Internal Diagram](images/nested_ref_audit_pdc2021_0101010__noise0.6_nested_PAR_8.png)
