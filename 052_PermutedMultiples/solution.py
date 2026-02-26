import math
import time

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
# contain the same digits.

def lenInt(n):
    return int(math.log10(n)) + 1

def firstDigit(n):
    while n >= 10:
        n = n / 10
    return int(n)

def ArePermutedMult(n):
    l = []
    for i in range(1, 7):
        a = n * i
        s = str(a)
        v = [int(str(c)) for c in s]
        v.sort()
        l.append(v)
    for i in range(1, len(l)):
        if l[i] != l[0]:
            return False
    return True

def PermutedMultiple():
    start_time = time.time()
    a = 0
    i = 0
    while a == 0:
        i += 1
        l = lenInt(i * 2)
        for x in range(3, 7):
            if lenInt(x * i) != l:
                break
            if x == 6:
                if ArePermutedMult(i):
                    a = i
        if firstDigit(i) >= 2:
            i += lenInt(i) * 10
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
    return a

def isPermutedMult2(n):
    return (sorted(str(n*2)) == sorted(str(n*3)) == sorted(str(n*3)) == sorted(str(n*4)) == sorted(str(n*5)) == sorted(str(n*6)))

def PermutedMultiple2():
    start_time = time.time()
    i = 123456
    limit = "166666"
    while not isPermutedMult2(i):
        x = str(i)
        if x[:-1] == 0:
            continue
        if i > int(limit[0:int(math.log10(i))+1]):
            i = int("1" + str(i))
        i += 1
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
    print(i)

print(PermutedMultiple())
