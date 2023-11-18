from __future__ import annotations
from typing import Any


class MaxHeap[Item: Any]:

    data: list[Item]

    def __init__(self):
        self.data = []

    def shift_up(self, index: int) -> None:
        current = index
        parent = (index - 1) // 2
        while current > 0 and self.data[index] > self.data[parent]:
            self.data[parent], self.data[current] = self.data[current], self.data[parent]
            current = parent
            parent = (current - 1) // 2
        # until parent node is smaller than current,
        # or you run out of list
        # change given node with parent


    def ship_down(self, index: int):
        pass

    def insert(self, new_value: Item) -> None:
        """
        To insert an element array:
        - first insert it in the end of array
        - then tickle it up by comparing it with parent and swapping
        """
        self.data.append(new_value)
        new_value_index = len(self.data) - 1
        is_stop = False
        while new_value_index // 2 > 0 and not is_stop:
            if self.data[new_value_index] > self.data[new_value_index // 2]:
                self.data[new_value_index], self.data[new_value_index // 2] = \
                    self.data[new_value_index // 2], self.data[new_value_index]
            else:
                is_stop = True
            new_value_index = new_value_index // 2

    def pop(self) -> Item:
        ...

    @classmethod
    def heapify(cls, values: list[Item]) -> MaxHeap[Item]:
        pass