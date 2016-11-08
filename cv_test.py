import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("tank.png",0)
img2 = cv2.imread("tank.png",1)

#hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#h,s,v = cv2.split(hsv)
#v-=255
#h-=255
#s+=255
#final_hsv = cv2.merge((h,s,v))


# define range of blue color in HSV
#lower_blue = np.array([110,50,50], dtype = "uint8")
#upper_blue = np.array([130,255,255], dtype = "uint8")
lower = np.array([200,200,200], dtype = "uint8")
upper = np.array([255,255,255], dtype = "uint8")

# Threshold the HSV image to get only white color
mask = cv2.inRange(img2, lower, upper)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(img2,img2, mask=mask)

#img2 = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
cv2.imwrite("tank_new_mask.png",mask)
cv2.imwrite("tank_new.png",res)

#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(img, (3, 3), 0)
tight = cv2.Canny(img, 225, 250)
tight2 = cv2.Canny(blurred, 225, 250)

blurred2 = cv2.GaussianBlur(mask, (1, 1), 0)
edge2 = cv2.Canny(blurred2, 225, 250)
cv2.imwrite("tank_final.png",edge2)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

cv2.imwrite("tank_new_sobelx.png",sobelx)
cv2.imwrite("tank_new_sobely.png",sobely)
cv2.imwrite("tank_new_edges.png",tight)
cv2.imwrite("tank_new_blurred.png",blurred)
cv2.imwrite("tank_new_edge_blurred.png",tight2)
