import cv2 as cv
import numpy as np

def rescale(frame, scale = .15):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dim = (width, height)
    
    return cv.resize(frame, dim, interpolation = cv.INTER_AREA)

img = cv.imread('Dog2.jpg')
img = rescale(img)
cv.imshow("DOG", img)

#Blank image 
blank = np.zeros(img.shape, dtype= 'uint8')
cv.imshow("BLANK", blank)

gray_scaled = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow("Gray Scale Image", gray_scaled)

#blur = cv.GaussianBlur(gray_scaled, (5,5), cv.BORDER_DEFAULT)
#cv.imshow("Blured", blur)


"""cann = cv.Canny(blur, 125, 175)
cv.imshow("Edges", cann)
"""
#RETR_EXTERNAL
#RETR_TREE

ret, thres = cv.threshold(gray_scaled, 125, 225, cv.THRESH_BINARY)
cv.imshow("Thresh", thres)

contours, higherarcies = cv.findContours(thres, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(len(contours))


#draimg contours
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow("drawn", blank)

cv.waitKey(0)