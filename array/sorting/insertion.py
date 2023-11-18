from mytypes import NumberArray


def sort_by_insertion(array: NumberArray) -> NumberArray:
    for index in range(1, len(array)):
        key = array[index]
        position = index
        while position > 0 and key < array[position - 1]:
            array[position] = array[position - 1]
            position -= 1
        array[position] = key
    return array


print(sort_by_insertion([44, 12, 35, 4, 2, 14]))