
import math
import time


def Solve(value):
    start_time = time.time()
    n_sol = 0
    d_sol = 0
    v_sol = 0

    three_by_seven = 3/7
    seven_by_three = 7/3
    for n in range(2,value):
        d = math.ceil(n*seven_by_three)
        if d > value: 
            end_time = time.time()-start_time
            print("Process finished --- %s seconds ---" % (end_time)) 
            return  n_sol, d_sol, v_sol
        v = n/d
        if v < three_by_seven and v > v_sol: 
            n_sol =n
            d_sol = d
            v_sol = v
    return False



print(Solve(1_000_0000))