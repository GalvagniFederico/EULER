import math

def isRightTriangle(a,b,c):
    return math.pow(a,2)+math.pow(b,2) == math.pow(c,2)

#print(isRightTriangle(30,40,50))

def GenerateTriangleCombination(p):
    combination = 0
    comb = set()
    for a in range(1,p-2):
        for b in range(a,p-a):
            c = p-a-b
            if (a+b+c == p):
                if isRightTriangle(a,b,c):
                    comb.add(str(a)+str(b)+str(c))
    return len(comb)

print(GenerateTriangleCombination(120))



def IntegerRightTriangles(n):
    result = 0
    max = 0
    
    for p in range(3, n+1):
        cur = GenerateTriangleCombination(p)
        print(p)
        if(cur > max):
            max = cur
            result = p

    return result

print(IntegerRightTriangles(1000))
