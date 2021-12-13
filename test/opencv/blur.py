import cv2 

image = cv2.imread("building.jpeg")

gaussian = cv2.GaussianBlur(image, (7,7), 0)
cv2.imwrite("tmp/gaussian.jpeg",gaussian)

median = cv2.medianBlur(image, 5)
cv2.imwrite("tmp/median.jpeg", median)

bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imwrite("tmp/bilateral.jpeg", bilateral)