def CoinPartitions():
    result = 0
    fib = [0,1]
    print(10000000%1000000)
    while fib[1]%1000000 !=0:
        t = fib[1]
        fib[1] += fib[0]
        fib[0] = t
        print(fib[1])

CoinPartitions()



    # 3 - 3
    # OOO
    # OO O
    # O O O

    # 4 - 4
    # OOOO
    # OOO O
    # OO OO
    # O O O O

    # 5 - 7
    #     OOOOO
    # OOOO   O
    # OOO   OO
    # OOO   O   O
    # OO   OO   O
    # OO   O   O   O
    # O   O   O   O   O

    # 6 - 11
    # OOOOOO
    # OOOOO O
    # OOOO OO
    # OOOO O O
    # OOO OOO
    # OOO OO O
    # OOO O O O
    # O0 0000
    # 00 00 00
    # 00 00 0 0
    # 00 0 0 0 0
    # 0 0 0 0 0 0
