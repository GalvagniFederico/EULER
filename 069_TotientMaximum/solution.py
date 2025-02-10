import time
import array

def Solve(n):
    maxTotient=0
    nMaxTotient = 0
    phi = array.array('i', range(n+1))
    for i in range(2,n+1,1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] -= phi[j]//i

        nDivTot = i/phi[i]
        if nDivTot > maxTotient:
            maxTotient = nDivTot
            nMaxTotient = i
    
    return nMaxTotient

print(Solve(1_000_000))