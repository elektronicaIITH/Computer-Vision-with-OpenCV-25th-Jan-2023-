import cv2
import numpy as np

# NumPy is a Python library used for working with arrays.

blank = np.zeros((600,600,3), dtype='uint8')
# uint8 is a datatype of image

# cv2.imshow('image',blank)

blank[:] = 255,235,205

# cv2.imshow('color',blank)

cv2.rectangle(blank,(0,0),(300,600), (0,0,0), cv2.FILLED)

#cv2.filled just fills the rectangle with the color 
# cv2.imshow('rectangle',blank)

cv2.circle(blank,(300,300),200,(100,0,200),2)
# cv2.imshow("circle",blank)

cv2.putText(blank,"HELLO...!",(150,300),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
cv2.putText(blank,"BYEE..!",(325,300),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
cv2.imshow('text',blank)

cv2.waitKey(0)