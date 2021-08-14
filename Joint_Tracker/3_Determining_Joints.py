
import cv2
import mediapipe    as mp
import numpy        as np

mp_drawing  = mp.solutions.drawing_utils    # <-- drawing utility , such as object detection
mp_pose     = mp.solutions.pose             # <-- https://google.github.io/mediapipe/solutions/solutions.html // we can check importing module

# VIDEO Feed ------------------------------------------------------------------------
cap = cv2.VideoCapture(0)                   # Find where VideoCaputre it is , And (0) means I have 1 capture Device Number 

# Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose : # <-- if you wanna more highquality of tracking or detection change the numbers 
    
    while cap.isOpened():
        ret, frame = cap.read()

        # Recolor Image to RGB
        image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)   # Change Our framge Color BGR to RGB image
        image.flags.writeable = False                 

        # Make Detection
        results = pose.process(image)                   # Using pose.process image gonna store our image 
        
        # Recolor back to BGR
        image.flags.writeable = True                    # re-Render our image by OpenCV , So it is why we use writeable False & True
        image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)   # Change Our frame Color RGB to BGR format

        # Extract LandMarks 
        try :   # if we didn't find any marks error will run but we can pass it by using try ~ except part
            landmarks = results.pose_landmarks.landmark # there are 33 l andmarks <- for lndmrk in mp_pose.PoseLandmark : print(lndmrk)
            # if you wanna know the number of landmarks
            # mp_pose.PoseLandmark.LEFT_SHOULDER.value            >> 11
            # landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value] >> shows axis points
        except :
            pass

        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(0,0,66),thickness=2,circle_radius=2),# <- change dot color    (BGR)
            mp_drawing.DrawingSpec(color=(0,66,0),thickness=2,circle_radius=2))# <- change line color   (BGR)

        cv2.imshow("Mediapipe Feed",image)

        if cv2.waitKey(10) & 0xFF == ord("q") :
            break

cap.release()
cv2.destroyAllWindows()
