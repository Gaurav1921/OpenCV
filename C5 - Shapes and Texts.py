""" CHAPTER 5: Shapes and Texts """

import cv2
import numpy as np
print("Package Imported")

# how to draw shapes (lines, rectangles) on images

img = np.zeros((512, 512), np.uint8)   # matrix filled with zeros (means black)  (512x512 pixels)
print(img)
print(img.shape)    # to check the dimensionality of the image

# This is a gray scale image as it has only 2D given (not the RGB value i.e. 3)
# to add the color functionality we have to give it 3 channels

img1 = np.zeros((512, 512, 3), np.uint8)
print(img1)

# img1[:] = 255, 0, 0    # to change color for whole screen we use img[:]
# img1[100:200, 100:300] = 0, 255, 0

# we will learn how to create lines
cv2.line(img1, (0,0), (512,512), (0,255,255), 3)     # or just write img.shape in place of (512,512) to get
                                                     # full diagonal line

cv2.rectangle(img1, (0,0), (300,300), (0,255,0), 2)

cv2.circle(img1, (100,100), 30, (0,255,0), 2)

# to fill the color inside the rectangle we can write cv2.FILLED inplace of thickness

""" Now we will learn how to put text in images """

cv2.putText(img1, "Gaurav is the Best", (200,100), cv2.FONT_HERSHEY_SIMPLEX , 1, (100,255,160), 1)

# to show the image on the screen
cv2.imshow("Image1", img1)

# so that it stays on the screen for us to see
cv2.waitKey(0)




