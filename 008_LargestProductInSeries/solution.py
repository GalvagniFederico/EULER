# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
# What is the value of this product?

def LargestProductInSeries(nd):
    f = open("digitmille.txt", "r") 
    s = f.read()
    n = [int(d) for d in str(s)]

    max = 0
    for i in range(nd-1, 999):
        product = 1
        for x in range(i, i-nd, -1):
            product *= n[x]
        if product > max:
            max = product

    return max

print(LargestProductInSeries(13))
