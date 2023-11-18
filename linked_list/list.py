from typing import Optional
from .node import Node


class LinkedList:

    head: Optional[Node]

    def __init__(self, head: Optional[Node] = None):
        self.head = head
        self._current = head

    def __iter__(self):
        self._current = self.head
        return self

    def __next__(self):
        if not self._current.next:
            raise StopIteration
        current_tmp = self._current
        self._current = self._current.next
        return current_tmp
