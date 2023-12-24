import math

class Node():
    def __init__(self, x, y, weight):
            self.x = x
            self.y = y
            self.weight = weight

def Solve():
    matrix = [[int(point) for point in line.replace("\n","").split(",")] for line in open("82_Path_Sum_Tree_Ways\matrix.txt") ]
    sizeX = len(matrix) 
    sizeY = len(matrix[0])

    visited = [[False for i in j] for j in matrix]
    
    #Add starting node [0][0] to the queue
    queue = [Node(0,0, matrix[0][0])]

    while (len(queue) > 0):
         
        # Pick lowest weight node from queue
        smallestWeight = queue[0].weight
        nextNodeIndex = 0
        for i in range(len(queue)):
            if queue[i].weight < smallestWeight:
                smallestWeight = queue[i].weight 
                nextNodeIndex = i

        
        nextNode = Node(queue[nextNodeIndex].x,queue[nextNodeIndex].y, queue[nextNodeIndex].weight) 
        del queue[nextNodeIndex]

        if visited[nextNode.x][nextNode.y]:
            continue

        # Set as visited
        visited[nextNode.x][nextNode.y] =True
         
        if nextNode.y == sizeY -1 and nextNode.x == sizeX-1:
            return nextNode.weight

        # Put next nodes in queue 
        # Right move
        if (nextNode.y + 1 < sizeY):
            queue.append(Node(nextNode.x, nextNode.y+1, nextNode.weight + matrix[nextNode.x][nextNode.y+1]))

        # Down move
        if (nextNode.x + 1 < sizeX):
            queue.append(Node(nextNode.x+1, nextNode.y, nextNode.weight + matrix[nextNode.x+1][nextNode.y]))

        # Up move
        if nextNode.x > 0:
            queue.append(Node(nextNode.x - 1, nextNode.y, nextNode.weight + matrix[nextNode.x - 1][nextNode.y]))

        # # Left move
        if (nextNode.y > 0):
            queue.append(Node(nextNode.x, nextNode.y - 1, nextNode.weight + matrix[nextNode.x][nextNode.y -1]))
    return -1

print(Solve())

