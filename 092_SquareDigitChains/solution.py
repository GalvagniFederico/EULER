# A number chain is created by continuously adding the square of the digits in a number
#  to form a new number until it has been seen before.
# For example,
# 44-32-13-10-1-1
# 85-89-145-42-20-4-16-37-58-89
# Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
#  What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
# How many starting numbers below ten million will arrive at 89?

# Since the max addition of a 7 digits number (9_999_999) its 81*7 = 567
# we can compute those in advance, also we can precompute the square of number 0 to 9

def squareadd(n):
	return sum([int(i)**2 for i in n])


def solve():
	count = 0
	
	sds = [0] * 1000
	for i in range(1000):
		n = i
		s = 0
		while n > 0:
			d = n % 10
			s += d * d
			n //= 10
		sds[i] = s
	
	ends_at_89 = [False] * 568
	for i in range(1, 568):
		n = i
		while n != 1 and n != 89:
			n = sds[n]          # one array lookup instead of digit loop
		ends_at_89[i] = (n == 89)
	
	count = 0
	for i in range(1, 10_000_000):
		s = sds[i % 1000] + sds[i // 1000 % 1000] + sds[i // 1000000]

		count += 1 * ends_at_89[s]

	return count

if __name__ == "__main__":
	import time
	start = time.time()
	print(solve())
	print("Process finished --- %s seconds ---" % (time.time() - start))