import cv2 as cv
import numpy as np

#adaptive thresholding, different part of the image will have different threshold value
#calculate the threshold for the smaller region of images
#gives a better result if the image has different illumination result at different region

img = cv.imread("sudoku.png", 0)

_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY) #Either 0 or 1
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)


cv.imshow("Image", img)
cv.imshow("Binary Threshold", th1)
cv.imshow("Adaptive Threshold Mean", th2)
cv.imshow("Adaptive Threshold Gaussian", th3)

cv.waitKey(0)
cv.destroyAllWindows()