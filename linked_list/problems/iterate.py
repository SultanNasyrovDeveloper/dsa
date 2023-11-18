from collections.abc import Callable

from ..generator import generate_linked_list
from ..list import LinkedList, Node


def iterate_over_linked_linked_list(
    llist: LinkedList,
    callback: Callable[[Node]]
):
    current = llist.root
    while current:
        callback(current)
        current = current.next


llist = generate_linked_list()
iterate_over_linked_linked_list(llist)