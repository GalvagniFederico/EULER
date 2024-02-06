from itertools import permutations, combinations
import operator

def DoOperations(numbers, operations, parenthesis):
    for p in parenthesis:
        operations[p[0]]()


def solution():
    numbers = [0,1,2,3,4,5,6,7,8,9]
    numbers = list(combinations(numbers,4))
    

    operations = [operator.add, operator.sub, operator.mul, operator.truediv]
    operations = list(permutations(operations, 3))
    # 0p
# 1234

# 2p
# (12)34
# 1(23)4
# 12(34)
# (12)(34)

# 3 p
# (123)4
# 1(234)

# comb
# ((12)3)4
# (1(23))4
# 1((23)4)
# 1(2(34))

    parenthesis = [[0,0,1], [1,1,2], [2,2,3], [1,[0,0,1], [2,2,3]]]
    parenthesis3 = [[0,2], [1,3]]
    
    print(operations[0][0](2,15))    

    sequence = set()
    sequence.add("10")
    numbers = [1,2,3,4]
    for n in numbers:
         for s in operations:
            for p in parenthesis:
                DoOperations(n, s, p)

            try: sequence.add(s[2](s[1](s[0](n[0], n[1]), n[2]), n[3])) 
            except: True
            try: sequence.add(s[2](s[1](s[0](n[0], n[1]),n[2]),n[3]))
            except: True

            try: sequence.add(s[2](s[0](n[0], s[1](n[1],n[2])), n[3]))# 1(23)4
            except: True
            
            try:  sequence.add(s[1](s[0](n[0], n[1]), s[2](n[2], n[3]))) # 12s[2](n[2], n[3])
            except: True
           
            try:  sequence.add(s[1](s[0](n[0], n[1]), s[2](n[2], n[3])))
            except: True
           

            # 3 p
            try: sequence.add(s[2](s[1](s[0](n[0], n[1]), n[2]),n[3]))# (123)4
            except: True
            
            try:  sequence.add(s[0](n[0], s[2](n[3],s[1](n[1], n[2]))))# 1(234)
            except: True
           
            

            sequence

            # comb

            
            try: sequence.add(s[2](s[1](s[0](n[0], n[1]), n[2]), n[3])) # ((12)3)4
            except: True
            
            try: sequence.add(s[2](s[0](n[0], s[1](n[1],n[2])), n[3]))# (1(23))4
            except: True
            
            try: sequence.add(s[0](n[0], s[2](s[1](n[1], n[2]),n[3])))# 1((23)4)
            except: True
           
            try:  sequence.add(s[0](n[0] , s[1](n[1], s[2](n[2], n[3])) ))# 1(2(34))
            except: True
            
    res = []
    for n in sequence:
        if isinstance(n, int):
            res.append(n)
    
    res = sorted(res)
    return res

print(solution()) 

# 0p
# 1234

# 2p
# (12)34
# 1(23)4
# 12(34)
# (12)(34)

# 3 p
# (123)4
# 1(234)

# comb
# ((12)3)4
# (1(23))4
# 1((23)4)
# 1(2(34))

