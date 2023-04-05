import math
import time
import itertools
from collections import defaultdict

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
def MultiplesOf3Or5(n):
    s = 0
    for i in range(n+1):
        if i%5 == 0 or i%3 == 0:
            s += i
    return s
#print(MultiplesOf3Or5(999))

def EvenFibonacciNumbers():
    fib = [1,1]
    fibEvenSum = 0
    while fib[1]<4000000:
        if(fib[1]%2 == 0 ):
            fibEvenSum += fib[1]

        temp = fib[1]
        fib[1] += fib[0]
        fib[0] = temp
    return str(fibEvenSum )   
#print(EvenFibonacciNumbers())


def LargestPrimeFactor(n):
    list_prime = []
    i = 2
    while(n != 1):

        if(n%i == 0):
            n/=i
            list_prime.append(i)
        else:
            i += 1
    return list_prime


def isPalindrome(n):
    n = str(n)

    for i in range(math.floor(len(n)/2)):
        if n[i] != n[len(n)-i-1] :
            return False
    return True     

#print(isPalindrome(96769))        

def LargestPalindromeProduct(digits):
    digits = 10**digits
    max = 0
    for i in range(digits, 0, -1):
        for j in range(digits, 0, -1):
            if(isPalindrome(i*j)):
                if(max < i*j):
                    max = i*j
    return max
#print(LargestPalindromeProduct(3))
def a(num,n):
    for i in range(n, 1, -1):
            if(num%i != 0):
                return False
    return True


def SmallestMultiple(n):
    num = n
    while True:
        
        if(a(num, n)):
            return num
        num += n
        
#print(SmallestMultiple(20))

def SumSquareDifference(n):
    sumsquare = 0
    sum = 0
    for i in range(n+1):
        sumsquare += i**2
        sum += i
        print(i,sumsquare)
    return sum**2 - sumsquare
#print(SumSquareDifference(100))
def CheckIfPrime(n):
    if(n <0): return False
    if(n == 1 or n== 0):
        return False
    for i in range(2,math.floor(n/2)+1):
        if(n%i == 0):
            return False
    return True

#print(CheckIfPrime(91))

def FindIndexPrime(th):
    primelist = []
    i = 2
    while not len(primelist) == th:
        if(CheckIfPrime(i)):
            primelist.append(i)

        i += 1
        
    return primelist[-1]

#print(FindIndexPrime(10001))

def LargestProductInSeries(nd):
    f = open("digitmille.txt", "r") 
    s = f.read()

   
    n = [int(d) for d in str(s)]

    max = 0
    for i in range(nd-1,999):
            product = 1
            for x in range(i, i-nd, -1):
                product *= n[x]
            if product > max:
                max = product

    return max
#print(LargestProductInSeries(13))

def Fibonacci1000Digit(n):
    start_time = time.time()
    f = [1, 1]
    i = 2
    l = 0
    while l != n:
        temp = f[1]
        f[1]+= f[0]
        f[0] = temp
        i += 1
        l = len(str(f[1]))
    
    return i

#print(Fibonacci1000Digit(1000))
def SumOfProperDivisors(n):
    sum = 0
    for i in range(math.floor(n/2), 0,-1):
        if(n%i == 0):
            sum += i

    return sum
    
#print(SumOfProperDivisors(28))
#SumOfProperDivisors(100000)

def AmicableNumber(n):
    #find all amicable number under 10000

    dn = []
    sum = 0
    for i in range(n):
        dn.append(SumOfProperDivisors(i))
    
    for i in range(n):
        for j in range(i, n):
            if(dn[i] == j and i == dn[j] and i != j):
                print(i, j)
                
                sum += dn[i] + dn[j]
            
                

    return sum
#print(AmicableNumber(10000))

def sOD(x):
	s = 1
	for i in range(2, int(math.sqrt(x)) + 1):
		if (x % i == 0):
			s += i
			s += x / i
	return s
            




def AmicableNumber2(n):
    dn = []
    sum = 0
    for i in range(1,n):
        j = sOD(i)
        if(sOD(j) == i and i != j):
            sum += i
      
    return sum

#print(AmicableNumber2(10000))

