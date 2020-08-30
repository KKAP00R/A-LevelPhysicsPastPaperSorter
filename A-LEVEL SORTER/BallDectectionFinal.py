#IMPORTING NECESSARY FILES
import cv2
import numpy as np
import imutils
import time

video = cv2.VideoCapture(0) #INITIALISING WEBCAM
loop, img = video.read() #DECLARING VARIABLE TO CAPTURE FRAME

#ALLOWING CAMERA TO WARM UP AND USER TO PREPARE THE OBJECT FOR DETECTION
time.sleep(2)

while loop:
    #CONTINUING EXTRACTION OF FRAMES IN A LOOP
    loop, img = video.read()
    #FLIPPING IMAGE TO MAKE IT STRAIGHT AS PER THE USER
    flipped = cv2.flip(img, 1)
    #PREPROCESSING ON THE IMAGE TO SHARPEN THE BALL, PUT THE BALL IN FOCUS
    img_sized = imutils.resize(flipped, width = 800)
    img_blur = cv2.GaussianBlur(img_sized, (11, 11), 0)
    img_hsv = cv2.cvtColor(img_blur, cv2.COLOR_BGR2HSV)
    
    #PREPROCESSING CREATION OF MASK ON COLOR RED(COLOR OF THE BALL)
    #THIS IS THE LOWER MASK RANGE - 0-10
    RedLower = np.array([0, 120, 70])
    RedUpper = np.array([10, 255, 255])
    mask_1 = cv2.inRange(img_hsv, RedLower, RedUpper)
    
    #THIS IS THE UPPER MASK RANGE 170-180
    RedLower = np.array([175, 120, 70])
    RedUpper = np.array([180, 255, 255])
    mask_2 = cv2.inRange(img_hsv, RedLower, RedUpper)
    #ADDING UP THE TWO MASKS TO FORM ONE COMPLETE MASK
    mask = mask_1 + mask_2
    #CREATING IMAGE FROM MASK
    output_img = img_sized.copy()
    output_img[np.array(mask == 0)] = 0

    #COPYING THE FRAME FOR DISPLAYING THE PROCESSING OF MASK IN THE REAL FRAME
    output = img_sized.copy()
    gray = cv2.cvtColor(output_img, cv2.COLOR_BGR2GRAY)
    img_circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.9, 100)
    #DRAW A CIRCLE AROUND THE PT. CIRCLE IS DETECTED (IF FOUND)
    if img_circles is not None:
        v1 = 0
        img_circles = np.round(img_circles[0,:].astype("int"))
        for (x, y, r) in img_circles:
            cv2.circle(output, (x,y), r, (255, 255, 0), 4)
            cv2.rectangle(output, (x, y), (x, y), (0, 255, 0), -3)
        cv2.imshow("OUTPUT", np.hstack([output]))
        cv2.imshow("WIN", output_img)
    #IF NOT FOUND JUST OUPTUT THE ORIGINAL IMAGE
    else:
        cv2.imshow("OUTPUT", output)
        cv2.imshow("WIN", output_img)
    key = cv2.waitKey(1)
    #USER CAN END THE PROGRAM BY PRESSING THE ESCAPE KEY
    if key == 27: 
        break
#AFTER BREAKING FROM VIDEO, RELEASE THE VIDEO CAM 
video.release()
#DESTROY THE OUTPUT WINDOW AFTER THE USER ENDS THE PROGRAM
cv2.destroyAllWindows()