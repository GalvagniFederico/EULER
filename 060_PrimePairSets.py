from utilities import PrimeList, isPrime
from itertools import combinations
import time
import numpy as np

# 060 - Prime Pair Sets

# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will
# always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents
# the lowest sum for a set of four primes with this property.
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

# I could store copies that failed to be pairsets so i don't need to process next sets containing them

def IsPrimePairSets(set):
    l = len(set)
    if  l%2 == 0:
        l = int( l/2) +1
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

def IsPrimePairSets2(set):
    for i in range(0, len(set)):
        for j in range(i+1, len(set)):
            if i == j:
                continue
            a = int(str(set[i]) + str(set[j]))
            b = int(str(set[j]) + str(set[i]))
            if not isPrime(a) or not isPrime(b):
                return False
    return True

#print(IsPrimePairSets([3, 11, 2069, 2297, 8219]))

def PrimePairSets():
    start_time = time.time()

    p_l = PrimeList(1000)

    c = list(combinations(p_l,5))
    
    doneSet = [False for i in range(len(c))]

    print("Found ", len(c), f" pairs in  {time.time() - start_time} seconds ---")

    
    for i in range(len(c)):
        if doneSet[i]:
            continue

        process_time = time.time()
        ppsRes = IsPrimePairSets(c[i])
       
        if ppsRes != True:
            rem_count = 0
            for j in range(i, len(c)):
                if c[j].__contains__(ppsRes[0]) and c[j].__contains__(ppsRes[1]):
                    doneSet[j] = True
                    rem_count +=1
                else:
                    break

            print(f"Checked if set ", i, f"is a Prime Pair Sets in {time.time() - process_time} seconds ---")
            print(f"Remove {rem_count} sets")
            #process_time = time.time()
            #i_rem = [i for i in range(0, len(c)) if c[i].__contains__(ppsRes[0]) and c[i].__contains__(ppsRes[1])]
            #print(f"Found all occurrences of failed set in {time.time() - process_time} seconds ---")

            # process_time = time.time()
            # c = np.delete(c,i_rem,0)
            
            # print("Removed ",len(i_rem),f"occurrence of failed set in {time.time() - process_time} ---")

            continue

        if ppsRes:
            print("===================== RESULT FOUND =====================")
            print(sum(c[i]))
            print(c[i])
            return sum(c[i])
    print(f"Process finished --- {time.time() - start_time} seconds ---")
    
#print(PrimePairSets())

# def IsPrimeCouple(a,b):
#     return isPrime(int(str(a) + str(b))) and isPrime(int(str(b) + str(a)))

def PrimePairSets_PartialCombinations():
    pl = PrimeList(10000)

    for a in range(len(pl)):

        for b in range(a+1,len(pl)):
            if IsPrimePairSets2([pl[a],pl[b]]):

                for c in range(b+1, len(pl)):
                    if IsPrimePairSets2([pl[a],pl[b],pl[c]]):

                        for d in range(c+1, len(pl)):
                            if IsPrimePairSets2([pl[a],pl[b],pl[c],pl[d]]):

                                for e in range(d+1, len(pl)):
                                    if IsPrimePairSets2([pl[a],pl[b],pl[c],pl[d],pl[e]]):
                                        print([pl[a],pl[b],pl[c],pl[d], pl[e]])
                                        print(sum([pl[a],pl[b],pl[c],pl[d], pl[e]]))
                                        return

    

PrimePairSets_PartialCombinations()