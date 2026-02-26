# Work out the first ten digits of the sum of one-hundred 50-digit numbers.

def LargeSum():
    f = open("largesum.txt", "r")
    lines = f.readlines()
    d = [int(line) for line in lines]
    sum = 0
    for n in d:
        sum += n
    return str(sum)[0:10]

print(LargeSum())
