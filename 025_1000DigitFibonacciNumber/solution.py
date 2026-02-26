import time

# The Fibonacci sequence is defined by the recurrence relation: F_n = F_{n-1} + F_{n-2}
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

def Fibonacci1000Digit(n):
    start_time = time.time()
    f = [1, 1]
    i = 2
    l = 0
    while l != n:
        temp = f[1]
        f[1] += f[0]
        f[0] = temp
        i += 1
        l = len(str(f[1]))
    return i

print(Fibonacci1000Digit(1000))
