'''
Write a function create_power_function(power) that returns a new function which, 
when called with a number, raises that number to the given power.
Hint: Similar to closures, have an inner function that uses the power from the outer function’s scope.
'''
def create_power_function(power):
    def power_function(number):
        return number ** power
    return power_function

square = create_power_function(2)
cube = create_power_function(3)

print(square(2))  # 4
print(cube(2))  # 8
print(square(3))  # 9
print(cube(3))  # 27