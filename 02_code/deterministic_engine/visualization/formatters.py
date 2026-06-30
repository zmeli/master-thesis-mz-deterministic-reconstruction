import re
from typing import List, Tuple

# Moved from tree_node.py
OP_SYMBOLS = {'SEQ': '→', 'XOR': '×', 'PAR': '∧', 'LOOP': '∗'}

def get_tree_string(node) -> str:
    """Returns the tree as a string using logical operator symbols for CLI display."""
    if node.operator == 'LEAF':
        return f"{node.name}:{node.frequency}"
    op_str = OP_SYMBOLS.get(node.operator, node.operator)
    child_strs = [get_tree_string(child) for child in node.children]
    return f"{op_str}({', '.join(child_strs)})"

def get_node_label(node, show_freq: bool = True) -> str:
    """Generates a formatted label string for Graphviz node boxes."""
    if node.operator == 'LEAF':
        return f"{node.name}\n(n={node.frequency})" if show_freq else node.name
        
    op_symbols = {'SEQ': '→ (SEQ)', 'XOR': '× (XOR)', 'PAR': '∧ (PAR)', 'LOOP': '↺ (LOOP)'}
    label = op_symbols.get(node.operator, node.operator)
    
    return f"{label}\n(n={node.frequency})" if show_freq else label

def get_flat_representation(node) -> str:
    """
    Recursively generates the atomic string representation.
    Visually flattens redundant structural brackets dynamically.
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
    # FIX: Using safe Unicode Light Vertical Bar '│' instead of standard pipe '|' 
    # to prevent breaking Markdown tables within backticks.
    if node.operator == 'XOR': return f"[{' │ '.join(child_strings)}]"
    if node.operator == 'LOOP': return f"({' ∗ '.join(child_strings)})"
    
    return ""

def is_sublist(small_list: List[str], large_list: List[str]) -> bool:
    """Safely checks if one list of activities is a contiguous sub-path of another."""
    n, m = len(small_list), len(large_list)
    for i in range(m - n + 1):
        if large_list[i:i+n] == small_list:
            return True
    return False

def print_analysis_report(
    tree_string: str, total_n: int, 
    forced_traces: List[Tuple[any, int, str]], show_legend: bool = True
):
    """Prints the CLI analysis report."""
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