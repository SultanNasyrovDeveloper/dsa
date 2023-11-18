import pytest
from heapq import heapify

from heap.generator import generate_min_heap
from heap.minheap import MinHeap


@pytest.fixture
def minheap() -> MinHeap:
    array = [i for i in range(100)]
    heapify(array)
    heap = MinHeap()
    heap.data = array
    return heap
