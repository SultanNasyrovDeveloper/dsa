"""
Find max product of two elements in array
"""
from mytypes import NumberArray


def max_product(array: NumberArray) -> int:
    first_max = float('-inf')
    second_max = float('-inf')

    for number in array:
        if number > first_max:
            first_max, second_max = number, first_max
        elif number > second_max:
            second_max = number

    return (first_max - 1) * (second_max - 1)


print(max_product([3, 6, 1, 4, 18, 22]))