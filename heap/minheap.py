from __future__ import annotations
from mytypes import Comparable


class MinHeap[Item: Comparable]:

    data: list[Item]
    size: int

    def __init__(self):
        self.data = []

    @classmethod
    def heapify[Element: Item](cls, array: list[Element]) -> MinHeap:
        heap = cls()
        heap.data = array
        for index in range(len(heap.data), 0, -1):
            heap._shift_down(index)
        return heap

    def _shift_up(self, index: int) -> None:
        parent = (index - 1) // 2
        while index > 0 and self.data[index] < self.data[parent]:
            self.data[parent], self.data[index] = self.data[index], self.data[parent]
            index = parent
            parent = (index - 1) // 2

    def _shift_down(self, index: int) -> None:
        array_length = len(self.data)
        while index < array_length:
            smallest = index
            left = (index * 2) + 1
            right = (index * 2) + 2

            if left < array_length and self.data[left] < self.data[smallest]:
                smallest = left
            if right < array_length and self.data[right] < self.data[smallest]:
                smallest = right
            if smallest == index:
                break

            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            index = smallest

    def push(self, item: Item) -> None:
        """
        Insert element in the end of list. 
        """
        self.data.append(item)
        self._shift_up(len(self.data) - 1)

    def pop(self) -> Item:
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        return_value = self.data.pop()
        self._shift_down(0)
        return return_value




