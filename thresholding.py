import cv2 as cv

img = cv.imread("Group_pic.jpg")

def rescale(frame, scale = 0.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    
    dim = (width, height)
    
    return cv.resize(frame, dim, interpolation = cv.INTER_AREA)

img = rescale(img, 0.15)
cv.imshow("Dog", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale image", gray)

#Simple thresholding
threshold, n_image = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Threshold image of 150", n_image)

threshold, thresh_inv = cv.threshold(gray, 200, 255, cv.THRESH_BINARY_INV)
cv.imshow("Threshold inverse", thresh_inv)
print(threshold)

#Adaptive thresholding
a_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 201, 10)
cv.imshow("Adaptive thresholding", a_thresh)

a_g_threshold = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 201, 10)
cv.imshow("Adaptive gaussian thresholding", a_g_threshold)

cv.waitKey(0)