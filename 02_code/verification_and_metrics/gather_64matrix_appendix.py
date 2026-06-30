"""Generates the full, detailed 64-permutation appendix for Chapter 5's
"Foundational System Verification" section: for every one of the 64
structural permutations of 3-operator combinations, under all 3 frequency
bias states (Balanced/Left/Right), this produces:
  - a structural PNG diagram of the tree (one per combination, saved into
    00_tex_files/Appendix/64_matrix/images/)
  - the tree's symbolic text representation with frequencies, per bias state
  - every forced Strict Trace / Activity Set the Deterministic Engine
    extracted for that bias state, deduplicated and sorted

...and writes the whole thing out as one ready-to-include LaTeX file at
00_tex_files/Appendix/64_matrix/64_matrix.tex.

Seeded (RANDOM_SEED=42) and using the same ROOT_N=500 as
gather_foundational_verification_results.py, so this detailed appendix
stays an exact, citable companion to the summary table already referenced
in Chapter 5's prose (Table~\\ref{tab:appendix-64-matrix}) and to the
"across all 192 runs..." finding stated there.
"""
import itertools
import random
from pathlib import Path

from manual_testing.tree_generator import RandomTreeGenerator
from core.analyzer import ProcessTreeAnalyzer
from visualization.visualizer import ProcessTreeVisualizer
from visualization.formatters import get_flat_representation as _unused_flat  # noqa: F401 (kept for reference)

RANDOM_SEED = 42
ROOT_N = 500
OPERATORS = ['SEQ', 'XOR', 'PAR', 'LOOP']
BIASES = {'Balanced': 'balanced', 'Left': 'left', 'Right': 'right'}
BIAS_SHORT = {'Balanced': 'Bal', 'Left': 'Left', 'Right': 'Right'}
LEVELS = 2  # (2**LEVELS)-1 = 3 operators per tree -> 4**3 = 64 permutations

ROOT = Path(__file__).resolve().parent
APPENDIX_DIR = ROOT / "00_tex_files" / "Appendix" / "64_matrix"
IMAGE_DIR = APPENDIX_DIR / "images"
OUT_TEX = APPENDIX_DIR / "64_matrix.tex"
# Path as referenced from 00_tex_files/ (the root all \includegraphics calls in
# this project resolve against, since no \graphicspath is configured in main.tex).
IMG_REL_PREFIX = "Appendix/64_matrix/images"

OP_TEX = {'SEQ': r'\rightarrow', 'XOR': r'\times', 'PAR': r'\wedge', 'LOOP': r'\circlearrowleft'}


def tex_escape(s: str) -> str:
    return str(s).replace('\\', r'\textbackslash{}').replace('_', r'\_').replace('%', r'\%').replace('&', r'\&')


def tex_tree_string(node) -> str:
    """LaTeX-safe equivalent of formatters.get_tree_string: OP(child, child) with frequencies."""
    if node.operator == 'LEAF':
        name = str(node.name)
        if name.lower() in ('tau', 'τ', 'none', 'empty_tau'):
            return rf"$\tau$:{node.frequency}"
        return f"{tex_escape(name)}:{node.frequency}"
    op = OP_TEX.get(node.operator, node.operator)
    children = ', '.join(tex_tree_string(c) for c in node.children)
    return f"${op}$({children})"


def tex_flat_repr(node) -> str:
    """LaTeX-safe equivalent of formatters.get_flat_representation, for forced-trace strings.

    Mirrors get_flat_representation's flattening of associative same-operator
    nesting (e.g. a SEQ directly inside a SEQ): the inner block's own wrapping
    delimiters are stripped so that ``<<A, B>, <C, D>>`` collapses to the
    behaviourally identical flat ``<A, B, C, D>`` -- matching what the CLI audit
    prints, instead of echoing the raw tree nesting.
    """
    if node.operator == 'LEAF':
        name = str(node.name)
        if name.lower() in ('tau', 'τ', 'none', 'empty_tau'):
            return r'$\tau$'
        return tex_escape(name)

    SEQ_OPEN, SEQ_CLOSE = r'$\langle$', r'$\rangle$'
    child_strings = []
    for child in node.children:
        child_str = tex_flat_repr(child)
        # Flatten associative same-operator nesting, like get_flat_representation.
        if child.operator == node.operator and node.operator in ('SEQ', 'PAR', 'XOR'):
            if node.operator == 'SEQ' and child_str.startswith(SEQ_OPEN) and child_str.endswith(SEQ_CLOSE):
                child_str = child_str[len(SEQ_OPEN):-len(SEQ_CLOSE)]
            elif node.operator == 'PAR' and child_str.startswith(r'\{') and child_str.endswith(r'\}'):
                child_str = child_str[len(r'\{'):-len(r'\}')]
            elif node.operator == 'XOR' and child_str.startswith('[') and child_str.endswith(']'):
                child_str = child_str[1:-1]
        child_strings.append(child_str)

    if node.operator == 'SEQ':
        return SEQ_OPEN + ', '.join(child_strings) + SEQ_CLOSE
    if node.operator == 'PAR':
        return r'\{' + ', '.join(child_strings) + r'\}'
    if node.operator == 'XOR':
        return '[' + ' ' + r'$\mid$' + ' '.join(child_strings) + ']'
    if node.operator == 'LOOP':
        return '(' + (' ' + r'$\ast$' + ' ').join(child_strings) + ')'
    return ''


