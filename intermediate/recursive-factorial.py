'''Write a function factorial(n) that returns the factorial of
a non-negative integer n using recursion.
'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
# Test
print(factorial(0)) # 1
print(factorial(1)) # 1
print(factorial(2)) # 2
print(factorial(3)) # 6
print(factorial(4)) # 24
print(factorial(5)) # 120