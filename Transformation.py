import cv2 as cv
import numpy as np

img  = cv.imread('Resources/Photos/park.jpg')
cv.imshow('image', img)

# shift image
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, 100, 100)
# cv.imshow('image', translated)

# Rotate
def rotate(img, angle, rotPoint = None):
    (width, height) = img.shape[:2]
    if rotPoint == None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, scale = 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 40)
cv.imshow('Rotated Image', rotated)




cv.waitKey(0)