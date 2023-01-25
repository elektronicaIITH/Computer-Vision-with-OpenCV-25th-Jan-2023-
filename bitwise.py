import cv2 as cv
import numpy as np

def rescale(frame, scale = 0.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    
    dim = (width, height)
    
    return cv.resize(frame, dim, interpolation = cv.INTER_AREA)

img = cv.imread('Dog2.jpg')
img = rescale(img, 0.15)
cv.imshow("DoG", img)

blank = np.zeros((400, 400), dtype = 'uint8')
cv.imshow("Blank", blank)

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow("Rect", rectangle)
cv.imshow("Cir", circle)

#bitwise and
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("AND", bitwise_and)

#bitwise or
bitwise__or = cv.bitwise_or(rectangle, circle)
cv.imshow("OR", bitwise__or)

#bitwise xor
xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("XOR", xor)

#biwise not
N_ot = cv.bitwise_not(rectangle)
cv.imshow("NOT", N_ot)


cv.waitKey(0)