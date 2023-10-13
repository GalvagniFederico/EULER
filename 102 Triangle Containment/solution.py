# Three distinct points are plotted at random on a Cartesian plane, for which -1000 <= x, y <= 1000, 
# such that a triangle is formed.

# Consider the following two triangles:
#   A(-340,495), B(-153,-910), C(835,-947)
#   X(-175,41), Y(-421,-714), Z(574,-645)
 
# It can be verified that triangle  ABC
# contains the origin, whereas triangle XYZ 
# does not.
#
# Using triangles.txt, a 27K text file containing the co-ordinates of one thousand "random" triangles, find the number of triangles 
# for which the interior contains the origin.
#
# NOTE: The first two examples in the file represent the triangles in the example given above.

import math
import cv2
import numpy as np

def ConvertX(x):
    return int(x/0.2)



def Solution():

    triangles = np.array([[int(points) for points in line.replace("\n","").split(",")] for line in open("102 Triangle Containment/triangles.txt")])
    
    img = np.zeros((400,400,3), dtype = "uint8")

    for triangle in triangles:
        cv2.line(img, (ConvertX(triangle[0]), ConvertX(triangle[1])), (ConvertX(triangle[2]), ConvertX(triangle[3])), (0, 0, 255), 1) 
        cv2.imshow('dark', img)
        cv2.line(img, (ConvertX(triangle[1]), ConvertX(triangle[2])), (ConvertX(triangle[3]), ConvertX(triangle[4])), (0, 255, 0), 1) 
        cv2.imshow('dark', img)
        cv2.line(img, (ConvertX(triangle[3]), ConvertX(triangle[4])), (ConvertX(triangle[0]), ConvertX(triangle[1])), (255, 0, 0), 1) 
        cv2.imshow('dark', img)
        cv2.waitKey(0)



    
    





    cv2.waitKey(0)


Solution()