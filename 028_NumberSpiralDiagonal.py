def NumberSpiralDiagonal(n):
    sum = 1
    num = 1
    for i in range(3,n+1,2):
        vert = (i-2)*4+4
        vert1 = (i-2)+num+1
        vert2 = vert1 + i-1
        vert3 = vert2 + i-1
        vert4 = vert3 + i-1
        sum += vert1 + vert2 + vert3 +vert4
        num += vert
        print(i,vert, num,"v"+str(vert1), vert2, vert3,vert4)
    return sum
print(NumberSpiralDiagonal(1001))
