from mytypes import NumberArray


def sort_by_merging(array: NumberArray) -> None:
    array_length = len(array)
    if array_length > 1:
        middle = array_length // 2
        left_subarray = array[:middle]
        right_subarray = array[middle:]

        sort_by_merging(left_subarray)
        sort_by_merging(right_subarray)

        i, j, k = 0, 0, 0
        while i < len(left_subarray) and j < len(right_subarray):
            if left_subarray[i] <= right_subarray[j]:
                array[k] = left_subarray[i]
                i += 1
            else:
                array[k] = right_subarray[j]
                j += 1
            k += 1

        while i < len(left_subarray):
            array[k] = left_subarray[i]
            i += 1
            k += 1

        while j < len(right_subarray):
            array[k] = right_subarray[j]
            j += 1
            k += 1


myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
sort_by_merging(myList)
print(myList)