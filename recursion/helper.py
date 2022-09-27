
from os import lseek


def checkOdd(array):
    result = []

    def checkFirst(array):
        if len(array) == 0:
            return 
        
        if array[0] % 2 != 0:
            result.append(array[0])
        return checkFirst(array[1:])
    checkFirst(array)
    print(result)

def checkOddPure(array):
    
    if len(array) == 0:
        return 
    newArr = []

    if array[0] % 2 != 0:
        return newArr + checkOddPure(array[1:])
    else:
        checkOddPure(array[1:])

    


def collatz(n):
    steps = 0 
    def checkCollatz(n):
        if n == 1:
            return 1 
        if n%2 == 0:
            checkCollatz(n/2)
        else:
            checkCollatz((3*n) + 1)
        steps = steps + 1
    checkCollatz(n)
    return steps

collatz(5)
# checkOdd([1,2,3,4,5,6,7,8])