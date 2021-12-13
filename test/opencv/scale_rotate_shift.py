import cv2 
import numpy as np 

img = cv2.imread("building.jpeg")
# height, width = img.shape[:2]
# # INTER_AREA for shrinking, INTER_CUBIC for zooming
# res = cv2.resize(img, (width//2,height//2), interpolation=cv2.INTER_CUBIC) 
# cv2.imwrite("tmp/building_half.jpeg", res)

# rows, cols = img.shape[:2]
# # matrix for rotation w.r.t center to 45 degree without scaling
# M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
# res = cv2.warpAffine(img, M, (cols,rows))
# cv2.imwrite("tmp/rotate.jpeg", res)

# rows,cols = img.shape[:2]
# # If shift is (x,y), then matrix would be 
# # [1 0 x]
# # [0 1 y]
# M = np.float32([[1,0,100],[0,1,50]])
# res = cv2.warpAffine(img,M,(cols,rows))
# cv2.imwrite("tmp/translation.jpeg",res)

edged = cv2.Canny(img, 100, 100)
cv2.imwrite("tmp/edged.jpeg", edged)