**An Analytical Approach to Control-flow Reconstruction Attacks on Business Process Models**

---

## Folder layout

```

├── 02_code/                          ← source code
│   ├── deterministic_engine/           the analytical core (the "engine")
│   │   ├── core/                       tree_node, data_assimilation,
│   │   │                               analyzer, batch_processor
│   │   ├── visualization/              formatters, visualizer, report_builder
│   │   ├── preProcessing/              log → letter-CSV / model prep
│   │   ├── manual_testing/             synthetic test-log generators
│   │   ├── main.py, interleaver.py
│   ├── verification_and_metrics/       auto_verifier_v2.py + exposure / KPI /
|
├── 03_data/                          ← curated evaluation data (see "Data" below)
│   ├── synthetic_stress_corpus/        29 hand-built test_*.csv structures
│   ├── bpic2021_pdc_sample/            the sampled PDC2021 .xes logs
│   │   ├── ground_truth/  test/  training/
│   ├── sepsis/                         Sepsis_Cases_decompressed.xes
│   └── bpic2017/README_BPIC2017.md     pointer to the 7 large BPIC2017 logs
│                                       (omitted for size; see file)
└── 04_results_and_calculations/      ← the numbers behind the thesis
    ├── databasis_eval_master.csv       master KPI table: 244 files × 6 noise
    │                                   levels = 1 464 rows (every Chapter 5 number)
    ├── COLUMN_REFERENCE.txt            plain-language definition of every column
    ├── output_summaries/               64-permutation, synthetic-nested,
    │                                   noise-sweep, operator-correlation,
    │                                   atomic-fallback, tree-exposure, bug notes
    └── sample_audit_reports/           the engine's own audit reports
        ├── synthetic_stress_audits/    one per stress-corpus file
        └── pdc2021_reports_quoted/     reports quoted in Ch. 5 / 6 / appendix
```

---

## Data: what the curated subset is

The thesis does **not** run on the full multi-gigabyte BPIC archives. It runs on
a fixed, reproducible 244-file evaluation corpus (RNG seed = 42), audited at six
noise thresholds (0.0–1.0) each → 1 464 rows in `databasis_eval_master.csv`.
(Note: the bundled `COLUMN_REFERENCE.txt` header still describes an earlier
111-file / 666-row pilot; the column definitions remain accurate, only the
corpus has since grown to the counts below.)

| corpus                | files | bundled here?                                   |
|-----------------------|-------|-------------------------------------------------|
| synthetic stress      | 29    | yes — `03_data/synthetic_stress_corpus/`        |
| BPIC2021 ground truth | 69*   | yes — `03_data/bpic2021_pdc_sample/ground_truth`|
| BPIC2021 test         | 69*   | yes — `03_data/bpic2021_pdc_sample/test`        |
| BPIC2021 training     | 69*   | yes — `03_data/bpic2021_pdc_sample/training`    |
| BPIC2017 (7 variants) | 7     | **no** — too large (~1.8 GB); see bpic2017 note |
| Sepsis (break-the-RAM)| 1     | yes — `03_data/sepsis/`                         |

\* the BPIC2021 files actually named in the master table were copied verbatim
from the working `data/BPIC2021/` tree. Public source for the raw archives:
BPI Challenge logs on 4TU.ResearchData. Even where a raw log is not bundled,
its full per-noise results are present in `databasis_eval_master.csv`.

---

## Running the engine

The engine targets Python 3 with the process-mining stack:

```
pip install pm4py pandas numpy matplotlib seaborn
```

Entry points: `02_code/deterministic_engine/main.py` (single run) and
`core/batch_processor.py` (corpus runs); verification/KPI extraction via
`02_code/verification_and_metrics/auto_verifier_v2.py`. The attack baseline in
`02_code/attack_baseline_CFR/` pins exact versions in its own `requirements.txt`.

Excluded from the upload (size / not thesis artifacts): full raw BPIC archives,
virtual environments, `__pycache__`, raw run logs, and the cited third-party
paper PDFs (all works are cited in `references.bib`).
