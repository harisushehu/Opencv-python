import numpy as np
import cv2

#img = cv2.imread("lena.jpg", 1)
img = np.zeros([500,500,3], np.uint8)

img = cv2.line(img, (0,0), (255,255),(125,80,90), 5)  # img, x coordinates, y, coordinates, BGR-color, thickness
img = cv2.arrowedLine(img, (0,255), (255, 255), (255, 255, 255), 3)
img = cv2.rectangle(img, (50,50), (255,255), (0,255,0), 4)
img = cv2.rectangle(img, (255,255), (480,480), (0,0,255), -1) # color -1 -> fill with provided color
img = cv2.circle(img, (380,150), 50, (0,0,0), 2)



font = cv2.FONT_HERSHEY_SIMPLEX

img = cv2.putText(img, 'opencv', (10, 450), font, 4, (0, 255, 255), 3, cv2.LINE_AA)

cv2.imshow("image", img)


cv2.waitKey(0)
cv2.destroyAllWindows()
