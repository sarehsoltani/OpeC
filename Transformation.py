import cv2 as cv
import numpy as np

img  = cv.imread('Resources/Photos/park.jpg')
cv.imshow('image', img)

# shift image
def translate(img, x, y):
    TransMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, TransMat, dimensions)

translated = translate(img, 100, 100)
cv.imshow('image', translated)
cv.waitKey(0)