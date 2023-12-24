def Solve():
    matrix = [[int(points) for points in line.replace("\n","").split(",")] for line in open("81 Path Sum two ways\matrix.txt") ]

    for x in range(len(matrix)-1,-1, -1):
        for y in range(len(matrix[x])-1,-1,-1):
            if y < len(matrix[x]) -1 and x < len(matrix) - 1:
                matrix[x][y] += min(matrix[x+1][y],matrix[x][y+1])
            elif x < len(matrix) -1:
                matrix[x][y] += matrix[x+1][y]
            elif y < len(matrix[x]) -1:
                matrix[x][y] += matrix[x][y+1] 



    return matrix[0][0]


print(Solve())