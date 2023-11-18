from typing import Optional

from binary_search_tree.node import Node
from mytypes import Comparable


def search(root: Node, value: Comparable) -> Optional[Node]:
    if root is None:
        return None
    if root.value == value:
        return root
    if root.value < value:
        return search(root.right, value)
    return search(root.left, value)