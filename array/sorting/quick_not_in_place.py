from mytypes import NumberArray


def quicksort(array: NumberArray):
    array_length = len(array)
    if array_length <= 1:
        return array

    pivot = array[-1]
    less = []
    equals = [pivot]
    greater = []

    for item in array[:-1]:
        if item < pivot:
            less.append(item)
        elif item > pivot:
            greater.append(item)
        else:
            equals.append(item)
    return quicksort(less) + equals + quicksort(greater)


assert quicksort([3, 2, 5]) == [2, 3, 5]
assert quicksort([9, 2, 6, 3, 5, 1, 7, 8, 4]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
