"""
Given an array of integers.
Find element that majority element. Majority element is that appears more than length / 2 times.

Solution:
- using sorting: O(n log n)/ O(1)
- using hashmap: O(n)/O(n)
- using moore voting algorithm: O(n)/ O(1)

"""
from mytypes import NumberArray


def find_majority_element(array: NumberArray) -> int:
    counter = 1
    majority_element = array[0]
    for item in array[1:]:
        if item == majority_element:
            counter += 1
        else:
            counter -= 1
            if counter <= 0:
                counter = 1
                majority_element = item
    return majority_element


test1 = [1, 3, 1, 1, 4, 1, 1, 5, 1, 1, 6, 2, 2]
expected1 = 1
print(find_majority_element(test1))
assert find_majority_element(test1) == expected1

test2 = [3, 2, 3]
expected2 = 3
assert find_majority_element(test2) == expected2

test3 = [10, 9, 9, 9, 10]
expected3 = 9
assert find_majority_element(test3) == expected3
