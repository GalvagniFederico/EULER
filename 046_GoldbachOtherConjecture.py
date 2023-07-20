import math
import time
from utilities import PrimeList, isPrime

# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

def GenerateOddNonPrimes(n):
    res = []
    i = 3
    while i<=n:
        
        if not isPrime(i):
            res.append(i)
        i+=2
    return res
    
def GenerateComposite(n, p):
    res = {}
    limit = int(math.sqrt(n)*2) +1

    for p1 in range(0,len(p)):
            for p3 in range(0,limit):
                r =  (p[p1] + (2*(p3*p3)))
                if r > n :
                    break
                res[r] = 1
    return res

def GoldbachOtherConjecture3():
    start_time = time.time()

    n = 10000
    composite = GenerateComposite(n, PrimeList(n))
    oddNPrimes = GenerateOddNonPrimes(n)

    for x in oddNPrimes:
            if not composite.__contains__(x):
                print(f"Process finished --- {time.time() - start_time} seconds ---")
                return x

print(GoldbachOtherConjecture3())
