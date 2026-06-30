import os
from pathlib import Path
from core.data_assimilation import DataAssimilation
from core.analyzer import ProcessTreeAnalyzer
from visualization.report_builder import ReportBuilder

def analyze_and_report(target_path: str, report_dir: str, image_dir: str, show_fragments: bool = False, show_as: bool = False, noise_threshold: float = 0.0):
    """
    Analyzes event logs and uses the ReportBuilder to generate a clean Markdown report.
    Smartly detects whether target_path is a single file or a directory of files.
    """
    path_obj = Path(target_path)

    report_path_obj = Path(report_dir)
    report_path_obj.mkdir(parents=True, exist_ok=True)
    
    # 1. Initialize our Mathematical Engine and Presentation Engine
    analyzer = ProcessTreeAnalyzer()
    
    # FIX: Pass the report directory so the builder can calculate relative image paths
    builder = ReportBuilder(image_dir=image_dir, report_dir=report_dir)
    
    # 2. Smart Path Detection (File vs Folder)
    valid_extensions = {'.csv', '.xes', '.xml', '.mxml', '.gz', '.xes.gz'}
    
    if path_obj.is_file():
        if path_obj.suffix.lower() in valid_extensions:
            data_files = [path_obj]
        else:
            print(f"[!] Error: The file '{path_obj.name}' is not a supported log format.")
            return
    elif path_obj.is_dir():
        data_files = [f for f in path_obj.rglob('*') if f.suffix.lower() in valid_extensions]
    else:
        print(f"[!] Error: The path '{target_path}' does not exist.")
        return
    
    if not data_files:
        print(f"No valid event log files found at '{target_path}'.")
        return

    print(f"Found {len(data_files)} file(s) to process. Starting analysis...")
    
    # 3. Process the files
    for i, filepath in enumerate(data_files, 1):
        print(f"Processing ({i}/{len(data_files)}): {filepath.name}")

        base_filename = f"{filepath.stem}_report"
        individual_report_path = report_path_obj / f"{filepath.stem}.md"

        counter = 1
        while individual_report_path.exists():
            individual_report_path = report_path_obj / f"{base_filename}_{counter}.md"
            counter += 1

        with open(individual_report_path, 'w', encoding='utf-8') as md_file:
            
            header = builder.build_document_header(
                title=f"Process Tree Analysis Report: {filepath.name}",
                description=f"**Source Path:** `{filepath}`"
            )
            md_file.write(header)
            
            try:
                print("    [~] 1. Loading log and mining Process Tree (PM4Py)...")
                root_tree = DataAssimilation.assimilate_from_file(str(filepath), analyzer, noise_threshold=noise_threshold)
                total_n = root_tree.frequency

                # --- EXTRACT METRICS ---
                fitness_raw = getattr(root_tree, 'pm4py_fitness', 'N/A')
                if isinstance(fitness_raw, dict):
                    fitness_val = fitness_raw.get('average_trace_fitness', fitness_raw.get('log_fitness', fitness_raw))
                else:
                    fitness_val = fitness_raw
                precision_val = getattr(root_tree, 'pm4py_precision', 'N/A')

                # --- INJECT CONFORMANCE BLOCK ---
                md_file.write(f"### Conformance Metrics (PM4Py)\n")
                md_file.write(f"- **Fitness:** `{fitness_val}`\n")
                md_file.write(f"- **Precision:** `{precision_val}`\n\n")

                print(f"    [~] 2. Engine calculating mathematical trace permutations (N={total_n})...")
                forced_traces = analyzer.analyze_forced_traces(root_tree, total_n)
                
                # --- EXTRACT THE REGISTRY (NEW) ---
                # We pull the dictionary copy immediately after analysis to ensure thread/loop safety.
                extracted_registry = analyzer.nested_blocks_registry.copy()
                
                print("    [~] 3. Generating visual diagrams and Markdown...")
                md_section = builder.build_markdown_section(
                    section_id=f"{filepath.stem}_{i}",
                    title="Analysis Results",
                    root_tree=root_tree,
                    forced_traces=forced_traces,
                    total_n=total_n,
                    show_fragments=show_fragments,
                    show_as=show_as,
                    nested_blocks_registry=extracted_registry,
                    dataset_name=filepath.name,             # <--- NEW
                    noise_threshold=noise_threshold,        # <--- NEW
                    added_tau_count=analyzer.added_tau_count# <--- NEW
                )
                md_file.write(md_section)
                print("    [+] Done!")
                
            except Exception as e:
                md_section = builder.build_markdown_section(
                    section_id=f"{filepath.stem}_{i}", title="Analysis Results", 
                    root_tree=None, forced_traces=[], total_n=0, error_msg=str(e)
                )
                md_file.write(md_section)
                print(f"  -> Error on {filepath.name}: {e}")

    print(f"\nSuccess! All {len(data_files)} report(s) saved to the '{report_dir}' folder.")