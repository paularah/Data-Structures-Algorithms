def countDown(n):
    if n <= 0:
        return 
    countDown(n-1)
    print(n)

def sumRange(n):
    if n == 1:
        return 1
    return n + sumRange(n-1)
    

def factorial(n):
    if n == 1:
        return 1 
    return n * factorial(n-1)

print(factorial(3))
# def collatz(n):
    
#     getCol

# print(sumRange(4))
# countDown(4)