from utilities import PrimeList, isPrime
from itertools import combinations
import time

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
                return False
    return True

print(isPrimePairSets([3,7,67,71,73]))

def PrimePairSets():
    start_time = time.time()
    p_l = PrimeList(200)
    p_l.remove(2)
    p_l.remove(5)

    c = []
    c.extend(combinations(p_l,5))
    print("Found ", len(c), "in  %s seconds ---" % (time.time() - start_time))

    for x in c:
        if sum(x)%3 == 0:
            continue

        if isPrimePairSets(x):
            print("===================== RESULT FOUND =====================")
            print(sum(x))
            return sum(x)
    print("Process finished --- %s seconds ---" % (time.time() - start_time))


print(PrimePairSets())