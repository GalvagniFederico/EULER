import math

def isPalindrom(n):
    n = str(n)
    for i in range(math.floor(len(n)/2)+1):
        if(n[i] != n[len(n)-i-1]):
            return False
    return True

#print(isPalindrom(132))

def intToBinary(n):
    binary = ""
    r = 0
    while n>=2:
        binary += str(n%2)
        n = n//2
        

    return str("1")+ binary[::-1]

#print(intToBinary(947))

def DoubleBasePalindromes(n):
    result = 0
    for i in range(n+1):
        if(isPalindrom(intToBinary(i)) and isPalindrom(i)):
            result += i
    return result

print(DoubleBasePalindromes(1000000))