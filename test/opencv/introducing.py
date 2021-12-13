import cv2 
image = cv2.imread('road.jpeg')

h,w = image.shape[:2]
print(f"Height: {h}, Width: {w}")

B,G,R = image[100,100] # randomly choose a pixel 100,100
print(B,G,R) # Extract RGB Value

B = image[100,100,0] # A specific channel
print(B)

roi = image[100:500, 200:700] # Region of Interest

resize = cv2.resize(image, (800,800)) # the problem is the aspect ratio of the image is not maintained.

ratio = 800/w 
dim = (800, int(h*ratio)) # new width and height tuple
resize_aspect = cv2.resize(image, dim)

center = (w//2, h//2)
matrix = cv2.getRotationMatrix2D(center, -45, 1.0) # a rotation matrix
rotated = cv2.warpAffine(image, matrix, (w,h))

output = image.copy()
rectangle = cv2.rectangle(output, (1500,900),(600,400),(255,0,0),2)