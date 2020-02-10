import cv2
from matplotlib import pyplot as plt

#matplotlib is a python 2D library which produces publication quality figures etc.

img = cv2.imread('lena.jpg')

cv2.imshow('Image', img)

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img2)
#plt.xticks([]), plt.yticks([]) #hide coordinate from the picture
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()