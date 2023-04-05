from utilities import SieveOfEratosthenes, isPrime

def TruncatablePrimes():
    result = 0
    primes = SieveOfEratosthenes(1000000)
    primes = primes[4:len(primes)-1]
    for n in primes:
        s = str(n)
        is_trunc = True
        for i in range(1,len(s)):
            t, r = int(s[i:]), int(s[0: len(s)-1])
            if(not isPrime(int(s[i:])) or not isPrime(int(s[:i]))):
                is_trunc = False
       
        if is_trunc:result +=n
    return result

print(TruncatablePrimes())