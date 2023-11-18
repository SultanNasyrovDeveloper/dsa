from random import randint

from .list import LinkedList, Node


def generate_linked_list(
    amount: int = 100,
    start: int = 0,
    sequential: bool = False,
) -> LinkedList:
    if amount == 0:
        return LinkedList()
    root = Node(
        randint(1, 100)
        if not sequential
        else start
    )
    current = root

    for number in range(start + 1, start + amount):
        node = Node(
            randint(1, 100)
            if not sequential
            else number
        )
        current.next = node
        current = node
    return LinkedList(root)
