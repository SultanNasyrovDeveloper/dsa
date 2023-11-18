from binary_search_tree.node import Node
from mytypes import Comparable


def insert(root: Node, value: Comparable) -> Node:
    if root is None:
        return Node(value)
    if value == root.value:
        return root
    elif root.value < value:
        insert(root.right, value)
    else:
        insert(root.left, value)
    return root
