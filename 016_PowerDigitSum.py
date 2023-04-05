import math
import time

def PowerDigitSum(n):
    s = str(2**n)
    result = 0
    for i in s:
        result += int(i)
    return result

def PowerDigitSumVector(n):
    start_time = time.time()
    r = [1]
    result = 0
    riporto = 0
    for i in range(n):
        for j in range(len(r)-1,-1,-1):
            product = (r[j]*2)+riporto

            if(product >= 10):
                r[j] = product - 10
                riporto = 1
                if(j == 0): 
                    r.insert(0, 1)
                    riporto = 0
            else:
                r[j] = product
                riporto = 0
    
    for i in range(len(r)):
        result += r[i]
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
    return result


print(PowerDigitSumVector(1000))