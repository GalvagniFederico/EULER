def PandigitalProduct():
    pand1_9 = ["1","2","3","4","5","6","7","8","9"]
    limit = 10000
    result = 0
    count = 0
    d = set()
    for i in range(limit):

        for j in range(i+1, limit-i):
            if(len(str(i)) + len(str(j)) + len(str(i*j))>9):
                break
            s = str(i) + str(j) +str(i*j)
            v =[c for c in s]
            v.sort()

            if(v == pand1_9):
                print(i,j,i*j)
                d.add(i*j)

    result = sum(d)
    print(result, count)
    print(d)

PandigitalProduct()