import cv2 as cv

img  = cv.imread('Resources/Photos/park.jpg')
cv.imshow('image', img)

# converting to grayscale
grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray image', grayImg)

# Blur: one way to reduce the noise is to apply a blur slide
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blurimage', blur)

'''
image gradient is the building block of any edge detection algorithm. 
The gradient can be defined as the change in the direction of the intensity level of an image. the gradient helps us measure how the image changes and based on sharp changes in the 
intensity levels; it detects the presence of an edge.
Image gradient is used to extract information from an image. It is one of the fundamental building blocks in image processing and edge detection. 
The main application of image gradient is in edge detection.
Gradient magnitude represents the strength of the change in the intensity level of the image
We can find out the gradient of any image by convoluting a filter over the image

More formally, an edge is defined as discontinuities in pixel intensity, or more simply, a sharp difference and change in pixel values.
'''


cv.waitKey(0)