import math
import time


    

def Solve(L):
    start_time = time.time()
    count = 0 
    
    comb = [0 for i in range(L+1)]
    for m in range(2, int(math.sqrt(L)), 1):
        for n in range(1,m,1):

            if (m+n)%2 != 1:
                continue
            if math.gcd(m,n) != 1:
                continue
            
            a = m**2-n**2
            b = 2*m*n
            c = m**2+n**2
            sum = a+b+c
            k=1

            kSum = k*sum
            while kSum <= L:
                comb[kSum]+=1
                k+=1
                kSum = k*sum


    for i in range(len(comb)):
        if comb[i] == 1:
            count+=1
    
    print(f"Process finished --- {time.time() - start_time} seconds ---")
    return count


print(Solve(1_500_000))
