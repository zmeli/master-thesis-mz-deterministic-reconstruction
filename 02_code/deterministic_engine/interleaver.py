import pandas as pd
import random
from datetime import datetime, timedelta

def interleave(traces):
    """Helper function to simulate Parallel (PAR) execution by randomly interleaving branches."""
    result = []
    ptrs = [0] * len(traces)
    while True:
        available = [i for i, p in enumerate(ptrs) if p < len(traces[i])]
        if not available:
            break
        choice = random.choice(available)
        result.append(traces[choice][ptrs[choice]])
        ptrs[choice] += 1
    return result

# ==========================================
# TRACE GENERATORS
# ==========================================

def generate_trace_seq_heavy():
    # Dominant: Sequence (1 to 15)
    trace = [f"Act_{i:02d}" for i in range(1, 16)]
    # Minor: XOR
    trace.append(random.choice(["Act_16", "Act_17"]))
    # Minor: PAR
    trace.extend(interleave([["Act_18"], ["Act_19"]])) 
    # Minor: LOOP
    for _ in range(random.randint(1, 3)): 
        trace.append("Act_20")
    return trace

def generate_trace_xor_heavy():
    # Minor: Sequence
    trace = ["Act_01", "Act_02"]
    # Dominant: XOR (Massive branching choice)
    path = random.choice([
        ["Act_03", "Act_04"], ["Act_05", "Act_06"], ["Act_07", "Act_08"],
        ["Act_09", "Act_10"], ["Act_11", "Act_12"], ["Act_13", "Act_14", "Act_15"]
    ])
    trace.extend(path) 
    # Minor: PAR
    trace.extend(interleave([["Act_16"], ["Act_17"]])) 
    # Minor: LOOP
    for _ in range(random.randint(1, 3)): 
        trace.append("Act_18")
    trace.extend(["Act_19", "Act_20"])
    return trace

def generate_trace_loop_heavy():
    # Minor: Sequence
    trace = ["Act_01"]
    # Dominant: LOOP (Massive 14-activity sequence looping 4 to 8 times)
    for _ in range(random.randint(4, 8)): 
        trace.extend([f"Act_{i:02d}" for i in range(2, 16)])
    # Minor: XOR
    trace.append(random.choice(["Act_16", "Act_17"])) 
    # Minor: PAR
    trace.extend(interleave([["Act_18"], ["Act_19"]])) 
    trace.append("Act_20")
    return trace

def generate_trace_par_heavy():
    # Minor: Sequence
    trace = ["Act_01"]
    # Dominant: PAR (15 activities executing concurrently in random order)
    par_branches = [
        ["Act_02", "Act_03"], ["Act_04"], ["Act_05"], ["Act_06"], ["Act_07"],
        ["Act_08"], ["Act_09"], ["Act_10"], ["Act_11"], ["Act_12"], 
        ["Act_13"], ["Act_14"], ["Act_15", "Act_16"]
    ]
    trace.extend(interleave(par_branches)) 
    # Minor: XOR
    trace.append(random.choice(["Act_17", "Act_18"])) 
    # Minor: LOOP
    for _ in range(random.randint(1, 3)): 
        trace.append("Act_19")
    trace.append("Act_20")
    return trace

# ==========================================
# DATASET CREATION
# ==========================================

def create_dataset(generator_func, num_cases=1000):
    rows = []
    # Start all logs conceptually on Jan 1st
    current_time = datetime(2024, 1, 1, 8, 0, 0) 
    
    for case_id in range(1, num_cases + 1):
        trace = generator_func()
        for act in trace:
            rows.append({
                "Case ID": f"Case_{case_id:04d}",
                "Activity": act,
                "Timestamp": current_time.strftime("%Y-%m-%d %H:%M:%S")
            })
            # 5 to 15 minutes between activities
            current_time += timedelta(minutes=random.randint(5, 15)) 
        # 1 to 12 hours before the next case starts
        current_time += timedelta(hours=random.randint(1, 12)) 
        
    return pd.DataFrame(rows)

if __name__ == "__main__":
    print("Generating datasets... this will take just a moment.")
    
    # Generate datasets (1000 traces each)
    df_seq = create_dataset(generate_trace_seq_heavy, 1000)
    df_seq.to_csv("dataset_01_seq_heavy.csv", index=False)
    print(f"Created dataset_01_seq_heavy.csv ({len(df_seq)} entries)")

    df_xor = create_dataset(generate_trace_xor_heavy, 1000)
    df_xor.to_csv("dataset_02_xor_heavy.csv", index=False)
    print(f"Created dataset_02_xor_heavy.csv ({len(df_xor)} entries)")

    df_loop = create_dataset(generate_trace_loop_heavy, 1000)
    df_loop.to_csv("dataset_03_loop_heavy.csv", index=False)
    print(f"Created dataset_03_loop_heavy.csv ({len(df_loop)} entries)")

    df_par = create_dataset(generate_trace_par_heavy, 1000)
    df_par.to_csv("dataset_04_par_heavy.csv", index=False)
    print(f"Created dataset_04_par_heavy.csv ({len(df_par)} entries)")
    
    print("\nAll datasets generated successfully!")