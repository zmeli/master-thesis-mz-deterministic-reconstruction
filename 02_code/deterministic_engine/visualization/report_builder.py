import os
from pathlib import Path
from typing import List, Tuple
from core.tree_node import ProcessTreeNode
from core.analyzer import ProcessTreeAnalyzer

from visualization.formatters import get_flat_representation, is_sublist

class ReportBuilder:
    def __init__(self, image_dir: str = None, report_dir: str = "."):
        # Force paths to absolute to fix the Markdown relative linking bug
        self.report_dir = Path(report_dir).resolve()
        self.report_dir.mkdir(parents=True, exist_ok=True)
        
        if image_dir:
            self.image_dir = Path(image_dir).resolve()
            self.image_dir.mkdir(parents=True, exist_ok=True)
            # Safely calculate the relative path from the MD file to the images folder
            try:
                self.rel_img_path = os.path.relpath(self.image_dir, self.report_dir).replace("\\", "/")
            except ValueError:
                self.rel_img_path = str(self.image_dir).replace("\\", "/")
        else:
            self.image_dir = None
            self.rel_img_path = ""

    def build_document_header(self, title: str, description: str = "") -> str:
        md_lines = [f"# {title}\n"]
        if description:
            md_lines.append(f"{description}\n")
        md_lines.append("---\n")
        return "\n".join(md_lines)

    def build_markdown_section(
        self, section_id: str, title: str, root_tree: ProcessTreeNode, 
        forced_traces: List[Tuple[ProcessTreeNode, int, str]], total_n: int, 
        error_msg: str = None, show_fragments: bool = False, show_as: bool = True,
        nested_blocks_registry: dict = None,  # NEW: Optional dictionary of registered blocks
        dataset_name: str = "Unknown", noise_threshold: float = 0.0, added_tau_count: int = 0
    ) -> str:
        """Standard Markdown generation for processing real event logs."""
        md_lines = [f"## {title}"]
        
        if error_msg:
            md_lines.append(f"**[!] Analysis Failed:** `{error_msg}`\n\n---\n")
            return "\n".join(md_lines)

        # 1. Gather all statistics
        stats = ProcessTreeAnalyzer.get_tree_stats(root_tree)
        
        fitness_raw = getattr(root_tree, 'pm4py_fitness', 'N/A')
        fitness_val = fitness_raw.get('average_trace_fitness', fitness_raw.get('log_fitness', fitness_raw)) if isinstance(fitness_raw, dict) else fitness_raw
        precision_val = getattr(root_tree, 'pm4py_precision', 'N/A')
        binarization_ops = getattr(root_tree, 'binarization_additions', 'N/A')
        
        nested_loops = sum(1 for n in (nested_blocks_registry or {}).values() if n.operator == 'LOOP')
        nested_pars = sum(1 for n in (nested_blocks_registry or {}).values() if n.operator == 'PAR')
        total_patterns = len(forced_traces)

        # 2. Build the Overview Table
        md_lines.append("### Dataset & Topology Overview")
        md_lines.append("| Metric | Value |")
        md_lines.append("| :--- | :--- |")
        md_lines.append(f"| **Dataset Name** | `{dataset_name}` |")
        md_lines.append(f"| **Noise Threshold** | `{noise_threshold}` |")
        md_lines.append(f"| **Fitness** | `{fitness_val}` |")
        md_lines.append(f"| **Precision** | `{precision_val}` |")
        md_lines.append(f"| **Unique Activities** | `{stats['num_activities']}` |")
        md_lines.append(f"| **XOR Operators** | `{stats['XOR']}` |")
        md_lines.append(f"| **LOOP Operators** | `{stats['LOOP']}` |")
        md_lines.append(f"| **SEQ Operators** | `{stats['SEQ']}` |")
        md_lines.append(f"| **PAR Operators** | `{stats['PAR']}` |")
        md_lines.append(f"| **Binarization Additions** | `{binarization_ops}` |")
        md_lines.append(f"| **Tau Operators Added** | `{added_tau_count}` |")
        md_lines.append(f"| **Total Found Patterns** | `{total_patterns}` |")
        md_lines.append(f"| **Nested LOOPs** | `{nested_loops}` |")
        md_lines.append(f"| **Nested PARs** | `{nested_pars}` |\n")

        if self.image_dir:
            from visualization.visualizer import ProcessTreeVisualizer
            
            master_img_filename = f"tree_{section_id}_master"
            master_img_path = self.image_dir / master_img_filename
            
            visualizer = ProcessTreeVisualizer(root_tree, show_frequencies=True)
            visualizer.render(str(master_img_path), format='png', view=False)
            
            md_img_link = f"{self.rel_img_path}/{master_img_filename}.png"
            md_lines.append(f"![Master Process Tree]({md_img_link})\n")
        
        md_lines.append(f"**Log Size (N):** {total_n}\n")
        md_lines.append("| Type | Min Freq | Reconstructed Path / Atomic Block | Subtree Diagram |")
        md_lines.append("| :--- | :--- | :--- | :--- |")

        if not forced_traces:
            md_lines.append("| - | 0 | *No traces forced* | - |")
        else:
            processed = []
            for node, freq, t_type in forced_traces:
                if not show_as and t_type == "AS": continue
                flat_str = get_flat_representation(node)
                processed.append((node, freq, t_type, flat_str))

            filtered_traces = []
            for n1, f1, t1, s1 in processed:
                is_fragment = False
                if not show_fragments and t1 == "ST" and len(s1) > 2:
                    s1_elements = s1[1:-1].split(', ')
                    for n2, f2, t2, s2 in processed:
                        if t2 == "ST" and f1 == f2 and s1 != s2:
                            s2_elements = s2[1:-1].split(', ')
                            if is_sublist(s1_elements, s2_elements):
                                is_fragment = True
                                break
                if not is_fragment:
                    filtered_traces.append((n1, f1, t1, s1))

            filtered_traces.sort(key=lambda x: (len(x[3]), x[1], 1 if x[2] == "ST" else 0), reverse=True)
            
            seen = set()
            st_count = 0
            
            for node, freq, t_type, clean_trace in filtered_traces:
                if clean_trace not in seen:
                    md_trace = clean_trace.replace('|', '&#124;')
                    diagram_cell = "-"
                    
                    if t_type == "ST" and node.operator != 'LEAF' and self.image_dir:
                        from visualization.visualizer import ProcessTreeVisualizer
                        
                        st_count += 1
                        st_img_filename = f"st_{section_id}_micro_{st_count}"
                        st_img_full_path = self.image_dir / st_img_filename
                        
                        st_visualizer = ProcessTreeVisualizer(node, show_frequencies=False)
                        st_visualizer.render(str(st_img_full_path), format='png', view=False)
                        
                        st_md_link = f"{self.rel_img_path}/{st_img_filename}.png"
                        diagram_cell = f"![ST]({st_md_link})"
                        
                    md_lines.append(f"| `[{t_type}]` | {freq} | {md_trace} | {diagram_cell} |")
                    seen.add(clean_trace)
                    
