# For a number written in Roman numerals to be considered valid there are basic rules which must be followed. 
# Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way 
# of writing a particular number.

# For example, it would appear that there are at least six ways of writing the number sixteen:

# IIIIIIIIIIIIIIII
# VIIIIIIIIIII
# VVIIIIII
# XIIIIII
# VVVI
# XVI

# However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be 
# the most efficient, as it uses the least number of numerals.

# The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers 
# written in valid, but not necessarily minimal, Roman numerals; see About... Roman Numerals for the 
# definitive rules for this problem.

# Find the number of characters saved by writing each of these in their minimal form.

# Note: You can assume that all the Roman numerals in the file contain no more than four consecutive 
# identical units.


# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000

from bidict import bidict
import math

romanTrans = bidict({
                    "I":1,
                    "V":5,
                    "X":10,
                    "L":50,
                    "C":100,
                    "D":500,
                    "M":1000})

romanValues = [1000,500,100,50,10,5,1]

def countDigit(n):
    return math.floor(math.log10(n)+1)

def get_digit(number, n):
    return number // 10**n % 10

def nextBiggerRoman(n):
    for i in range(len(romanValues)-1,0,-1):
        if romanValues[i]>n:
            return romanValues[i]

def DeserializeRoman(romanNumber: str) -> int:
    deserialized = [romanTrans[l] for l in romanNumber]
    
    result = 0
    i = 0 
    while i < len(deserialized):
        if i < len(deserialized)-1 and deserialized[i]<deserialized[i+1]:
            result += deserialized[i+1]-deserialized[i]
            i+=2
        else:
            result+= deserialized[i]
            i+=1
    return result

allowedSubtraction = {
    1 : [5,10],
    10: [50,100],
    100: [500,1000]
}

def SerializeRoman(number: int) -> str:
    romanNumber = ""
    iV = 0 # romanValues index

    while number!=0:
        cVL = romanTrans.inv[romanValues[iV]]
        cV = romanValues[iV]

        dC = countDigit(number)-1
        fD = get_digit(number,dC)
        cleanNumber = fD * (10**dC)

        # if first digit is 4 or 9 we are doing subtraction
        
        if fD == 4 or fD == 9:
            sub1 = nextBiggerRoman(number - cleanNumber)
            sub2 = nextBiggerRoman(cleanNumber)
            romanNumber+= romanTrans.inv[nextBiggerRoman(number - cleanNumber)] + romanTrans.inv[nextBiggerRoman(cleanNumber)] 
            number -= (sub2-sub1)

        # iV+=1

                
           
    return romanNumber
        
number = 1249
print(get_digit(number,3))
print(countDigit(number)-1)
print(get_digit(number,countDigit(number)-1)*(10**(countDigit(number)-1)))
print(SerializeRoman(49))

#922
#CMXXII