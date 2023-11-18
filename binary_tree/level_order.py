from queue import SimpleQueue
from binary_tree.node import Node


def traverse_level_order(root: Node) -> list:
    if root is None:
        return
    
    queue = SimpleQueue()
    queue.put(root)

    while not queue.empty(): ...

