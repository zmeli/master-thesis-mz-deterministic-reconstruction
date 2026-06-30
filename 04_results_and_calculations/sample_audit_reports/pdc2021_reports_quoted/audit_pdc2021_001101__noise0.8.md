# Process Engine Audit Report

## Dataset & Audit Overview
| Metric | Value |
| :--- | :--- |
| **Dataset Name** | `pdc2021_001101.xes` |
| **Noise Threshold** | `0.8` |
| **Fitness** | `0.7837906918254022` |
| **Precision** | `0.6870229007633588` |
| **Total Cases in Log** | `250` |
| **Unique Activities** | `34` |
| **XOR Operators** | `21` |
| **LOOP Operators** | `20` |
| **SEQ Operators** | `21` |
| **PAR Operators** | `9` |
| **Binarization Additions** | `20` |
| **Tau Operators Added** | `15` |
| **Total Found Patterns** | `162` |
| **Verified Patterns** | `95` |
| **Discrepancy Patterns** | `30` |
| **Ghost Patterns** | `1` |
| **Nested LOOPs** | `20` |
| **Nested PARs** | `9` |
| **Tree Exposure (Strict, End-to-End % of N)** | `0.00%` |
| **Tree Exposure (Strict, Fragment-Level % of N)** | `11.75%` |
| **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N)** | `5.67%` |
| **Tree Exposure (Local-Strict % of N)** | `100.00%` |
| **Tree Exposure (Local-Strict, >=2 activities, % of N)** | `5.67%` |
| **Total Forced Volume (incl. unresolved AS, % of N)** | `0.00%` |
| **AS-Resolved Volume (% of N)** | `0.00%` |
| **AS-Resolved Volume, PAR-only (% of N)** | `0.00%` |
| **AS-Resolved Volume, LOOP-only (% of N)** | `0.00%` |
| **AS-Opaque Volume (% of N)** | `0.00%` |
| **Data Exposure (Confirmed % of Claimed Volume)** | `90.31%` |
| **Data Exposure, ST-only (% confirmed)** | `90.35%` |
| **Data Exposure, ST + ST-in-PAR (% confirmed)** | `93.20%` |
| **Data Coverage, ST-only (% of real log)** | `30.55%` |
| **Data Coverage, ST + ST-in-PAR (% of real log)** | `85.05%` |
| **Data Coverage, Total (% of real log)** | `95.80%` |
| **Max Fractional Exposure (Worst-Case Normalized)** | `2.43%` |
| **Avg Fractional Exposure (Typical-Case Normalized)** | `24.71%` |
| **Mean Absolute Exposure Volume (events/case)** | `4.19` |

---

## Original PM4Py Tree

![Original PM4Py Tree](images/orig_tree_audit_pdc2021_001101__noise0.8.png)


```text
->( 't10', X( 't06', 't11' ), +( *( 't05', tau ), X( *( 't15', tau ), *( 't04', tau ) ) ), 't16', 't20', X( tau, ->( X( tau, ->( 't24', 't23' ) ), X( +( *( 't22', tau ), *( 't17', tau ), *( 't21', tau ) ), ->( 't34', 't26', 't27', 't28' ) ), *( 't42', tau ), *( 't39', tau ), 't43', *( 't44', tau ), X( tau, ->( 't71', X( tau, 't70' ) ) ), +( *( 't36', tau ), *( 't47', tau ), *( 't37', tau ), *( 't46', tau ), *( 't40', tau ) ), +( *( 't48', tau ), *( 't68', tau ) ), *( 't62', tau ) ) ), *( 't65', tau ), +( *( 't55', tau ), X( tau, *( 't56', tau ) ) ) )
```

## Assimilated Master Tree

![Assimilated Master Tree](images/custom_tree_audit_pdc2021_001101__noise0.8.png)



## Trace Verification

