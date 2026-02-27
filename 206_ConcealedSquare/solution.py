# Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
# where each "_" is a single digit.

# Consideration to narrow the search
# 1] n^2 ends with 0 so n must be divisible by 10
# 2] the square is 19 digits so n is roughly between
# sqrt(10^18) and sqrt(2*10^18)
# 3] n ends in 30 or 70 (because (n/10)^2 must end in 9_, only 3 and 7 squared end in 9)

import math

def check(n):
	si = str(n * n)
	pattern = "1_2_3_4_5_6_7_8_9_0"
	for j in range(0, len(si), 2):
		if si[j] != pattern[j]:
			return False
	return True

def solve():
	n_min = math.floor(math.sqrt(10**18))
	n_max = math.ceil(math.sqrt(1.92939495969798990*(10**18)))
	# Round n_min up to next multiple of 100
	n_min = n_min - (n_min % 100)
	for i in range(n_min, n_max, 100):
		if check(i + 30): return i + 30
		if check(i + 70): return i + 70

if __name__ == "__main__":
	import time
	start = time.time()
	print(solve())
	print("Process finished --- %s seconds ---" % (time.time() - start))