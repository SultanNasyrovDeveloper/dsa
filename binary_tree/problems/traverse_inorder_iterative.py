"""
Traverse a binary tree in order without using recursion.

Solutions:
- using stack

"""
from typing import Any

from binary_tree.tree import Node, BinaryTree
from binary_tree.utils import print_binary_tree


def traverse_using_stack(root: Node) -> list[Any]:
    result = []
    stack = []
    current = root
    while current or stack:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            result.append(current.value)
            current = current.right
    return result


tree = BinaryTree.generate_binary_tree()
print_binary_tree(tree.root)
print(traverse_using_stack(tree.root))