| Type | Abstract Pattern | Variations Observed | Predicted Freq | Actual Log Freq | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[ST]` | `t10` | Exact Token Match | $\ge$ 250 | **250** | ✅ **VERIFIED** |
| `[ST]` | `t06` | Exact Token Match | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[ST]` | `t11` | Exact Token Match | $\ge$ 133 | **133** | ✅ **VERIFIED** |
| `[ST (in LOOP_2)]` | `t05` | Exact Token Match | $\ge$ 117 | **117** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t05⟩` | Exact Token Match | $\ge$ 49 | **117** | ✅ **VERIFIED** |
| `[AS (in PAR_1)]` | `[nested LOOP_2]` | Exact Token Match | $\ge$ 1 | **117** | ✅ **VERIFIED** |
| `[ST (in LOOP_3)]` | `t15` | Exact Token Match | $\ge$ 77 | **77** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t15⟩` | Exact Token Match | $\ge$ 77 | **77** | ✅ **VERIFIED** |
| `[ST (in LOOP_4)]` | `t04` | Exact Token Match | $\ge$ 6 | **6** | ✅ **VERIFIED** |
| `[ST (in PAR_1)]` | `⟨t04⟩` | Exact Token Match | $\ge$ 6 | **6** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_1]` | Exact Token Match | $\ge$ 83 | **118** | ✅ **VERIFIED** |
| `[ST]` | `t16` | Exact Token Match | $\ge$ 64 | **64** | ✅ **VERIFIED** |
| `[ST]` | `t20` | Exact Token Match | $\ge$ 192 | **192** | ✅ **VERIFIED** |
| `[ST (in LOOP_6)]` | `t22` | Exact Token Match | $\ge$ 140 | **140** | ✅ **VERIFIED** |
| `[ST (in PAR_5)]` | `⟨t22⟩` | Exact Token Match | $\ge$ 140 | **140** | ✅ **VERIFIED** |
| `[ST (in LOOP_8)]` | `t17` | Exact Token Match | $\ge$ 266 | **266** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨t17⟩` | Exact Token Match | $\ge$ 62 | **266** | ✅ **VERIFIED** |
| `[AS (in PAR_7)]` | `[nested LOOP_8]` | Exact Token Match | $\ge$ 1 | **266** | ✅ **VERIFIED** |
| `[ST (in LOOP_9)]` | `t21` | Exact Token Match | $\ge$ 273 | **273** | ✅ **VERIFIED** |
| `[ST (in PAR_7)]` | `⟨t21⟩` | Exact Token Match | $\ge$ 55 | **273** | ✅ **VERIFIED** |
| `[AS (in PAR_7)]` | `[nested LOOP_9]` | Exact Token Match | $\ge$ 1 | **273** | ✅ **VERIFIED** |
| `[AS (in PAR_5)]` | `[nested PAR_7]` | Exact Token Match | $\ge$ 164 | **212** | ✅ **VERIFIED** |
| `[AS]` | `[nested PAR_5]` | Exact Token Match | $\ge$ 164 | **248** | ✅ **VERIFIED** |
| `[ST]` | `t34` | Exact Token Match | $\ge$ 86 | **106** | ✅ **VERIFIED** |
| `[ST]` | `t26` | Exact Token Match | $\ge$ 86 | **106** | ✅ **VERIFIED** |
| `[ST]` | `t27` | Exact Token Match | $\ge$ 86 | **106** | ✅ **VERIFIED** |
| `[ST]` | `t28` | Exact Token Match | $\ge$ 72 | **72** | ✅ **VERIFIED** |
| `[ST]` | `⟨t27, τ⟩` | Exact Token Match | $\ge$ 14 | **106** | ✅ **VERIFIED** |
| `[ST]` | `⟨t26, t27, τ⟩` | Exact Token Match | $\ge$ 14 | **106** | ✅ **VERIFIED** |
| `[ST]` | `⟨t26, t27⟩` | Exact Token Match | $\ge$ 86 | **106** | ✅ **VERIFIED** |
| `[ST]` | `⟨t34, t26, t27, τ⟩` | Exact Token Match | $\ge$ 14 | **56** | ✅ **VERIFIED** |
| `[ST (in LOOP_10)]` | `t42` | Exact Token Match | $\ge$ 316 | **316** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_10]` | Exact Token Match | $\ge$ 1 | **217** | ✅ **VERIFIED** |
| `[ST (in LOOP_11)]` | `t39` | Exact Token Match | $\ge$ 337 | **337** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_11]` | Exact Token Match | $\ge$ 1 | **210** | ✅ **VERIFIED** |
| `[ST (in LOOP_12)]` | `t44` | Exact Token Match | $\ge$ 154 | **154** | ✅ **VERIFIED** |
| `[ST]` | `t71` | Exact Token Match | $\ge$ 38 | **38** | ✅ **VERIFIED** |
| `[ST (in LOOP_14)]` | `t36` | Exact Token Match | $\ge$ 438 | **438** | ✅ **VERIFIED** |
| `[ST (in PAR_13)]` | `⟨t36⟩` | Exact Token Match | $\ge$ 62 | **438** | ✅ **VERIFIED** |
| `[AS (in PAR_13)]` | `[nested LOOP_14]` | Exact Token Match | $\ge$ 1 | **438** | ✅ **VERIFIED** |
| `[ST (in LOOP_16)]` | `t47` | Exact Token Match | $\ge$ 222 | **222** | ✅ **VERIFIED** |
| `[ST (in PAR_15)]` | `⟨t47⟩` | Exact Token Match | $\ge$ 222 | **222** | ✅ **VERIFIED** |
| `[ST (in LOOP_18)]` | `t37` | Exact Token Match | $\ge$ 192 | **192** | ✅ **VERIFIED** |
| `[ST (in PAR_17)]` | `⟨t37⟩` | Exact Token Match | $\ge$ 192 | **192** | ✅ **VERIFIED** |
| `[ST (in LOOP_20)]` | `t46` | Exact Token Match | $\ge$ 327 | **327** | ✅ **VERIFIED** |
| `[ST (in PAR_19)]` | `⟨t46⟩` | Exact Token Match | $\ge$ 173 | **327** | ✅ **VERIFIED** |
| `[AS (in PAR_19)]` | `[nested LOOP_20]` | Exact Token Match | $\ge$ 1 | **327** | ✅ **VERIFIED** |
| `[ST (in LOOP_21)]` | `t40` | Exact Token Match | $\ge$ 229 | **229** | ✅ **VERIFIED** |
| `[ST (in PAR_19)]` | `⟨t40⟩` | Exact Token Match | $\ge$ 229 | **229** | ✅ **VERIFIED** |
| `[ST (in LOOP_23)]` | `t48` | Exact Token Match | $\ge$ 185 | **185** | ✅ **VERIFIED** |
| `[ST (in PAR_22)]` | `⟨t48⟩` | Exact Token Match | $\ge$ 185 | **185** | ✅ **VERIFIED** |
| `[ST (in LOOP_24)]` | `t68` | Exact Token Match | $\ge$ 185 | **185** | ✅ **VERIFIED** |
| `[ST (in PAR_22)]` | `⟨t68⟩` | Exact Token Match | $\ge$ 185 | **185** | ✅ **VERIFIED** |
| `[ST (in LOOP_25)]` | `t62` | Exact Token Match | $\ge$ 264 | **264** | ✅ **VERIFIED** |
| `[ST]` | `⟨t62⟩` | Exact Token Match | $\ge$ 106 | **157** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_25]` | Exact Token Match | $\ge$ 1 | **187** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_22], [nested LOOP_25]⟩` | Exact Token Match | $\ge$ 1 | **55** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_13], [nested PAR_22], [nested LOOP_25]⟩` | Exact Token Match | $\ge$ 1 | **20** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_13], τ⟩` | Exact Token Match | $\ge$ 65 | **243** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_13], [nested PAR_22], t62⟩` | Exact Token Match | $\ge$ 13 | **20** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_13]⟩` | Exact Token Match | $\ge$ 157 | **243** | ✅ **VERIFIED** |
| `[ST]` | `⟨t44, τ⟩` | Exact Token Match | $\ge$ 61 | **66** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, τ, [nested PAR_13]⟩` | Exact Token Match | $\ge$ 3 | **243** | ✅ **VERIFIED** |
| `[ST]` | `⟨t43, t44⟩` | Exact Token Match | $\ge$ 58 | **66** | ✅ **VERIFIED** |
| `[ST]` | `⟨t39, τ⟩` | Exact Token Match | $\ge$ 9 | **162** | ✅ **VERIFIED** |
| `[ST]` | `⟨t42, t39, t43⟩` | Exact Token Match | $\ge$ 1 | **46** | ✅ **VERIFIED** |
| `[ST]` | `⟨t42, t39⟩` | Exact Token Match | $\ge$ 97 | **149** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_5], t42, t39⟩` | Exact Token Match | $\ge$ 11 | **149** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_5], t42⟩` | Exact Token Match | $\ge$ 98 | **177** | ✅ **VERIFIED** |
| `[ST]` | `⟨t34, t26, t27, t28, t42⟩` | Exact Token Match | $\ge$ 6 | **40** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 54 | **248** | ✅ **VERIFIED** |
| `[ST (in LOOP_26)]` | `t65` | Exact Token Match | $\ge$ 366 | **366** | ✅ **VERIFIED** |
| `[ST]` | `⟨t65⟩` | Exact Token Match | $\ge$ 134 | **185** | ✅ **VERIFIED** |
| `[AS]` | `[nested LOOP_26]` | Exact Token Match | $\ge$ 1 | **245** | ✅ **VERIFIED** |
| `[ST (in LOOP_28)]` | `t55` | Exact Token Match | $\ge$ 465 | **465** | ✅ **VERIFIED** |
| `[ST (in PAR_27)]` | `⟨t55⟩` | Exact Token Match | $\ge$ 35 | **465** | ✅ **VERIFIED** |
| `[AS (in PAR_27)]` | `[nested LOOP_28]` | Exact Token Match | $\ge$ 1 | **465** | ✅ **VERIFIED** |
| `[ST (in LOOP_29)]` | `t56` | Exact Token Match | $\ge$ 495 | **495** | ✅ **VERIFIED** |
| `[ST (in PAR_27)]` | `⟨t56⟩` | Exact Token Match | $\ge$ 5 | **495** | ✅ **VERIFIED** |
| `[AS (in PAR_27)]` | `[nested LOOP_29]` | Exact Token Match | $\ge$ 1 | **495** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested LOOP_26], [nested PAR_27]⟩` | Exact Token Match | $\ge$ 1 | **25** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, τ⟩` | Exact Token Match | $\ge$ 82 | **192** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, t24, t23⟩` | Exact Token Match | $\ge$ 52 | **84** | ✅ **VERIFIED** |
| `[ST]` | `⟨t20, t24⟩` | Exact Token Match | $\ge$ 52 | **84** | ✅ **VERIFIED** |
| `[ST]` | `⟨t16, t20⟩` | Exact Token Match | $\ge$ 6 | **64** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t20, τ⟩` | Exact Token Match | $\ge$ 18 | **192** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, t20⟩` | Exact Token Match | $\ge$ 128 | **192** | ✅ **VERIFIED** |
| `[ST]` | `⟨[nested PAR_1], τ⟩` | Exact Token Match | $\ge$ 19 | **118** | ✅ **VERIFIED** |
| `[ST]` | `⟨τ, τ, t20⟩` | Exact Token Match | $\ge$ 45 | **192** | ✅ **VERIFIED** |
| `[ST]` | `⟨t11, τ⟩` | Exact Token Match | $\ge$ 50 | **133** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11, τ⟩` | Exact Token Match | $\ge$ 50 | **133** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ, τ⟩` | Exact Token Match | $\ge$ 32 | **250** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t06⟩` | Exact Token Match | $\ge$ 2 | **2** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, t11⟩` | Exact Token Match | $\ge$ 133 | **133** | ✅ **VERIFIED** |
| `[ST]` | `⟨t10, τ⟩` | Exact Token Match | $\ge$ 115 | **250** | ✅ **VERIFIED** |
| `[ST]` | `t24` | Exact Token Match | $\ge$ 110 | **106** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t23` | Exact Token Match | $\ge$ 110 | **106** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t24, t23⟩` | Exact Token Match | $\ge$ 110 | **106** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t27, t28⟩` | Exact Token Match | $\ge$ 72 | **70** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t26, t27, t28⟩` | Exact Token Match | $\ge$ 72 | **70** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t34, t26, t27, t28⟩` | Exact Token Match | $\ge$ 72 | **42** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t34, t26, t27⟩` | Exact Token Match | $\ge$ 86 | **56** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t34, t26⟩` | Exact Token Match | $\ge$ 86 | **56** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t42⟩` | Exact Token Match | $\ge$ 184 | **179** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t39⟩` | Exact Token Match | $\ge$ 163 | **162** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t43` | Exact Token Match | $\ge$ 154 | **66** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t44⟩` | Exact Token Match | $\ge$ 154 | **66** | ⚠️ **DISCREPANCY** |
| `[ST]` | `t70` | Exact Token Match | $\ge$ 93 | **47** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t71, t70⟩` | Exact Token Match | $\ge$ 38 | **11** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨τ, t70⟩` | Exact Token Match | $\ge$ 55 | **47** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_17)]` | `[nested PAR_19]` | Exact Token Match | $\ge$ 250 | **166** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_15)]` | `[nested PAR_17]` | Exact Token Match | $\ge$ 250 | **129** | ⚠️ **DISCREPANCY** |
| `[AS (in PAR_13)]` | `[nested PAR_15]` | Exact Token Match | $\ge$ 250 | **120** | ⚠️ **DISCREPANCY** |
| `[AS]` | `[nested PAR_13]` | Exact Token Match | $\ge$ 250 | **243** | ⚠️ **DISCREPANCY** |
| `[AS]` | `[nested PAR_22]` | Exact Token Match | $\ge$ 185 | **148** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_22], t62⟩` | Exact Token Match | $\ge$ 106 | **53** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_13], [nested PAR_22], t62⟩` | Exact Token Match | $\ge$ 106 | **20** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨[nested PAR_13], [nested PAR_22]⟩` | Exact Token Match | $\ge$ 185 | **51** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨τ, [nested PAR_13], [nested PAR_22]⟩` | Exact Token Match | $\ge$ 92 | **51** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t71, t70, [nested PAR_13]⟩` | Exact Token Match | $\ge$ 38 | **1** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨τ, t70, [nested PAR_13]⟩` | Exact Token Match | $\ge$ 55 | **1** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t44, τ, [nested PAR_13]⟩` | Exact Token Match | $\ge$ 61 | **54** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t39, t43⟩` | Exact Token Match | $\ge$ 67 | **50** | ⚠️ **DISCREPANCY** |
| `[AS]` | `[nested PAR_27]` | Exact Token Match | $\ge$ 250 | **221** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t65, [nested PAR_27]⟩` | Exact Token Match | $\ge$ 134 | **25** | ⚠️ **DISCREPANCY** |
| `[ST]` | `⟨t24, t23, [nested PAR_5]⟩` | Exact Token Match | $\ge$ 24 | **0** | ❌ **GHOST PATTERN** |

