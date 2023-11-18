from mytypes import Comparable


class Node[Value: Comparable]:

    def __init__(self, value: Value) -> None:
        self.value = value
        self.left = None
        self.right = None
