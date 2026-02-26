import math

# Find the product of the coefficients, a and b, for the quadratic expression n^2 + an + b
# that produces the maximum number of primes for consecutive values of n, starting with n = 0.

def CheckIfPrime(n):
    if n < 0: return False
    if n == 1 or n == 0:
        return False
    for i in range(2, math.floor(n/2)+1):
        if n % i == 0:
            return False
    return True

def QuadraticPrimes(num):
    max_pair = (0, 0, 0)
    for a in range(-num, num):
        for b in range(-num, num):
            n, count = 0, 0
            while True:
                v = n*n + a*n + b
                if CheckIfPrime(v): count = count + 1
                else: break
                n = n + 1
            if count > max_pair[2]:
                max_pair = (a, b, count)

    print(max_pair[0] * max_pair[1])

QuadraticPrimes(1001)
