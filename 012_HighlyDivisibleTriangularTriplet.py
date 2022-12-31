import time

def factors(num):
    l = []
    for div in range(1, int(num**0.5) + 1):
        if num % div == 0:
            l.append( div)
            other = num // div
            if other != div:
                l.append(other)
    return l
#print(factors(28))

def HighlyDivisibleTriangle(n):
    start_time = time.time()
    
    tr= 3
    inc = 3
    
    while True:
        temp = len(factors(tr))
        if(temp>=n):
            print("Process finished --- %s seconds ---" % (time.time() - start_time))
            return tr
        tr += inc
        inc+=1

print(HighlyDivisibleTriangle(500))