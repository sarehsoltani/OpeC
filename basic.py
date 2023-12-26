import cv2 as cv

img  = cv.imread('Resources/Photos/park.jpg')
cv.imshow('image', img)

# converting to grayscale
grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray image', grayImg)



# Blur: one way to reduce the noise is to apply a blur slide: (7,7) is kernel size: the window that opencv use to calculte the bulr image
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('blurimage', blur)    

'''
image gradient is the building block of any edge detection algorithm. 
The gradient can be defined as the change in the direction of the intensity level of an image. the gradient helps us measure how the 
image changes and based on sharp changes in the 
intensity levels; it detects the presence of an edge.
Image gradient is used to extract information from an image. It is one of the fundamental building blocks in image processing and 
edge detection. 
The main application of image gradient is in edge detection.
Gradient magnitude represents the strength of the change in the intensity level of the image
We can find out the gradient of any image by convoluting a filter over the image

More formally, an edge is defined as discontinuities in pixel intensity, or more simply, a sharp difference and change in pixel values.
'''
# edge detection or cascading: there are alot of methods for detecting edges. The popular edge detection algorithm is canny
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canndy Edges', canny)   # for reducing the number of edges, we can pass the blur image to canny 

'''
Dilation adds pixels to the boundaries of objects in an image, 
while erosion removes pixels on object boundaries.
'''
# dilating the image: make the edges thicker
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow("dilated", dilated)

eroding = cv.erode(dilated, (3,3), iterations=3)
cv.imshow("Eroded", eroding)


#resize 
resized =  cv.resize(img, (300,300), interpolation=cv.INTER_CUBIC) #interpolation = cv.INTER_AREA is used when you are shrinking the image to the dimensions smaller than they are. INTER_CUBIC: enlarging the image
cv.imshow("Resized", resized)

# Cropping
cropped = img[50:300, 300:500]
cv.imshow('Cropped', cropped) 

cv.waitKey(0)