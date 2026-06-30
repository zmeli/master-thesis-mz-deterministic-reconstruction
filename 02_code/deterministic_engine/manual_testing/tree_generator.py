import random
import warnings
import ast
from core.tree_node import ProcessTreeNode

'''
Class: RandomTreeGenerator
Description: 
    Generates process trees for testing purposes. It can create fully random structures or 
    build trees following specific blueprint tuples while handling syntax errors.

Methods:
    - __init__: Initializes the generator state. Returns None. 
      Called by: main.py.
    - _get_next_activity_name: Generates incremental letters (A, B, C). Returns str. 
      Called by: _generate_random_tree_recursive, _generate_from_blueprint_recursive.
    - generate_random_tree: Public entry point for random generation. Returns ProcessTreeNode. 
      Called by: main.py.
    - generate_from_blueprint: Public entry point for tuple blueprint generation. Returns ProcessTreeNode. 
      Called by: main.py.
    - _generate_random_tree_recursive: Internal recursive random tree builder. Returns ProcessTreeNode. 
      Called by: RandomTreeGenerator.generate_random_tree, and recursively by itself.
    - _generate_from_blueprint_recursive: Internal recursive blueprint builder. Returns ProcessTreeNode. 
      Called by: RandomTreeGenerator.generate_from_blueprint, and recursively by itself.
    - assign_frequencies: Distributes root frequency top-down algorithmically. Returns None. 
      Called by: main.py, and recursively by itself.
'''
class RandomTreeGenerator:
    def __init__(self):
        self.operators = ['SEQ', 'XOR', 'PAR', 'LOOP']
        self._activity_counter = 0

    # Returns the next letter in the alphabet as an activity name (A, B, ..., Z, AA, AB, ...).
    def _get_next_activity_name(self) -> str:
        n = self._activity_counter
        self._activity_counter += 1
        result = ""
        while n >= 0:
            result = chr(65 + (n % 26)) + result
            n = n // 26 - 1
        return result

    # Public entry point: resets the activity counter and builds a random binary tree.
    def generate_random_tree(self, max_depth: int) -> ProcessTreeNode:
        self._activity_counter = 0
        return self._generate_random_tree_recursive(max_depth, current_depth=0)

    # Public entry point: resets the activity counter and builds a tree from a blueprint.
    def generate_from_blueprint(self, blueprint) -> ProcessTreeNode:
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

    # Recursively builds a random binary tree by selecting random operators and limiting depth.
    def _generate_random_tree_recursive(self, max_depth: int, current_depth: int) -> ProcessTreeNode:
        if current_depth >= max_depth or (current_depth > 0 and random.random() < 0.3):
            return ProcessTreeNode(operator="LEAF", name=self._get_next_activity_name())

        op = random.choice(self.operators)
        node = ProcessTreeNode(operator=op)
        node.add_child(self._generate_random_tree_recursive(max_depth, current_depth + 1))
        node.add_child(self._generate_random_tree_recursive(max_depth, current_depth + 1))
        return node

    # Recursively builds a specific tree structure from parsed blueprint tuples.
    # Fills missing tuple positions with auto-named leaves and validates structural errors.
    def _generate_from_blueprint_recursive(self, blueprint) -> ProcessTreeNode:
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

    # Distributes a total root frequency top-down to provide the mathematical ground truth
    # for validating the analyzer's bottom-up frequency calculations.
    def assign_frequencies(self, node: ProcessTreeNode, total_frequency: int, bias: str = None):
        """
        Distributes frequencies top-down. 
        :param bias: 'left', 'right', 'balanced', or None (Random).
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