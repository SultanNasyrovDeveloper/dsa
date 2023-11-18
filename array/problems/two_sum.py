"""
Given an array of integers.
Find indexes of two values such that they add up to a target value.
Target value if given as a second attribute to a function. You can not use the same element twice.

Solutions:
- brute force
Scan through all possible combinations using nested loop technique
Time complexity: O(n**2)
Space complexity: O(1)

- one pass
Time Complexity: O(n)
Space complexity: O(n)
"""
from mytypes import NumberArray


def find_two_sum_quadratic(array: NumberArray, target: int) -> tuple[int, int]:
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] + array[j] == target:
                return i, j
    return -1, -1


def bubble_sort(array) -> None:
    array_length = len(array)
    for i in range(array_length - 1):
        is_swapped = False
        for j in range(array_length - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        if not is_swapped:
            return


def find_two_sum_using_sorting(array: NumberArray, target: int) -> tuple[int, int]:
    bubble_sort(array)
    print(array)
    low, high = 0, len(array) - 1
    while low < high:
        if array[low] + array[high] == target:
            return low, high
        elif array[low] + array[high] > target:
            high -= 1
        else:
            low += 1
    return -1, -1


test1 = [3, 4, 1, 36, 7, 22]
target1 = 37
expected1 = 2, 3
assert find_two_sum_quadratic(test1, target1) == expected1
print(find_two_sum_using_sorting(test1, target1))
assert find_two_sum_using_sorting(test1, target1) == expected1

assert find_two_sum_quadratic(test1, 100) == (-1, -1)
assert find_two_sum_using_sorting(test1, target1) == (-1, -1)
print('All tests passed')
