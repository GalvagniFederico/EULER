def Solve(iteration):
    result = 0

    numerator = 3
    denominator = 2

    iteration -=1
    for expansion in range(iteration):
        if len(str(numerator)) > len(str(denominator)):
            result+=1
        
        #Generate next expansion
        
        newDenominator = numerator + denominator
        newNumerator = newDenominator + denominator

        numerator = newNumerator
        denominator = newDenominator

    return result

print(Solve(1000))