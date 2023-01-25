import cv2

img = cv2.imread('katherine.jpg')
cv2.imshow('kat',img)

#RGB to gray
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow('gray',gray)

#RGB to HSV

hsv = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
cv2.imshow('HSV',hsv)

cv2.waitKey(0)