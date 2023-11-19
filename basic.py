import cv2 as cv

img  = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('image', img)

# converting to grayscale
grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray image', grayImg)
cv.waitKey(0)