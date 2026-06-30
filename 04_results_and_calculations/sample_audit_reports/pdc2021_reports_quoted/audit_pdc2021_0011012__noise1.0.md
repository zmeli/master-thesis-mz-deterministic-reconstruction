# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_0011012.xes` |
| **Noise Threshold** | `1.0` |
| **Fitness** | `0.6079703914616117` |
| **Precision** | `0.8792932628797886` |
| **Total Cases in Log** | `1000` |
| **Unique Activities** | `29` |
| **XOR Operators** | `27` |
| **LOOP Operators** | `3` |
| **SEQ Operators** | `16` |
| **PAR Operators** | `1` |
| **Binarization Additions** | `17` |
| **Tau Operators Added** | `15` |
| **Total Found Patterns** | `91` |
| **Verified Patterns** | `59` |
| **Discrepancy Patterns** | `8` |
| **Ghost Patterns** | `0` |
| **Nested LOOPs** | `3` |
| **Nested PARs** | `1` |
| **Tree Exposure (Strict, End-to-End % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `41.76%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `27.60%` |
| **Tree Exposure (Local-Strict % of N)** | `92.34%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `46.87%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `0.00%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `0.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `99.72%` |
| **Data Exposure, ST-only (% confirmed)** | `99.68%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `99.67%` |
| **Data Coverage, ST-only (% of real log)** | `81.58%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `98.69%` |
| **Data Coverage, Total (% of real log)** | `100.00%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `2.64%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `41.76%` |
| **Mean Absolute Exposure Volume (events/case)** | `1.56` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_0011012__noise1.0.png)


```text
->( 't10', X( 't11', ->( 't06', 't04' ) ), 't05', X( 't15', ->( 't16', 't20' ) ), +( *( 't17', tau ), ->( 't21', 't24', 't23' ) ), 't22', X( 't27', 't42', 't26', 't39', *( 't34', tau ) ), X( 't71', ->( 't43', 't44', X( tau, 't36', 't46', 't68', *( 't40', tau ) ), X( 't69', 't70' ), 't65' ) ), 't55' )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_0011012__noise1.0.png)



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
| `[ST]` | `t27` | Exact Token Match | $\ge$ 152 | **235** | ✅ **VERIFIED** |
| `[ST]` | `t42` | Exact Token Match | $\ge$ 232 | **357** | ✅ **VERIFIED** |
| `[ST]` | `t26` | Exact Token Match | $\ge$ 153 | **236** | ✅ **VERIFIED** |
| `[ST]` | `t39` | Exact Token Match | $\ge$ 232 | **357** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t34` | Exact Token Match | $\ge$ 356 | **356** | ✅ **VERIFIED** |
| `[ST]` | `⟨t34⟩` | Exact Token Match | $\ge$ 106 | **278** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_3]` | Exact Token Match | $\ge$ 1 | **317** | ✅ **VERIFIED** |
| `[ST]` | `t71` | Exact Token Match | $\ge$ 103 | **109** | ✅ **VERIFIED** |
| `[ST]` | `t43` | Exact Token Match | $\ge$ 118 | **118** | ✅ **VERIFIED** |
| `[ST]` | `t44` | Exact Token Match | $\ge$ 119 | **119** | ✅ **VERIFIED** |
| `[ST]` | `t36` | Exact Token Match | $\ge$ 337 | **358** | ✅ **VERIFIED** |
| `[ST]` | `t46` | Exact Token Match | $\ge$ 339 | **360** | ✅ **VERIFIED** |
| `[ST]` | `t68` | Exact Token Match | $\ge$ 57 | **61** | ✅ **VERIFIED** |
| `[ST (in LOOP_4)]` | `t40` | Exact Token Match | $\ge$ 174 | **174** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_4]` | Exact Token Match | $\ge$ 1 | **155** | ✅ **VERIFIED** |
| `[ST]` | `t69` | Exact Token Match | $\ge$ 144 | **144** | ✅ **VERIFIED** |
| `[ST]` | `t70` | Exact Token Match | $\ge$ 99 | **99** | ✅ **VERIFIED** |
| `[ST]` | `t65` | Exact Token Match | $\ge$ 359 | **359** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t65⟩` | Exact Token Match | $\ge$ 116 | **359** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t36⟩` | Exact Token Match | $\ge$ 218 | **358** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t46⟩` | Exact Token Match | $\ge$ 220 | **360** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t40⟩` | Exact Token Match | $\ge$ 35 | **136** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, τ, t36⟩` | Exact Token Match | $\ge$ 100 | **358** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, τ, t46⟩` | Exact Token Match | $\ge$ 102 | **360** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t44⟩` | Exact Token Match | $\ge$ 1 | **119** | ✅ **VERIFIED** |
| `[ST]` | `t55` | Exact Token Match | $\ge$ 471 | **471** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t55⟩` | Exact Token Match | $\ge$ 9 | **471** | ✅ **VERIFIED** |
| `[ST]` | `⟨t42, τ⟩` | Exact Token Match | $\ge$ 11 | **357** | ✅ **VERIFIED** |
| `[ST]` | `⟨t39, τ⟩` | Exact Token Match | $\ge$ 11 | **357** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], τ⟩` | Exact Token Match | $\ge$ 233 | **472** | ✅ **VERIFIED** |
| `[ST]` | `⟨t15, τ⟩` | Exact Token Match | $\ge$ 31 | **497** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t15⟩` | Exact Token Match | $\ge$ 160 | **497** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11⟩` | Exact Token Match | $\ge$ 183 | **222** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06, t04⟩` | Exact Token Match | $\ge$ 196 | **222** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06, τ⟩` | Exact Token Match | $\ge$ 224 | **468** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06⟩` | Exact Token Match | $\ge$ 461 | **468** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 233 | **959** | ✅ **VERIFIED** |
| `[ST]` | `⟨t06, t04⟩` | Exact Token Match | $\ge$ 237 | **229** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t16, t20⟩` | Exact Token Match | $\ge$ 113 | **110** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_1)]` | `⟨t24, t23⟩` | Exact Token Match | $\ge$ 230 | **229** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_1)]` | `⟨t21, t24, t23⟩` | Exact Token Match | $\ge$ 230 | **226** | ⚠️ **DISCREPANCY** |
| `[ST (in PAR_1)]` | `⟨t21, t24⟩` | Exact Token Match | $\ge$ 230 | **227** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t40⟩` | Exact Token Match | $\ge$ 154 | **136** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t69, t65⟩` | Exact Token Match | $\ge$ 144 | **142** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t70, t65⟩` | Exact Token Match | $\ge$ 99 | **98** | ⚠️ **DISCREPANCY** |

## Audit Summary
- **Perfect Pattern Verifications:** 59
- **Frequency Discrepancies:** 8
- **Ghost Patterns (Fatal):** 0
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 41.76%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 27.60%
- **Tree Exposure (Local-Strict % of N):** 92.34% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 46.87%
- **Total Forced Volume (incl. unresolved AS, % of N):** 0.00%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 0.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 99.72%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 99.68%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 99.67%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 81.58%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 98.69%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 100.00%
- **Max Fractional Exposure (Worst-Case Normalized):** 2.64% (expected length: 133.16 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 41.76% (expected length: 8.42 events)
- **Mean Absolute Exposure Volume:** 1.56 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_2]`
- **Internal Structure:** `(t17 ∗ τ)`
- **Block Frequency:** 466

