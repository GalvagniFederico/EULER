import math
import time
from utilities import PrimeList, isPrime

# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
# 9—7+2x1'
# = X 22
# 15
# 3+2 x 32
# 21
# 25 — 7 + 2 X 32
# 27 = 19+2 x 22
# 33 = 31 +2 x 12
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

def nextCompisiteOdd(n):
    while True:
        n+=1
        if not isPrime(n) and n%2==1:
            return n


def GoldbachOtherConjecture():
    primes = PrimeList(1000000)

    p1 = 0
    p2 = 0
    pw = [pow(i,2) for i in range(1,1000000)]

    pwI = 0
    n = 9

    

    while True:
        found = False
        p1=0
        while primes[p1] < n:
            p2=0
            while primes[p1] + primes[p2] <= n:
                pwI = 0
                while primes[p1] + (primes[p2]*pw[pwI]) <= n:
                    if (primes[p1] + (primes[p2]*pw[pwI])) == n:
                        found = True
                        break
                    pwI +=1
                
                if found:
                    break
                p2+=1

            if found:
                break
            p1+=1
        
        if not found:
            return n
        else:
            print(n)
        
        n = nextCompisiteOdd(n)

def GoldbachOtherConjecture2():
    primes = PrimeList(1000000)

    p1 = 0
    p2 = 0
    pw = [pow(i,2) for i in range(1,1000000)]

    pwI = 0
    n = 9

    

    while True:
        found = False
        pwI=0
        while pw[pwI] < n:
            p2=0
            while primes[p2]*pw[pwI] < n:
                p1 = 0
                while primes[p1] + (primes[p2]*pw[pwI]) <= n:
                    if (primes[p1] + (primes[p2]*pw[pwI])) == n:
                        found = True
                        break
                    p1 +=1
                
                if found:
                    break
                p2+=1

            if found:
                break
            pwI+=1
        
        if not found:
            return n
        else:
            print(n)
        
        n = nextCompisiteOdd(n)


#print(GoldbachOtherConjecture())

def GenerateOddNonPrimes(n):
    res = []
    while True:
        n+=1
        if not isPrime(n) and n%2==1:
            res.append(n)
    
def GenerateComposite(n):
    res = []

    p = PrimeList(n)
    pw = []

    x = 1
    while True:
        pw_n = pow(x,2)

        if pw_n > n:
            break
        pw.append(pw_n)
        x +=1

    for p1 in range(len(p)):
        for p2 in range(p1,len(p)):
            for p3 in range(len(pw)):
                r =  (p1 + (p2*p3))

                if isPrime(r) and r%2==1:
                    res.append(r)

    return res



print(GenerateComposite(1000))


def GoldbachOtherConjecture3():
    oddNPrimes = GenerateOddNonPrimes(1000)
    composite = GenerateComposite(1000)
