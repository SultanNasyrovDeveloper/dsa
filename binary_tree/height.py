from typing import Optional

from binary_tree.node import Node


def find_height(root: Node) -> int:
    """
    Height of a tree is number of edges in the longest path from root to leaf node.
    """
    if not root:
        return 0
    else:
        left_depth = find_height(root.left)
        right_depth = find_height(root.right)
        return max(left_depth, right_depth) + 1
