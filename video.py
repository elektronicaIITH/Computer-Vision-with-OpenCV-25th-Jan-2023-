import cv2

cap = cv2.VideoCapture('peoplewalking.mp4')

while True:
    istrue, frame = cap.read()

    cv2.imshow("video",frame)

    if cv2.waitKey(100) & 0xFF == ord('a'):
        break

#press 'a' to close the video window  

cap.release()
cv2.destroyAllWindows()