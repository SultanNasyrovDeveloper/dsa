"""
Given an of integer that is strictly increasing at first and then maybe decreasing.
Find a peak. EG maximum element in the array.

Solutions:
- linear search
Time Complexity: O(n)
Space Complexity: O(1)
- iterate over array and save max element in some variable.
- if next item in the array is smaller than current this is the peak

- binary search
"""
from typing import Optional

from mytypes import NumberArray


def find_peak_linear(array: NumberArray) -> Optional[int]:
    if len(array) == 0:
        return None
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return array[i]
    return array[-1]


def find_peak_binary(array: NumberArray) -> Optional[int]:
    if len(array) == 0:
        return

    low, high = 0, len(array) - 1
    while low < high:
        middle = (low + high) // 2
        # if next element after middle is smaller and previous is smaller
        # you found a target

        # if next is greater set low to middle + 1
        # if next is smaller and previous is lower
        if array[middle] > array[middle + 1]:
            if array[middle - 1] < array[middle]:
                return array[middle]
            else:
                high = middle - 1
        else:
            low = middle + 1
    return array[-1]


test1 = [2, 5, 7, 12, 22, 14, 11, 9, 7, 6, 5]
target1 = 22
assert find_peak_linear(test1) == target1
assert find_peak_binary(test1) == target1

test2 = [1, 2, 3, 4, 5]
target2 = 5
assert find_peak_linear(test2) == target2
assert find_peak_binary(test2) == target2

assert find_peak_linear([]) is None
assert find_peak_binary([]) is None


