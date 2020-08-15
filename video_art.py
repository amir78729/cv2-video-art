import cv2
import numpy as np

cap = cv2.VideoCapture('giphy.mp4')



i = 0
while True:
    i += 1
    print(i)
    ret, frame = cap.read()
    if ret == True:
        # print(np.mean(frame))
        array = np.array(frame)
        mean = np.mean(array)
        print(mean)
        cv2.imshow('Video', frame)
        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()

