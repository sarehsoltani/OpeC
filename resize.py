import cv2 as cv

def resizeFrame(img, scale = 0.75):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dimensions = (width, height)
    resizedImg = cv.resize(img, dimensions)
    return resizedImg

#resize image
# img = cv.imread('Resources/Photos/cat_large.jpg')
# resizedImg = resizeFrame(img)
# cv.imshow('Image', img)
# cv.imshow('Image1', resizedImg)
# # print(img.shape) #height, width, channels = img.shape 
# cv.waitKey(0)

#resize video
vidCapture = cv.VideoCapture('Resources/Videos/dog.mp4')
while True:
    isTrue, frame = vidCapture.read()
    resizedFrm = resizeFrame(frame)
    cv.imshow('video1',frame)
    cv.imshow('video2', resizedFrm)
    if cv.waitKey(20) & 0xFF == 'q':
        break
vidCapture.release()
cv.destroyAllWindows()


