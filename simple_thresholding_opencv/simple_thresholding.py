import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('gradient.png', 0)


#if pixel value is < 127, pixel = 0 else if pixel value > 127, pixel = 255
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY) #Either 0 or 1

#if pixel value is > 127, pixel = 0 else if pixel value < 127, pixel = 255
_, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV) #Inverse of what is gotten from binary

#if pixel value < 127, the value will not change else if pixel value >= 127, pixel = 127
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)

#if pixel value < 127, the pixel value = 0 else if pixel value >= 127, pixel will remain the same
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)

#if pixel value > 127, the pixel value = 0 else if pixel value < 127, pixel will remain the same
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV) #Inverse of thrash to zero

#cv.imshow('Image', img)
#cv.imshow('Threshold', th1)
#cv.imshow('Threshold Inverse', th2)
#cv.imshow('Threshold Trunc', th3)
#cv.imshow('Threshold ToZero', th4)
#cv.imshow('Threshold ToZero Inverse', th5)
images = [img, th1, th2, th3, th4, th5,]
titles = ['Image', 'Threshold', 'Threshold Inverse', 'Threshold Trunc', 'Th ToZero', 'Th ToZero Inverse']

for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
#cv.waitKey(0)
#cv.destroyAllWindows()