import math

# Let d(n) be defined as the sum of proper divisors of n.
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair.
# Evaluate the sum of all the amicable numbers under 10000.

def SumOfProperDivisors(n):
    sum = 0
    for i in range(math.floor(n/2), 0, -1):
        if n % i == 0:
            sum += i
    return sum

def sOD(x):
    s = 1
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            s += i
            s += x / i
    return s

def AmicableNumber(n):
    dn = []
    sum = 0
    for i in range(n):
        dn.append(SumOfProperDivisors(i))
    
    for i in range(n):
        for j in range(i, n):
            if dn[i] == j and i == dn[j] and i != j:
                print(i, j)
                sum += dn[i] + dn[j]
    return sum

def AmicableNumber2(n):
    dn = []
    sum = 0
    for i in range(1, n):
        j = sOD(i)
        if sOD(j) == i and i != j:
            sum += i
    return sum

print(AmicableNumber2(10000))
