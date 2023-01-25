import numpy as np
import cv2 as cv

img = cv.imread('Dog2.jpg')

def rescale(frame, scale = 0.5):
    height = int(frame.shape[0]*scale)
    width = int(frame.shape[1]*scale)
    dim = (width, height)
    
    return cv.resize(frame, dim, interpolation = cv.INTER_AREA)

img = rescale(img, scale = 0.15)
cv.imshow("DOG", img)


blank = np.zeros(img.shape[:2], dtype= 'uint8')

mask = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow("Mask", mask)

new_mask = cv.rectangle(blank.copy(), (100, 100), (300, 300), 255, -1)
cv.imshow("New Mask", new_mask)

masked_image = cv.bitwise_and(img, img, mask= mask)
cv.imshow("Masked image", masked_image)

new_masked_image = cv.bitwise_and(img, img, mask = new_mask)
cv.imshow("New masked image", new_masked_image)

cv.waitKey(0)