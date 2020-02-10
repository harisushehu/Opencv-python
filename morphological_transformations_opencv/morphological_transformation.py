import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('j.png', cv.IMREAD_GRAYSCALE)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

kernal = np.ones((2,2), np.uint8)

dilation = cv.dilate(mask, kernal, iterations=2)
erosion = cv.erode(mask, kernal,iterations=1)
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernal) #erosion followed by dilation
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernal)#dilation followed by erosion -> opposite opening
mg = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernal) #morphological gradient
th = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernal) #tophat

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()



#img = cv.imread('j.png', cv.IMREAD_GRAYSCALE)
#_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

#kernal = np.ones((2,2), np.uint8)

#dilation = cv.dilate(img, kernal, iterations=2)
#erosion = cv.erode(img, kernal,iterations=1)
#opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernal) #erosion followed by dilation
#closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernal)#dilation followed by erosion -> opposite opening
#mg = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernal) #morphological gradient
#th = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernal) #tophat

