from utilities import PrimeList, isPrime
from itertools import combinations
import time

# 060 - Prime Pair Sets

# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will
# always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents
# the lowest sum for a set of four primes with this property.
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

# I could store copies that failed to be pairsets so i don't need to process next sets containing them

def isPrimePairSets(set):
    l = len(set)
    if  l%2 == 0:
        l = int( l/2)
    else:
        l = int(( l+1)/2)
    

    for i in range(0, l):
        for j in range(i+1, len(set)):
            if i == j:
                continue
            a = int(str(set[i]) + str(set[j]))
            b = int(str(set[j]) + str(set[i]))
            if not isPrime(a) or not isPrime(b):
                return [set[j], set[i]]
    return True

print(isPrimePairSets([3,7,67,71,73]))

def PrimePairSets():
    start_time = time.time()
    p_l = PrimeList(100)

    failedSets = [[2,5],[2,5]]

    c = []
    c.extend(combinations(p_l,5))
    print("Found ", len(c), " pairs in  %s seconds ---" % (time.time() - start_time))

    for x in c:
        if sum(x)%3 == 0:
            continue
        found = False
        for z in range(0, len(failedSets)):
            if x.__contains__(failedSets[z][0]) or x.__contains__(failedSets[z][1]):
                break
        if

        b = isPrimePairSets(x)

        if b != True:
            failedSets.append(b)
            continue

        if isPrimePairSets(x):
            print("===================== RESULT FOUND =====================")
            print(sum(x))
            return sum(x)
    print("Process finished --- %s seconds ---" % (time.time() - start_time))


print(PrimePairSets())