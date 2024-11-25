# It is easily proved that no equilateral triangle exists with integral length sides and integral area. 
# However, the almost equilateral triangle 5-5-6 has an area of 12 square units.
# We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the
#  third differs by no more than one unit.

#Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area
#  and whose perimeters do not exceed one billion. 

import math


def is_area_int(a, b):
    # Calculate the semi-perimeter
    s = (a*2 + b) / 2
    # Calculate the area using Heron's formula
    area = math.sqrt(s * math.pow(s - a,2) * (s - b))
    return area == int(area)

print(is_area_int(5,6))

def Solve(limit):
    sum_of_perimeters = 0
    
    for a in range(2,limit+1,1):
        a2 = a*2
        b1 = a-1
        if is_area_int(a, b1):
            sum_of_perimeters+=a2+b1

        b2 = a+1
        if is_area_int(a, b2):
            sum_of_perimeters+=a2+b2

        
        a+=1
    return sum_of_perimeters

print(Solve(1_000_000))