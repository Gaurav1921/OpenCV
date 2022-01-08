""" CHAPTER 3: Basic Functions """

import cv2
print("Package Imported")

img = cv2.imread("download.png")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # converts images into different colors
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)    # to make our image blurry
# ksize will only have odd nos

imgCanny = cv2.Canny(img, 200, 200)        # for edge detection
# 100, 100 are thresold values ( to reduce a lot of edges we can increase the thresolds)

import numpy as np

# we can also increase the thikness of our edges so that they are visible properly
kernel = np.ones((3, 3), np.uint8)   # or kernel = (3,3)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
# iterations means thickness

imgEroded = cv2.erode(imgDialation, kernel, iterations=1)
# erodeion is opposite of dilation i.e. reducing the thickness of the img
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)