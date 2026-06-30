"""
Gathers results for the thesis's "Evaluating Synthetic Nested Structures" section
(Chapter 5): parses every audit_*.md report already generated for the synthetic
stress-test datasets (output/stress_tests/audit, output/InterleaveData/audit) and
produces one summary table, sorted by Precision, to support the claim that the
Ghost Trace phenomenon (engine-predicted patterns absent from the raw log) correlates
with PM4Py model underfitting -- i.e. that Ghost counts climb as Precision drops.

Re-run any time new synthetic datasets are audited; safe against partial batches.
"""
from pathlib import Path
import csv

from report_parsing import extract_overview_fields_from_file, extract_skipped_count, to_float

SOURCE_DIRS = [
    Path("output/stress_tests/audit"),
    Path("output/InterleaveData/audit"),
]

FIELDS = [
    "Dataset Name", "Fitness", "Precision", "Total Cases in Log", "Unique Activities",
    "XOR Operators", "LOOP Operators", "SEQ Operators", "PAR Operators",
    "Nested LOOPs", "Nested PARs",
    "Total Found Patterns", "Verified Patterns", "Discrepancy Patterns", "Ghost Patterns",
    "Tree Exposure (Strict, End-to-End % of N)", "Tree Exposure (Strict, Fragment-Level % of N)",
    "Total Forced Volume (incl. unresolved AS, % of N)", "AS-Resolved Volume (% of N)",
    "AS-Opaque Volume (% of N)", "Data Exposure (Confirmed % of Claimed Volume)",
]


def parse_report(path: Path, source: str) -> dict:
    raw = extract_overview_fields_from_file(path, FIELDS)
    row = {"Source": source, "File": raw.get("Dataset Name") or path.stem}
    for label in FIELDS[1:]:
        row[label] = to_float(raw.get(label))
    row["Skipped (Complexity > 1000)"] = extract_skipped_count(path.read_text(encoding="utf-8"))
    total = (row.get("Verified Patterns") or 0) + (row.get("Discrepancy Patterns") or 0) + (row.get("Ghost Patterns") or 0)
    row["Ghost Ratio %"] = round((row.get("Ghost Patterns") or 0) / total * 100, 2) if total > 0 else 0.0
    row["Operator Mix"] = "+".join(
        op for op, cnt in [("SEQ", row.get("SEQ Operators")), ("XOR", row.get("XOR Operators")),
                           ("PAR", row.get("PAR Operators")), ("LOOP", row.get("LOOP Operators"))]
        if cnt and cnt > 0
    ) or "none"
    return row


def main():
    rows = []
    for source_dir in SOURCE_DIRS:
        if not source_dir.exists():
            print(f"[!] Skipping missing directory: {source_dir}")
            continue
        for md_file in sorted(source_dir.glob("audit_*.md")):
            rows.append(parse_report(md_file, source_dir.parent.name))

    if not rows:
        print("No synthetic stress-test reports found yet.")
        return

    rows.sort(key=lambda r: (r["Precision"] if r["Precision"] is not None else -1))

    out_csv = Path("output/synthetic_nested_structures_summary.csv")
    fieldnames = ["Source", "File"] + FIELDS[1:] + ["Skipped (Complexity > 1000)", "Ghost Ratio %", "Operator Mix"]
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    out_md = Path("output/synthetic_nested_structures_summary.md")
    with out_md.open("w", encoding="utf-8") as f:
        f.write("# Synthetic Nested Structures: Precision vs. Ghost Trace Summary\n\n")
        f.write("Sorted by ascending PM4Py Precision, to support the underfitting/Ghost Trace "
                "correlation claim in Section 5.4. Re-run `gather_synthetic_nested_results.py` "
                "after auditing new synthetic datasets.\n\n")
        f.write("| " + " | ".join(fieldnames) + " |\n")
        f.write("| " + " | ".join(":---" for _ in fieldnames) + " |\n")
        for row in rows:
            cells = [str(row.get(h, "")) for h in fieldnames]
            f.write("| " + " | ".join(cells) + " |\n")

    print(f"Wrote {out_csv} and {out_md} ({len(rows)} reports across {len(SOURCE_DIRS)} source dirs).")
    low_precision_high_ghost = [r for r in rows if (r["Precision"] or 1) < 0.5 and r["Ghost Ratio %"] > 0]
    print(f"Files with Precision < 0.5 AND at least one Ghost Pattern: {len(low_precision_high_ghost)} / {len(rows)}")


if __name__ == "__main__":
    main()
