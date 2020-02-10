import cv2
import numpy as np

def nothing():
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow('Tracking')
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)


while 1:

    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos('LH', 'Tracking')
    l_s = cv2.getTrackbarPos('LS', 'Tracking')
    l_v = cv2.getTrackbarPos('LV', 'Tracking')

    u_h = cv2.getTrackbarPos('UH', 'Tracking')
    u_s = cv2.getTrackbarPos('US', 'Tracking')
    u_v = cv2.getTrackbarPos('UV', 'Tracking')



    l_b = np.array([l_h,l_s,l_v]) #lower color
    u_b = np.array([u_h,u_s,u_v]) #upper color

    #l_b = np.array([30, 30, 84])  # lower color green
    #u_b = np.array([77, 255, 255])  # upper color green

    l_b = np.array([88, 157, 72])  # lower color blue
    u_b = np.array([151, 255, 255])  # upper color blue

    #l_b = np.array([4, 193, 185])  # lower color orange
    #u_b = np.array([35, 255, 255])  # upper color orange

    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)


    key = cv2.waitKey(1)

    if key == 27:
        break;
cap.release()
cv2.destroyAllWindows()