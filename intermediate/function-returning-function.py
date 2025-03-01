def make_multiplier(n):
    def multiplier(x):
        return n * x
    return multiplier

# Test
double = make_multiplier(2)
print(double(5)) # 10
print(double(10)) # 20

triple = make_multiplier(3)
print(triple(5)) # 15
print(triple(10)) # 30

quadruple = make_multiplier(4)
print(quadruple(5)) # 20
print(quadruple(10)) # 40
