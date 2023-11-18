from __future__ import annotations
from typing import Any, Optional


class Node:

    next: Optional[Node]
    value: Any

    def __init__(self, value: Any):
        self.next = None
        self.value = value

    def __str__(self):
        return str(self.value)
