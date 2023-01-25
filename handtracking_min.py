import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture(0)

mphands = mp.solutions.hands
hands = mphands.Hands()

draw = mp.solutions.drawing_utils

while True:
    ret, frame = cap.read()
    frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    
    if results.multi_hand_landmarks:
        for h_l in results.multi_hand_landmarks:
            draw.draw_landmarks(frame, h_l, mphands.HAND_CONNECTIONS)
            
    if ret == False:
        continue
    #cv.putText(frame, "Handtracking", (60, 60), cv.FONT_HERSHEY_PLAIN, 4, (0, 255, 0), 2)
    cv.imshow("Video Frame", frame)
    key = cv.waitKey(1) & 0xFF
    
    if key == ord('q'):
        break
    
    #print(fps)



cap.release()
cv.destroyAllWindows()