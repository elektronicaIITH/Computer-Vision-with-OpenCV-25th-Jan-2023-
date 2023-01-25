import cv2

img = cv2.imread('katherine.jpg')

def rescaleframe(frame,scale = 0.5): 
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv2.resize(frame,dimensions,interpolation = cv2.INTER_AREA)

resized_img = rescaleframe(img)

cv2.imshow('image',resized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()