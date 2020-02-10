import cv2
import numpy as np

events = [i for i in dir(cv2) if 'EVENT' in i]

print(events)

def click_events(event, x,y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        cv2.circle(img, (x,y), 5, (255,255,255), -1)
        cv2.imshow('image', img)
        mycolorImage = np.zeros((512,512,3), np.uint8)

        mycolorImage[:] = [blue, green, red]
        cv2.imshow('color', mycolorImage)


#img = np.zeros((512,512,3), np.uint8)
img = cv2.imread('lena.jpg')
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_events)

cv2.waitKey(0)
cv2.destroyAllWindows()