## Audit Summary
- **Perfect Pattern Verifications:** 95
- **Frequency Discrepancies:** 30
- **Ghost Patterns (Fatal):** 1
- **Skipped (Complexity > 1000):** 0
- **Tree Exposure (Strict, End-to-End % of N):** 0.00%
- **Tree Exposure (Strict, Fragment-Level % of N):** 11.75%
- **Tree Exposure (Strict, Fragment-Level, >=2 activities, % of N):** 5.67%
- **Tree Exposure (Local-Strict % of N):** 100.00% ⚠️ *includes locally-known content inside opaque PAR/LOOP blocks -- can read near 100% even when End-to-End is 0%*
- **Tree Exposure (Local-Strict, >=2 activities, % of N):** 5.67%
- **Total Forced Volume (incl. unresolved AS, % of N):** 0.00%
- **AS-Resolved Volume (% of N):** 0.00%
- **AS-Resolved Volume, PAR-only (unordered co-occurrence, % of N):** 0.00%
- **AS-Resolved Volume, LOOP-only (unknown redo count, % of N):** 0.00%
- **AS-Opaque Volume (% of N):** 0.00%
- **Data Exposure (Confirmed % of Claimed Volume):** 90.31%
- **Data Exposure, ST-only (% of claimed ST volume confirmed in log):** 90.35%
- **Data Exposure, ST + ST-in-PAR (% of claimed volume confirmed in log):** 93.20%
- **Data Coverage, ST-only (% of real log explained by VERIFIED strict patterns):** 30.55%
- **Data Coverage, ST + ST-in-PAR (% of real log explained):** 85.05%
- **Data Coverage, Total (% of real log explained by any VERIFIED pattern):** 95.80%
- **Max Fractional Exposure (Worst-Case Normalized):** 2.43% (expected length: 265.85 events)
- **Avg Fractional Exposure (Typical-Case Normalized):** 24.71% (expected length: 26.12 events)
- **Mean Absolute Exposure Volume:** 4.19 events/case

