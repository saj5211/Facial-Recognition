#Writing on Images
import numpy as np
import cv2

img = cv2.imread('image.png', cv2.IMREAD_COLOR)
cv2.line(img,(0,0),(150,150), (255,255,255), 15)
cv2.rectangle(img, (15,25), (200,150), (0,255,0), 15)
cv2.circle(img, (100,63), 55, (0,0,255), -1)
points = np.array([[10,5],[15,62],[12,34],[98,21],[16,12],[36,45]], np.int32)
points = points.reshape((-1,1,2))
cv2.polylines(img, [points],True, (255,0,255),3)
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,'OpeCV tuts', (0,130), font, 1, (255,255,0),5,cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()