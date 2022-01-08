""" CHAPTER 8: Color Detection """

import cv2
import numpy as np

print("Package Imported")

# we will detect the orange colour


# now we will define some color values, some ranges in which we want our color to be.
# We will define color hue, saturation and value limits

# but we don't know the max and min value of orange colour so we will introduce stack bars to play with it
# creating a new window by the name Track Bars
def empty(a):
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",240,240)

cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)   # after some tests we got this as the default value
cv2.createTrackbar("Hue Max","TrackBars",19,179,empty)   # and set to that
cv2.createTrackbar("Sat Min","TrackBars",110,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",240,255,empty)
cv2.createTrackbar("Val Min","TrackBars",153,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

# min value of hue is 0 and max value of hue is 360 (in opencv we have till 179)
# at last we have to enter a function which functions everytime when something changes on track
# bar or when user changes trackbar)


"""
img = cv2.imread('download.png')
# first we will convert it into hsv
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# to read these track value so that it applies on our image
h_min = cv2.getTrackbarPos("Hue Min", 'Track Bars')
print(h_min)
"""

# to keep getting the value we need to put it in a loop as we have to run it again again to keep getting
# that value

while True:
    img = cv2.imread('download.png')
# first we will convert it into hsv
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# to read these track value so that it applies on our image
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    # we will now create a mask (it will filter out and give us the filtered out image of that colour
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    
    # to find out the colour of the car we will put replace white (value =1) colour with orange color using mask for
    # exact dimension.
    # the final step is to combine the mask and the original image by using bitwise
    # we are checking wherever we have these white images (in mask) we are getting from the original image
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('Original', img)
    cv2.imshow('HSV', imgHSV)
    cv2.imshow('Mask', mask)
    cv2.imshow("Result", imgResult)

    cv2.waitKey(1)


# we want to keep all the colors black that we don't want


