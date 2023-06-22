import math

def arraySum(a):
    return sum(i for i in a)

#It is possible to write ten as the sum of primes in exactly five different ways:
# 7 + 3
# 5 + 5
# 5 + 3 + 2
# 3 + 3 + 2 + 2
# 2 + 2 + 2 + 2 + 2
#What is the first value which can be written as the sum of primes in over five thousand different ways?

# Reference:
# https://en.wikipedia.org/wiki/Partition_(number_theory)
#Project Euler Problem 77
def PrimeSummations():
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79]
    
    L, target = 5000, 11
    while True:
        ways = [1] + [0]*target
        for p in primes:
            for i in range(p, target+1):
                ways[i] += ways[i-p]
        if ways[target] > L: break    
        target += 1

    print("First value written as the sum of primes \nin over", L, "ways:", target)
            



PrimeSummations()

        
