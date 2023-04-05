import math
def FactiorialSum(n):
    return sum([int(i) for i in str(math.factorial(n))])

print(FactiorialSum(100))
