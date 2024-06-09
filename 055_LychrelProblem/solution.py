def Solve():
    solution = 0
    for n in range(1,10000):
        Lychrel = True
        for i in range(50):
            n += int(str(n)[::-1])
            if str(n) == str(n)[::-1]:
                Lychrel = False
                break
        
        if Lychrel:
            solution+=1

    print(solution) 
                
Solve() 