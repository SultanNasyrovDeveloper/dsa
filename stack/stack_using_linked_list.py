from __future__ import annotations
from typing import Optional


class Node[Value]:

    def __init__(self, value: Value) -> None:
        self.value = value
        self.next = Node[Value]


class Stack[Value]:
    def __init__(self, head: Optional[Node[Value]]) -> None:
        self.head = head
