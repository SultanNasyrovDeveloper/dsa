from __future__ import annotations

from typing import Any, Optional


class QueueNode:
    value: Any
    node: Optional[QueueNode]

    def __init__(self, value: Any, _next: Optional[QueueNode] = None):
        self.value = value
        self.next = _next


class Queue:
    """
    Queue implementation using Linked List with tail pointer.
    """
    root: Optional[QueueNode]
    tail: Optional[QueueNode]
    capacity: int
    size: int

    def __init__(self, root: Optional[QueueNode] = None, capacity: int = 10):
        self.root = root
        self.tail = root
        self.capacity = capacity
        self.size = 1 if root else 0

    def enqueue(self, value):
        if not self.root:
            new_node = QueueNode(value)
            self.root = new_node
            self.tail = new_node
        else:
            self.root = QueueNode(value, self.root)
        self.size += 1

    def dequeue(self) -> Any:
        if not self.root:
            return
        dequeued = self.root
        self.root = self.root.next
        if self.tail == dequeued:
            self.tail = None
        self.size -= 1
        return dequeued.value


