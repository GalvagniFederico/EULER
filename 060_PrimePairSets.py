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

#print(isPrimePairSets([3,7,67,71,73]))

def del_list_inplace(l, id_to_del):
    for i in sorted(id_to_del, reverse=True):
       del(l[i])

def PrimePairSets():
    start_time = time.time()

    p_l = PrimeList(200)
    

    counter = [0,0,0]

    c = np.array(list(combinations(p_l,5)))
    
    doneSet = [False for i in range(len(c))]

    print("Found ", len(c), f" pairs in  {time.time() - start_time} seconds ---")

    
    for i in range(len(c)):
        if c[i]:
            continue
        
        process_time = time.time()
        ppsRes = IsPrimePairSets(x)
        print(f"Checked if is a Prime Pair Sets in {time.time() - process_time} seconds ---")

        if ppsRes != True:
            counter[0] += 1

            process_time = time.time()
            i_rem = [i for i in range(0, len(c)) if c[i].__contains__(ppsRes[0]) and c[i].__contains__(ppsRes[1])]
            print(f"Found all occurrences of failed set in {time.time() - process_time} seconds ---")

            process_time = time.time()
            c = np.delete(c,i_rem,0)
            
            print("Removed ",len(i_rem),f"occurrence of failed set in {time.time() - process_time} ---")

            continue

        if ppsRes(x):
            print("===================== RESULT FOUND =====================")
            print(sum(x))
            return sum(x)
    print(f"Process finished --- {time.time() - start_time} seconds ---")
    print("Rem Access ", counter[0])

print(PrimePairSets())

def test():
    arr = np.array([0,1,2,3,4,5,6,7,8,9])
    
    arr = np.delete(arr, [0,2,4])
    print(arr)
    
test()