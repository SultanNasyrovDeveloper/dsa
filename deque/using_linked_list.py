from __future__ import annotations
from typing import Any, Optional


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.previous = None
        self.next = None


class Deque:

    front: Optional[Node]
    tail: Optional[Node]
    size: int
    capacity: int

    def __init__(self, capacity: int = 10) -> None:
        self.front = None
        self.tail = None
        self.size = 0
        self.capacity = capacity

    def __str__(self):
        output = []
        current = self.front
        while current:
            output.append(current.data)
            current = current.next
        return str(output)

    def is_empty(self) -> bool:
        return not self.front

    def get_front(self) -> Optional[Node]:
        return self.front

    def get_tail(self) -> Optional[Node]:
        return self.tail

    def push(self, value: Any) -> None:
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def push_front(self, value: Any) -> None:
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
            self.tail = new_node
        else:
            new_node.next = self.front
            self.front.previous = new_node
            self.front = new_node
        self.size += 1

    def pop(self) -> Optional[Any]:
        if self.is_empty():
            return
        deleted = self.tail
        self.tail = deleted.previous
        if self.tail is None:
            self.front = None
        else:
            self.tail.next = None
        self.size -= 1
        return deleted.data

    def pop_front(self):
        if self.is_empty():
            return
        deleted = self.front
        self.front = deleted.next
        if self.front is None:
            self.tail = None
        else:
            self.front.previous = None
        self.size -= 1
        return deleted.data




