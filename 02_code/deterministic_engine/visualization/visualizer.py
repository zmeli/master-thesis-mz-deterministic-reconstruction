import graphviz
import sys
from core.tree_node import ProcessTreeNode

from visualization.formatters import get_node_label

class ProcessTreeVisualizer:
    """
    Renders a process tree as a PDF/PNG diagram using Graphviz.

    Builds a Graphviz digraph from a :class:`ProcessTreeNode`, styling leaves and
    operator nodes differently and optionally annotating each node with its
    frequency.

    Args:
        root: The root node of the tree to visualize.
        show_frequencies: If ``True``, annotate each node with its frequency.

    Attributes:
        root: The tree root being rendered.
        show_frequencies: Whether frequency annotations are shown.
        dot: The underlying Graphviz ``Digraph`` being assembled.
    """
    def __init__(self, root: ProcessTreeNode, show_frequencies: bool = True):
        self.root = root
        self.show_frequencies = show_frequencies
        self.dot = graphviz.Digraph(comment='Process Tree')
        self.dot.attr('node', shape='box', style='rounded,filled', fontname='Segoe UI Symbol')
        
    def render(self, filename='process_tree_output', format='pdf', view=False):
        """
        Build the diagram and write it to disk in the given format.

        Populates the graph from the tree, then renders it. A missing Graphviz
        executable or any other rendering failure is caught and reported as a
        warning rather than raised, so batch runs are not interrupted.

        Args:
            filename: Output path without extension.
            format: Output format (e.g. ``'pdf'`` or ``'png'``).
            view: If ``True``, open the rendered file and print a confirmation.

        Returns:
            None. The diagram is written to ``filename.format`` (when successful).
        """
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
        """
        Add ``node`` and its descendants (with edges) to the Graphviz graph.

        Uses the node's object id as its graph id, colors and shapes it by type
        (leaf vs operator), then recurses into each child, drawing a parent-child
        edge for every one.

        Args:
            node: The subtree root to add to the graph.

        Returns:
            None. The graph is mutated in place.
        """
        node_id = str(id(node))
        
        # Call the pure function from formatters instead of the removed class method
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