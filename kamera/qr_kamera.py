import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
from cv2 import VideoWriter_fourcc

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
i = 1
recording = False

# open output video file stream
video = cv2.VideoWriter('snimka.avi', VideoWriter_fourcc(*'MP42'), 25.0, (640, 480))

while True:
    _, frame = cap.read()
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        data = obj.data.decode('utf-8')
        print(data)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.rectangle(frame, (obj.rect.left, obj.rect.top), (obj.rect.left + obj.rect.width, obj.rect.top + obj.rect.height), (0, 255, 0), 2)
        cv2.putText(frame, str(data), (50, 50), font, 1, (205, 0, 100), 3)
    cv2.imshow("Video", frame)
    if recording == True:
        video.write(frame)
    key = cv2.waitKey(1) & 0xff
    if key == 113:  # ESC key = 27, q = 113
        cap.release()
        video.release()
        cv2.destroyAllWindows()
        break

    if key == ord('s'):
        cv2.imwrite('test' + str(i) + '.png', frame)
        i = i + 1

    if key == ord('r'):
        if recording == False:
            recording = True
        else:
            recording = False

        