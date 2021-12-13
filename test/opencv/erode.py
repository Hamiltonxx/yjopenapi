import cv2 
import numpy as np 

image = cv2.imread("geeks4geeks.png")

# kernel = np.ones((5,5),np.uint8)
kernel2 = np.ones((6,6),np.uint8)

# eroded = cv2.erode(image, kernel)
eroded2 = cv2.erode(image, kernel2, cv2.BORDER_REFLECT)

# cv2.imwrite("tmpimg/eroded.png", eroded)
cv2.imwrite("tmpimg/eroded2.png", eroded2)