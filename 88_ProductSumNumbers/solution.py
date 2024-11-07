import math
import itertools

def Solve(limit):
    min_product_sums = [float('inf')] * (limit + 1)

    def find_combinations(product, summation, count, start):
        k = product - summation + count
        if k <= limit:
            min_product_sums[k] = min(min_product_sums[k], product)
            for i in range(start, (limit // product) * 2):
                find_combinations(product * i, summation + i, count + 1, i)

    find_combinations(1, 1, 1, 2)

    unique_values = set(min_product_sums[2:])
    return sum(unique_values)

# Run the function for k in range 2 to 12000
print(Solve(12000))