def build_blueprint(ops_iter, current_level: int, max_level: int):
    op = next(ops_iter)
    if current_level >= max_level:
        return (op, 'LEAF', 'LEAF')
    left = build_blueprint(ops_iter, current_level + 1, max_level)
    right = build_blueprint(ops_iter, current_level + 1, max_level)
    return (op, left, right)


def main():
    random.seed(RANDOM_SEED)
    generator = RandomTreeGenerator()
    analyzer = ProcessTreeAnalyzer()

    IMAGE_DIR.mkdir(parents=True, exist_ok=True)

    num_operators = (2 ** LEVELS) - 1
    permutations = list(itertools.product(OPERATORS, repeat=num_operators))
    print(f"Generating detailed appendix for {len(permutations)} permutations x {len(BIASES)} biases...")

    tex_parts = [
        r"\subsection*{Foundational System Verification: Full 64-Permutation Matrix}",
        r"\label{app:64-matrix-full}",
        "",
        (r"This appendix gives the full detail behind the summary table referenced in "
         r"Section~\ref{sec:foundational-verification} (Table~\ref{tab:appendix-64-matrix}): "
         rf"for every one of the {len(permutations)} structural permutations of 3-operator "
         r"combinations ($\{$SEQ, XOR, PAR, LOOP$\}^3$, balanced binary trees), under each of the "
         r"three frequency bias states (\textbf{Balanced}, \textbf{Left}, \textbf{Right}; "
         rf"root frequency $N={ROOT_N}$), this section lists the mined tree's structural diagram, "
         r"its symbolic text representation with frequencies, and every Strict Trace (ST) / "
         r"Activity Set (AS) the Deterministic Engine forced for that bias state. "
         r"Results are seeded (random seed 42) for exact, citable reproducibility -- the same "
         r"seed and root frequency used for the summary table. "
         r"In the tables below the three bias states are collapsed into shared "
         r"\textbf{Bal}/\textbf{Left}/\textbf{Right} columns giving the Min Freq each bias "
         r"forced for that trace; ``--'' means the trace is not forced under that bias. "
         r"Where the mined tree is identical across biases it is printed once."),
        "",
    ]

    for i, ops_tuple in enumerate(permutations, 1):
        blueprint = build_blueprint(iter(ops_tuple), current_level=1, max_level=LEVELS)
        ops_str = ", ".join(ops_tuple)
        ops_filename = "_".join(ops_tuple)

        bias_rows = []  # list of (bias_label, tree_tex, [(type, freq, trace_tex), ...])
        master_tree = None

        for bias_label, bias_value in BIASES.items():
            tree = generator.generate_from_blueprint(blueprint)
            if bias_label == 'Balanced':
                master_tree = tree
            generator.assign_frequencies(tree, total_frequency=ROOT_N, bias=bias_value)
            analyzer.compute_frequencies(tree)
            tree_tex = tex_tree_string(tree)
            forced_traces = analyzer.analyze_forced_traces(tree, ROOT_N)

            formatted = []
            for node, freq, t_type in forced_traces:
                formatted.append((t_type, freq, tex_flat_repr(node)))
            formatted.sort(key=lambda x: (0 if x[0] == "ST" else 1, -x[1], -len(x[2])))

            seen = set()
            deduped = []
            for t_type, freq, trace_tex in formatted:
                if trace_tex not in seen:
                    deduped.append((t_type, freq, trace_tex))
                    seen.add(trace_tex)
            bias_rows.append((bias_label, tree_tex, deduped))

        # One structural PNG per combination (Balanced/master tree, no frequencies shown)
        img_filename = f"tree_{i:02d}_{ops_filename}"
        visualizer = ProcessTreeVisualizer(master_tree, show_frequencies=False)
        visualizer.render(str(IMAGE_DIR / img_filename), format='png', view=False)

        # Collapse the three bias states into one table: rows are distinct
        # (type, trace) pairs in first-appearance order, with a Min-Freq column
        # per bias ("--" where that trace is not forced under that bias).
        trees = {bias_label: tree_tex for bias_label, tree_tex, _ in bias_rows}
        order = []                 # [(t_type, trace_tex), ...] first-appearance order
        freq_map = {}              # {(t_type, trace_tex): {bias_label: freq}}
        for bias_label, _tree_tex, deduped in bias_rows:
            for t_type, freq, trace_tex in deduped:
                key = (t_type, trace_tex)
                if key not in freq_map:
                    freq_map[key] = {}
                    order.append(key)
                freq_map[key][bias_label] = freq

        ops_tex = tex_escape(ops_str)
        tex_parts.append(rf"\subsubsection*{{{i}. Operators: \texttt{{{ops_tex}}}}}")
        tex_parts.append(r"\nopagebreak\vspace{2pt}")

        # trees: print once if identical across all biases, else one line per bias
        uniq = [trees.get(b, "") for b in BIASES]
        if uniq[0] and uniq.count(uniq[0]) == 3:
            trees_body = rf"\textbf{{Tree (all biases):}}\\[2pt] {uniq[0]}"
        else:
            lines = [r"\textbf{Trees:}"]
            for b in BIASES:
                lines.append(rf"\textbf{{{BIAS_SHORT[b]}}}\, {trees.get(b, '')}")
            trees_body = r"\\[2pt] ".join(lines)

        # diagram left (captioned -> List of Figures), trees right
        tex_parts.append(r"\noindent")
        tex_parts.append(r"\begin{minipage}[t]{0.34\textwidth}")
        # \vspace{0pt} pins the [t] reference baseline to the top of the minipage;
        # without it a lone tall image baselines at its bottom, dragging the
        # right-hand trees text down to image-bottom level.
        tex_parts.append(r"\vspace{0pt}")
        tex_parts.append(r"\centering")
        tex_parts.append(r"\captionsetup{font=footnotesize}")
        tex_parts.append(rf"\includegraphics[width=\linewidth]{{{IMG_REL_PREFIX}/{img_filename}.png}}")
        tex_parts.append(rf"\captionof{{figure}}[Permutation {i}: \texttt{{{ops_tex}}}]{{Mined process tree for permutation {i} (\texttt{{{ops_tex}}}).}}")
        tex_parts.append(rf"\label{{fig:app64-{i:02d}}}")
        tex_parts.append(r"\end{minipage}\hfill")
        tex_parts.append(r"\begin{minipage}[t]{0.62\textwidth}")
        tex_parts.append(r"\vspace{0pt}")
        tex_parts.append(rf"{{\footnotesize\raggedright {trees_body}\par}}")
        tex_parts.append(r"\end{minipage}")
        tex_parts.append(r"\par\vspace{6pt}")

        # table (captioned -> List of Tables)
        tex_parts.append(rf"\captionof{{table}}[Permutation {i} forced traces: \texttt{{{ops_tex}}}]{{Forced traces and atomic blocks for permutation {i} (\texttt{{{ops_tex}}}) under each bias state.}}")
        tex_parts.append(rf"\label{{tab:app64-{i:02d}}}")
        tex_parts.append(r"\nopagebreak")
        tex_parts.append(r"\begin{center}\footnotesize")
        tex_parts.append(r"\begin{tabular}{l p{7.6cm} ccc}")
        tex_parts.append(r"\toprule")
        tex_parts.append(r"\textbf{Type} & \textbf{Forced Trace / Atomic Block} & \textbf{Bal} & \textbf{Left} & \textbf{Right} \\")
        tex_parts.append(r"\midrule")
        if not order:
            tex_parts.append(r"\multicolumn{5}{c}{\textit{No traces forced}} \\")
        for t_type, trace_tex in order:
            cells = [freq_map[(t_type, trace_tex)].get(b, "--") for b in BIASES]
            # Brace the Type cell so a leading "[" is not parsed as \\[len] / \midrule[len].
            tex_parts.append(rf"{{[{tex_escape(t_type)}]}} & {trace_tex} & {cells[0]} & {cells[1]} & {cells[2]} \\")

        tex_parts.append(r"\bottomrule")
        tex_parts.append(r"\end{tabular}")
        tex_parts.append(r"\end{center}")
        tex_parts.append("")

        if i % 8 == 0:
            print(f"  ... {i}/{len(permutations)} combinations done")

    OUT_TEX.write_text("\n".join(tex_parts), encoding="utf-8")

    # graphviz's .render() leaves the intermediate DOT source file behind
    # alongside each .png; clean those up so the subfolder holds only images.
    for leftover in IMAGE_DIR.iterdir():
        if leftover.suffix != ".png":
            leftover.unlink()

    print(f"\nWrote {OUT_TEX} ({len(permutations)} combinations, {len(permutations)} PNGs in {IMAGE_DIR})")


if __name__ == "__main__":
    main()