---

## Nested Structures Reference
The following complex blocks were abstracted during the audit to prevent combinatorial explosion:\n
### `[nested LOOP_2]`
- **Internal Structure:** `(t05 ∗ τ)`
- **Block Frequency:** 83

- **Max Loop Iterations:** `34`
- **Max Sub-Sequence Length:** `69` steps (if one case consumes all iterations)

![nested LOOP_2 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_2.png)

### `[nested LOOP_3]`
- **Internal Structure:** `(t15 ∗ τ)`
- **Block Frequency:** 77

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_3 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_3.png)

### `[nested LOOP_4]`
- **Internal Structure:** `(t04 ∗ τ)`
- **Block Frequency:** 6

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_4 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_4.png)

### `[nested PAR_1]`
- **Internal Structure:** `{(t05 ∗ τ), [(t15 ∗ τ) │ (t04 ∗ τ)]}`
- **Block Frequency:** 83



![nested PAR_1 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_1.png)

### `[nested LOOP_6]`
- **Internal Structure:** `(t22 ∗ τ)`
- **Block Frequency:** 140

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_6 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_6.png)

### `[nested LOOP_8]`
- **Internal Structure:** `(t17 ∗ τ)`
- **Block Frequency:** 164

- **Max Loop Iterations:** `102`
- **Max Sub-Sequence Length:** `205` steps (if one case consumes all iterations)

