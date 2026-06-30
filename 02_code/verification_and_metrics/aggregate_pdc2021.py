"""
Aggregates the per-file audit_*.md reports under output/BPIC2021_Verification
(Training_Logs / Test_Logs / Ground_Truth_Logs, each split by noise_<level>)
into one summary table per (subfolder, noise level).

Safe to re-run while auto_verifier_v2.py's BPIC2021 sweep is still writing
new reports -- it just reflects whatever has been completed so far, and
prints a per-group file count so partial groups are visible in the table.
"""
from pathlib import Path
import csv

from report_parsing import extract_overview_fields_from_file, to_float, extract_skipped_count

ROOT = Path("output/BPIC2021_Verification")

OVERVIEW_FIELDS = {
    "Fitness": "Fitness",
    "Precision": "Precision",
    "Total Cases in Log": "Total Cases",
    "Total Found Patterns": "Total Found Patterns",
    "Verified Patterns": "Verified",
    "Discrepancy Patterns": "Discrepancy",
    "Ghost Patterns": "Ghost",
    "Binarization Additions": "Binarization Additions",
    "Tau Operators Added": "Tau Operators Added",
    "Tree Exposure (Model-Forced % of N)": "Tree Exposure %",
    "Data Exposure (Confirmed % of Claimed Volume)": "Data Exposure %",
}


def parse_report(path: Path) -> dict:
    raw = extract_overview_fields_from_file(path, OVERVIEW_FIELDS.keys())
    row = {}
    for raw_label, key in OVERVIEW_FIELDS.items():
        value = raw.get(raw_label)
        if value is None:
            continue
        row[key] = to_float(value)
    row["Skipped"] = extract_skipped_count(path.read_text(encoding="utf-8"))
    return row


def main():
    groups = {}  # (subfolder, noise) -> list of row dicts

    for subfolder_dir in sorted(ROOT.iterdir()):
        if not subfolder_dir.is_dir() or subfolder_dir.name == "aggregate_summary":
            continue
        for noise_dir in sorted(subfolder_dir.glob("noise_*")):
            noise = noise_dir.name.replace("noise_", "")
            rows = []
            for md_file in sorted(noise_dir.glob("audit_*.md")):
                rows.append(parse_report(md_file))
            if rows:
                groups[(subfolder_dir.name, noise)] = rows

    summary_rows = []
    for (subfolder, noise), rows in sorted(groups.items()):
        n = len(rows)

        def avg(key):
            vals = [r[key] for r in rows if r.get(key) is not None]
            return sum(vals) / len(vals) if vals else float("nan")

        def total(key):
            return sum(r.get(key, 0.0) or 0.0 for r in rows)

        summary_rows.append({
            "Subfolder": subfolder,
            "Noise": noise,
            "Files": n,
            "Avg Fitness": avg("Fitness"),
            "Avg Precision": avg("Precision"),
            "Total Cases": total("Total Cases"),
            "Total Found Patterns": total("Total Found Patterns"),
            "Verified": total("Verified"),
            "Discrepancy": total("Discrepancy"),
            "Ghost": total("Ghost"),
            "Skipped": total("Skipped"),
            "Binarization Additions": total("Binarization Additions"),
            "Tau Operators Added": total("Tau Operators Added"),
            "Avg Tree Exposure %": avg("Tree Exposure %"),
            "Avg Data Exposure %": avg("Data Exposure %"),
        })

    out_dir = ROOT
    out_dir.mkdir(parents=True, exist_ok=True)

    csv_path = out_dir / "aggregate_summary.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(summary_rows[0].keys()) if summary_rows else [])
        writer.writeheader()
        for row in summary_rows:
            writer.writerow(row)

    md_path = out_dir / "aggregate_summary.md"
    with md_path.open("w", encoding="utf-8") as f:
        f.write("# PDC2021 Aggregate Verification Summary\n\n")
        f.write("Generated from all `audit_*.md` reports currently present under "
                "`output/BPIC2021_Verification/`. Re-run `aggregate_pdc2021.py` "
                "after the verifier sweep finishes (or progresses further) to refresh.\n\n")
        if not summary_rows:
            f.write("_No reports found yet._\n")
        else:
            headers = list(summary_rows[0].keys())
            f.write("| " + " | ".join(headers) + " |\n")
            f.write("| " + " | ".join(":---" for _ in headers) + " |\n")
            for row in summary_rows:
                cells = []
                for h in headers:
                    v = row[h]
                    if isinstance(v, float):
                        cells.append(f"{v:.4f}" if "Avg" in h or "%" in h else f"{v:.0f}")
                    else:
                        cells.append(str(v))
                f.write("| " + " | ".join(cells) + " |\n")

    print(f"Wrote {csv_path} and {md_path} ({len(summary_rows)} groups, "
          f"{sum(len(r) for r in groups.values())} reports total).")


if __name__ == "__main__":
    main()