- **Max Loop Iterations:** `123`
- **Max Sub-Sequence Length:** `247` steps (if one case consumes all iterations)

![nested LOOP_2 Internal Diagram](images/nested_ref_audit_pdc2021_0011012__noise1.0_nested_LOOP_2.png)

### `[nested PAR_1]`
- **Internal Structure:** `{(t17 ∗ τ), ⟨t21, [⟨[t24 │ τ], t23⟩ │ τ]⟩}`
- **Block Frequency:** 466



![nested PAR_1 Internal Diagram](images/nested_ref_audit_pdc2021_0011012__noise1.0_nested_PAR_1.png)

### `[nested LOOP_3]`
- **Internal Structure:** `(t34 ∗ τ)`
- **Block Frequency:** 231

- **Max Loop Iterations:** `125`
- **Max Sub-Sequence Length:** `251` steps (if one case consumes all iterations)

![nested LOOP_3 Internal Diagram](images/nested_ref_audit_pdc2021_0011012__noise1.0_nested_LOOP_3.png)

### `[nested LOOP_4]`
- **Internal Structure:** `(t40 ∗ τ)`
- **Block Frequency:** 164

- **Max Loop Iterations:** `10`
- **Max Sub-Sequence Length:** `21` steps (if one case consumes all iterations)

![nested LOOP_4 Internal Diagram](images/nested_ref_audit_pdc2021_0011012__noise1.0_nested_LOOP_4.png)
