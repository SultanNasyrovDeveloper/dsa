from typing import Optional


class Node[Value]:
    def __init__(self, value: Value) -> None:
        self.value = value
        self.next: Optional[Node] = None