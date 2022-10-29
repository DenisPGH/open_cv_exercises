import numpy as np
import cv2 as cv
img = cv.imread('ex.jpg',0)
#imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret,thresh = cv.threshold(img,100,255,0)
contours,hierarchy = cv.findContours(thresh, 1, 2)
print(contours)
cnt = contours[0]
M = cv.moments(cnt)
print( M )
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print(cx,cy)