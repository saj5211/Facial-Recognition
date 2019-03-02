#Complex Image operations
import numpy as np
import cv2

img1 = cv2.imread('image.jpg')
img2 = cv2.imread('image2.jpg')
img3 = cv2.imread('image.png')

#Addition operators
#add = img1+img2
#This one adds the pixel value. Ex (155,211,79) +
# (50,170,200) = (205,381,279)=(205,255,255)
#add = cv2.add((img1,img2)
#weighted = cv2.addWeighted(img1,0.5,img2,0.4,0)

rows, cols, channels = img3.shape
roi = img1[0:rows,0:cols]
img2gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img3_fg = cv2.bitwise_and(img3,img3, mask=mask)

dst = cv2.add(img1_bg, img3_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('add',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()