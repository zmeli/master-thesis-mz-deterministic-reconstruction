import re
from typing import List

class ProcessTreeNode:
    """
    Data structure representing a single node in a process tree.
    Strictly restricts the tree to a binary structure.
    """
    def __init__(self, operator: str, name: str = None, frequency: int = 0):
        self.operator = operator.upper()
        self.name = name
        self.frequency = frequency
        self.children: List['ProcessTreeNode'] = []
        
        # --- NEW: Conformance Metric Containers ---
        self.pm4py_fitness = "N/A"
        self.pm4py_precision = "N/A"

    def add_child(self, child: 'ProcessTreeNode'):
        if self.operator == 'LEAF':
            raise ValueError("LEAF nodes cannot have children.")
        if len(self.children) >= 2:
            raise ValueError(f"Operator {self.operator} cannot have more than 2 children.")
        self.children.append(child)

    def get_atomic_representation(self) -> str:
        """
        Compresses any subtree into an atomic structural footprint.
        This allows parent equations to treat complex subtrees as unified objects.
        """
        if self.operator == 'LEAF':
            return self.name
        
        child_reps = [c.get_atomic_representation() for c in self.children]
        
        if self.operator == 'PAR':
            return f"{{{', '.join(child_reps)}}}"    # Activity Set: {A, B}
        elif self.operator == 'XOR':
            return f"[{' | '.join(child_reps)}]"     # Choice Set: [A | B]
        elif self.operator == 'SEQ':
            return f"⟨{', '.join(child_reps)}⟩"      # Strict Sequence: ⟨A, B⟩
        elif self.operator == 'LOOP':
            return f"({child_reps[0]} ∗ {child_reps[1]})" # Loop Construct
            
        return f"{self.operator}({', '.join(child_reps)})"

    @classmethod
    def from_string(cls, tree_str: str) -> 'ProcessTreeNode':
        """Parses a text string into a ProcessTreeNode."""
        tree_str = tree_str.strip().rstrip(')')
        
        if '(' not in tree_str:
            if ':' in tree_str:
                name, freq_part = tree_str.split(':')
                freq = int(freq_part.strip().rstrip(')'))
                return cls("LEAF", name.strip(), freq)
            return cls("LEAF", tree_str.strip(), 0)

        match = re.match(r"^(\w+)\((.*)$", tree_str)
        if not match:
            raise ValueError(f"Invalid format: {tree_str}")

        op_name = match.group(1).upper()
        content = match.group(2)
        node = cls(op_name)
        
        children_strs = cls._split_top_level_commas(content)
        
        # Enforce the binary constraint during parsing.
        if len(children_strs) > 2:
            raise ValueError(f"Input error: {op_name} has {len(children_strs)} children. Max allowed is 2.")
        
        for child_str in children_strs:
            node.add_child(cls.from_string(child_str))
            
        return node

    @staticmethod
    def _split_top_level_commas(content: str) -> list:
        """Helper that safely splits string arguments."""
        parts, bracket_level, current = [], 0, []
        for char in content:
            if char == '(': bracket_level += 1
            elif char == ')': bracket_level -= 1
            if char == ',' and bracket_level == 0:
                parts.append("".join(current).strip())
                current = []
            else: current.append(char)
        if current: parts.append("".join(current).strip())
        return parts