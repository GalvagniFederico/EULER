import math
import time
import sys

prime_set = {}

# Prime checking function
def is_prime(n):
    if n in prime_set:
        return prime_set[n]
    if n <= 1:
        prime_set[n] = False
        return False
    if n <= 3:
        prime_set[n] = True
        return True
    if n % 2 == 0 or n % 3 == 0:
        prime_set[n] = False
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            prime_set[n] = False
            return False
        i += 6
    prime_set[n] = True
    return True

# Generate the tile with the maximum prime differences
def solve_euler_128(nth_tile):
    prime_diff_tiles = [1]  # Start with the center tile
    n = 2  # Start checking from the second tile
    count = 1  # We already have the first tile
    start_time = time.time()

    

    while count < nth_tile:
        ring = (3 + int(math.sqrt(12 * (n - 1) - 3))) // 6
        pos_in_ring = n - 1 - 3 * ring * (ring - 1)

        if pos_in_ring == 0 or pos_in_ring == ring - 1:
            if pos_in_ring == 0:
                neighbors = [n - 6 * (ring - 1), n - 6 * (ring - 1) + 1, n + 6 * ring - 1]
            else:
                neighbors = [n - 6 * (ring - 1) - 1, n + 6 * (ring - 1) - 1, n + 6 * ring - 1]

            prime_diff_count = sum(is_prime(abs(n - neighbor)) for neighbor in neighbors)

            if prime_diff_count == 3:
                prime_diff_tiles.append(n)
                count += 1
                disp = f"Current tile: {n} -- Current ring: {ring} -- Prime tiles found: {len(prime_diff_tiles)}"
                disp += " -- Eta: " + '{0:02.0f}:{1:02.0f}'.format(*divmod((time.time()-start_time) * 60, 60))
                sys.stdout.write("\r" + disp)
                sys.stdout.flush()

        

        
        n += 1

    return prime_diff_tiles[nth_tile - 1]

# Finding the 2000th tile
print(solve_euler_128(10))
