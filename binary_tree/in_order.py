"""
In order traversal of linked list.
"""
from binary_tree.node import Node
from mytypes import Comparable


def traverse_inorder_recursive(node: Node) -> list[Comparable]:
    result = []
    left_children_values = None