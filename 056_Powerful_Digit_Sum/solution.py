import math
def Solve(a,b):
    result = 0
    for i in range(0,a + 1):
        for j in range(0,b +1):
            power = i
            for x in range(j-1):
                power *= i
                
            digitSum = 0
            for c in str(power).split(",")[0]:
                digitSum += int(c)

            if digitSum > result:
                result = digitSum

    return result

print(Solve(99,99))