def LargeSum():
    f = open("largesum.txt", "r")
    lines = f.readlines()
    d = [int(line) for line in lines]
    print(d)
    sum = 0
    for n in d:
        sum+=n
    
    return str(sum)[0:10]

#print(LargeSum())



def QuadraticPrimes(num):
    max_pair = (0,0,0)
    for a in range(-num, num):
        for b in range(-num, num): # b >= 2, a + b + 1 >= 2
            n, count = 0, 0
            while True:
                v = n*n + a*n + b
                
                if CheckIfPrime(v): count = count + 1
                else: break
                n = n + 1
            if count > max_pair[2]:
                max_pair = (a,b,count)

    print(max_pair[0] * max_pair[1])

#QuadraticPrimes(1001)


def SievePrime(n):
    start_time = time.time()
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False
    p = 2
    while p*p <= n:
        if prime[p] == True:

            for i in range(p*p, n+1, p):
                prime[i] = False
        p+=1
    c=0

    arr = []
    for i in range(len(prime)):
        if(prime[i]):
            arr.append(i)
    #print("Process finished --- %s seconds ---" % (time.time() - start_time))
    
    return arr, prime

def isPrime(n):
    if n <= 1:
        return False
    if n % 2 == 0:
        return n == 2
 
    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
    return True
 

def primeSquare(n):
    start_time = time.time()
    arr = []
    for n in range(1,n):
        if(isPrime(n)):
            arr.append(n)
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
    
    
    t1 = time.time()
    



#print(SievePrime(10))

