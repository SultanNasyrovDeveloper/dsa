from heapq import heapify


def generate_max_heap(size: int): ...


def generate_min_heap(size: int):
    array = [i for i in range(size)]
    heapify(array)
    return array
