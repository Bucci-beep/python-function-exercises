def apply_function(func, value):
    return func(value)

def max_value(numbers):
    return apply_function(max, numbers)

# Test
print(max_value([1, 12, 3, 4, 5])) # 12
print(max_value([1, 12, 3, 14, 5, 6])) # 14
print(max_value([1, 12, 3, 4, 15, 6, 7])) # 15
print(max_value([1, 12, 3, 4, 5, 16, 7, 8])) # 16
