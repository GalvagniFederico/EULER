import itertools
import time

# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
# is unusual in two ways: (i) each of the three terms are prime, and,
# (ii) each of the 4-digit numbers are permutations of one another.
# Find the other 4-digit increasing sequence with this property.

def SievePrimeArray(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False
    p = 2
    while p*p <= n:
        if prime[p] == True:
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1
    return prime

def FindSequence(ps_prime):
    sequence = []
    for i in range(len(ps_prime)):
        sequence.clear()
        sequence.append(ps_prime[i])
        for j in range(i+1, len(ps_prime)):
            if ps_prime[j] - ps_prime[i] == 3330:
                sequence.append(ps_prime[j])
                for k in range(j+1, len(ps_prime)):
                    if ps_prime[k] - ps_prime[j] == 3330:
                        sequence.append(ps_prime[k])
                        return sequence
    return None

def PrimePermutationSequence(n):
    p_b = SievePrimeArray(n)

    for i in range(1000, n):
        digits = [int(x) for x in str(i)]
        n_digits = len(digits)
        n_power = n_digits - 1
        permutations = itertools.permutations(digits)

        ps = [sum(v * (10**(n_power - i)) for i, v in enumerate(item)) for item in permutations]

        ps_prime = []
        for j in range(len(ps)):
            if p_b[ps[j]] and len(str(ps[j])) > 3:
                ps_prime.append(ps[j])

        if len(ps_prime) < 3:
            continue

        ps_prime = FindSequence(ps_prime)
        if ps_prime is None:
            continue
        print(ps_prime)

PrimePermutationSequence(9999)
