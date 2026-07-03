import random
import warnings
import ast
from core.tree_node import ProcessTreeNode

class RandomTreeGenerator:
    """
    Generates binary process trees for testing.

    Produces either fully random structures (bounded by depth) or trees matching
    a supplied blueprint tuple, tolerating malformed blueprints by warning and
    falling back. Also assigns synthetic top-down frequencies to provide a
    mathematical ground truth for validating the analyzer.

    Attributes:
        operators: The structural operators available for generation.
    """
    def __init__(self):
        self.operators = ['SEQ', 'XOR', 'PAR', 'LOOP']
        self._activity_counter = 0

    def _get_next_activity_name(self) -> str:
        """Return the next spreadsheet-style activity name (A, B, …, Z, AA, …)."""
        n = self._activity_counter
        self._activity_counter += 1
        result = ""
        while n >= 0:
            result = chr(65 + (n % 26)) + result
            n = n // 26 - 1
        return result

    def generate_random_tree(self, max_depth: int) -> ProcessTreeNode:
        """
        Build a random binary tree, resetting activity naming first.

        Args:
            max_depth: Maximum depth of the generated tree.

        Returns:
            The root :class:`ProcessTreeNode` of the random tree.
        """
        self._activity_counter = 0
        return self._generate_random_tree_recursive(max_depth, current_depth=0)

    def generate_from_blueprint(self, blueprint) -> ProcessTreeNode:
        """
        Build a tree from a blueprint, resetting activity naming first.

        Accepts a nested tuple/list or its string form; strings are parsed with
        :func:`ast.literal_eval`, and a malformed blueprint triggers a warning and
        a fallback to a random tree of depth 3.

        Args:
            blueprint: A nested ``(op, left, right)`` structure, or its string
                representation.

        Returns:
            The root :class:`ProcessTreeNode` built from the blueprint.
        """
        self._activity_counter = 0
        
        # If a string is passed, safely parse it as a Python tuple using ast.literal_eval.
        if isinstance(blueprint, str):
            blueprint = blueprint.strip()
            # Detect whether the string looks like a tuple or list literal.
            if blueprint.startswith('(') or blueprint.startswith('['):
                try:
                    blueprint = ast.literal_eval(blueprint)
                except SyntaxError:
                    warnings.warn(
                        f"Blueprint syntax error (likely a missing comma or mismatched brackets): "
                        f"{blueprint}\n-> Falling back to random tree."
                    )
                    return self.generate_random_tree(max_depth=3)
                except ValueError:
                    warnings.warn(
                        f"Invalid value in blueprint: {blueprint}\n-> Falling back to random tree."
                    )
                    return self.generate_random_tree(max_depth=3)

        return self._generate_from_blueprint_recursive(blueprint)

    def _generate_random_tree_recursive(self, max_depth: int, current_depth: int) -> ProcessTreeNode:
        """
        Recursively build a random binary subtree.

        Emits a named leaf once ``max_depth`` is hit or, past the root, with a
        30% early-stop probability; otherwise picks a random operator and
        generates two children.

        Args:
            max_depth: Maximum depth allowed.
            current_depth: Depth of the node being generated.

        Returns:
            The generated :class:`ProcessTreeNode` subtree.
        """
        if current_depth >= max_depth or (current_depth > 0 and random.random() < 0.3):
            return ProcessTreeNode(operator="LEAF", name=self._get_next_activity_name())

        op = random.choice(self.operators)
        node = ProcessTreeNode(operator=op)
        node.add_child(self._generate_random_tree_recursive(max_depth, current_depth + 1))
        node.add_child(self._generate_random_tree_recursive(max_depth, current_depth + 1))
        return node

    def _generate_from_blueprint_recursive(self, blueprint) -> ProcessTreeNode:
        """
        Recursively build a subtree from a parsed blueprint node.

        Handles ``None``/``"LEAF"`` (auto-named leaf), operator strings, and
        ``(op, left, right)`` tuples, filling missing positions with leaves.
        Structural problems -- unknown operators, missing commas between
        operators, or excess tuple elements -- emit warnings and fall back to a
        sensible default rather than raising.

        Args:
            blueprint: The blueprint node (``None``, string, or tuple) to build.

        Returns:
            The generated :class:`ProcessTreeNode` subtree.
        """
        if blueprint is None or blueprint == "LEAF":
            return ProcessTreeNode(operator="LEAF", name=self._get_next_activity_name())
            
        if isinstance(blueprint, str):
            op = blueprint.upper()
            if op in self.operators:
                node = ProcessTreeNode(operator=op)
                node.add_child(self._generate_from_blueprint_recursive(None))
                node.add_child(self._generate_from_blueprint_recursive(None))
                return node
            else:
                if blueprint.upper() not in ['LEAF', '']:
                    warnings.warn(f"'{blueprint}' is not a known operator. Treating it as a LEAF.")
                return ProcessTreeNode(operator="LEAF", name=blueprint)
                
        elif isinstance(blueprint, tuple):
            if len(blueprint) == 0:
                return ProcessTreeNode(operator="LEAF", name=self._get_next_activity_name())

            op = str(blueprint[0]).upper()
            
            # Detect missing commas between operators in a tuple string
            # (e.g., 'SEQ' 'PAR' concatenated as 'SEQPAR' due to a missing comma).
            known_ops_in_string = [o for o in self.operators if o in op]
            if len(known_ops_in_string) > 1:
                warnings.warn(
                    f"Suspicious operator '{op}'. Missing comma between "
                    f"{known_ops_in_string}? Falling back to '{known_ops_in_string[0]}'."
                )
                op = known_ops_in_string[0]
            elif op not in self.operators and op != 'LEAF':
                warnings.warn(
                    f"Invalid operator '{op}'. Known operators are {self.operators}. Falling back to 'SEQ'."
                )
                op = 'SEQ'

            node = ProcessTreeNode(operator=op)
            
            # Guard against too many elements in the tuple — max 2 children per operator.
            if len(blueprint) > 3:
                excess = blueprint[3:]
                warnings.warn(
                    f"Too many elements in tuple for '{op}'. "
                    f"Max 2 children per operator. Ignoring: {excess}"
                )

            left = blueprint[1] if len(blueprint) > 1 else None
            node.add_child(self._generate_from_blueprint_recursive(left))
            
            right = blueprint[2] if len(blueprint) > 2 else None
            node.add_child(self._generate_from_blueprint_recursive(right))
            
            return node
            
        else:
            warnings.warn(f"Invalid blueprint type: {type(blueprint)}. Generating a LEAF instead.")
            return ProcessTreeNode(operator="LEAF", name=self._get_next_activity_name())

    def assign_frequencies(self, node: ProcessTreeNode, total_frequency: int, bias: str = None):
        """
        Distribute a root frequency top-down to create a ground-truth tree.

        Provides the reference frequencies used to validate the analyzer's
        bottom-up calculations. SEQ/PAR pass the full count to each child; XOR
        splits it per ``bias``; LOOP derives loop-back traffic per ``bias``.

        Args:
            node: Subtree root to populate (modified in place).
            total_frequency: Token count entering ``node``.
            bias: Distribution bias -- ``'left'``, ``'right'``, ``'balanced'``, or
                ``None`` for a purely random split.

        Returns:
            None. Frequencies are written onto the nodes in place.
        """
        node.frequency = total_frequency
        if node.operator == 'LEAF': return

        if node.operator in ('SEQ', 'PAR'):
            for child in node.children: 
                self.assign_frequencies(child, total_frequency, bias)
                
        elif node.operator == 'XOR':
            if total_frequency == 0:
                for child in node.children: 
                    self.assign_frequencies(child, 0, bias)
            else:
                # --- BIAS LOGIC ---
                if bias == 'left':
                    split = random.randint(total_frequency // 2, total_frequency)
                elif bias == 'right':
                    split = random.randint(0, total_frequency // 2)
                elif bias == 'balanced':
                    # Exactly 50/50 deterministic split
                    split = total_frequency // 2
                else:
                    # Purely random split (0% to 100%)
                    split = random.randint(0, total_frequency)
                    
                self.assign_frequencies(node.children[0], split, bias)
                self.assign_frequencies(node.children[1], total_frequency - split, bias)
                
        elif node.operator == 'LOOP':
            if bias == 'balanced':
                # Deterministic loop: Exactly 50% of the incoming traffic loops back
                loop_backs = total_frequency // 2 if total_frequency > 0 else 0
            else:
                # Random loopbacks
                loop_backs = random.randint(0, total_frequency * 2) if total_frequency > 0 else 0
                
            self.assign_frequencies(node.children[0], total_frequency + loop_backs, bias)
            self.assign_frequencies(node.children[1], loop_backs, bias)