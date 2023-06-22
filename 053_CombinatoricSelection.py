import math
import time


def Combinatoric(n,r):
    return (math.factorial(n))/(math.factorial(r)*math.factorial((n-r)))

def CombinatoricSelections():
    res = 0
    start_time = time.time()
    for n in range(23,101):
        f = False
        for r in range(2, n):
            if Combinatoric(n,r) > 1_000_000:
                f = True
                res+=1
            else:
                if f:
                    break
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
    return res


#print(CombinatoricSelections())
print( Combinatoric(100,5))








