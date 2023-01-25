import cv2 as cv

def rescale(frame, scale = 0.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    
    dim = (width, height)
    
    return cv.resize(frame, dim, interpolation = cv.INTER_AREA)

img = cv.imread('Dog2.jpg')
img = rescale(img, 0.19)
cv.imshow("Dog", img)

#Averaging Blur
blur = cv.blur(img, (50, 1))
cv.imshow("Average blur", blur)

#Median blur
median = cv.medianBlur(img, 7)
cv.imshow("Median blur", median)

#Gaussian blur 
gauss = cv.GaussianBlur(img, (15, 15), 0)
cv.imshow("Gaussian blur", gauss)


#Bilateral Blur
bilateral = cv.bilateralFilter(img, 20, 15, 15)
#(image, diameter, sigma_color, sigma_space)
cv.imshow("Bilateral", bilateral)


cv.waitKey(0)