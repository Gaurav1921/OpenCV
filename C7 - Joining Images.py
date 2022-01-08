""" CHAPTER 7: Joining Images """

import cv2
import numpy as np
print("Package Imported")

img = cv2.imread('download.png')

# to put all the images in 1 window so that its easy to navigate the images

imgHor = np.hstack((img, img))        # to stack the image in the horizontal direction
imgVer = np.vstack((img,img))

cv2.imshow("Horizontal", imgHor)
cv2.imshow("Vertical", imgVer)


# 1. issue is that we cannot resize the image (comes as it is) and other one is that
# 2. if both don't have the same number of channels then it wont work (as everything here is related to matrix)
# i.e. we cant stack the grayscale to an 3 valued image

cv2.waitKey(0)