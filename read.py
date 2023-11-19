import cv2 as cv

img = cv.imread('Resources/Photos/cat_large.jpg')
#handling size
cv.imshow('Cat', img)
cv.waitKey(0)