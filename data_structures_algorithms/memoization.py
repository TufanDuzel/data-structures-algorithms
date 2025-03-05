# Fibonacci
def fib(n: int) -> int:
    x, y = 0, 1
    
    for i in range(n):
        x, y = y, x + y
        
    return x

# Dictionary - Memoization
memo = {}

def memoization(n):
    if n not in memo:
        memo[n] = fib(n)
        
    return memo[n]

myList = [5, 10, 15, 5, 20, 15, 5, 10, 5, 100, 10, 20, 15, 100, 5, 10]

for num in myList:
    print(memoization(num))