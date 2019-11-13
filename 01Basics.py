
import cv2
print(cv2.__version__)

# img = imread('faces_detected.jpeg')

import cv2 as cv
flags = [i for i in dir(cv) if i.startswith('COLOR_')]
# print( flags )

img  = cv2.imread('faces_detected.jpg',cv2.IMREAD_GRAYSCALE)

cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()