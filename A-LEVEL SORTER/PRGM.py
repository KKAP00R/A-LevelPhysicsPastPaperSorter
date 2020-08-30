import cv2
import numpy as np

def circledetection():
    photo=cv2.imread("ball.jpg",)
    photo=cv2.medianBlur(photo, 5)
    cimg=cv2.cvtColor(photo,cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(photo,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    
    cv2.imshow('detected circles',cimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

circledetection()