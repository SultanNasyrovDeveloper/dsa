from mytypes import NumberArray


def sort_using_bubble(array: NumberArray):
    array_length = len(array)
    last_index = array_length - 1

    # Traverse through all array elements
    for i in range(array_length):
        swapped = False

        # Last i elements are already in place
        for j in range(0, last_index - i):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

        if not swapped:
            break
