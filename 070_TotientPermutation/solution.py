import time
import math
import array
from collections import Counter

def Solve(n):
    start_time = time.time()
    phi = array.array('i', range(n+1))

    minPermTotient = n
    nMinPermTotient = 0

    for i in range(2,n+1,1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] -= phi[j]//i
        
        nDivTot = i/phi[i]
        if nDivTot < minPermTotient:

            # Check if its a permutation
            iList = ''.join(sorted(str(i)))
            phiList = ''.join(sorted(str(phi[i])))

            if iList == phiList:
                minPermTotient=nDivTot
                nMinPermTotient = i

    print(f"Process finished --- {time.time() - start_time} seconds ---")
    return nMinPermTotient, minPermTotient


print(Solve(1_000_000))
