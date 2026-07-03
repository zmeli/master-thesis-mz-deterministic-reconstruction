import re
from typing import List, Tuple

# Moved from tree_node.py
OP_SYMBOLS = {'SEQ': '→', 'XOR': '×', 'PAR': '∧', 'LOOP': '∗'}

def get_tree_string(node) -> str:
    """
    Render a tree as a nested string using operator symbols for CLI display.

    Leaves are shown as ``name:frequency``; operators use their symbol from
    ``OP_SYMBOLS`` (e.g. ``→``, ``×``) wrapping their children.

    Args:
        node: The (sub)tree root to render.

    Returns:
        The symbolic string representation of the tree.
    """
    if node.operator == 'LEAF':
        return f"{node.name}:{node.frequency}"
    op_str = OP_SYMBOLS.get(node.operator, node.operator)
    child_strs = [get_tree_string(child) for child in node.children]
    return f"{op_str}({', '.join(child_strs)})"

def get_node_label(node, show_freq: bool = True) -> str:
    """
    Build a formatted label for a Graphviz node box.

    Leaves show their name; operators show their symbol and name (e.g.
    ``× (XOR)``). A frequency line (``n=...``) is appended when requested.

    Args:
        node: The node to label.
        show_freq: If ``True``, include the node's frequency in the label.

    Returns:
        The multi-line label string.
    """
    if node.operator == 'LEAF':
        return f"{node.name}\n(n={node.frequency})" if show_freq else node.name
        
    op_symbols = {'SEQ': '→ (SEQ)', 'XOR': '× (XOR)', 'PAR': '∧ (PAR)', 'LOOP': '↺ (LOOP)'}
    label = op_symbols.get(node.operator, node.operator)
    
    return f"{label}\n(n={node.frequency})" if show_freq else label

def get_flat_representation(node) -> str:
    """
    Render a node's atomic representation, flattening redundant brackets.

    Uses the bracket notation ``⟨…⟩`` (SEQ), ``{…}`` (PAR), ``[… │ …]`` (XOR),
    and ``(… ∗ …)`` (LOOP). Nested children of the same associative operator have
    their outer brackets stripped so the result reads flat rather than deeply
    nested.

    Args:
        node: The (sub)tree root to render.

    Returns:
        The flattened atomic string representation.
    """
    if node.operator == 'LEAF':
        return str(node.name)
        
    child_strings = []
    for child in node.children:
        child_str = get_flat_representation(child)
        
        # Flatten associative operators (SEQ inside SEQ, PAR inside PAR, etc.)
        if child.operator == node.operator and node.operator in ('SEQ', 'PAR', 'XOR'):
            # Only strip if the string actually starts and ends with the correct brackets
            if (child_str.startswith('⟨') and child_str.endswith('⟩')) or \
               (child_str.startswith('{') and child_str.endswith('}')) or \
               (child_str.startswith('[') and child_str.endswith(']')):
                child_str = child_str[1:-1]
                
        child_strings.append(child_str)
        
    if node.operator == 'SEQ': return f"⟨{', '.join(child_strings)}⟩"
    if node.operator == 'PAR': return f"{{{', '.join(child_strings)}}}"
    if node.operator == 'XOR': return f"[{' │ '.join(child_strings)}]"
    if node.operator == 'LOOP': return f"({' ∗ '.join(child_strings)})"
    
    return ""

def is_sublist(small_list: List[str], large_list: List[str]) -> bool:
    """
    Check whether ``small_list`` occurs as a contiguous slice of ``large_list``.

    Args:
        small_list: The candidate sub-path of activities.
        large_list: The full path to search within.

    Returns:
        ``True`` if ``small_list`` appears contiguously in ``large_list``.
    """
    n, m = len(small_list), len(large_list)
    for i in range(m - n + 1):
        if large_list[i:i+n] == small_list:
            return True
    return False

def print_analysis_report(
    tree_string: str, total_n: int, 
    forced_traces: List[Tuple[any, int, str]], show_legend: bool = True
):
    """
    Print the deterministic reconstruction report to the CLI.

    Renders a header, then a de-duplicated table of forced traces sorted by
    length, frequency, and type, followed by an optional legend explaining the
    trace types and bracket notation.

    Args:
        tree_string: Symbolic string of the analyzed tree (for the header).
        total_n: Log size (root token count) to display.
        forced_traces: List of ``(node, frequency, type)`` tuples to tabulate.
        show_legend: If ``True``, append the notation legend.

    Returns:
        None. Output is printed to stdout.
    """
    print("\n" + "="*85)
    print("DETERMINISTIC CONTROL-FLOW RECONSTRUCTION")
    print("="*85)
    print(f"Target Tree : {tree_string}")
    print(f"Log Size (N): {total_n}")
    print("-" * 85)
    print(f"{'Type':<5} | {'Min Freq':<10} | {'Reconstructed Path / Atomic Block'}")
    print("-" * 85)
    
    if not forced_traces:
        print("No traces forced.\n" + "="*85)
        return

    forced_traces.sort(
        key=lambda x: (len(get_flat_representation(x[0])), x[1], 1 if x[2] == "ST" else 0), 
        reverse=True
    )
    
    seen = set()
    for node, freq, t_type in forced_traces:
        clean_trace = get_flat_representation(node)
        if clean_trace not in seen:
            print(f"[{t_type:<2}] | {freq:<10} | {clean_trace}")
            seen.add(clean_trace)
        
    print("="*85)
    
    if show_legend:
        print("LEGEND:\n" + "-" * 85)
        print(" [ST] Strict Trace  : Explicit chronological execution guaranteed.")
        print(" [AS] Activity Set  : Execution guaranteed, order variable.")
        print("\n ⟨ A, B ⟩    : SEQ  (Strict Sequence)")
        print(" { A, B }    : PAR  (Activity Set)")
        print(" [ A │ B ]   : XOR  (Choice Set)")
        print(" ( A ∗ B )   : LOOP (Loop)")
        print("="*85)