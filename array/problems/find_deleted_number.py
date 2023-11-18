"""
Given an array of numbers starting from 1 to n.
Array is not sorted and some number was deleted. Find number that was deleted from array.

Considerations:
0 < n > array.length + 1

1 - time complexity(n log n) space complexity (1)
- sort array
- iterate over array starting from the second element
- if current element is greater that previous by more than 1 it means result is previous item + 1

2 - time complexity(n), space complexity(n)
iterate over list and put all items into the set
then iterate over number starting from 1 to array length + 1
on every step check if number in set.
if item is not in the set that it is the target

3 - subtract sum of elements in array with sum of math progression
"""
from mytypes import NumberArray


def find_deleted_number(array: NumberArray) -> int:
    return ((len(array) + 1) * (len(array) + 2) // 2) - sum(array)


assert find_deleted_number([1, 2, 4]) == 3
assert find_deleted_number([])