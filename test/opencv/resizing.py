import cv2 
# import numpy as np 
# import matplotlib.pyplot as plt 

image = cv2.imread("building.jpeg")  # 1877 x 1056

half = cv2.resize(image, (0,0), fx=0.1, fy=0.1)
bigger = cv2.resize(image, (1050,1610))
stretch_near = cv2.resize(image, (780,540), interpolation=cv2.INTER_NEAREST)

# cv2.imshow("original",image)

cv2.imwrite("tmpimg/half.jpeg",half)
cv2.imwrite("tmpimg/bigger.jpeg",bigger)
cv2.imwrite("tmpimg/near.jpeg",stretch_near)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# titles = ["Original", "Half", "Bigger", "Interpolation Nearest"]
# images = [image, half, bigger, stretch_near]
# count = 4 
# for i in range(count):
#     plt.subplot(2,2,i+1)
#     plt.title(titles[i])
#     plt.imshow(images[i])

# images = [(image,"Original"),(half,"Half"),(bigger,"Bigger"),(stretch_near,"Interpolation Nearest")]
# for idx,x in enumerate(images):
#     plt.subplot(2,2,idx+1)
#     plt.title(x[1])
#     plt.imshow(x[0])

# plt.show()