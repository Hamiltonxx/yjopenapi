import cv2 
import numpy as np 

img = cv2.imread('building.jpeg')

kernel = np.ones((5,5), np.uint8)

img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)

cv2.imwrite("tmp/erosion.jpeg",img_erosion)
cv2.imwrite("tmp/img_dilation.jpeg",img_dilation)