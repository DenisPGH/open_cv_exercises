import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('japan.jpg')
print(img[0,0]) # access picsel walue [Blue, Green, Red]

print(img.shape) # rows, columns, and channels for the image

#cv.imshow('img',img)

ball = img[280:340, 330:390] # change area in the image
img[273:333, 100:160] = ball
img[0,0] = [255,255,255] # change one picsel
print(img[0,0])

# plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')
# plt.show()

cv.imshow('image',img)
cv.waitKey(1000) # ms
cv.destroyAllWindows()
