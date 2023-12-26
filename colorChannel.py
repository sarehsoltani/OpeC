import cv2 as cv

img  = cv.imread('Resources/Photos/park.jpg')
cv.imshow('image', img)

'''
These pictures display as grayscale images that show the distribution of pixel intensities.
Ligher regions shows there is a far more concentration of those pixel values, and darker shows a little or even no pixels in that region.
For example in blue picture of this park, the sky is almost white that shows the high concentration of blue in the sky

'''
b, g, r = cv.split(img)
cv.imshow('blue', b)
cv.imshow('red', r)
cv.imshow('green', g)

cv.waitKey(0)