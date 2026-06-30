"""
Tests whether deterministic reconstruction efficacy (Tree Exposure / Data Exposure)
is statistically linked to a model's control-flow operator distribution (SEQ/XOR/PAR/LOOP).

Scans every audit_*.md report under output/BPIC2021_Verification (currently the only
report set produced in the new format that carries both the per-operator counts and the
Tree/Data Exposure KPIs -- see Section 5.2 of the thesis). Safe to re-run while the live
verifier sweep is still writing new reports.

Produces:
  - output/BPIC2021_Verification/operator_exposure_correlation.csv  (per-file raw data)
  - output/BPIC2021_Verification/operator_exposure_summary.md       (correlations + per-dominant-operator table)
  - output/BPIC2021_Verification/operator_exposure_bar.png          (bar chart: mean exposure by dominant operator)
"""
from pathlib import Path
import csv

import numpy as np
from scipy.stats import pearsonr
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from report_parsing import extract_overview_fields_from_file, to_float

ROOT = Path("output/BPIC2021_Verification")

FIELDS = {
    "SEQ Operators": "SEQ",
    "XOR Operators": "XOR",
    "PAR Operators": "PAR",
    "LOOP Operators": "LOOP",
    "Tree Exposure (Model-Forced % of N)": "TreeExposure",
    "Data Exposure (Confirmed % of Claimed Volume)": "DataExposure",
}


def parse_report(path: Path) -> dict | None:
    raw = extract_overview_fields_from_file(path, FIELDS.keys())
    row = {}
    for raw_label, key in FIELDS.items():
        parsed = to_float(raw.get(raw_label))
        if parsed is None:
            return None  # missing or unparseable field voids the whole row
        row[key] = parsed
    return row


def main():
    rows = []
    for md_file in ROOT.rglob("audit_*.md"):
        row = parse_report(md_file)
        if row is None:
            continue
        total_ops = row["SEQ"] + row["XOR"] + row["PAR"] + row["LOOP"]
        if total_ops == 0:
            continue
        row["SEQ_ratio"] = row["SEQ"] / total_ops
        row["XOR_ratio"] = row["XOR"] / total_ops
        row["PAR_ratio"] = row["PAR"] / total_ops
        row["LOOP_ratio"] = row["LOOP"] / total_ops
        row["dominant"] = max(("SEQ", "XOR", "PAR", "LOOP"), key=lambda k: row[k])
        row["file"] = md_file.name
        rows.append(row)

    if not rows:
        print("No matching reports found yet.")
        return

    csv_path = ROOT / "operator_exposure_correlation.csv"
    fieldnames = ["file", "SEQ", "XOR", "PAR", "LOOP", "SEQ_ratio", "XOR_ratio",
                  "PAR_ratio", "LOOP_ratio", "dominant", "TreeExposure", "DataExposure"]
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    # --- Correlations: operator ratio vs. each exposure metric ---
    correlations = []
    for op in ["SEQ", "XOR", "PAR", "LOOP"]:
        ratios = np.array([r[f"{op}_ratio"] for r in rows])
        for metric in ["TreeExposure", "DataExposure"]:
            values = np.array([r[metric] for r in rows])
            if np.std(ratios) == 0 or np.std(values) == 0:
                r_val, p_val = float("nan"), float("nan")
            else:
                r_val, p_val = pearsonr(ratios, values)
            correlations.append((op, metric, r_val, p_val))

    # --- Mean exposure grouped by dominant operator ---
    dominant_groups = {}
    for row in rows:
        dominant_groups.setdefault(row["dominant"], []).append(row)

    group_stats = {}
    for op, group in dominant_groups.items():
        tree_vals = np.array([r["TreeExposure"] for r in group])
        data_vals = np.array([r["DataExposure"] for r in group])
        group_stats[op] = {
            "n": len(group),
            "tree_mean": tree_vals.mean(), "tree_std": tree_vals.std(),
            "data_mean": data_vals.mean(), "data_std": data_vals.std(),
        }

    # --- Write summary markdown ---
    md_path = ROOT / "operator_exposure_summary.md"
    with md_path.open("w", encoding="utf-8") as f:
        f.write("# Operator Distribution vs. Exposure: Correlation Analysis\n\n")
        f.write(f"Computed over {len(rows)} audit reports under `output/BPIC2021_Verification/`. "
                "Re-run `operator_exposure_analysis.py` after the verifier sweep progresses further.\n\n")

        f.write("## Pearson correlation: operator share vs. exposure KPI\n\n")
        f.write("| Operator | Metric | r | p-value |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")
        for op, metric, r_val, p_val in correlations:
            f.write(f"| {op} | {metric} | {r_val:.4f} | {p_val:.4g} |\n")

        f.write("\n## Mean exposure by dominant operator type\n\n")
        f.write("| Dominant Operator | N | Mean Tree Exposure % | Mean Data Exposure % |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")
        for op in ["SEQ", "XOR", "PAR", "LOOP"]:
            if op not in group_stats:
                continue
            s = group_stats[op]
            f.write(f"| {op} | {s['n']} | {s['tree_mean']:.2f} ± {s['tree_std']:.2f} | "
                    f"{s['data_mean']:.2f} ± {s['data_std']:.2f} |\n")

    # --- Bar chart: mean Tree/Data Exposure by dominant operator ---
    ops_present = [op for op in ["SEQ", "XOR", "PAR", "LOOP"] if op in group_stats]
    x = np.arange(len(ops_present))
    width = 0.35

    fig, ax = plt.subplots(figsize=(7, 5))
    tree_means = [group_stats[op]["tree_mean"] for op in ops_present]
    tree_stds = [group_stats[op]["tree_std"] for op in ops_present]
    data_means = [group_stats[op]["data_mean"] for op in ops_present]
    data_stds = [group_stats[op]["data_std"] for op in ops_present]

    ax.bar(x - width / 2, tree_means, width, yerr=tree_stds, label="Tree Exposure %", capsize=4)
    ax.bar(x + width / 2, data_means, width, yerr=data_stds, label="Data Exposure %", capsize=4)
    ax.set_xticks(x)
    ax.set_xticklabels([f"{op}\n(n={group_stats[op]['n']})" for op in ops_present])
    ax.set_ylabel("Exposure %")
    ax.set_title("Mean Exposure by Dominant Control-Flow Operator")
    ax.legend()
    fig.tight_layout()
    fig.savefig(ROOT / "operator_exposure_bar.png", dpi=150)

    print(f"Analyzed {len(rows)} reports. Wrote {csv_path}, {md_path}, and operator_exposure_bar.png.")


if __name__ == "__main__":
    main()
