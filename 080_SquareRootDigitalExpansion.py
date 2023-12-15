# It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal 
# expansion of such square roots is infinite without any repeating pattern at all.
# The square root of two 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475

# For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for 
# all the irrational square roots.

# Long division method to find square root

# TODO: refactor

import math
import time
from decimal import *
# Solve the quotient*2*X * X <= 456 by founding the biggest X that accomplish the terms of the equation 
def findX(quotient, dividend):
    res = 0
    oldRes = 0
    x = 0

    while True:
        
        res = int(str(quotient*2)+str(x)) * x
        if res >= dividend:
            break
        x+=1
        oldRes = res

    return oldRes, x-1


def DigitalExpansionSum(n, digits):
    originalN = n
    n = str(n) + ''.join([str(elem) for elem in ["00" for i in range(digits)]])
    
    perfectSquare = 0
    i = 1

    if len(n)%2==1:
        firstPartition = n[:1]
    else:
        firstPartition = n[:2]
    
    while i*i <= originalN:
        perfectSquare = math.pow(i,2)
        if i*i == originalN:
            return i
        i+=1
        if i*i == originalN:
            return i

    
    if perfectSquare == originalN:
        return n
    quotient = str(int(math.sqrt(perfectSquare)))
    reminder = int(firstPartition) - perfectSquare
    
    n = n[len(firstPartition):]


    if len(n) % 2==1:
        iteration=int(len(n)/2) + 1
    else:
        iteration=int(len(n)/2)



    for i in range(0, iteration):
        
        couple = n[i*2:(i*2)+2]
        divisor = int(str(int(reminder)) + couple)

        res = findX(int(quotient), divisor)
        quotient += str(res[1])
        reminder = divisor-res[0]

    return quotient[:len(quotient)-digits] + "." + quotient[len(quotient)-digits:]

#print(DigitalExpansionSum(9,100))

def SquareRootDigitalExpansion(n):
    result = 0
    for i in range(1,n):
            
            res =  DigitalExpansionSum(i,99)
            if not str(res).__contains__("."):
                continue
            res = res.split(".")
            res1 = res[0]
            res = res[1]
            
            res = str(res)
            res = [int(i) for i in res]
            res = sum(res) + int(res1)
            result += res

    return result
            

getcontext().prec = 101
# print(DigitalExpansionSum(100,99))
# print(Decimal(2).sqrt())

print(SquareRootDigitalExpansion(101))