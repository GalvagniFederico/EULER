import math

def SumOfProperDivisors(n):
    sum = 0
    for i in range(math.floor(n**0.5), 0,-1):
        if(n%i == 0):
            sum += i

    return sum

def SieveOfEratosthenes(n):
      
    # Create a boolean array "prime[0..n]" and
    # initialize all entries it as true. A value
    # in prime[i] will finally be false if i is
    # Not a prime, else true.
    prime = [True for i in range(n+1)]
    prime_list = []
    p = 2
    while(p * p <= n):
          
        # If prime[p] is not changed, then it is
       # a prime
        if (prime[p] == True):
            # Update all multipless of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    c = 0
 
    # Print all prime numbers
    for p in range(2, n):
        if prime[p]:
            c += 1
            prime_list.append(p)
    return prime_list



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

def PrimeList(n):
    primelist = [2,3]
    i = 5
    while i<n:
        if(isPrime(i)):
            primelist.append(i)
        i += 2
    return primelist


#PrimeList(1000000)