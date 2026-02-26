# Find the difference between the sum of the squares of the first one hundred natural numbers
# and the square of the sum.

def SumSquareDifference(n):
    sumsquare = 0
    sum = 0
    for i in range(n+1):
        sumsquare += i**2
        sum += i
    return sum**2 - sumsquare

print(SumSquareDifference(100))
