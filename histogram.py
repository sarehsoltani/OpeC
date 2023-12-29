'''
histogram allows you to visualize the distribution of pixel intensities in an image.
we can compute the histogram for rgb or graysclae images
'''

import cv2 as cv
import matplotlib.pyplot as plt 
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

blank =  np.zeros(img.shape[:2], 'uint8')
# cv.imshow("blank", blank)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('circle', mask)

masked = cv.bitwise_and(gray, gray, mask= mask)
cv.imshow('masked', masked)



'''
grayscale histogram: hist size is # of bins , the range of pixel values
'''
#gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])
# plt.figure()
# plt.title('Grayscale histogram')
# plt.xlabel('bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# color histogram
# plt.figure()
# plt.title('Colorful histogram')
# plt.xlabel('bins')
# plt.ylabel('# of pixels')
# colors = ('b', 'g', 'r')
# for i,col in enumerate(colors):
#     hist = cv.calcHist([img], [i], None, [256], [0, 256])
#     plt.plot(hist, color = col)
#     plt.xlim([0,256])
# plt.show()
cv.waitKey(0)   