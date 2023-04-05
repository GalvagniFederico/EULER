import math
def DigitFifthPowers(p):
    i = 1
    res = 0
    limit = 0

    while True:
        if (math.pow(9,p)*i) < (math.pow(10,i)) :
            limit = math.pow(10,i)
            print(limit)
            break
        i+=1
    i = 2
    
    while i<limit:
        sum = 0
        for c in str(i):
            sum+=math.pow(int(c),p)
        if sum == i:
            res += i
            print(i)
        i+=1

    return res


print(DigitFifthPowers(8))