import math
import cv2
import numpy as np
import time 

class Node():
    def __init__(self, x, y, weight, path):
            self.x = x
            self.y = y
            self.weight = weight
            self.path = path

img = np.zeros((1000,1000,3), dtype = "uint8")

def Draw(matrix, path):
    matrixDim = 10
    for i in range(len(matrix) + 1):
        cv2.line(img, [i*matrixDim, 0], [i*matrixDim,matrixDim*len(matrix)],(255,255,255),1)

    for i in range(len(matrix[0]) + 1):
        cv2.line(img, [0,i*matrixDim], [matrixDim*len(matrix),i*matrixDim],(255,255,255),1)
    
  

    for x in path:
        cv2.rectangle(img,[x[0]* matrixDim, x[1]*matrixDim],[x[0]* matrixDim +matrixDim, x[1]*matrixDim + matrixDim], (255,0,0))

    cv2.imshow("triangle",img)
    cv2.waitKey(10)
            
    


def Solve():
    matrix = [[int(point) for point in line.replace("\n","").split(",")] for line in open("82_Path_Sum_Tree_Ways\matrix.txt") ]
    # matrix = [
    #     [1,1,8,8,8],
    #     [8,1,8,8,8],
    #     [1,1,8,8,8],
    #     [1,8,1,1,1],
    #     [1,1,1,8,1]
    #     ]
    # matrix = [
    #     [131,673,234,103,18],
    #     [201,96,342,965,150],
    #     [630,803,746,422,111],
    #     [537,699,497,121,956],
    #     [805,732,524,37,331]
    # ]
    matrix =[ 
    [1,1,1],
    [1,1,1],
    [0,1,1]]

    sizeY = len(matrix) 
    sizeX = len(matrix[0])

    visited = [[False for i in j] for j in matrix]
    queue = []

    queue.append(Node(0,0,matrix[0][0], [[0,0]]))

    while (len(queue) > 0):
         
        # Pick lowest weight node from queue
         
        smallestWeight = queue[0].weight
        nextNodeIndex = 0

        for i in range(len(queue)):
            if queue[i].weight < smallestWeight:
                nextNodeIndex = i
        
        nextNode = Node(queue[nextNodeIndex].x,queue[nextNodeIndex].y, queue[nextNodeIndex].weight, queue[nextNodeIndex].path) 
        del queue[nextNodeIndex]

        if visited[nextNode.y][nextNode.x]:
            continue

        # Set as visited
        visited[nextNode.y][nextNode.x] =True
         
        if nextNode.x == sizeX -1 and nextNode.y == sizeY -1:
            return nextNode.weight

        # Put next nodes in queue 
        # Right move
        path = []
        if (nextNode.y + 1 < sizeY):
            path = [i for i in nextNode.path]
            path.append([nextNode.x,nextNode.y+1])
            queue.append(Node(nextNode.x, nextNode.y+1, nextNode.weight + matrix[nextNode.x][nextNode.y+1],path))

        path = []
        # Down move
        if (nextNode.x + 1 < sizeX):
            path = [i for i in nextNode.path]
            path.append([nextNode.x+1,nextNode.y])
            queue.append(Node(nextNode.x+1, nextNode.y, nextNode.weight + matrix[nextNode.x+1][nextNode.y], path))

        # Draw(matrix, nextNode.path)
    return -1



print(Solve())

