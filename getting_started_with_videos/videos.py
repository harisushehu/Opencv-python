import cv2

#cap = cv2.VideoCapture('C:/Users/Hp/PycharmProjects/getting_started_with_videos/video.mp4') #video
cap = cv2.VideoCapture(0) #open webcam

fourcc = cv2.VideoWriter.fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

i = 0

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:

        print('Width : ', cap.get(cv2.CAP_PROP_FRAME_WIDTH), ' Height : ', cap.get(cv2.CAP_PROP_FRAME_HEIGHT), end="")
        print('\n')

        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", gray)

        """count = str(i)
        cv2.imwrite("image"+""+count+".png", gray)
        i+=1""" # Save frames from a video file


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break;




cap.release()
out.release()
cv2.destroyAllWindows()