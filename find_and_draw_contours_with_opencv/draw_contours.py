import cv2
import numpy as np

img = cv2.imread("opencv-logo.png")
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#contour is a curve joining all the continous point along the bondary which are having the same color or intensity
#contours can be useful tool for shape analysis, object detection or object recognition
#we generally use binary image for finding contours


ret, thresh = cv2.threshold(imgray, 127, 255, 0) #first find threshold then contour
contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

print("Number of contours = " + str(len(contours)))
print(contours[0])

#cv2.drawContours(img, contours, -1, (0, 255, 0), 3) #-1 in 3rd argurment makes it possible to draw all the contours which are found on the image
cv2.drawContours(img, contours, 8, (0, 255, 0), 3) # -1 can be replace with any index among contour no to find find the contour at the index

cv2.imshow("Image", img)
cv2.imshow("Image Gray", imgray)


cv2.waitKey(0)
cv2.destroyAllWindows()