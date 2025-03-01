# a function is_even(n) that returns True if n is even and False if it's odd.

def is_even(num):
    return num % 2 == 0

def is_odd(num):
    return num % 2 != 0

num = 5
if is_even(num):
    print(True)
else:
    print(False)
