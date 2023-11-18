from typing import Optional

from mytypes import NumberArray


def partition(array: NumberArray, low: int, high: int) -> int:
    """
    Solution
        - select pivot
        - partition all elements in array that less in left side
        - and put pivot point in the middle
    """
    pivot = array[high]
    last_less = low
    for j in range(low, high):
        if array[j] <= pivot:
            array[last_less], array[j] = array[j], array[last_less]
            last_less += 1
    array[last_less], array[high] = array[high], array[last_less]
    return last_less


def quicksort(
    array: NumberArray,
    low: int = 0,
    high: Optional[int] = None
) -> None:
    high = high or len(array) - 1
    if low < high:
        high = high or len(array) - 1
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index - 1)
        quicksort(array, pivot_index + 1, high)


test = [1, 2, 3, 4, 5]
partition(test, 0, len(test) - 1)
print(test)