# --- NEW: Append Nested Blocks Reference Section ---
        if nested_blocks_registry:
            md_lines.append("### Nested Structures Reference")
            md_lines.append("The following complex blocks were abstracted to simplify the main trace table:\n")
            
            for block_id, original_node in nested_blocks_registry.items():
                md_lines.append(f"#### `[{block_id}]`")
                
                # Fetch the flat representation to show what's inside
                flat_rep = get_flat_representation(original_node)
                md_lines.append(f"- **Internal Structure:** `{flat_rep}`")
                md_lines.append(f"- **Block Frequency:** {original_node.frequency}\n")

                # --- CALCULATE LOOP MAX LENGTH ---
                if original_node.operator == 'LOOP':
                    # Safe fetch of REDO frequency
                    redo_freq = getattr(original_node.children[1], 'frequency', 0) if len(original_node.children) > 1 else 0
                    max_steps = (redo_freq * 2) + 1
                    md_lines.append(f"- **Max Loop Iterations:** `{redo_freq}`")
                    md_lines.append(f"- **Max Sub-Sequence Length:** `{max_steps}` steps (if one case consumes all iterations)\n")
                else:
                    md_lines.append("\n") # Formatting spacer
                
                # Generate a micro-diagram specifically for this nested block
                if self.image_dir:
                    from visualization.visualizer import ProcessTreeVisualizer
                    
                    # Clean the ID for safe file paths (e.g. "nested_PAR_1")
                    safe_id = block_id.replace(" ", "_")
                    ref_img_filename = f"nested_ref_{section_id}_{safe_id}"
                    ref_img_path = self.image_dir / ref_img_filename
                    
                    # Render the localized diagram
                    ref_visualizer = ProcessTreeVisualizer(original_node, show_frequencies=True)
                    ref_visualizer.render(str(ref_img_path), format='png', view=False)
                    
                    ref_md_link = f"{self.rel_img_path}/{ref_img_filename}.png"
                    md_lines.append(f"![{block_id} Internal Diagram]({ref_md_link})\n")
            
        md_lines.append("\n---\n")
        return "\n".join(md_lines)

    def build_compact_permutation_section(self, section_idx: int, ops_str: str, ops_filename: str, results: list, master_tree=None) -> str:
        """
        Builds the custom Markdown format for the Level 2 Testlauf report.
        """
        md_lines = [f"### {section_idx}. Blueprint Operators: `{ops_str}`\n"]

        # Render the structural blueprint diagram if available
        if master_tree and self.image_dir:
            from visualization.visualizer import ProcessTreeVisualizer
            
            master_img_filename = f"tree_{section_idx}_{ops_filename}"
            master_img_path = self.image_dir / master_img_filename
            
            visualizer = ProcessTreeVisualizer(master_tree, show_frequencies=False)
            visualizer.render(str(master_img_path), format='png', view=False)
            
            md_img_link = f"{self.rel_img_path}/{master_img_filename}.png"
            md_lines.append(f"![Tree {ops_filename}]({md_img_link})\n")

        md_lines.append("| Bias | Generated Tree (Frequencies) | Type | Min Freq | Forced Trace / Atomic Block |")
        md_lines.append("| :--- | :--- | :--- | :--- | :--- |")

        for res in results:
            bias = res['bias']
            tree_str = res.get('tree_str', '-')
            
            if res['error']:
                md_lines.append(f"| **{bias}** | `{tree_str}` | - | - | ⚠️ *Error: {res['error']}* |")
                continue
                
            if not res['traces']:
                md_lines.append(f"| **{bias}** | `{tree_str}` | - | 0 | *No traces forced* |")
                continue
                
            formatted_traces = []
            for node, freq, t_type in res['traces']:
                flat_str = get_flat_representation(node)
                clean_str = flat_str.replace('|', '&#124;') # Safe Markdown pipe escape
                formatted_traces.append((t_type, freq, clean_str))
                
            # Sort: Priority to AS vs ST, then Frequency descending, then trace length
            formatted_traces.sort(key=lambda x: (0 if x[0] == "ST" else 1, -x[1], -len(x[2])))
            
            seen = set()
            is_first_row = True
            
            for t_type, freq, clean_trace in formatted_traces:
                if clean_trace not in seen:
                    # Only print the bias and tree string on the first row of the group
                    b_disp = f"**{bias}**" if is_first_row else ""
                    t_disp = f"`{tree_str}`" if is_first_row else ""
                    
                    md_lines.append(f"| {b_disp} | {t_disp} | `[{t_type}]` | {freq} | {clean_trace} |")
                    seen.add(clean_trace)
                    is_first_row = False

        md_lines.append("\n---\n")
        return "\n".join(md_lines)