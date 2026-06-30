"""
Builds one big combined table across all 8 completed Training_Logs noise-level batches:
the existing Dataset & Audit Overview fields (parsed from each audit_*.md report --
Fitness, Precision, operator counts, Tree/Data Exposure, etc.) plus the three fractional
exposure variants (Max/Avg/Mean), recalculated fresh per file/noise-level pair.

The fractional variants cannot be derived from the rendered .md text alone -- they need
the full process tree object with per-node frequencies and the engine's internal
Full/Prefix/Suffix state buckets, neither of which is fully serialized into the report.
They must be recomputed from the original .xes input files.

To avoid repeating the original verifier's slowest step, this script builds the tree
with DataAssimilation.assimilate_from_file(..., compute_metrics=False), which skips
PM4Py's Fitness/Precision token-based replay (the `replaying log with TBR` step that
made the original 224-file/noise-level batches take 15h down to ~1h each). This same
toggle is also wired into auto_verifier_v2.LogTraceVerifier(compute_fitness_precision=
False) for future full-audit runs. Fitness and Precision are instead read back from the
existing, already-computed report text here -- no information is lost, the expensive
replay is just not redone.
"""
import sys
from pathlib import Path
import csv

sys.path.insert(0, str(Path(__file__).parent))
from core.data_assimilation import DataAssimilation
from core.analyzer import ProcessTreeAnalyzer
from report_parsing import extract_overview_fields_from_file
from fractional_exposure import (
    expected_length_max, expected_length_avg, fractional_exposure,
    absolute_exposure_volume,
)

TRAINING_DIR = Path("data/BPIC2021/Training Logs")
REPORT_ROOT = Path("output/BPIC2021_Verification/Training_Logs")
NOISE_LEVELS = ["0.0", "0.1", "0.2", "0.4", "0.5", "0.6", "0.8", "1.0"]

OVERVIEW_FIELDS = [
    "Dataset Name", "Noise Threshold", "Fitness", "Precision", "Total Cases in Log",
    "Unique Activities", "XOR Operators", "LOOP Operators", "SEQ Operators", "PAR Operators",
    "Binarization Additions", "Tau Operators Added", "Total Found Patterns",
    "Verified Patterns", "Discrepancy Patterns", "Ghost Patterns", "Nested LOOPs", "Nested PARs",
    "Tree Exposure (Model-Forced % of N)", "Data Exposure (Confirmed % of Claimed Volume)",
]


def parse_overview(md_path: Path) -> dict:
    return extract_overview_fields_from_file(md_path, OVERVIEW_FIELDS)


def analyze_one(file_path: Path, noise_threshold: float, md_path: Path) -> dict:
    overview = parse_overview(md_path)

    analyzer = ProcessTreeAnalyzer(max_traces_per_node=10000)
    root_tree = DataAssimilation.assimilate_from_file(
        str(file_path), analyzer, noise_threshold=noise_threshold, compute_metrics=False,
    )
    analyzer.nested_blocks_registry.clear()
    analyzer._block_counter = 0
    analyzer._block_id_cache = {}
    final_state = analyzer._analyze_recursive(root_tree, root_tree.frequency)
    registry = analyzer.nested_blocks_registry

    root_n = root_tree.frequency
    tree_exposure_recalc = (sum(f for _, f, _ in final_state["full"]) / root_n * 100) if root_n > 0 else 0.0

    max_len = expected_length_max(root_tree, registry)
    avg_len = expected_length_avg(root_tree, registry)
    max_res = fractional_exposure(root_tree, final_state, registry, max_len, include_residual=True)
    avg_res = fractional_exposure(root_tree, final_state, registry, avg_len, include_residual=True)
    mean_res = absolute_exposure_volume(root_tree, final_state, registry)

    row = {"file": file_path.name, "noise_level": noise_threshold, "N": root_n}
    row.update({k.replace(" ", "_").replace("(", "").replace(")", "").replace("%", "pct").replace("/", "_").replace(".", ""): v
                for k, v in overview.items()})
    row["TreeExposure_recalculated"] = round(tree_exposure_recalc, 4)
    row["Max_fractional_pct"] = round(max_res["fractional_pct"], 4)
    row["Max_expected_len"] = round(max_res["expected_len"], 4)
    row["Avg_fractional_pct"] = round(avg_res["fractional_pct"], 4)
    row["Avg_expected_len"] = round(avg_res["expected_len"], 4)
    row["Mean_events_per_case"] = round(mean_res["events_per_case"], 4)
    return row


def main(limit_per_noise: int = None):
    all_rows = []
    fieldnames = None

    for noise in NOISE_LEVELS:
        noise_dir = REPORT_ROOT / f"noise_{noise}"
        md_files = sorted(noise_dir.glob("audit_*.md"))
        if limit_per_noise:
            md_files = md_files[:limit_per_noise]

        print(f"\n=== noise={noise}: {len(md_files)} files ===")
        for i, md_path in enumerate(md_files, 1):
            stem = md_path.stem.replace("audit_", "")
            xes_path = TRAINING_DIR / f"{stem}.xes"
            if not xes_path.exists():
                print(f"  [!] Missing input file for {md_path.name}, skipping")
                continue
            try:
                row = analyze_one(xes_path, float(noise), md_path)
                all_rows.append(row)
                if fieldnames is None:
                    fieldnames = list(row.keys())
                if i % 25 == 0 or i == len(md_files):
                    print(f"  [{i}/{len(md_files)}] {md_path.name} done")
            except Exception as e:
                print(f"  [!] FAILED on {md_path.name} (noise={noise}): {e}")

    out_csv = Path("output/BPIC2021_Verification/big_table_all_noise_levels.csv")
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in all_rows:
            writer.writerow(row)

    print(f"\nWrote {len(all_rows)} rows -> {out_csv}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit-per-noise", type=int, default=None)
    args = parser.parse_args()
    main(limit_per_noise=args.limit_per_noise)
