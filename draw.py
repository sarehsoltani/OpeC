import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
# blank[:] = 0,255,0
cv.imshow('image', blank)
# cv.waitKey(0)

#draw rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2,250), (0.0,255), thickness=cv.FILLED)

#draw circle
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 50, (0,0,255))
cv.imshow('circle', blank)
cv.waitKey(0)