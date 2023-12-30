import cv2 as cv

'''
Face detection involves detecting a presence of a face within an image by using the classifiers.
OpenCV has a pre_trained classifier named haarcascade. Face detection doesn't involve skin tone or colors 
so we convert the image to gray scale. Haar cascade look at objects in the image and 
using the edges to determine whether it's a face or not.

https://medium.com/analytics-vidhya/haar-cascades-explained-38210e57970d
https://mccormickml.com/2013/12/13/adaboost-tutorial/#:~:text=AdaBoost%20is%20a%20popular%20boosting,female%20based%20on%20their%20height.

The detectMultiScale function is a part of the OpenCV library and is commonly used for object 
detection in images. It takes a grayscale image as input and returns a list of rectangles where the target object is found. The function employs the Haar Cascade classifier
to detect objects at different scales and locations within the image.

Haar cascades XML files are used in computer vision and particularly in the field of object detection. They are a part of the Haar-like feature-based cascade classifiers, originally proposed by Viola and Jones. These classifiers are utilized to identify objects or patterns within images.
The Haar cascade XML file contains a trained model that includes a series of stages, each comprising multiple weak classifiers. These weak classifiers are based on Haar-like features, which are simple rectangular filters applied to subsections of an image to detect specific patterns like edges, corners, or textures.
During training, the cascade classifier learns to differentiate between positive samples (images containing the object to be detected) and negative samples (images without the object). The XML file encapsulates the learned information about the features and classifiers that can be utilized for object detection purposes.
This XML file can be used with libraries like OpenCV, a popular computer vision library, to perform object detection tasks. OpenCV provides methods to load these pre-trained Haar cascade XML files and apply them to images or video streams for object detection tasks such as face detection, pedestrian detection, or other objects of interest.

XML files are the pre-trained classifiers




'''

img = cv.imread('Resources/Photos/group 2.jpg')
cv.imshow('person', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person', gray)

# CascadeClassifier class reads those lines in xml file and store them in a var
# Let's load the required XML classifiers.
f_cascade = cv.CascadeClassifier('haar_face.xml')

# We use detectMultiScale() to find faces or eyes
# scaleFactor – Parameter specifying how much the image size is reduced at each image scale.
# minNeighbors – Parameter specifying how many neighbors each candidate rectangle should have to retain it.
faces = f_cascade.detectMultiScale(gray, 1.1, 6)
print(faces)
print(f'Number of detected faces = {len(faces)}')
for (x,y,w,h) in faces:
    cv.rectangle(img, (x,y), (x+w, y+h), (0, 255,0), thickness=2)
cv.imshow('Detected Faces', img)

cv.waitKey(0)