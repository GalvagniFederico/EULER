import math

def ChampernowneConstant(n):
    result = 0
    fib = [0,1]
    while fib[1]%1000000 != 0:
        t = fib[1]
        fib[1] += fib[0]
        fib[0] = t
        print(fib[1])


    print(result)

    