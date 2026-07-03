import re
from typing import List

class ProcessTreeNode:
    """
    A single node in a strictly binary process tree.

    A node is either a ``LEAF`` (an activity or silent tau, identified by
    ``name``) or a structural operator (``SEQ``, ``XOR``, ``PAR``, ``LOOP``)
    with at most two children. The class enforces the binary constraint on
    construction and offers helpers to render a node's atomic footprint and to
    parse a node back from its text form.

    Args:
        operator: Node type -- ``'LEAF'`` or an operator name (case-insensitive,
            stored upper-cased).
        name: Activity label for leaf nodes; ``None`` for operator nodes.
        frequency: Occurrence count associated with this node.

    Attributes:
        operator: The upper-cased node type.
        name: The leaf label (or ``None``).
        frequency: The node's occurrence count.
        children: The node's child nodes (at most two).
        pm4py_fitness: Optional PM4Py fitness metric attached downstream.
        pm4py_precision: Optional PM4Py precision metric attached downstream.
    """
    def __init__(self, operator: str, name: str = None, frequency: int = 0):
        self.operator = operator.upper()
        self.name = name
        self.frequency = frequency
        self.children: List['ProcessTreeNode'] = []
        
        self.pm4py_fitness = "N/A"
        self.pm4py_precision = "N/A"

    def add_child(self, child: 'ProcessTreeNode'):
        """
        Append a child node, enforcing the leaf and binary constraints.

        Args:
            child: The node to add as a child of this node.

        Raises:
            ValueError: If this node is a ``LEAF``, or if it already has two
                children.
        """
        if self.operator == 'LEAF':
            raise ValueError("LEAF nodes cannot have children.")
        if len(self.children) >= 2:
            raise ValueError(f"Operator {self.operator} cannot have more than 2 children.")
        self.children.append(child)

    def get_atomic_representation(self) -> str:
        """
        Compress this subtree into an atomic structural footprint string.

        Renders the node using operator-specific notation -- ``{A, B}`` for PAR,
        ``[A | B]`` for XOR, ``⟨A, B⟩`` for SEQ, ``(A ∗ B)`` for LOOP -- so that
        parent equations can treat complex subtrees as unified objects.

        Returns:
            The atomic string representation of this subtree.
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
        """
        Parse a text representation into a ProcessTreeNode tree.

        Accepts operator expressions of the form ``OP(child, child)`` and leaf
        entries of the form ``name`` or ``name:frequency``, recursing into nested
        children while enforcing the binary (max two children) constraint.

        Args:
            tree_str: The textual tree to parse.

        Returns:
            The root :class:`ProcessTreeNode` of the parsed tree.

        Raises:
            ValueError: If the string is malformed or an operator has more than
                two children.
        """
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
        """
        Split a child-argument string on top-level commas only.

        Tracks bracket depth so that commas inside nested ``(...)`` expressions
        are ignored, keeping each child argument intact.

        Args:
            content: The comma-separated argument string to split.

        Returns:
            The list of trimmed top-level argument substrings.
        """
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