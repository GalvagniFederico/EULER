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
import time 

x = 0
y = 1




def ConvertPoint(p):

    return [round((p[0] +1000)*0.2), 400 - (round((p[1] +1000)*0.2))]

def ConvertLinear(p):
    return round(p*0.2)

def DrawPoint(img, point, color):
    point = ConvertPoint(point)
    cv2.circle(img, (point[0],point[1]), 3,color,2)

def DrawSegment(img, a, b, color):
    a = ConvertPoint(a)
    b = ConvertPoint(b)
    cv2.line(img, (a[x], a[y]), (b[x], b[y]), color, 1)


def DrawTriangle(triangle, img):
    a = triangle[0]
    b = triangle[1]
    c = triangle[2]

    DrawSegment(img,a,b,  (255,0,0))
    DrawSegment(img,b,c,  (0,255,0))
    DrawSegment(img,c,a,  (0,0,255))

    text = "A(" + str(a[x]) + "," + str(a[y]) +"), " + "B(" + str(b[x]) + "," + str(b[y]) +"), " + "C(" + str(c[x]) + "," + str(c[y]) +")"
    cv2.putText(img,text,(20,12),cv2.FONT_HERSHEY_DUPLEX,0.4,(200,200,200))

def DistanceBetweenTwoPoints(p1,p2):
    return math.sqrt(math.pow(p2[x] - p1[x],2) + math.pow(p2[y] - p1[y],2))


def SlopeFromPoints(segment):
    a,b=0,1
    m = ((segment[a][y]-segment[b][y])/(segment[a][x]-segment[b][x]))
    return m

def FindQ(a,m):
    # y = mx + q
    # q = y-mx
    q = a[y]-(m*a[x])
    return q

def CenterOfSegment(line):
    a, b = 0,1
    return [(line[a][x] + line[b][x])/2,(line[a][y] + line[b][y])/2]


def SegmentIntersection(m1,q1,m2,q2):
    # y = m1x + c1
    # y = m2x + c2
    # m1x + c1 = m2x +c2 
    # x = (c1 - c2)/(m2 - m1)
    x = (q1 - q2)/(m2 - m1)
    y = (m1 * x) +q1
    return [x,y]

def TriangleCOG(triangle, centerAB, centerBC):
    a, b, c = 0,1,2

    segment1 = [centerAB, triangle[c]]
    segment2 = [centerBC, triangle[a]]
    m1 = SlopeFromPoints(segment1)
    m2 = SlopeFromPoints(segment2)
    q1 = FindQ(triangle[c],m1)
    q2 = FindQ(centerBC,m2)
    intersection = SegmentIntersection(m1,q1,m2,q2)

    return intersection
    

def Solution():    
    img = np.zeros((500,400,3), dtype = "uint8")
    imgClone = img.copy()

    a = 0
    b = 1
    c = 2

    triangles = np.array([[int(points) for points in line.replace("\n","").split(",")] for line in open("102 Triangle Containment/triangles.txt")])
    triangles = triangles.reshape(len(triangles),3,2)

    origin = [0,0]

    for triangle in triangles:
        centerAB = CenterOfSegment([[triangle[a][x],triangle[a][y]],[triangle[b][x],triangle[b][y]]])
        centerBC = CenterOfSegment([[triangle[b][x],triangle[b][y]],[triangle[c][x],triangle[c][y]]])
        centerCA = CenterOfSegment([[triangle[c][x],triangle[c][y]],[triangle[a][x],triangle[a][y]]])

        CenterOfGravity = TriangleCOG(triangle, centerAB, centerBC)

        DistanceCogOrigin = DistanceBetweenTwoPoints(CenterOfGravity, origin)

        ### DRAWING ###
        img = imgClone.copy()

        # Triangle
        DrawTriangle(triangle, img)

        # Draw Median Line 
        DrawSegment(img, centerAB, triangle[c], (252, 245, 95))
        DrawSegment(img, centerBC, triangle[a], (252, 245, 95))
        DrawSegment(img, centerCA, triangle[b], (252, 245, 95))

        # Origin Radius
        cv2.circle(img, ConvertPoint(CenterOfGravity),ConvertLinear(DistanceCogOrigin),(123,43,53))

        # Segment Middle Point
        DrawPoint(img, centerAB, (200,200,200))
        DrawPoint(img, centerBC, (200,200,200))
        DrawPoint(img, centerCA, (200,200,200))

        # Line from COG to origin
        DrawSegment(img, CenterOfGravity, origin, (0,255,0))

        # Center of Gravity
        DrawPoint(img, CenterOfGravity, (0,0,255))

        # Origin
        DrawPoint(img,origin, (255,0,255))


        # Draw
        cv2.imshow("triangle",img)

        cv2.waitKey(0)



Solution()