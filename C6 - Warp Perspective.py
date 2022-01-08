""" CHAPTER 6:  Warp Perspective"""

import cv2
import numpy as np
print("Package Imported")


# we will carve out the the king card from those 4 cards and for that we need 4 points (will apply warp perspective)
img = cv2.imread("kings.png")

# we will define the 4 corners of our card (already we should know)
# to know the values we can open ms paints to know with the help of cursor
pts1 = np.float32([[300, 39], [430, 110], [206, 214], [326, 286]])

width, height = 250,350     # the new image will have this width and height
pts2 = np.float32([[0,0], [width,0], [0,height], [width,height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)   # required for perspective itself
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Image_Output", imgOutput)

cv2.waitKey(0)