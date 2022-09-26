def binarySearch(array, value):

    left = 0 
    right = len(array) - 1
    middle = int((left + right)/2)

    while left < right and array[middle] != value:
        if array[middle] > value:
            right = middle - 1
        else:
            left = middle + 1 
        middle = int((left + right)/2)
    
    if array[middle] == value:
        return True
    return False

print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 21))
