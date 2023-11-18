"""
Given an array of numbers.
For each item find number of elements in array that smaller.

Solutions:
- brute force O(n^2)/O(1)
for each element in array
iterate over whole array and calculate number of number that smaller

- sorted list and counter dict O(n)/O(n)
sort the array
iterate over sorted list and save its index in counter dict
this will be number of element that smaller
that iterate over input array and for every element
get number of smaller elements
"""
from mytypes import NumberArray


def quicksort(array):

    if len(array) <= 1:
        return array

    pivot = array[-1]
    less = []
    equals = [pivot]
    greater = []

    for i in range(len(array) - 1):
        if array[i] > pivot:
            greater.append(array[i])
        elif array[i] < pivot:
            less.append(array[i])
        else:
            equals.append(array[i])
    return quicksort(less) + equals + quicksort(greater)


def count_smaller_than_current(array: NumberArray) -> NumberArray:
    sorted_array = quicksort(array)
    counter = {}
    for i in range(len(sorted_array) - 1, -1, -1):
        counter[sorted_array[i]] = i

    result = []
    for i in array:
        result.append(counter[i])
    return result