![nested LOOP_8 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_8.png)

### `[nested LOOP_9]`
- **Internal Structure:** `(t21 ∗ τ)`
- **Block Frequency:** 164

- **Max Loop Iterations:** `109`
- **Max Sub-Sequence Length:** `219` steps (if one case consumes all iterations)

![nested LOOP_9 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_9.png)

### `[nested PAR_7]`
- **Internal Structure:** `{(t17 ∗ τ), (t21 ∗ τ)}`
- **Block Frequency:** 164



![nested PAR_7 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_7.png)

### `[nested PAR_5]`
- **Internal Structure:** `{[(t22 ∗ τ) │ τ], (t17 ∗ τ), (t21 ∗ τ)}`
- **Block Frequency:** 164



![nested PAR_5 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_5.png)

### `[nested LOOP_10]`
- **Internal Structure:** `(t42 ∗ τ)`
- **Block Frequency:** 250

- **Max Loop Iterations:** `66`
- **Max Sub-Sequence Length:** `133` steps (if one case consumes all iterations)

![nested LOOP_10 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_10.png)

### `[nested LOOP_11]`
- **Internal Structure:** `(t39 ∗ τ)`
- **Block Frequency:** 250

- **Max Loop Iterations:** `87`
- **Max Sub-Sequence Length:** `175` steps (if one case consumes all iterations)

