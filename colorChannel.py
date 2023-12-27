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

"""
For removing the noises and smoothing, we can apply blur methods. 
cv.blur(): smooth the image by calculating the intensity of middle index = avg surroonding ones
the higher kernel size the more being blured 
cv.Gaussianblur : it gives weight to each surronding points and then avg them: it results in less blured one but higher quality
cv.median: better result but it is not good for big kernel size. It acts better in lower
bilateral: make the img blur and keep the edges as well
"""



cv.waitKey(0)