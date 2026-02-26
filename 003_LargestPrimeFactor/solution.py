# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

def LargestPrimeFactor(n):
    list_prime = []
    i = 2
    while n != 1:
        if n % i == 0:
            n /= i
            list_prime.append(i)
        else:
            i += 1
    return list_prime

print(LargestPrimeFactor(600851475143))
