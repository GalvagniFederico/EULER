import time

def DistinctPower(n):
    return len({a**b:True for a in range(2,n+1) for b in range(2,n+1)})
    

# start_time = time.time()
# print(DistinctPower(1000))
# print("Process finished --- %s seconds ---" % (time.time() - start_time))

def DistincPower2(n):
    start_time = time.time()
    d = {}
    for a in range(2,n+1):
        for b in range(a,n+1):
            d[a**b] = True
            d[b**a] = True

    print("Process finished --- %s seconds ---" % (time.time() - start_time)) 
    return len(d)

print(DistincPower2(1000))
