# Thesis Upload Package

**An Analytical Approach to Control-flow Reconstruction Attacks on Business Process Models**
Melanie Maria Zumtobel — University of Liechtenstein, Information Systems

This package bundles the thesis together with every accompanying artifact the
thesis refers to: the source code, the curated data the evaluation runs on, and
the calculation/result documents behind the reported numbers, figures, and
appendices.

---

## Folder layout

```
upload/
├── README.md                         ← this file (manifest + provenance)
├── 01_thesis/                        ← the thesis document
│   ├── NOTE_compiled_pdf.md            status of the compiled PDF (read me)
│   └── latex_source/                   full, self-contained LaTeX source
│       ├── main.tex, unili.cls, references.bib, frontpage.tex
│       ├── sections/                   all chapters (0-abstract … 9-appendix)
│       ├── images/                     figures used in the thesis
│       └── Appendix/                   appendix text + each experiment's
│                                       own scripts & data (see mapping below)
├── 02_code/                          ← source code
│   ├── deterministic_engine/           the analytical core (the "engine")
│   │   ├── core/                       tree_node, data_assimilation,
│   │   │                               analyzer, batch_processor
│   │   ├── visualization/              formatters, visualizer, report_builder
│   │   ├── preProcessing/              log → letter-CSV / model prep
│   │   ├── manual_testing/             synthetic test-log generators
│   │   ├── main.py, interleaver.py
│   ├── verification_and_metrics/       auto_verifier_v2.py + exposure / KPI /
│   │                                   correlation / gather scripts
│   └── attack_baseline_CFR/            Lahann/Pfeiffer Control-Flow
│                                       Reconstruction reference implementation
│                                       (the stochastic baseline compared against)
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

## Where each thesis artifact comes from

| Thesis reference | Artifact in this package |
|---|---|
| Worked example `test_01_seq_par.csv` (Ch. 4 / audit-examples appendix) | `03_data/synthetic_stress_corpus/test_01_seq_par.csv`; report in `04_.../sample_audit_reports/synthetic_stress_audits/audit_test_01_seq_par.md` |
| LOOP+PAR worked example `test_27_par_loop_noxor.csv` (Ch. 5) | same data folder; audit in synthetic_stress_audits |
| 64-permutation matrix (appendix `64_matrix`) | `04_.../output_summaries/foundational_verification_64_permutations.{csv,md}`; figures in `latex_source/images/appendix/64_matrix`; generator `gather_64matrix_appendix.py` (02_code) |
| Synthetic nested structures table | `04_.../output_summaries/synthetic_nested_structures_summary.{csv,md}`; generator `gather_synthetic_nested_results.py` |
| Exposure-vs-coverage toy figure (`pdc2021_0000101.xes`, Ch. 5 noise) | data in bpic2021_pdc_sample/training; reports `pdc2021_reports_quoted/audit_pdc2021_0000101*`; figure source `output/_make_exposure_vs_coverage_toy_figure.py` (in latex_source build inputs) |
| Zero-noise audit excerpt `audit_pdc2021_110101__noise0.0.md` (Ch. 6) | `04_.../sample_audit_reports/pdc2021_reports_quoted/` |
| Operator-vulnerability correlations (appendix `operator_vuln`) | data CSVs in `latex_source/Appendix/operator_vuln/`; `_operator_correlation.csv` + noise-sweep CSVs in output_summaries |
| Noise-filtering paradox (appendix `noise_filtering`) | scripts + data in `latex_source/Appendix/noise_filtering/` |
| k-anonymity sweep (appendix `k_anon`) | `_kanon_sweep_{full,summary}.csv` in `latex_source/Appendix/k_anon/` |
| Break-the-RAM scaling (appendix `break_the_ram`) | scripts + progress/RSS CSVs in `latex_source/Appendix/break_the_ram/` |
| Stochastic-vs-deterministic comparison (appendix `stoch_vs_det`) | scripts + per-strategy match reports in `latex_source/Appendix/stoch_vs_det/`; baseline code in `02_code/attack_baseline_CFR/` |
| All Chapter 5 KPI definitions & values | `04_.../databasis_eval_master.csv` + `COLUMN_REFERENCE.txt` |

> Each appendix experiment keeps its own scripts and data next to its `.tex`
> under `latex_source/Appendix/<experiment>/`, so every appendix is
> self-contained and reproducible in place.

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
