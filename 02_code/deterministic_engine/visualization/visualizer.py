import graphviz
import sys
from core.tree_node import ProcessTreeNode

# NEW: Import the extracted formatting logic
from visualization.formatters import get_node_label

'''
Class: ProcessTreeVisualizer
Description: 
    Creates and renders visual PDF/PNG diagrams of process trees using the Graphviz library.
'''
class ProcessTreeVisualizer:
    def __init__(self, root: ProcessTreeNode, show_frequencies: bool = True):
        self.root = root
        self.show_frequencies = show_frequencies
        self.dot = graphviz.Digraph(comment='Process Tree')
        # 'Segoe UI Symbol' (vs. plain 'Arial') covers the operator glyphs ∧ (PAR)
        # and ↺ (LOOP); Arial lacks them and graphviz renders missing glyphs as boxes.
        self.dot.attr('node', shape='box', style='rounded,filled', fontname='Segoe UI Symbol')
        
    def render(self, filename='process_tree_output', format='pdf', view=False):
        """Generates the tree nodes and edges, then saves to the specified format (PDF/PNG)."""
        self._add_nodes_recursive(self.root)
        
        try:
            self.dot.render(filename, view=view, format=format)
            
            # Only print confirmation when a file is opened interactively (prevents log spam in batch runs).
            if view:
                print(f"Tree visualization saved as {filename}.{format}")
                
        except graphviz.backend.ExecutableNotFound:
            print("\n[!] WARNING: Graphviz is not installed on your system PATH.")
            print("    Skipping image generation. To enable visualizations, please install Graphviz:")
            print("    Windows: winget install graphviz")
            print("    Mac: brew install graphviz")
            print("    Linux: sudo apt install graphviz\n")
        except Exception as e:
            print(f"\n[!] WARNING: Failed to render visualization due to: {e}\n")

    def _add_nodes_recursive(self, node: ProcessTreeNode):
        node_id = str(id(node))
        
        # FIX: Call the pure function from formatters instead of the removed class method
        label = get_node_label(node, show_freq=self.show_frequencies)
        
        if node.operator == 'LEAF':
            color = "#E1F5FE"  # Light Blue
            shape = "ellipse"
        else:
            color = "#FFF9C4"  # Light Yellow
            shape = "box"

        self.dot.node(node_id, label, fillcolor=color, shape=shape)

        for child in node.children:
            child_id = str(id(child))
            self.dot.edge(node_id, child_id)
            self._add_nodes_recursive(child)