import os
import itertools
import random
from manual_testing.tree_generator import RandomTreeGenerator
from core.analyzer import ProcessTreeAnalyzer
from visualization.report_builder import ReportBuilder
from visualization.formatters import get_tree_string

class PermutationDocumenter:
    """
    Automates the stress-testing of operator permutations and biases dynamically.
    Generates a highly compact, exact-match Markdown report.
    """
    def __init__(self):
        self.generator = RandomTreeGenerator()
        self.analyzer = ProcessTreeAnalyzer()
        self.operators = ['SEQ', 'XOR', 'PAR', 'LOOP']
        
        self.biases = {'Balanced': 'balanced', 'Left': 'left', 'Right': 'right'}

    def _build_blueprint_recursive(self, ops_iterator, current_level: int, max_level: int):
        """
        Build a nested blueprint tuple by consuming operators from an iterator.

        Draws the next operator for this level and, until ``max_level`` is
        reached, recurses to build a left and right subtree; at the deepest level
        the operator's children are both ``'LEAF'``.

        Args:
            ops_iterator: Iterator yielding operator names in pre-order.
            current_level: Depth of the node currently being built (1-based).
            max_level: Maximum depth before children become leaves.

        Returns:
            A nested ``(op, left, right)`` blueprint tuple.
        """
        op = next(ops_iterator)
        if current_level >= max_level:
            return (op, 'LEAF', 'LEAF')
        
        left = self._build_blueprint_recursive(ops_iterator, current_level + 1, max_level)
        right = self._build_blueprint_recursive(ops_iterator, current_level + 1, max_level)
        return (op, left, right)

    def generate_markdown_report(
        self, levels: int = 2, filepath: str = None, image_dir: str = None, 
        root_n: int = 500, max_sample: int = 64
    ):
        """
        Generate a Markdown report over operator permutations of a fixed depth.

        Enumerates every operator combination for a tree of ``levels`` levels
        (optionally down-sampling to ``max_sample``), and for each permutation
        builds trees under Balanced/Left/Right frequency biases, runs the
        analyzer, and writes a compact permutation section to the report file.

        Args:
            levels: Number of operator levels per generated tree.
            filepath: Output Markdown path; defaults to an ``output/`` path
                derived from ``levels`` when ``None``.
            image_dir: Directory for generated diagrams; defaults similarly.
            root_n: Root frequency assigned to each generated tree.
            max_sample: Cap on the number of permutations tested; ``None`` or a
                value above the total tests them all.

        Returns:
            None. The report is written to ``filepath`` and a success line is
            printed.
        """
        if filepath is None:
            filepath = f"output/audit_reports/Testlauf_L{levels}_Vollstaendig.md"
        if image_dir is None:
            image_dir = f"output/audit_reports/Bilder_L{levels}_Test"

        num_operators = (2 ** levels) - 1
        all_permutations = list(itertools.product(self.operators, repeat=num_operators))
        
        if max_sample and len(all_permutations) > max_sample:
            permutations = random.sample(all_permutations, max_sample)
        else:
            permutations = all_permutations

        # Create directories safely
        report_dir = os.path.dirname(os.path.abspath(filepath))
        os.makedirs(report_dir, exist_ok=True)
        
        # Initialize builder with explicitly resolved paths
        builder = ReportBuilder(image_dir=image_dir, report_dir=report_dir)
        
        with open(filepath, 'w', encoding='utf-8') as file:
            desc = (f"This document tests configurations with **{levels} levels of operators** "
                    f"({num_operators} operators total per tree). Each configuration is tested "
                    f"against three frequency bias states: **Random (None), Left-Heavy, and Right-Heavy.**\n\n"
                    f"**Root Frequency (N):** {root_n}\n"
                    f"**Combinations Tested:** {len(permutations)} (out of 64 mathematically possible)")
            
            file.write(builder.build_document_header(f"Process Tree Analyzer - Level {levels} Permutation Report", desc))

            for i, ops_tuple in enumerate(permutations, 1):
                ops_iterator = iter(ops_tuple)
                blueprint = self._build_blueprint_recursive(ops_iterator, current_level=1, max_level=levels)
                
                ops_str = ", ".join(ops_tuple)
                ops_filename = "_".join(ops_tuple)
                permutation_results = []
                master_tree = None
                
                for bias_label, bias_value in self.biases.items():
                    try:
                        test_tree = self.generator.generate_from_blueprint(blueprint)
                        self.generator.assign_frequencies(test_tree, total_frequency=root_n, bias=bias_value)
                        
                        # Use Balanced as the master structural tree
                        if bias_label == 'Balanced':
                            master_tree = test_tree
                            
                        self.analyzer.compute_frequencies(test_tree)
                        
                        # Extract the exact symbolic math layout
                        tree_string_sym = get_tree_string(test_tree)
                        forced_traces = self.analyzer.analyze_forced_traces(test_tree, root_n)
                        
                        permutation_results.append({
                            'bias': bias_label,
                            'tree_str': tree_string_sym,
                            'error': None,
                            'traces': forced_traces
                        })
                        
                    except Exception as e:
                        permutation_results.append({'bias': bias_label, 'tree_str': '-', 'error': str(e), 'traces': []})
                        
                md_section = builder.build_compact_permutation_section(
                    section_idx=i,
                    ops_str=ops_str,
                    ops_filename=ops_filename,
                    results=permutation_results,
                    master_tree=master_tree
                )
                file.write(md_section)
                    
        print(f"Success! Exact match report saved to: {os.path.abspath(filepath)}")