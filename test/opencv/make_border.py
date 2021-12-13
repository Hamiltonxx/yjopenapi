import cv2 

image = cv2.imread("geeks4geeks.png")
# bordered = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_CONSTANT,None,value=0)
bordered2 = cv2.copyMakeBorder(image,100,100,50,50,cv2.BORDER_REFLECT)

cv2.imwrite("tmp/bordered2.png",bordered2)