import cv2
import datetime

#cap = cv2.VideoCapture('C:/Users/Hp/PycharmProjects/getting_started_with_videos/video.mp4')
cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


#cap.set(3, 1208) #width
#cap.set(4, 720) #height

print(cap.get(3)) #print 1280 -> set it's value according to the available resolution
print(cap.get(4))

while(cap.isOpened()):

    ret, frame = cap.read()

    if ret == True:

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width :' + str(cap.get(3)) +' '+ 'Height :' + str(cap.get(4))
        date = str(datetime.datetime.now())
        frame = cv2.putText(frame, text, (10, 50), font, 1, (0, 255, 255), 3, cv2.LINE_AA)
        frame = cv2.putText(frame, date, (10, 470), font, 1, (0, 255, 255), 3, cv2.LINE_AA)

        cv2.imshow('frame', frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break;

cap.release()
cv2.destroyAllWindows()




