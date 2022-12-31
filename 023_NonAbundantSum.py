from utilities import SumOfProperDivisors as SPD
import time

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
# However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed 
# as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def NonAbundantSum():
    limit = 28123
    result = 0
    start_time = time.time()
    # Find all abundant number under 28123

    abundant = [False]*limit
    for i in range(limit-1, 0, -1):
        if(SPD(i)>i):
            abundant[i] = True
        else:
            abundant[i] = False


    print("Finished searching abundant : "+ str(time.time()-start_time))
    n = [False]*limit
    for i in range(len(abundant)):
        for j in range(i, len(abundant)-i-1):
            sum = i+j
            if(sum < limit):
                n[sum] = True

    print("Finished search non abundant sum : "+ str(time.time()-start_time))
    result = 0
    for i in range(len(n)-1, -1, -1):
        if(n[i] == False):
            result += i
    return result



        

print(NonAbundantSum())