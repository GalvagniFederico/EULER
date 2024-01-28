from itertools import combinations
import time

def CanBeRappresented(number, cube1, cube2):
    # number[0] in cube1 and number[1] in cube2 and viceversa
    if (number[0] in cube1 and number[1] in cube2) or (number[1] in cube1 and number[0] in cube2):
        return True
    
    # 6/9 case    
    if number[0] == 6 or number[0] == 9:
        if ((6 in cube1 or 9 in cube1) and number[1] in cube2) or \
            ((6 in cube2 or 9 in cube2) and number[1] in cube1):
            return True
    elif number[1] == 6 or number[1] == 9:
        if ((6 in cube1 or 9 in cube1) and number[0] in cube2) or \
            ((6 in cube2 or 9 in cube2) and number[0] in cube1):
            return True
    return False



def solution():
    result = 0
    cube = list(combinations([i for i in range(0,10)],6))
    square = [[0,1], [0,4], [0,6], [1,6], [2,5], [3,6], [6,4], [8,1]]

    for c1 in range(len(cube)):
        for c2 in range(c1, len(cube)):

                       
            valid = True
            for sq in square:
                if not CanBeRappresented(sq,cube[c1], cube[c2]):
                    valid = False
                    break
            if valid:
                result+=1


    return result

st = time.time()
print(solution())
print("--------- Process completed in " + str((time.time() - st) * 1000) + " ms ---------")