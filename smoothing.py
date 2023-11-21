import cv2 as cv
'''
we smooth an image when it has alot of noises caused from camera sensors, lighting. 
we can smooth out the image and reduce some of the noise by applying some bluring method. 
for applying the bluring methods, they are alot of way of calculating the pixel intensity of middle pixel in a kernel. 
kernel is a window that drow over the image.

'''
img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cat', img)

# Averageing: calculate the center pixel value by averaging all of thr surronding pixel intensities
average = cv.blur(img, (7,7))
cv.imshow('Avg blur', average)

# Gaussian Blur: 
# instead of computing the avg of all this surronding pixels, each of surronding pixels gives a particular weight. The average of the products of those weights gives you the value for the center one. So, it gives you less blur one compared to averaging one. So the gaussian blur is more natural as compared to the avg. 
# sigmaX is the standard deviation in x direction
gassian = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gassian)

# Median: finding the median of surronding pixels instead of average. It's more effective than previous ones.
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)  # less blur than gaussian one

# Bilateral: the most effective method: it blurs an image without reducing the edges
bilateral = cv.bilateralFilter(img, 5, 15, 50)
cv.imshow('bilateral Blur', bilateral)



cv.waitKey(0)   