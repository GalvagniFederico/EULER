def Solve():
    print("")
    # matrix = [
    #     [131,673,234,103,18],
    #     [201,96,342,965,150],
    #     [630,803,746,422,111],
    #     [537,699,497,121,956],
    #     [805,732,524,37,331]
    # ]
    matrix = [[int(points) for points in line.replace("\n","").split(",")] for line in open("81 Path Sum two ways/matrix.txt") ]


    
    matrix2 = [[j for j in i] for i in matrix]
    
    for x in range(len(matrix)-1,-1, -1):
        for y in range(len(matrix[x])-1,-1,-1):
            if y < len(matrix[x]) -1 and x < len(matrix) - 1:
                matrix[x][y] += min(matrix[x+1][y],matrix[x][y+1])
            elif x < len(matrix) -1:
                matrix[x][y] += matrix[x+1][y]
            elif y < len(matrix[x]) -1:
                matrix[x][y] += matrix[x][y+1] 



    return matrix[0][0]


def prova():
    matrix = [[int(points) for points in line.replace("\n","").split(",")] for line in open("81 Path Sum two ways/matrix.txt") ]
    modified = [[999999999 for i in range(81)] for j in range(81)]

    for i in range(80):
        for j in range(80):
            modified[i][j] = matrix[i][j]

    modified[80][79] = modified[79][80] = modified[80][80] = 0

    for i in range(79, -1, -1):
        for j in range(79, -1, -1):
            modified[i][j] += min(modified[i + 1][j], modified[i][j + 1])

    print(modified[0][0])
print(Solve())
#prova()