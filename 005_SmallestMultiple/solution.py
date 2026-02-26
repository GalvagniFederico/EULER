# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def a(num, n):
    for i in range(n, 1, -1):
        if num % i != 0:
            return False
    return True

def SmallestMultiple(n):
    num = n
    while True:
        if a(num, n):
            return num
        num += n

print(SmallestMultiple(20))
