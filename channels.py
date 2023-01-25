import cv2 as cv
import numpy as np

img = cv.imread('katherine.jpg')
cv.imshow('image',img)

b,g,r = cv.split(img)

cv.imshow('blue',b)
cv.imshow('Green',g)
cv.imshow('red',r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

cv.waitKey(0)