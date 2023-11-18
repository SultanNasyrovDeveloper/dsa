"""
Given a list of integers.
Find the highest product of three integers from that array
"""
from typing import Optional
from mytypes import NumberArray


def merge_sort(array: NumberArray):
    array_length = len(array)
    if array_length <= 1:
        return array

    middle = array_length // 2
    left_subarray = array[:middle]
    right_subarray = array[middle:]

    merge_sort(left_subarray)
    merge_sort(right_subarray)

    i, j, k = 0, 0, 0

    while i < len(left_subarray) and j < len(right_subarray):
        if left_subarray[i] <= right_subarray[j]:
            array[k] = left_subarray[i]
            i += 1
        else:
            array[k] = right_subarray[j]
            j += 1
        k += 1

    while i < len(left_subarray):
        array[k] = left_subarray[i]
        i += 1
        k += 1

    while j < len(right_subarray):
        array[k] = right_subarray[j]
        j += 1
        k += 1


def max_product_of_three(array: NumberArray) -> Optional[int]:
    if len(array) < 3:
        return None
    # sort the array
    merge_sort(array)
    # get product of last three elements
    product_of_last_three = array[-1] * array[-2] * array[-3]
    # get product of first two element ain case there are any negative number
    product_of_first_two_and_last = array[0] * array[1] * array[-1]
    # return max from these two numbers
    return max(product_of_last_three, product_of_first_two_and_last)


assert max_product_of_three([]) is None
assert max_product_of_three([5, 1, 3, 4]) == 60
assert max_product_of_three([2, -5, -4, 2, 3]) == 60
