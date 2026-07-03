"""
Generate synthetic CSV stress-test event logs.

Each generator function returns one case's activity sequence for a known
control-flow structure (sequence, choice, parallel, loop, and nested
combinations). :func:`write_log` repeatedly samples a generator to build a log
with synthetic timestamps and writes it to ``data/stress_tests/``. Running the
module as a script produces the full suite of ten test logs.
"""
import csv
import random
import itertools
from datetime import datetime, timedelta
import os

# Create a dedicated folder for these stress tests
os.makedirs('data/stress_tests', exist_ok=True)

def write_log(filename, generator_func, min_events=100):
    """
    Build a CSV event log by repeatedly sampling a case generator.

    Draws whole cases from ``generator_func`` until at least ``min_events`` rows
    exist, assigns each event an increasing synthetic timestamp, and writes the
    result to ``data/stress_tests/<filename>``.

    Args:
        filename: Output CSV filename (within the stress-tests folder).
        generator_func: Zero-argument callable returning one case's list of
            activity names.
        min_events: Minimum number of event rows to generate.

    Returns:
        None. The log is written to disk and a summary line is printed.
    """
    events = []
    case_id = 1
    # Start all logs on June 1st, 2026
    current_time = datetime(2026, 6, 1, 8, 0, 0)

    # Generate cases until we hit the minimum entry requirement
    while len(events) < min_events:
        case_activities = generator_func()
        for act in case_activities:
            events.append([case_id, act, current_time.strftime("%Y-%m-%d %H:%M:%S")])
            # Add a random time jump between 1 and 15 minutes for realistic timestamps
            current_time += timedelta(minutes=random.randint(1, 15))
        case_id += 1

    filepath = f'data/stress_tests/{filename}'
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Case ID', 'Activity', 'Timestamp'])
        writer.writerows(events)
    print(f"Generated '{filename}': {len(events)} entries across {case_id - 1} cases.")

# ==========================================
# MATHEMATICAL STRUCTURAL GENERATORS
# ==========================================

def seq_par():
    """Return one case of ``A -> PAR(B, C) -> D`` (B and C in either order)."""
    par_block = ['B', 'C'] if random.random() > 0.5 else ['C', 'B']
    return ['A'] + par_block + ['D']

def seq_xor():
    """Return one case of ``A -> XOR(B, C) -> D`` (exactly one of B or C)."""
    choice = ['B'] if random.random() > 0.5 else ['C']
    return ['A'] + choice + ['D']

def loop_std():
    """Return one case of ``A -> LOOP(B, C) -> D`` with a random redo count."""
    trace = ['A', 'B'] # DO
    while random.random() > 0.4: # 60% chance to REDO
        trace.extend(['C', 'B'])
    trace.append('D')
    return trace

def par_xor():
    """Return one case of ``PAR(A, XOR(B, C)) -> D`` (A and the choice interleave)."""
    choice = ['B'] if random.random() > 0.5 else ['C']
    return ['A'] + choice + ['D'] if random.random() > 0.5 else choice + ['A'] + ['D']

def xor_seq():
    """Return one case of ``XOR(SEQ(A, B), C) -> D`` (the A,B branch or the C branch)."""
    return ['A', 'B', 'D'] if random.random() > 0.5 else ['C', 'D']

def xor_xor():
    """Return one case of ``XOR(A, B) -> XOR(C, D) -> E`` (two independent choices)."""
    c1 = ['A'] if random.random() > 0.5 else ['B']
    c2 = ['C'] if random.random() > 0.5 else ['D']
    return c1 + c2 + ['E']

def par_par():
    """Return one case of ``PAR(A, B) -> PAR(C, D) -> E`` (each pair in either order)."""
    p1 = ['A', 'B'] if random.random() > 0.5 else ['B', 'A']
    p2 = ['C', 'D'] if random.random() > 0.5 else ['D', 'C']
    return p1 + p2 + ['E']

def xor_loop():
    """Return one case of ``A -> XOR(LOOP(B, C), D) -> E`` (loop branch or D branch)."""
    if random.random() > 0.5:
        trace = ['B']
        while random.random() > 0.5:
            trace.extend(['C', 'B'])
        return ['A'] + trace + ['E']
    else:
        return ['A', 'D', 'E']

def deep_seq():
    """Return the single deterministic case ``A -> B -> C -> D -> E``."""
    return ['A', 'B', 'C', 'D', 'E']

def nested_par():
    """Return one case of ``A -> PAR(B, PAR(C, D)) -> E`` (B, C, D in any order)."""
    # Mathematically, PAR(B, PAR(C, D)) means B, C, and D can happen in any permutation.
    perms = list(itertools.permutations(['B', 'C', 'D']))
    return ['A'] + list(random.choice(perms)) + ['E']

# ==========================================
# EXECUTION
# ==========================================
if __name__ == "__main__":
    print("Generating 10 Stress Test Datasets...\n" + "-"*40)
    write_log('test_01_seq_par.csv', seq_par)
    write_log('test_02_seq_xor.csv', seq_xor)
    write_log('test_03_loop_std.csv', loop_std)
    write_log('test_04_par_xor.csv', par_xor)
    write_log('test_05_xor_seq.csv', xor_seq)
    write_log('test_06_xor_xor.csv', xor_xor)
    write_log('test_07_par_par.csv', par_par)
    write_log('test_08_xor_loop.csv', xor_loop)
    write_log('test_09_deep_seq.csv', deep_seq)
    write_log('test_10_nested_par.csv', nested_par)
    print("-" * 40 + "\nSuccess! All files saved to data/stress_tests/")