![nested LOOP_11 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_11.png)

### `[nested LOOP_12]`
- **Internal Structure:** `(t44 ∗ τ)`
- **Block Frequency:** 154

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_12 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_12.png)

### `[nested LOOP_14]`
- **Internal Structure:** `(t36 ∗ τ)`
- **Block Frequency:** 250

- **Max Loop Iterations:** `188`
- **Max Sub-Sequence Length:** `377` steps (if one case consumes all iterations)

![nested LOOP_14 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_14.png)

### `[nested LOOP_16]`
- **Internal Structure:** `(t47 ∗ τ)`
- **Block Frequency:** 222

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_16 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_16.png)

### `[nested LOOP_18]`
- **Internal Structure:** `(t37 ∗ τ)`
- **Block Frequency:** 192

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_18 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_18.png)

### `[nested LOOP_20]`
- **Internal Structure:** `(t46 ∗ τ)`
- **Block Frequency:** 250

- **Max Loop Iterations:** `77`
- **Max Sub-Sequence Length:** `155` steps (if one case consumes all iterations)

![nested LOOP_20 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_20.png)

### `[nested LOOP_21]`
- **Internal Structure:** `(t40 ∗ τ)`
- **Block Frequency:** 229

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_21 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_21.png)

### `[nested PAR_19]`
- **Internal Structure:** `{(t46 ∗ τ), [(t40 ∗ τ) │ τ]}`
- **Block Frequency:** 250



