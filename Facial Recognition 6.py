#filtering
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #hsv hue sat value
    # lower_blue = np.array([90,150,100])
    # upper_blue = np.array([150,255,255])
    #
    # mask = cv2.inRange(hsv, lower_blue,upper_blue)
    # res = cv2.bitwise_and(frame,frame,mask=mask)

    #types of blurs
    #kernel = np.ones((15,15), np.float32)/225
    #smoothed = cv2.filter2D(res,-1,kernel)
    #blur = cv2.GaussianBlur(res, (15,15),0)
    #median = cv2.medianBlur(res, 15)
    #bilateral = cv2.bilateralFilter(res, 15,75,75)

    #Morphology, Better detection
    # kernel = np.ones((5,5), np.uint8)
    # erosion = cv2.erode(mask, kernel, iterations=1)
    # dilation = cv2.dilate(mask, kernel, iterations=1)
    # opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN,kernel)
    # closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    #2 more types, tophat and blackhat.
    #Tophat diff between input image and opening image
    #Blackhat is the same but instead of opening its closing

    # cv2.imshow('frame', frame)
    # cv2.imshow('mask', mask)






    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelx = cv2.Sobel(frame,cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    edges = cv2.Canny(frame, 100,200)


    cv2.imshow('test', edges)
    # cv2.imshow('test2', sobely)



    k = cv2.waitKey(5) & 0xFF

    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()