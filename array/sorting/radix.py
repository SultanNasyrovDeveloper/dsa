from mytypes import NumberArray


def radixsort(array: NumberArray) -> NumberArray:

    # get max number from array
    max_number = float('-inf')
    for number in array:
        max_number = number if number > max_number else max_number
    max_number_length = len(str(max_number))

    return array