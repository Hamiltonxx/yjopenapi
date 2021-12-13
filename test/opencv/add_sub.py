import cv2 

image1 = cv2.imread('1-500x250-3.jpeg')
image2 = cv2.imread('2-500x250-2.jpeg')

weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)
# sub = cv2.subtract(image1, image2)

cv2.imshow('Weighted Image', weightedSum)

cv2.waitKey(0)
cv2.destroyAllWindows()