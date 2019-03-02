# Matching sample template in image
import numpy as np
import cv2
import matplotlib.pyplot as plt
cv2.ocl.setUseOpenCL(False)
img = cv2.imread('image10.jpg',0)
template = cv2.imread('image9.jpg',0)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img,None)
kp2, des2 = orb.detectAndCompute(template,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1,des2)
matches = sorted(matches, key=lambda x:x.distance)

img3 = cv2.drawMatches(template,kp1,img,kp2,matches[:10], None,flags=2)
plt.imshow(img3)
plt.show()
