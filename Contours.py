import cv2 as cv
import numpy as np
import os

'''
Countours are boundaries of objs. line or curves that connect the dots around the obhects. Different from edges. 
Usefull for object detection and recognition
'''

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow("Image", img)
cv.imwrite('img.jpg', img)

grayed = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayed", grayed)
cv.imwrite('graded.jpg', grayed)

blured = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow("Blured", blured)
cv.imwrite('Blured.jpg', blured)

# edge detection
canny = cv.Canny(blured,125, 175)
cv.imshow("Canny Edges", canny)
cv.imwrite('CannyEdges.jpg', canny)
# contour detection
# Method 1: Make the image blur and then find the edges with canny
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# print(f'{len(contours)} contours')

'''
Method 2: 
another way to detect edges is using threshold. 
threshold look at image and try to binarized it. 
if the pixel value is below 125 convert it to zero or black, and above the 125 set to white. 
So it takes an image and then try to binarize it. 
cv.THRESH_BINARY: it is the threshold method that binarize the image
'''

ret, thresh = cv.threshold(grayed, 125, 255, cv.THRESH_BINARY )
cv.imshow('Thresh Edges', thresh)
cv.imwrite('Threshedges.jpg', thresh)
# in order to reduce the number of contours we can pass the blur one to calculate the edges and then find contours


'''
In order to find contours, we can use the findContours method. this method returns two things: contours and hierachies
findContours: it looks to the structed elements or the found edges (output of canny).
the returned contour is a python list of all the coordinates of the contours. hierarchies: representation of them
cv.RETR_LIST: It returns the list of all countours
cv.CHAIN_APPROX_NONE: IT is the countour approximation methods. CHAIN_APPROX_NONE: it does nothing.  
CHAIN_APPROX_SIMPLE: It compresses all the return contours in the simple ones. For example: instead of returning all contours of a line, it just returns two end points.
#of contours is the lenght of the countours 
'''
# contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours')

'''
Visualize the contours: 
drow the found contours on the blank image
'''
blank = np.zeros(img.shape, dtype='uint8')
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow("Contours Drown", blank)
cv.imwrite('Contours.jpg', blank)
cv.waitKey(0)