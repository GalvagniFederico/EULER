import time 
import math
from itertools import combinations

def generate_combinations(arr):
    n = len(arr)
    result = []

    # Iterate over all possible bitmasks
    for mask in range(0, 2 ** (n - 1)):
        combo = []
        current_number = arr[0]
        for i in range(1, n):
            # Check if the current bit is set
            if mask & (1 << (i - 1)):
                # If set, group the current number with the next digit
                current_number = current_number * 10 + arr[i]
            else:
                # If not set, add the current number to the combo and start a new group
                combo.append(current_number)
                current_number = arr[i]
        # Add the last group
        combo.append(current_number)
        result.append(combo)

    return result


generate_combinations([6,7,2,4])
def is_s_number(N):
    # Get the digits of N^2
    digits = [int(digit) for digit in str(N ** 2)]
    
    # Generate all non-empty combinations of the digits

    for comb in generate_combinations(digits):
        if len(comb) == 1: continue
        if sum(comb) == N:
            return True
    return False


def Solve(N):
    result = 0 
    for i in range(1,int(math.sqrt(N)+1)):
        if i%2==0 or i%3==0 or i%5==0:
            if is_s_number(i):
                print(i,i**2)
                result += i**2
    
    return result


if __name__ == "__main__":
    start_time = time.time()
    N = 10**4
    print(Solve(N))

    print(f"Process finished --- {time.time() - start_time} seconds ---")
