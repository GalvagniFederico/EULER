# http://radiusofcircle.blogspot.com

# time module
import time

# time at the start of program execution
start = time.time()

# 4 digit triangular numbers
tria = [n*(n+1)/2 for n in range(45, 141)]

# 4 digit square numbers
squa = [pow(n, 2) for n in range(32, 100)]

# 4 digit pentagonal numbers
pent = [n*(3*n-1)/2 for n in range(26, 82)]

# 4 digit hexagonal numbers
hexa = [n*(2*n-1) for n in range(23, 71)]

# 4 digit heptagonal numbers
hept = [n*(5*n-3)/2 for n in range(21, 64)]

# 4 digit octagonal numbers
octa = [n*(3*n-2) for n in range(19, 59)]

# tuples of 4 digit number split into 2-2 digits
# triangular numbers tuples
tria_div = [(x/100, x - (x/100)*100) for x in tria]

# square numbers tuples
squa_div = [(x/100, x - (x/100)*100) for x in squa]

# pentagonal numbers tuples
pent_div = [(x/100, x - (x/100)*100) for x in pent]

# hexagonal numbers tuples
hexa_div = [(x/100, x - (x/100)*100) for x in hexa]

# heptagonal numbers tuples
hept_div = [(x/100, x - (x/100)*100) for x in hept]

# octagonal numbers tuples
octa_div = [(x/100, x - (x/100)*100) for x in octa]

# all polygonal numbers except octagonal numbers
tsphh = [hept_div, hexa_div, pent_div, squa_div, tria_div]

# function to find the sum of the given tuples
def find_sum(numbers):
    summation = 0
    for num in numbers:
        summation += num[0]*100+num[1]
    print (summation)

# polgon 2
for polygon2 in tsphh:
    # octagonal number tuples will be polygon 1
    for n1 in octa_div:
        # for each number in polygon 2
        for n2 in polygon2:
            # check the cyclicity
            if n1[1] == n2[0]:
                # polygon 3
                for polygon3 in tsphh:
                    # check if we are not using the same polygon again
                    if polygon3 != polygon2:
                        # for each number in polygon 3
                        for n3 in polygon3:
                            # check the cylicity
                            if n2[1] == n3[0]:
                                # polygon 4
                                for polygon4 in tsphh:
                                    if (polygon4 != polygon3 and
                                        polygon4 != polygon2):
                                        for n4 in polygon4:
                                            if n3[1] == n4[0]:
                                                # polygon 5
                                                for polygon5 in tsphh:
                                                    if (polygon5 != polygon4 and
                                                        polygon5 != polygon3 and
                                                        polygon5 != polygon2):
                                                        for n5 in polygon5:
                                                            if n4[1] == n5[0]:
                                                                # polygon 6
                                                                for polygon6 in tsphh:
                                                                    if (polygon6 != polygon5 and
                                                                        polygon6 != polygon4 and
                                                                        polygon6 != polygon3 and
                                                                        polygon6 != polygon2):
                                                                        for n6 in polygon6:
                                                                            if n6[0] == n5[1] and n6[1] == n1[0]:
                                                                                numbers = [n1, n2, n3, n4, n5, n6]
                                                                                find_sum(numbers)

