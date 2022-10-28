import cv2 as cv
flags = [i for i in dir(cv) if i.startswith('COLOR_')]
#print( flags ) # 150 ways to change the flags colors
#  BGR → Gray  cv.COLOR_BGR2GRAY. BGR → HSV, cv.COLOR_BGR2HSV

import numpy as np
img = cv.imread('japan.jpg')
cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    lower_green = np.array([50, 100,100])
    upper_green = np.array([70, 255, 255])
    # Threshold the HSV image to get only blue colors
    mask_1 = cv.inRange(hsv, lower_blue, upper_blue)
    mask_2 = cv.inRange(hsv, lower_green, upper_green)
    # Bitwise-AND mask and original image
    mask=cv.bitwise_or(mask_1,mask_2)
    res = cv.bitwise_and(frame,frame, mask= mask)
    #res = cv.bitwise_and(frame,res, mask= mask_2)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(1) & 0xFF
    if k == 27: # esc
        break
cv.destroyAllWindows()

########## How to find HSV values to track?
##  take [H-10, 100,100] and [H+10, 255, 255] as the lower bound and upper bound respectively.

green = np.uint8([[[0,255,0 ]]])
hsv_green = cv.cvtColor(green,cv.COLOR_BGR2HSV)
print( hsv_green ) #[[ 60 255 255]]]

# 28.10.2022 Image Processing in OpenCV >>> Geometric Transformations of Images