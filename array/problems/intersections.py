"""
given two arrays with number
Return third array that contains elements that appear in both arrays.

Solutions:
- brute force nested loop O(n^2)

- sorting and two pointers
sort both arrays
initialize two pointers

- dicts
iterate over first array and count number of each element in array.
iterate over second array and if element in counter map than put it into result array
lower count of current element in counter

Time Complexity: O(nk)
Space Complexity: O(n)

"""
from mytypes import NumberArray


def intersections(first: NumberArray, second: NumberArray) -> NumberArray:
    counter = {}
    result = []

    for item in first:
        counter[item] = counter.get(item, 0) + 1
    for item in second:
        if counter.get(item, 0) > 0:
            result.append(item)
            counter[item] -= 1
    return result


print(intersections([1, 2, 3], [2, 3, 4, 5]))