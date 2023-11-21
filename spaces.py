import cv2 as cv

'''
color space is a system of representing an array of pixel color like RGB, Grayscale.
Default way of opencv to read images is BGR. but matplotlib reads RGB
'''
img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('image', img)

# BRG to Gray. graysacle show the distribution of pixel intensity at particularlocations of your image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# BGR to HSV:hue saturation value and it is based on how human conceive of color
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

# BGR to LAB: wash version of BRG: human based 
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('hsv', lab)


cv.waitKey(0)  