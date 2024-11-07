def sum_of_proper_divisors(n):
    divisors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors)

def find_longest_amicable_chain(limit):
    sums = [0] * limit
    for i in range(1, limit):
        sums[i] = sum_of_proper_divisors(i)

    max_chain_length = 0
    smallest_member = 0
    visited = [False] * limit

    for i in range(1, limit):
        if visited[i]:
            continue

        current = i
        chain = []
        while current < limit and not visited[current]:
            visited[current] = True
            chain.append(current)
            current = sums[current]

            if current in chain:
                idx = chain.index(current)
                chain_length = len(chain) - idx
                if current == chain[-1] and chain_length > max_chain_length:
                    max_chain_length = chain_length
                    smallest_member = min(chain[idx:])
                break

    return smallest_member, max_chain_length

# Run the function with a limit of 1,000,000
limit = 1000000
smallest_member, max_chain_length = find_longest_amicable_chain(limit)
print(f"Smallest member of the longest chain: {smallest_member}")
print(f"Length of the longest chain: {max_chain_length}")