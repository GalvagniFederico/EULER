import math
import time

def CheckIfPrime(n):


    for i in range(2,math.floor(math.sqrt(n)),2):
        if(n%i == 0):
            return False
    return True

def SummationOfPrimes(n):
    start_time = time.time()
    sum = 2
    a = [n]
    for i in range(3,n, 2):
        if(CheckIfPrime(i)):
            sum += i
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
    return sum

#print(SummationOfPrimes(1000000))

def QuadraticPrimes(num):
    max_pair = (0,0,0)
    for a in range(-num, num):
        for b in range(max(2, 1-a), num): # b >= 2, a + b + 1 >= 2
            n, count = 0, 0
            while True:
                v = n*n + a*n + b
                
                if CheckIfPrime(v): count = count + 1
                else: break
                n = n + 1
            if count > max_pair[2]:
                max_pair = (a,b,count)

    print(max_pair[0] * max_pair[1])

#QuadraticPrimes(100)