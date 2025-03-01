# Function that returns the maximum value of a list of numbers

def max_value(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max

# Test
print(max_value([1, 12, 3, 4, 5])) # 5