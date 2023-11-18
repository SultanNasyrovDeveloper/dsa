"""
Given sorted array of integers(can be negative).
Return an array of sorted items.

Solutions:
- using sort
Time Complexity O(n log n)
Space complexity: Based on sorting algorithm

- using two lists and sort
Time Complexity

- using two pointers
create result array
create two pointer one pointing to the start of array and second to the end
on every step select the highest absolute value and put its square to result array
"""
from mytypes import NumberArray


def get_sorted_squares(array: NumberArray) -> NumberArray:
    """
    Separately calculate negative and positive squares into two arrays.
    Then merge them using algorithm similarly to mergesort merging.
    """
    result = []
    squares_of_negative_numbers = [number ** 2 for number in array if number < 0]
    squares_of_positive_numbers = [number ** 2 for number in array if number >= 0]

    squares_of_negative_numbers = squares_of_negative_numbers[::-1]

    i, j = 0, 0
    while i < len(squares_of_negative_numbers) and j < len(squares_of_positive_numbers):
        if squares_of_negative_numbers[i] <= squares_of_positive_numbers[j]:
            result.append(squares_of_negative_numbers[i])
            i += 1
        else:
            result.append(squares_of_positive_numbers[j])
            j += 1

    while i < len(squares_of_negative_numbers):
        result.append(squares_of_negative_numbers[i])
        i += 1

    while j < len(squares_of_positive_numbers):
        result.append(squares_of_positive_numbers[j])
        j += 1

    return result


print(get_sorted_squares([-5, -1, 0, 23]))
