from dynamic_array import DynamicArray


# Checks if a val in present in an array
def contains(array, val):
    for i in range(array.arr_len()):
        if array.arr_get(i) == val:
            return True
    return False


def reverse(array):
    # get the index of the last element in the array
    index = array.arr_len() - 1
    # creates a new array object to save the reverse copy of the initial array
    new = DynamicArray()
    # loops through the array in reverse and sets the values to the new arr
    for i in range(array.arr_len()):
        new.arr_set(i, (array.arr_get(index)))
        index -= 1
    # loops through the reverse copy and sets the values back to the original array
    for i in range(array.arr_len()):
        array.arr_set(i, new.arr_get(i))
    # Deletes the new array from memory
    del new
    # alternatively simply set new to None
    return array.values


def insert(array, val, index):
    # Push every other element in the array one place index upward until the index
    for i in range(array.arr_len(), index, -1):
        array.arr_set(i, array.arr_get(i - 1))
    # set value at the new space created
    array.arr_set(index, val)
    return array.values
