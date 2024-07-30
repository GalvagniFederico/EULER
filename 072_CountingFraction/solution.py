
import math
import time


def FindNext():
    n_sol = 0
    d_sol = 0
    v_sol = 0
    count = 0

    for n in range(2,value):
        d = math.ceil((n*1)/2)
        if d > value: 
            return  count
        v = n/d
        if v < 1/3 and v > v_sol:
            count += 1 
            n_sol = n
            d_sol = d
            v_sol = v

def Solve(value, n_low, d_low):
    n_sol = 1
    d_sol = 2

    v_sol = 0
    count = 0

    for n in range(2,value):
        d = math.ceil((n*d_low)/n_low)
        if d > value and v_sol != 1/3:
            count+=Solve(value, n_sol, d_low)
        v = n/d
        if v < 1/3 and v > v_sol:
            count += 1 
            n_sol = n
            d_sol = d
            v_sol = v
    return count



print(Solve(8))