""" CHAPTER 2: Read Images-Videos-Webcam """

import cv2
print("Package Imported")

img = cv2.imread("lambo.jpeg")       # this means we are reading a image

cv2.imshow('Output', img)              # to display the image

"""
The image did appear but it went out very quickly
"""

cv2.waitKey(0)           # 0 means it will wait till infinite millisec and if value inserted then in ms wait period

"""
2. For Videos
"""

# cap = cv2.VideoCapture('Whatever Path paste here')

# A video is just a seqeunce of images, so we will need a while loop to go through each image one by one."""

"""
while True:
    sucess, img = cap.read()          # save our image in img adn tell us whether it was successful or not
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
"""


"""Using a WebCam"""

# instead of file path we will use id of webcam i.e 1 if one webcam, 2 if 2 webcams are there

cap = cv2.VideoCapture(0)     # created a webcam object
cap.set(3, 640)    # id 3 with 640 width
cap.set(4, 480)    # id 4 with 480 height
cap.set(10, 100)   # for brightness id is 10 and set to 100

while True:
    sucess, img = cap.read()          # save our image in img adn tell us whether it was sucessful or not
    cv2.imshow("Video", img)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break




