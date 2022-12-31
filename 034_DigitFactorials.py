import math

def DigitFactiorial():
    limit = 2540160
    sum_df = 0
    df = []
    for i in range(3,limit+1):
        sum_if = 0
        for c in str(i):
            sum_if += math.factorial(int(c))
        if(sum_if == i): 
            sum_df+= sum_if

    return sum_df

print(DigitFactiorial())