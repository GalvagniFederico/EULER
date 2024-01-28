# The cube 41063625 (345^3) can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3)
#In fact 41063625 (345^3) is the smallest cube which has exactly three permutations of its digits which are also cube.

# Find the smallest cube for which exactly five permutations of its digits are cube.

from itertools import combinations, permutations
import math
from decimal import Decimal
import time

def solution1(count):
    n = 1

    orderedPermutationsCount = {}

    while True:
        orderedPermutation = "".join(sorted(str(n**3)))

        if orderedPermutationsCount.__contains__(orderedPermutation):
            orderedPermutationsCount[orderedPermutation][0] += 1
            orderedPermutationsCount[orderedPermutation].append(n)
            if orderedPermutationsCount[orderedPermutation][0] == count:
                return min(orderedPermutationsCount[orderedPermutation][1:])**3
        else:
            orderedPermutationsCount[orderedPermutation] = [1, n]

        n+=1


st = time.time()
print(solution1(5))
print(f"Process finished --- {(time.time() - st)*1000} ms ---")

