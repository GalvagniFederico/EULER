# Find the first four consecutive integers to have four distinct prime factors each.
# What is the first of these numbers?

def npf(number):
    """function which will return the number of prime factors"""
    i = 2
    a = set()
    while i < number**0.5 or number != 1:
        if number % i == 0:
            number = number / i
            a.add(i)
            i -= 1
        i += 1
    return len(a)

def DistinctPrimesFactors(d):
    count_series = 0
    first_occurence = 0
    i = 1
    while True:
        count = npf(i)
        if count == d:
            count_series += 1
            if first_occurence == 0:
                first_occurence = i
            if count_series == d:
                print(first_occurence)
                return
        else:
            count_series = 0
            first_occurence = 0
        i += 1

DistinctPrimesFactors(4)
