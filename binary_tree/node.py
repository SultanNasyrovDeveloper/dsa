from __future__ import annotations

from typing import Any, Optional


class Node[Value: Any]:

    def __init__(self, value: Value) -> None:
        self.value: Value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def __str__(self) -> str:
        return str(self.value)
