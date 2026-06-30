import os
import pandas as pd
import pm4py
import concurrent.futures

def evaluate_noise_range(log_path: str, output_md: str, timeout_seconds: int = 60):
    print(f"[*] Starting Iterative Evaluation for: {log_path}")
    
    # ==========================================
    # 1. LOAD THE DATA ONCE
    # ==========================================
    print("[*] Loading and formatting event log into memory (this may take a moment)...")
    if log_path.lower().endswith('.csv'):
        df = pd.read_csv(log_path, low_memory=False)
        if 'Case ID' in df.columns and 'concept:name' not in df.columns:
            df.rename(columns={'Activity': 'concept:name'}, inplace=True)
            
        log = pm4py.format_dataframe(
            df, 
            case_id='Case ID' if 'Case ID' in df.columns else 'case:concept:name', 
            activity_key='concept:name', 
            timestamp_key='Complete Timestamp' if 'Complete Timestamp' in df.columns else 'time:timestamp'
        )
    else:
        log = pm4py.read_xes(log_path)
        
    print("[+] Log loaded successfully! Beginning iteration...\n")

    # Initialize the Markdown Report
    md_lines = [
        "# Process Model Iteration Report",
        f"**Source Log:** `{os.path.basename(log_path)}`",
        "This report evaluates the Inductive Miner across noise thresholds from 0.0 to 1.0.",
        "---"
    ]

    # ==========================================
    # 2. ITERATE FROM 0.0 TO 1.0
    # ==========================================
    # Generates [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    thresholds = [i / 10.0 for i in range(11)]

    for noise in thresholds:
        print(f"➔ Testing Noise Threshold: {noise:.1f} ... ", end="", flush=True)
        md_lines.append(f"## Threshold: {noise:.1f}")

        # Use a ThreadPoolExecutor to enforce a timeout on the C-based miner
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(pm4py.discover_process_tree_inductive, log, noise)
            try:
                # Wait for the miner to finish. If it hits the timeout, it raises an error.
                tree = future.result(timeout=timeout_seconds) 
            except concurrent.futures.TimeoutError:
                print(f"[TIMEOUT] (> {timeout_seconds}s)")
                md_lines.append(f"> ⚠️ **Timeout:** Mining exceeded {timeout_seconds} seconds. The log is too unstructured (spaghetti) at this threshold.\n")
                continue
            except Exception as e:
                print(f"[ERROR]")
                md_lines.append(f"> ❌ **Error during mining:** `{str(e)}`\n")
                continue

        # If we reach here, mining succeeded. Calculate metrics!
        print("[MINED] -> Calculating Metrics...", end="", flush=True)
        try:
            net, im, fm = pm4py.convert_to_petri_net(tree)
            fitness_results = pm4py.fitness_token_based_replay(log, net, im, fm)
            precision_val = pm4py.precision_token_based_replay(log, net, im, fm)
            fitness_val = fitness_results.get('log_fitness', fitness_results.get('average_trace_fitness', 0))
            
            print(f" [DONE] (Fitness: {fitness_val:.2%})")
            
            # Add successful results to the report
            md_lines.extend([
                f"* **Fitness:** `{fitness_val:.2%}`",
                f"* **Precision:** `{precision_val:.2%}`",
                "",
                "**Discovered Tree:**",
                "```text",
                str(tree),
                "```",
                "---"
            ])
        except Exception as e:
            print(f" [EVAL ERROR]")
            md_lines.append(f"> ❌ **Error during evaluation:** `{str(e)}`\n")


    # ==========================================
    # 3. SAVE THE FINAL REPORT
    # ==========================================
    md_content = "\n".join(md_lines)
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(md_content)
        
    print(f"\n[+] Iteration complete! Full results saved to {output_md}")


# ==========================================
# Run the script
# ==========================================
if __name__ == "__main__":
    TARGET_LOG = "data/BPIC2017/simulated-log.xml" 
    OUTPUT_FILE = "BPIC17simulated_Threshold_Analysis.md"
    
    # Run the sweep with a 60-second timeout per threshold
    evaluate_noise_range(TARGET_LOG, OUTPUT_FILE, timeout_seconds=60)