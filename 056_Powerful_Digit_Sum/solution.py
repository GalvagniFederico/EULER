import math



def Solve(a,b):
    result = 0
    
    for ia in range(1,a+1):
        for ib in range(1,b):
            if len(str(ia**ib)) == ib:
                result+= 1
    return result

print(Solve(9,22))