def SievePrimeArray(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False
    p = 2
    while p*p <= n:
        if prime[p] == True:

            for i in range(p*p, n+1, p):
                prime[i] = False
        p+=1
    c=0

    return prime


def circularPrime(n):
    start_time = time.time()
    
    p = SievePrimeArray(n)
    count = len(p) +2 # +2 because 2 and 5 wouldnt be counted

    for i in range(len(p)):
        s = str(p[i])
        if s.__contains__("2")  or s.__contains__("0") or s.__contains__("8") or s.__contains__("6") or s.__contains__("4") or s.__contains__("5"):
            count -= 1
            continue
        for j in range(0,len(s)):
            if not CheckIfPrime(p[i]):
                count -= 1
                break
                
            #rotation
            s = s[1:len(s)] +s[0]   
        
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
    print(count)
        
#circularPrime(1000000)

def ConsecutivePrimeSum(n):
    
    p, p_b = SievePrime(n) #p contains an array with all the prime number [2-n]
    #p_b contains an array of bool of lenght n where the element [i] is true if [i] is prime

    start_time = time.time()
    l = 0
    for i in range(len(p)-1, 1,-1):
        if p[i] < n/3:
            l = i-1
            break
    max_sum = 0
    count = 0

    for i in range(l):
        sum = 0

        for j in range(i, l):

            sum += p[j]

            if(sum>n):
                break

            if(p_b[sum] and sum > max_sum and j-i > count):
                max_sum = sum
                count = j-i


    print("Process finished --- %s seconds ---" % (time.time() - start_time))
    return max_sum

def permute(xs, low=0):
    if low + 1 >= len(xs):
        yield xs
    else:
        for p in permute(xs, low + 1):
            yield p        
        for i in range(low + 1, len(xs)):        
            xs[low], xs[i] = xs[i], xs[low]
            for p in permute(xs, low + 1):
                yield p        
            xs[low], xs[i] = xs[i], xs[low]



#print(ConsecutivePrimeSum(1000000))

def FindSequence(ps_prime):
    sequence = []
    ver = []
    for i in range(len(ps_prime)):
        sequence.clear()
        sequence.append(ps_prime[i])
        for j in range(i+1, len(ps_prime)):
            if(ps_prime[j] - ps_prime[i] == 3330):
                sequence.append(ps_prime[j])
                for k in range(j+1, len(ps_prime)):
                    if(ps_prime[k] - ps_prime[j] == 3330):
                        sequence.append(ps_prime[k])                    
                        return sequence
    return None

def PrimePermutationSequence(n):
    p_b = SievePrimeArray(n)

    for i in range(1000,n):
        
        
        
        digits = [int(x) for x in str(i)]
        n_digits = len(digits)
        n_power = n_digits - 1
        permutations = itertools.permutations(digits)

        ps = [sum(v * (10**(n_power - i)) for i, v in enumerate(item)) for item in permutations]
        count_prime = 0

        ps_prime =[]
        for i in range(len(ps)):

            if p_b[ps[i]]  and len(str(ps[i])) > 3:
                ps_prime.append(ps[i])
                count_prime += 1

        if(count_prime < 3):
            continue

        ps_prime = FindSequence(ps_prime)
        if(ps_prime == None):
            continue
        print(ps_prime)

        

#PrimePermutationSequence(9999)

def npf(number):
    """function which will return
    the number of prime factors"""
    i = 2
    a = set()
    while i < number**0.5 or number != 1:
        if number % i == 0:
            number = number/i
            a.add(i)
            i -= 1
        i += 1
        
    return (len(a))     

def DistinctPrimesFactors(d):
    
    count_series = 0
    first_occurence = 0
    i = 1
    while True:
    
        count = npf(i)
        if(count == d):
            count_series += 1
            if(first_occurence == 0):
                first_occurence = i
            if count_series == d:
                print(first_occurence)
                return
        else:
            count_series = 0
            first_occurence = 0
            
        i+=1
def lenInt(n):
    return int(math.log10(n))+1

def firstDigit(n) :
 
    # Remove last digit from number
    # till only one digit is left
    while n >= 10:
        n = n / 10

    # return the first digit
    return int(n)




def ArePermutedMult(n):
    l = []
    for i in range(1,7):
        a = n*i
        s  = str(a)
        v = [int(str(c)) for c in s]
        v.sort()
        l.append(v)
    for i in range(1, len(l)):
        if(l[i] != l[0]):
            return False
    return True


#print(ArePermutedMult(125874))
        

#ArePermutedMult(1000)
def PermutedMultiple():
    start_time = time.time()
    a = 0
    incr = 1
    i = 0
    while a == 0:
        i += 1
        l = lenInt(i*2)
        
        for x in range(3,7):
            if(lenInt(x*i) != l):
                break
            if  x == 6:
                if(ArePermutedMult(i)):
                    a = i
                
        if(firstDigit(i) >= 2):
            i += lenInt(i)*10
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
    return a

#print(PermutedMultiple())

def isPermutedMult2(n):
    return (sorted(str(n*2)) == sorted(str(n*3)) == sorted(str(n*3)) == sorted(str(n*4)) == sorted(str(n*5)) == sorted(str(n*6)))


def PermutedMultiple2():
    start_time = time.time()
    i = 123456
    # can t be a number greater log10(i)+1 * 0.166666666 
    # Example: 167.000*2 = 334.000 and 167.000 * 6 = 1.002.000
    # They arent of the same length
    limit = "166666" 
    while not isPermutedMult2(i):
        x = str(i)
        if(x[:-1] == 0):
            continue
        
        if(i > int(limit[0:int(math.log10(i))+1])):
            i = int("1" + str(i))
        i+=1

    print("Process finished --- %s seconds ---" % (time.time() - start_time))
    print(i)
    
#PermutedMultiple2()                   
#PermutedMultiple()

#print(lenInt(10000))              

# start_time = time.time()
# print(next(n for n in itertools.count(1) if all(sorted(str(n*m))==sorted(str(n)) for m in range(2,7))))
# print("Process finished --- %s seconds ---" % (time.time() - start_time))
 

    



#print(len(list(factors(28))))



def Division(n,d):
    res = ""
    while len(res)<= 7:
        if(d>n):
            n = n*10
            res+= "0"
        else:
            res += str(n//d)
            n = n%d
            n *= 10
            if(n == 0):
                return str("0." +  res[1:] + "0"*(7-len(res)))
                
    return str("0." +res [1:])

def plusMinus(arr):
    # Write your code here
    elements = [0,0,0]
    for e in arr:
        if(e == 0):
            elements[2]+=1
            continue
        if(e > 0):
            elements[0] +=1
        else:
            elements[1] +=1
    
    l = len(arr)
    elements = [Division(i,l) for i in elements]
    
    
    print(elements[0])
    print(elements[1])
    print(elements[2])
            
    pass

plusMinus([0,1,-2,-6,2,0,2,3])