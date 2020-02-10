import cv2

print("Hello World")

print(cv2.__version__)

img = cv2.imread("lena.jpg", -1)

cv2.imshow("image", img)
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()

if img is None:
    print("Image could not be found")
else:
    print("Image has been found")

