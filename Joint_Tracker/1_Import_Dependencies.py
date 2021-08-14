import cv2
import mediapipe    as mp
import numpy        as np

mp_drawing  = mp.solutions.drawing_utils    # <-- drawing utility , such as object detection
mp_pose     = mp.solutions.pose             # <-- https://google.github.io/mediapipe/solutions/solutions.html // we can check importing module

# VIDEO Feed ------------------------------------------------------------------------
cap = cv2.VideoCapture(0)                   # Find where VideoCaputre it is , And (0) means I have 1 capture Device Number 

while cap.isOpened():                       # Open Our WebCam on While Loops
    ret, frame = cap.read()                 # Gain two variables in our VideoCaputre func (ret , frame) // ret doesn't have any information
    cv2.imshow("Mediapipe Feed", frame)     # Wanna Show our WebCam Named "Mediapipe Feed" and windows that have variable 'frame' matrix

    if cv2.waitKey(10) & 0xFF == ord("q"):  # Make a Stop key -> click the WebCam Windows and press 'q' button on 10 ms
        break


cap.release()                               # to release our WebCam
cv2.destroyAllWindows()                     # All Windows closing
