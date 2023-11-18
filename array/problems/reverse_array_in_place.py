"""
Reverse array in place.
Iterate from start to middle element - floor(length / 2)
swap current element with array length - 1 - current index
"""


def reverse_array_in_place(array: list[int]) -> None:
    array_length = len(array)
    last_index = array_length - 1
    for index in range(array_length // 2):
        array[index], array[last_index - index] = array[last_index - index], array[index]


array1 = [1, 2, 3]
reverse_array_in_place(array1)
assert array1 == [3, 2, 1]

array2 = [3, 4, 5, 6, 7, 87]
reverse_array_in_place(array2)
assert array2 == [87, 7, 6, 5, 4, 3]