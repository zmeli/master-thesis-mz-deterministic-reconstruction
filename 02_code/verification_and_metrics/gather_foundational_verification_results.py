"""
Gathers results for the thesis's "Foundational System Verification" section
(Chapter 5): generates all 64 structural permutations of 3-operator combinations
({SEQ,XOR,PAR,LOOP}^3, balanced binary trees) across the 3 frequency bias states
(Balanced/Left/Right) used by manual_testing.documenter.PermutationDocumenter, and
classifies the Deterministic Engine's output for each into Strict Trace (ST) /
Activity Set (AS) / Error outcomes -- directly producing the appendix table the
thesis text currently flags as "[APPENDIX REF: Insert reference to a table...]".

Reuses the same tree-generation logic as PermutationDocumenter, but skips the
markdown-diagram rendering (ReportBuilder) entirely, since only the classification
counts -- not the rendered tree images -- are needed for this summary table.

Seeded (RANDOM_SEED below) for reproducibility: RandomTreeGenerator.assign_frequencies
draws its left/right split and loop redo-count via unseeded random.randint() calls, so
re-running this script without a fixed seed reshuffles the exact frequencies drawn each
time. Confirmed in practice: across two unseeded runs, the qualitative ST-only-vs-Mixed
classification was stable for every combination except one (XOR_SEQ_LOOP, Right bias),
which occasionally drew a zero-repeat frequency for its LOOP node -- a degenerate loop
whose redo branch never fires, which correctly produces no Activity Set per the engine's
own documented behavior (Section 4.5.2, "Scope of the Opaque Encapsulation"). Seeding
makes the appendix table below an exact, citable snapshot rather than one example among
several equally valid ones.
"""
import itertools
import random
from pathlib import Path
import csv

from manual_testing.tree_generator import RandomTreeGenerator
from core.analyzer import ProcessTreeAnalyzer

RANDOM_SEED = 42

OPERATORS = ['SEQ', 'XOR', 'PAR', 'LOOP']
BIASES = {'Balanced': 'balanced', 'Left': 'left', 'Right': 'right'}
ROOT_N = 500
LEVELS = 2  # (2**LEVELS)-1 = 3 operators per tree -> 4**3 = 64 permutations


def build_blueprint(ops_iter, current_level: int, max_level: int):
    op = next(ops_iter)
    if current_level >= max_level:
        return (op, 'LEAF', 'LEAF')
    left = build_blueprint(ops_iter, current_level + 1, max_level)
    right = build_blueprint(ops_iter, current_level + 1, max_level)
    return (op, left, right)


def classify(traces) -> dict:
    st_count = sum(1 for _, _, t in traces if t.startswith("ST"))
    as_count = sum(1 for _, _, t in traces if t.startswith("AS"))
    if st_count and as_count:
        outcome = "Mixed (ST+AS)"
    elif st_count:
        outcome = "ST only"
    elif as_count:
        outcome = "AS only"
    else:
        outcome = "No patterns"
    return {"ST_count": st_count, "AS_count": as_count, "Outcome": outcome}


def main():
    random.seed(RANDOM_SEED)
    generator = RandomTreeGenerator()
    analyzer = ProcessTreeAnalyzer()

    num_operators = (2 ** LEVELS) - 1
    permutations = list(itertools.product(OPERATORS, repeat=num_operators))
    print(f"Testing {len(permutations)} operator permutations x {len(BIASES)} bias states "
          f"= {len(permutations) * len(BIASES)} runs...")

    rows = []
    for ops_tuple in permutations:
        blueprint = build_blueprint(iter(ops_tuple), current_level=1, max_level=LEVELS)
        for bias_label, bias_value in BIASES.items():
            row = {"Operators": "_".join(ops_tuple), "Bias": bias_label}
            try:
                tree = generator.generate_from_blueprint(blueprint)
                generator.assign_frequencies(tree, total_frequency=ROOT_N, bias=bias_value)
                analyzer.compute_frequencies(tree)
                traces = analyzer.analyze_forced_traces(tree, ROOT_N)
                row.update(classify(traces))
                row["Error"] = ""
            except Exception as e:
                row.update({"ST_count": 0, "AS_count": 0, "Outcome": "ERROR", "Error": str(e)})
            rows.append(row)

    out_csv = Path("output/foundational_verification_64_permutations.csv")
    fieldnames = ["Operators", "Bias", "ST_count", "AS_count", "Outcome", "Error"]
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    # Per-operator-combination summary (collapsing the 3 bias states into one outcome set)
    by_combo = {}
    for row in rows:
        by_combo.setdefault(row["Operators"], []).append(row)

    out_md = Path("output/foundational_verification_64_permutations.md")
    with out_md.open("w", encoding="utf-8") as f:
        f.write("# Foundational System Verification: 64-Permutation Matrix\n\n")
        f.write(f"All {len(permutations)} structural permutations of 3-operator combinations "
                f"({'/'.join(OPERATORS)}), each tested under Balanced/Left/Right frequency bias "
                f"(N={ROOT_N}). Supports the appendix table referenced in Section 5.3 "
                "(Foundational System Verification).\n\n")
        f.write("| Operators | Balanced | Left | Right | Any Errors? |\n")
        f.write("| :--- | :--- | :--- | :--- | :--- |\n")
        for combo, combo_rows in sorted(by_combo.items()):
            outcomes = {r["Bias"]: r["Outcome"] for r in combo_rows}
            any_error = "Yes" if any(r["Outcome"] == "ERROR" for r in combo_rows) else "No"
            f.write(f"| `{combo}` | {outcomes.get('Balanced','-')} | {outcomes.get('Left','-')} | "
                    f"{outcomes.get('Right','-')} | {any_error} |\n")

    error_count = sum(1 for r in rows if r["Outcome"] == "ERROR")
    print(f"Wrote {out_csv} and {out_md} ({len(rows)} runs, {error_count} errors).")
    outcome_totals = {}
    for r in rows:
        outcome_totals[r["Outcome"]] = outcome_totals.get(r["Outcome"], 0) + 1
    print("Outcome distribution across all runs:", outcome_totals)


if __name__ == "__main__":
    main()
