from itertools import permutations, product
from fractions import Fraction

# Generate all possible results for a given set of four digits
def possible_results(digits):
    results = set()
    # Go through all possible orders of the digits
    for perm in permutations(digits):
        # Go through all possible operations
        for ops in product("+-*/", repeat=3):
            # Evaluate the expressions with different parentheses
            try:
                # (a op1 b) op2 c) op3 d
                results.add(eval(f"({perm[0]} {ops[0]} {perm[1]}) {ops[1]} {perm[2]} {ops[2]} {perm[3]}"))
            except ZeroDivisionError:
                pass
            try:
                # ((a op1 b) op2 (c op3 d))
                results.add(eval(f"(({perm[0]} {ops[0]} {perm[1]}) {ops[1]} ({perm[2]} {ops[2]} {perm[3]}))"))
            except ZeroDivisionError:
                pass
            try:
                # (a op1 (b op2 (c op3 d)))
                results.add(eval(f"({perm[0]} {ops[0]} ({perm[1]} {ops[1]} ({perm[2]} {ops[2]} {perm[3]})))"))
            except ZeroDivisionError:
                pass
            try:
                # (a op1 ((b op2 c) op3 d))
                results.add(eval(f"({perm[0]} {ops[0]} (({perm[1]} {ops[1]} {perm[2]}) {ops[2]} {perm[3]}))"))
            except ZeroDivisionError:
                pass
            try:
                # ((a op1 b) op2 c) op3 d
                results.add(eval(f"(({perm[0]} {ops[0]} {perm[1]}) {ops[1]} {perm[2]}) {ops[2]} {perm[3]}"))
            except ZeroDivisionError:
                pass
    # Only keep positive integer results
    return {int(result) for result in results if result > 0 and result == int(result)}

# Find the longest set of consecutive integers from 1
def longest_consecutive(results):
    n = 1
    while n in results:
        n += 1
    return n - 1

# Main function to find the optimal set of digits
def find_optimal_digits():
    max_consecutive = 0
    best_digits = None
    for a in range(1, 10):
        for b in range(a + 1, 10):
            for c in range(b + 1, 10):
                for d in range(c + 1, 10):
                    results = possible_results([a, b, c, d])
                    consecutive = longest_consecutive(results)
                    if consecutive > max_consecutive:
                        max_consecutive = consecutive
                        best_digits = (a, b, c, d)
    return best_digits, max_consecutive

# Run the function
best_digits, max_consecutive = find_optimal_digits()
print("Best digits:", best_digits)
print("Max consecutive integers:", max_consecutive)
