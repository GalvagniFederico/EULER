import math
import time

# The number, 197, is called a circular prime because all rotations of the digits:
# 197, 971, and 719, are themselves prime.
# How many circular primes are there below one million?

def CheckIfPrime(n):
    if n < 0: return False
    if n == 1 or n == 0:
        return False
    for i in range(2, math.floor(n/2)+1):
        if n % i == 0:
            return False
    return True

def SievePrimeArray(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False
    p = 2
    while p*p <= n:
        if prime[p] == True:
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1
    return prime

def circularPrime(n):
    start_time = time.time()
    p = SievePrimeArray(n)
    count = len(p) + 2  # +2 because 2 and 5 wouldn't be counted

    for i in range(len(p)):
        s = str(p[i])
        if s.__contains__("2") or s.__contains__("0") or s.__contains__("8") or s.__contains__("6") or s.__contains__("4") or s.__contains__("5"):
            count -= 1
            continue
        for j in range(0, len(s)):
            if not CheckIfPrime(p[i]):
                count -= 1
                break
            # rotation
            s = s[1:len(s)] + s[0]

    print("Process finished --- %s seconds ---" % (time.time() - start_time))
    print(count)

circularPrime(1000000)
