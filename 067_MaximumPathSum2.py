import time 

def MaximumPathSum():
    start_time = time.time()
    triangle = [[int(i) for i in line.replace("\n", "").split(" ")] for line in open("file/067_MaximumPathSum2.txt", "r").readlines()]
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
    print(time.time()-start_time)
    return max(last)
print(MaximumPathSum())