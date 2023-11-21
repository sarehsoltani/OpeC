import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow("Image", img)

grayed = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayed", grayed)

blured = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow("Blured", blured)

canny = cv.Canny(blured,125, 175)
cv.imshow("Canny Edges", canny)

'''
another way to detect edges is using threshold. 
threshold look at image and try to binarized it. 
if the pixel value is below 125 convert it to zero or black, and above the 125 set to white. 
So it takes an image and then try to binarize it. 
'''
ret, thresh = cv.threshold(grayed, 125, 255, cv.THRESH_BINARY )
cv.imshow('thresh', thresh)
# in order to reduce the number of contours we can pass the blur one to calculate the edges and then find contours

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours ')


cv.waitKey(0)