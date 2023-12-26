import cv2 as cv
#reading image
img = cv.imread('Resources/Photos/cat_large.jpg')
cv.imshow('Cat', img)
cv.waitKey(0)   
# #waitkey() function of Python OpenCV allows users to display a window for given milliseconds or until any key is pressed.
# -215: assertion failed: cannot find and read the media we shared or it runs out of the frames

# #reading videos
# capture = cv.VideoCapture('Resources/Videos/dog.mp4')
# # read video frame by frame
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('video', frame)
#     if cv.waitKey(20) & 0xFF ==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()
# Define a video caoture obj
# cap = cv.VideoCapture('./Resources/Videos/kitten.mp4')
# while(True):
#     # capture the video frame by frame 
#     isTrue , frame = cap.read()
#     cv.imshow('frame', frame)
#     if cv.waitKey(20) & 0xFF == ord('q'):
#         break

# cap.release()
# cv.destroyAllWindows()