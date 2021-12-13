import cv2 

img = cv2.imread("building.jpeg", cv2.IMREAD_COLOR)
# img = cv2.imread("geeks4geeks.png", 0) # use 0 to read image in grayscale mode

# cv2.imwrite("grayscale.png", img)
B,G,R = cv2.split(img)

cv2.imshow("original", img)
cv2.waitKey(0)

cv2.imshow("blue",B)
cv2.waitKey(0)

cv2.imshow("Green",G)
cv2.waitKey(0)

cv2.imshow("red",R)
cv2.waitKey(0)

cv2.destroyAllWindows()

# cv2.imshow("Cute Kitens", img)

# cv2.waitKey(0) # Hold the window on screen

# cv2.destroyAllWindows()