from math import factorial

def sum_of_digit_factorials(n):
    return sum(factorial(int(digit)) for digit in str(n))


def chain_length(n,cache):
    seen = set()
    original = n
    while n not in seen:
        if n in cache:
            cache[original] = len(seen) + cache[n]
            return cache[original]
        seen.add(n)
        n = sum_of_digit_factorials(n)
    chain_len = len(seen)
    cache[original] = chain_len
    return chain_len


def Solve(limit):
    cache = {}
    count = 0 
    for i in range(1, limit):
        if chain_length(i, cache) == 60:
            count += 1
    return count

print(Solve(1_000_000))