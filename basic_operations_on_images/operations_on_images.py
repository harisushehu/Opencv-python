import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

print(img.size)
print(img.shape)
print(img.dtype)

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

img = cv2.resize(img, (512,512))
img2 = cv2.resize(img2, (512,512))

#dstImg = cv2.add(img, img2)

dstImg = cv2.addWeighted(img, 0.9, img2, 0.1, 0) #img has 90% of the weight whereas img2 has 10% of the weight
dstImg2 = cv2.addWeighted(img, 0.5, img2, 0.5, 0) #both img and img2 has 50% of the weight

cv2.imshow('image', dstImg)
cv2.imshow('image2', dstImg2)
cv2.waitKey(0)
cv2.destroyAllWindows()
