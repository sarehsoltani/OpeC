'''
Thresholding means binarization of an image. Convert an image to a binary image where 
pixels are either 0 or blank, or 255 or white. 
For doing that, we set a threshold and every pixel with lower than 
that will be consider as 0, and higher than threshold will be set to 255.
Two type of thresholding: Simple or adaptive
'''
import cv2 as cv

img =  cv.imread('Resources/Photos/cat.jpg')
cv.imshow('img', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Simple thresholding
threshold, thresh =  cv.threshold(gray, 140, 255, cv.THRESH_BINARY)  #threshold is 150, and thresh is the binarized image
cv.imshow('thresh', thresh)

cv.waitKey(0)

