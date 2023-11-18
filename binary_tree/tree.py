from __future__ import annotations
from collections.abc import Callable
from random import randint
from typing import Optional

from binary_tree.node import Node
from binary_tree.utils import print_binary_tree


class BinaryTree:
    def __init__(self, root: Optional[Node]):
        self.root: Optional[Node] = root

    @classmethod
    def generate_binary_tree(cls) -> BinaryTree[int]:
        root = Node(randint(1, 100))
        root.left = Node(randint(1, 100))
        root.right = Node(randint(1, 100))
        root.left.left = Node(randint(1, 100))
        root.left.right = Node(randint(1, 100))
        root.right.left = Node(randint(1, 100))
        root.right.right = Node(randint(1, 100))
        return BinaryTree(root)

    def print(self, node, level: int = 0):

        if node is not None:
            self.print(node.left, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.value))
            self.print(node.right, level + 1)

    def traverse_level_order(self):
        pass


