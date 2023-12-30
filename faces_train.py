import os
import numpy as np
import cv2 as cv

p = []
for i in os.listdir('Resources/Faces/train/'):
    p.append(i)
print(p) 

DIR = r'/Users/sarehsoltani/Documents/OpeCV/Resources/Faces/train/'

features = []
label = []
