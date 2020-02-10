import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#img = cv.imread('opencv-logo.png')
img = cv.imread('lena.jpg')
#img = cv.imread('salt_and_pepper.png')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

kernal = np.ones((5,5), np.float32) / 25 #mean filter
dst = cv.filter2D(img, -1, kernal) #homogenius kernal
blur = cv.blur(img, (5,5)) #blurring

#Guassian filter (blur) uses different weight kernal -> removes high frequency noise from the image
#pixel in middle have higher weights and side(s) have smaller weights

gblur = cv.GaussianBlur(img, (5,5), 0)

#median filter -> replace each pixel value with median of it's neighbouring pixel
#very good when dealing with salt and pepper noise (with some white and black pixel)
medianblur = cv.medianBlur(img, 5, 1) #kernel size must be odd


#by using homogenius, mean filter, gfilter and medianfilter we not only dissolve the noise but also
# smooth the edges but sometimes, we need to preserve the edges even if the image is blurred

bilateralFilter = cv.bilateralFilter(img, 9, 75, 75) #highly effective in noise removal while keeping the edge sharp
#75, 75 sigma color and sigma space

titles = ['image', '2D Convolution', 'blur', 'GaussianBlur', 'MedianBlur', 'BilateralFilter']
images = [img, dst, blur, gblur, medianblur, bilateralFilter]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()