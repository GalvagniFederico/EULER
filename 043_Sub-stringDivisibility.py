
from itertools import permutations
 


def IsDivisible(n):
    s = str(n)
    div = [2,3,5,7,11,13,17]
    for i in range(1,7,1):
        ss = int(s[i:i+3])
        d = div[i-1]
        if ss%d!=0:
            return False
        
    return True

print(IsDivisible(1406357289))

def SubStringdDvisibility():
    sum = 0
    inc = 1
    string = "0123456789"
    string = list(string)
    permu = permutations(string, 9)
    #return 1430952867 + 1460357289 + 1406357289 + 4130952867 + 4160357289 + 4106357289

    for i in list(permu):
        if i[0] == "0":
            continue

        s = str().join(i)
        if IsDivisible(int(s)):
            sum += int(s)
    return sum

 
print(SubStringdDvisibility())


