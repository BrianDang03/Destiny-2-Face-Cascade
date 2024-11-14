import numpy as np
import cv2

def detect_destiny_face(reference_video):
    cap = cv2.VideoCapture(reference_video)

    destiny_face_cascade = cv2.CascadeClassifier('../destiny_face_cascade/classifier/cascade.xml')

    while True:
        ret, frame = cap.read()
    
        # Image, Scale Factor: 1.3 shrinks image down, min neighbors: multi rectangles how accurate do I have to be, minSize: how small the object is, maxSize: how big the object is.   
        faces = destiny_face_cascade.detectMultiScale(frame, 1.15, 3)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)

        frame = cv2.resize(frame, (0, 0), fx = 0.5, fy = 0.5)
        cv2.imshow("Video", frame)

        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()