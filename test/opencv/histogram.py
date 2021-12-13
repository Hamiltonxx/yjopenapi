import cv2 
import matplotlib.pyplot as plt 

img = cv2.imread("building.jpeg", 0)
histg = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(histg)

# plt.hist(img.ravel(),256,[0,256])

plt.show()
