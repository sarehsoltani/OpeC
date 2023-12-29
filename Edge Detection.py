import cv2 as cv
import numpy as np

img  = cv.imread('Resources/Photos/park.jpg')
cv.imshow('image', img)

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# edge detection
canny = cv.Canny(gray,125, 175)
cv.imshow("Canny Edges", canny)

# Lablacian
"""
A Laplacian filter is an edge detector used to compute the second derivatives of an image,
measuring the rate at which the first derivatives change. This determines 
if a change in adjacent pixel values is from an edge or continuous progression.
Laplacian computes the gradient of gray scale image. When you transition from white to black and vise versa 
the slope will be negative and positive ==> absolute
"""
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Lablacian Edges", lap)

cv.waitKey(0)