import cv2
import os
import numpy as np

img = cv2.imread("lena.jpg")

layer = img.copy()

gp = [layer] #gp -> Gaussian Pyramid

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i), layer)

layer = gp[5]
cv2.imshow("upper level Gaussian Pyramid", layer)

#Laplacian doesn't have a function on itself
lp = [layer] #laplacian is formed by the difference between the level in the Gaussian Pyramid (GP) and the extended
             # version of its upper level GP

for i in range(5,0,-1):   #higher limit, lower limit, reduce in  ##Always lower limit not reached so this will print 5,4,3,2 and 1
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i),laplacian)

#Laplacian Pyramid (LP) is more or less like edge detection (it only show black image)
#Uses of GP and LP -> helps us to blend the images and reconstruct the image

cv2.imshow("Original Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()


"""
lr1 = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr1)
hr1 = cv2.pyrUp(lr2) #Higher resolution image NOT same as Lower resoulution 1 image even after increase because once you have
#decrease the resolution of the using PyrDown, you lose the information in the image and even after increase, you can't recover
#the lose info. Thus, the image in hr1 will be a little blurred compared to the image in lr1

cv2.imshow("Original Image", img)
cv2.imshow("pyrDown 1 image", lr1)
cv2.imshow("pyrDown 2 image", lr2)
cv2.imshow("pyrUp 1 image", hr1)

cv2.imshow("Original Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""

