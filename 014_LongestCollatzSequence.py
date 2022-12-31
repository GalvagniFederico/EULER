import math
def LargestCollatzSequence(n):
    result = 0
    max = 0
    for i in range(1,n+1, 2):
        t = CollatzSequence(i)
        if t > max: 
            max = t
            result = i
    return result, max

def CollatzSequence(n):
    result = 1
    while n != 1:
        if(n%2 == 0):
            n = int(n/2)
        else:
            n = (3*n)+1
        result += 1
    return result

print(LargestCollatzSequence(1000000))

