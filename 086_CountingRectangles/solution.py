import math
import time

def CountRectangles(w,h):
    sum = 0
    w_r=1
    h_r=1
    dim = set()
    for w_r in range(1,w+1):
    
        for h_r in range(1,h+1):
            dim.add((w_r,h_r))

    for d in dim:
        w_c = w-d[0]+1
        h_c = h-d[1]+1
        sum += w_c*h_c


    return sum
def Solve():
    closestCount = 0 
    closestArea = 0

    w = 1
    h = 1
    newCount = 1

    for w in range(1,100):
        newCount = 1
        for h in range(w+1,100):
            lastCount = newCount
            newCount = CountRectangles(w,h)
            
            if abs(2_000_000 - newCount) < abs(2_000_000 - closestCount):
                closestCount = newCount
                closestArea = w*h
            elif abs(2_000_000 - newCount) > abs(2_000_000 - lastCount): break
                    
    return closestArea
        


start_time = time.time()
print(Solve())
print("Process finished --- %s seconds ---" % (time.time() - start_time)) 