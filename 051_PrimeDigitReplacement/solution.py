from utilities import isPrime, NextPrime, SieveOfEratosthenes
import itertools
import time


def solve():    
    n = 3
    subIndexesComb =[[[0],[0]],[[0],[0]]]
    n_len = len(str(n))
    primeIndex = 1
    primes = {}
    for p in SieveOfEratosthenes(9999999):
        primes[p] = False


    for l in range(2,7):
        newSub=[]
        for i in range(1,l):
            newSub.append(list(itertools.combinations([int(j) for j in range(0,l+1)],i)))
        subIndexesComb.append(newSub)

    for n in primes:
        if primes[n]: continue
        n_len = len(str(n))
        primeToCheck = []
        
        for i in range(n_len-1, 0, -1):
            for subIndexes in subIndexesComb[n_len][i-1]:
                if n_len-1 in subIndexes:continue
                numberOfPrimes = 0
                for sub in range(0,10):
                    sI=str(n)
                    for index in subIndexes: 
                        sI = sI[:index] + str(sub) + sI[index+1:]
                    if isPrime(int(sI)) and sI[0] != "0":
                        primeToCheck.append(int(sI))
                        numberOfPrimes+=1

                if numberOfPrimes == 8:
                    return n

        for p in primeToCheck:
            primes[p]=True
            
start_time = time.time()
print(solve())
print("Process finished --- %s seconds ---" % (time.time() - start_time)) 