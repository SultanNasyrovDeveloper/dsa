from mytypes import NumberArray


def sort_by_selection(array: NumberArray) -> NumberArray:
    array_length = len(array)
    for i in range(array_length):
        smallest_item_index = i
        for j in range(i + 1, array_length):
            if array[j] < array[smallest_item_index]:
                smallest_item_index = j
        array[i], array[smallest_item_index] = array[smallest_item_index], array[i]
    return array


print(sort_by_selection([66, 12, 35, 2, 89, 4, 17]))