![nested PAR_19 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_19.png)

### `[nested PAR_17]`
- **Internal Structure:** `{[(t37 ∗ τ) │ τ], (t46 ∗ τ), [(t40 ∗ τ) │ τ]}`
- **Block Frequency:** 250



![nested PAR_17 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_17.png)

### `[nested PAR_15]`
- **Internal Structure:** `{[(t47 ∗ τ) │ τ], [(t37 ∗ τ) │ τ], (t46 ∗ τ), [(t40 ∗ τ) │ τ]}`
- **Block Frequency:** 250



![nested PAR_15 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_15.png)

### `[nested PAR_13]`
- **Internal Structure:** `{(t36 ∗ τ), [(t47 ∗ τ) │ τ], [(t37 ∗ τ) │ τ], (t46 ∗ τ), [(t40 ∗ τ) │ τ]}`
- **Block Frequency:** 250



![nested PAR_13 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_13.png)

### `[nested LOOP_23]`
- **Internal Structure:** `(t48 ∗ τ)`
- **Block Frequency:** 185

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_23 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_23.png)

### `[nested LOOP_24]`
- **Internal Structure:** `(t68 ∗ τ)`
- **Block Frequency:** 185

- **Max Loop Iterations:** `0`
- **Max Sub-Sequence Length:** `1` steps (if one case consumes all iterations)

![nested LOOP_24 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_24.png)

### `[nested PAR_22]`
- **Internal Structure:** `{(t48 ∗ τ), (t68 ∗ τ)}`
- **Block Frequency:** 185



![nested PAR_22 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_22.png)

### `[nested LOOP_25]`
- **Internal Structure:** `(t62 ∗ τ)`
- **Block Frequency:** 185

- **Max Loop Iterations:** `79`
- **Max Sub-Sequence Length:** `159` steps (if one case consumes all iterations)

![nested LOOP_25 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_25.png)

### `[nested LOOP_26]`
- **Internal Structure:** `(t65 ∗ τ)`
- **Block Frequency:** 250

- **Max Loop Iterations:** `116`
- **Max Sub-Sequence Length:** `233` steps (if one case consumes all iterations)

![nested LOOP_26 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_26.png)

### `[nested LOOP_28]`
- **Internal Structure:** `(t55 ∗ τ)`
- **Block Frequency:** 250

- **Max Loop Iterations:** `215`
- **Max Sub-Sequence Length:** `431` steps (if one case consumes all iterations)

![nested LOOP_28 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_28.png)

### `[nested LOOP_29]`
- **Internal Structure:** `(t56 ∗ τ)`
- **Block Frequency:** 250

- **Max Loop Iterations:** `245`
- **Max Sub-Sequence Length:** `491` steps (if one case consumes all iterations)

![nested LOOP_29 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_LOOP_29.png)

### `[nested PAR_27]`
- **Internal Structure:** `{(t55 ∗ τ), [τ │ (t56 ∗ τ)]}`
- **Block Frequency:** 250



![nested PAR_27 Internal Diagram](images/nested_ref_audit_pdc2021_001101_nested_PAR_27.png)
