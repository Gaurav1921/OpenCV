""" CHAPTER 4: Resizing and Cropping """

import cv2
import numpy as np
print("Package Imported")

# in opencv the positve y direction is downwards and positve x direction is rightwards

img = cv2.imread("download.png")
print(img.shape)

# to resize the image
imgResize = cv2.resize(img, (500, 300))

# to crop an image
imgCropped = img[0:200, 100:500]
# here we dont need an opencv functionality, we can do it using matrix itself (img[height, width])

cv2.imshow("Image", img)
cv2.imshow("Resized Image", imgResize)
cv2.imshow("Cropped Image", imgCropped)

print(imgResize.shape)
cv2.waitKey(0)

