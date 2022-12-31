

def MaximumPathSum():
    triangle = [[int(i) for i in line.replace("\n", "").split(" ")] for line in open("file/018_MaximumPathSum.txt", "r").readlines()]
    #triangle = [[3], [7,4], [2,4,6], [8, 5, 9, 3]]
    last = triangle[0]
    for i in range(1, len(triangle)):
        len_linea =  len(triangle[i])
        current = [0]*len_linea
        for j in range(len_linea):
            
            if(j == 0):
                current[j] = triangle[i][0] + last[0]
            elif (j == len_linea-1) :
                current[j] = triangle[i][len_linea-1] + last[len_linea-2]
            else:
                current[j] = max(last[j]+triangle[i][j], last[j-1]+triangle[i][j])
        last = current
    return max(last)
print(MaximumPathSum())