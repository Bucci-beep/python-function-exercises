'''Write a function greet(name, greeting="Hello") that prints a greeting message. 
If no greeting is provided, it should default to "Hello".'''

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Test
greet("Alice") # Hello, Alice!
greet("Alice", "Hi") # Hi, Alice!
greet("Alice", "Good morning") # Good morning, Alice!
greet("Alice", "Good evening") # Good evening, Alice!
greet("Alice", "Good night") # Good night, Alice!

