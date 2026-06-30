"""Empirically demonstrates why the Atomic Fallback mechanism (core/analyzer.py's
opaque "[nested PAR_k]" encapsulation, and auto_verifier_v2.py's COMPLEX-pattern
guard) is necessary, by deliberately reconstructing the *naive* enumeration path
the engine would take WITHOUT it, and running that naive path until it is killed
for exceeding a safety memory cap or wall-clock timeout.

This script makes NO changes to core/analyzer.py or auto_verifier_v2.py. The
"naive" interleaving function below is a verbatim copy of
auto_verifier_v2.LogTraceVerifier._interleave_sequences, called directly without
the two guard checks (`len(combinations) > 50`, `len(all_interleavings) > 1000`)
that constitute the Atomic Fallback in practice. The unmodified engine is also
called, on the same input size, to show its actual (instant, fallback-protected)
behaviour for comparison.

Usage: py -3.12 demo_atomic_fallback_failure.py
"""
import csv
import math
import multiprocessing as mp
import string
import sys
import time
from pathlib import Path

import psutil

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from core.tree_node import ProcessTreeNode
from auto_verifier_v2 import LogTraceVerifier

_UNSUPERVISED_MODE = len(sys.argv) > 1 and sys.argv[1] == "--unsupervised"
SAFETY_MEM_CAP_MB = int(sys.argv[2]) if (len(sys.argv) > 2 and not _UNSUPERVISED_MODE) else 1536
SAFETY_TIMEOUT_S = int(sys.argv[3]) if (len(sys.argv) > 3 and not _UNSUPERVISED_MODE) else 30
POLL_INTERVAL_S = 0.05
K_VALUES = [int(sys.argv[1])] if (len(sys.argv) > 1 and not _UNSUPERVISED_MODE) else list(range(5, 15))
OUT_CSV = ROOT / "output" / "atomic_fallback_demo_results.csv"


def naive_interleave_sequences(sequences):
    """Verbatim copy of auto_verifier_v2.LogTraceVerifier._interleave_sequences,
    reproduced standalone (not imported, not modified) so it can be called
    directly without the calling guards that normally protect it."""
    active_seqs = [s for s in sequences if s]
    if not active_seqs:
        return [[]]
    if len(active_seqs) == 1:
        return [active_seqs[0]]

    result = []
    for i in range(len(active_seqs)):
        first_elem = active_seqs[i][0]
        remaining_seqs = [s[:] for s in active_seqs]
        remaining_seqs[i] = remaining_seqs[i][1:]
        for tail in naive_interleave_sequences(remaining_seqs):
            result.append([first_elem] + tail)

    return [list(x) for x in set(tuple(x) for x in result)]


def _naive_worker(k, result_queue):
    """Runs in a child process so the parent can kill it on OOM/timeout
    without taking down this session."""
    branches = [[letter] for letter in string.ascii_uppercase[:k]]
    t0 = time.time()
    out = naive_interleave_sequences(branches)
    elapsed = time.time() - t0
    result_queue.put(("completed", len(out), elapsed))


def _naive_worker_unsupervised(k, result_queue):
    """Same as _naive_worker, but used for the unsupervised run: catches
    MemoryError itself so a genuine allocation failure is reported back to the
    parent rather than the child just vanishing. If the OS kills the process
    outright (no Python exception raised), the parent observes that via
    proc.exitcode instead -- this function exists to catch the cooperative case."""
    branches = [[letter] for letter in string.ascii_uppercase[:k]]
    t0 = time.time()
    try:
        out = naive_interleave_sequences(branches)
        elapsed = time.time() - t0
        result_queue.put(("completed", len(out), elapsed))
    except MemoryError:
        elapsed = time.time() - t0
        result_queue.put(("memory_error", None, elapsed))


def run_naive_unsupervised(k, max_wait_s=2400, report_every_s=10.0):
    """Lets the guard-free enumeration run with NO memory cap, only a generous
    backstop wall-clock timeout, so that on a genuine OOM it is the Python
    process itself (or the OS) that terminates it -- not this script. Memory
    is still polled periodically purely for reporting/progress, never to kill."""
    ctx = mp.get_context("spawn")
    q = ctx.Queue()
    proc = ctx.Process(target=_naive_worker_unsupervised, args=(k, q))
    proc.start()
    t0 = time.time()
    peak_rss_mb = 0.0
    last_report = 0.0
    status, count, elapsed = "running", None, None

    try:
        ps_proc = psutil.Process(proc.pid)
        while proc.is_alive():
            now = time.time() - t0
            try:
                rss_mb = ps_proc.memory_info().rss / (1024 * 1024)
                peak_rss_mb = max(peak_rss_mb, rss_mb)
            except psutil.NoSuchProcess:
                break
            if now - last_report >= report_every_s:
                print(f"  ... k={k} still running: t={now:.1f}s, RSS={rss_mb:.1f} MB", flush=True)
                last_report = now
            if now > max_wait_s:
                proc.terminate()
                status = "killed_backstop_timeout"
                elapsed = now
                break
            time.sleep(POLL_INTERVAL_S)
        proc.join(timeout=10)

        if status == "running":
            # proc.is_alive() became False on its own: either it finished
            # cooperatively (queue has a result) or it died (MemoryError
            # caught and queued, or the OS killed it with nothing queued).
            if not q.empty():
                tag, count, elapsed = q.get()
                status = tag  # "completed" or "memory_error"
            else:
                status = f"died_unreported (exitcode={proc.exitcode})"
                elapsed = time.time() - t0
    finally:
        if proc.is_alive():
            proc.kill()
            proc.join()

    return status, count, elapsed, peak_rss_mb


