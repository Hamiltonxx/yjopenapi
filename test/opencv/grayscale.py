import cv2 

image = cv2.imread("building.jpeg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite("tmp/gray.jpeg",gray_image)