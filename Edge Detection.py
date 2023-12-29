import cv2 as cv
import numpy as np

img  = cv.imread('Resources/Photos/park.jpg')
cv.imshow('image', img)

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# edge detection
# 1. Lablacian
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
cv.imwrite('Lablacian.jpg', lap)

# 2. Sobel: it computes the gradient into two directions (x and y)
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combinedSobel = cv.bitwise_or(sobelx, sobely)

cv.imshow("Sobel X", sobelx)
cv.imshow("Sobel Y", sobely)
cv.imshow("Combined Sobel", combinedSobel)
cv.imwrite('CombinedSobel.jpg', combinedSobel)

# 3. Canny: it is the more advanced one that uses the sobel in one of its steps
canny = cv.Canny(gray,150, 175)
cv.imshow("Canny Edges", canny)
cv.imwrite('Canny.jpg', canny)

cv.waitKey(0)