def run_naive_with_guard(k):
    """Spawns _naive_worker(k) and kills it if it exceeds the safety memory cap
    or wall-clock timeout, polling RSS in the parent process."""
    ctx = mp.get_context("spawn")
    q = ctx.Queue()
    proc = ctx.Process(target=_naive_worker, args=(k, q))
    proc.start()
    t0 = time.time()
    peak_rss_mb = 0.0
    status, count, elapsed = "killed", None, None

    try:
        ps_proc = psutil.Process(proc.pid)
        while proc.is_alive():
            now = time.time() - t0
            try:
                rss_mb = ps_proc.memory_info().rss / (1024 * 1024)
                peak_rss_mb = max(peak_rss_mb, rss_mb)
            except psutil.NoSuchProcess:
                break
            if rss_mb > SAFETY_MEM_CAP_MB:
                proc.terminate()
                status = "killed_memory"
                elapsed = now
                break
            if now > SAFETY_TIMEOUT_S:
                proc.terminate()
                status = "killed_timeout"
                elapsed = now
                break
            time.sleep(POLL_INTERVAL_S)
        else:
            pass
        proc.join(timeout=5)
        if status == "killed" and not q.empty():
            tag, count, elapsed = q.get()
            if tag == "completed":
                status = "completed"
    finally:
        if proc.is_alive():
            proc.kill()
            proc.join()

    return status, count, elapsed, peak_rss_mb


def run_real_engine(k):
    """Calls the ACTUAL, unmodified engine on an equivalent k-branch PAR block
    (binarized, as core/tree_node.py enforces max 2 children per node), and
    times how long the real, fallback-protected path takes."""
    letters = string.ascii_uppercase[:k]
    node = ProcessTreeNode("LEAF", letters[0], 1)
    for letter in letters[1:]:
        new_par = ProcessTreeNode("PAR")
        new_par.add_child(node)
        new_par.add_child(ProcessTreeNode("LEAF", letter, 1))
        node = new_par

    verifier = LogTraceVerifier(compute_fitness_precision=False)
    t0 = time.time()
    result = verifier._generate_valid_patterns(node)
    elapsed = time.time() - t0
    return result == [["COMPLEX"]], elapsed


def main():
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    print(f"{'k':>3} {'k!':>15} {'naive_status':>16} {'naive_time_s':>12} {'naive_peak_mb':>13} "
          f"{'real_is_complex':>15} {'real_time_s':>11}")

    for k in K_VALUES:
        factorial = math.factorial(k)
        naive_status, naive_count, naive_time, naive_peak_mb = run_naive_with_guard(k)
        real_is_complex, real_time = run_real_engine(k)

        rows.append(dict(
            k=k, factorial=factorial, naive_status=naive_status,
            naive_result_count=naive_count, naive_time_s=naive_time,
            naive_peak_rss_mb=round(naive_peak_mb, 1),
            real_returned_complex=real_is_complex, real_time_s=round(real_time, 5),
        ))
        print(f"{k:>3} {factorial:>15,} {naive_status:>16} "
              f"{('%.2f' % naive_time) if naive_time is not None else 'n/a':>12} "
              f"{naive_peak_mb:>13.1f} {str(real_is_complex):>15} {real_time:>11.5f}")

        if naive_status in ("killed_memory", "killed_timeout"):
            print(f"  -> naive enumeration killed at k={k} ({naive_status}); "
                  f"stopping sweep (larger k only gets worse).")
            break

    with open(OUT_CSV, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"\nWrote {OUT_CSV}")


def main_unsupervised():
    """py -3.12 demo_atomic_fallback_failure.py --unsupervised <k> [max_wait_s]
    Runs the guard-free enumeration with NO memory cap, letting the process
    fail on its own (MemoryError or an OS-level kill) rather than this script
    pre-emptively terminating it. Use with care: this is intended to let
    memory genuinely run out."""
    k = int(sys.argv[2])
    max_wait_s = int(sys.argv[3]) if len(sys.argv) > 3 else 2400
    print(f"Running k={k} ({math.factorial(k):,} interleavings) UNSUPERVISED "
          f"(no memory cap, backstop timeout={max_wait_s}s)...")
    status, count, elapsed, peak_mb = run_naive_unsupervised(k, max_wait_s=max_wait_s)
    print(f"\nResult: k={k} status={status} elapsed={elapsed} peak_rss_mb={peak_mb:.1f} count={count}")

    out_path = ROOT / "output" / f"atomic_fallback_unsupervised_k{k}.csv"
    with open(out_path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["k", "factorial", "status", "elapsed_s", "peak_rss_mb", "result_count"])
        writer.writeheader()
        writer.writerow(dict(k=k, factorial=math.factorial(k), status=status,
                              elapsed_s=elapsed, peak_rss_mb=round(peak_mb, 1), result_count=count))
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--unsupervised":
        main_unsupervised()
    else:
        main()
