import time

# Which prime, below one-million, can be written as the sum of the most consecutive primes?

def SievePrime(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False
    p = 2
    while p*p <= n:
        if prime[p] == True:
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1

    arr = []
    for i in range(len(prime)):
        if prime[i]:
            arr.append(i)
    return arr, prime

def ConsecutivePrimeSum(n):
    p, p_b = SievePrime(n)

    start_time = time.time()
    l = 0
    for i in range(len(p)-1, 1, -1):
        if p[i] < n/3:
            l = i - 1
            break
    max_sum = 0
    count = 0

    for i in range(l):
        sum = 0
        for j in range(i, l):
            sum += p[j]
            if sum > n:
                break
            if p_b[sum] and sum > max_sum and j-i > count:
                max_sum = sum
                count = j - i

    print("Process finished --- %s seconds ---" % (time.time() - start_time))
    return max_sum

print(ConsecutivePrimeSum(1000000))
