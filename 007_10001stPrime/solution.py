import math

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def CheckIfPrime(n):
    if n < 0: return False
    if n == 1 or n == 0:
        return False
    for i in range(2, math.floor(n/2)+1):
        if n % i == 0:
            return False
    return True

def FindIndexPrime(th):
    primelist = []
    i = 2
    while not len(primelist) == th:
        if CheckIfPrime(i):
            primelist.append(i)
        i += 1
    return primelist[-1]

print(FindIndexPrime(10001))
