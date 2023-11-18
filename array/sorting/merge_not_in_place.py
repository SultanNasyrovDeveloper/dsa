from mytypes import NumberArray


def sort_by_merging(array: NumberArray) -> NumberArray:
    array_length = len(array)
    if array_length <= 1:
        return array

    middle = array_length // 2
    left_subarray = array[:middle]
    right_subarray = array[middle:]

    sorted_array = []
    left_subarray = sort_by_merging(left_subarray)
    right_subarray = sort_by_merging(right_subarray)

    i, j = 0, 0
    while i < len(left_subarray) and j < len(right_subarray):
        if left_subarray[i] <= right_subarray[j]:
            sorted_array.append(left_subarray[i])
            i += 1
        else:
            sorted_array.append(right_subarray[j])
            j += 1

    while i < len(left_subarray):
        sorted_array.append(left_subarray[i])
        i += 1

    while j < len(right_subarray):
        sorted_array.append(right_subarray[j])
        j += 1
    return sorted_array


myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(sort_by_merging(myList))