""" CHAPTER 9: Contour/Shape Detection """

import cv2
import numpy as np

print("Package Imported")

# using the corner (contour) points of the objects, we will define the shape of the object
# we have packages, image. we are going to categorize each of them and we will show how many corner points do they have
# and also show the area


# before we didn't create functions but now there are more codes in here so we will define functions

def getContours(img):       # it will input an image
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # cv2.RETR_EXTERNAL: it retrieves the extreme outer contours, there are  other modes too but this one is best fit to get the outer
    # details
    # cv2.CHAIN_APPROX_NONE: to get all the outer contours (leaving no contour left)

    # we will loop through each contour
    for cnt in contours:
        # to find the area
        area = cv2.contourArea(cnt)  # input will be the contour's area that we want to find out
        print(area)

        # -1: as we want to draw all the contours

        # now we are going to check for the minimum area ( we will give it a threshold)
        # not necessary but good thing so that it does not detect any noise ( we will take the above code below there)

        if area > 500:       # 500 pixels
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            # we will calculate the curve length, it will help us approximate the corners of our edges/shapes.
            peri = cv2.arcLength(cnt, True)     # it is a closed curve so yes it is true
            print(peri)                         # this gives us the contour/shape perimeter
            # to approximate how many corner points we have
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            print(len(approx))       # anything above 4 is a circle

            # creating object corners
            objCor = len(approx)          # it will give us the number of corners

            # creating a bounding box around our detected boxes (to build bounding box we have to know x,y,w,h)
            x, y, w, h = cv2.boundingRect(approx)      # this will give us the x, y, width, height of each of the
                                                       # objects and shapes
            if objCor == 3:
                objectType = 'Triangle'
            elif objCor == 4:          # 2 possibilities i.e square and rectangle
                 aspRatio = w/float(h)            # so what we will do is divide width and height (same for square) if 1 then
                 if aspRatio > 0.95 and aspRatio < 1.05:                      # square otherwise rectangle. aspect ratio = width/height
                     objectType= "Square"
                 else:
                     objectType = "Rectangle"
            elif objCor == 5:
                objectType = "Pentagon"
            elif objCor == 6:
                objectType = "Hexagon"
            else:
                objectType = "Circle"

            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)  # x,y is the one of the edges of the contours
            cv2.putText(imgContour, objectType, (x + w//2 - 30, y + h//2), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,160,250), 2)



img = cv2.imread('shapes.jfif')
imgContour = img.copy()      # to copy the original image, which is to be used in the getContours function

# preprocessing the image, converting it into grayscale and then we will find the edges and then find corner points

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)    # higher the sigma, more the blur
imgCanny = cv2.Canny(imgBlur, 50, 50)
# imgBlank = np.zeros_like(img)        (to make blank images of black color i.e 0 values)

getContours(imgCanny)
# cv2.imshow("Original", img)
# cv2.imshow("Gray", imgGray)
# cv2.imshow("Blur", imgBlur)
# cv2.imshow("Canny", imgCanny)
cv2.imshow("Contour", imgContour)    # now we can see a blue colour border over all the shapes (it means it has detected
                                     # all the corner points
# cv2.imshow("Blank", imgBlank)


cv2.waitKey(0)



