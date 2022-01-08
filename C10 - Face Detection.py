""" CHAPTER 10: Face Detection """

import cv2
import numpy as np

print("Package Imported")

# to detect faces we will use the technique proposed by Viola and Jones (for almost a decade)

# we will collect lots of positive images - images of faces
# we will collect lots of negative images - images of anything but faces
# we will train the data using these positives and negatives and create a cascade (XML) file that will help us find faces

# in here we wont train any model instead we will use a pretent file for faces  (provided by OpenCV)
# OpenCV has already given default cascades which can detect eye, cat face, full body, frontal face, licence plate, etc

# to create custom cascades go to Murtaza's Workshop YT lectures

# we will add our cascade
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('face.jfif')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(img, 1.1, 4)   # scale should be more than 1
print(faces)

# for creating a rectangle (boundary box) shape around the faces that we have detected.
# for that we have to loop through all the faces that we have detected

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 255), 2)

# to detect more objects such as cars, mobiles, etc, then we can make our own custom cascades

cv2.imshow("Result", img)

cv2.waitKey(0)


