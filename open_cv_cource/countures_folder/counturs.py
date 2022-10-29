import numpy as np
import cv2 as cv
im = cv.imread('ex.jpg')
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 20, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) #CHAIN_APPROX_NONE
print(len(contours))

cv.drawContours(im, contours, -1, (255,255,0), 2)

# opredelen broi
cnt = contours[90]
cv.drawContours(im, [cnt], 0, (0,255,0), 3)

x,y,w,h = cv.boundingRect(cnt)
cv.rectangle(im,(x,y),(x+w,y+h),(255,255,200),2)

(x,y),(MA,ma),angle = cv.fitEllipse(cnt)
print('angle=',angle)


cv.imshow('res',im)
k = cv.waitKey(5000)
# if k == 27: # esc
#     break
cv.destroyAllWindows()
cnt = contours[0]
M = cv.moments(cnt)
print( M )
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print(cx,cy)