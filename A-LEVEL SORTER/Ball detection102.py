import cv2
frame = cv2.imread("frame0.jpg")
diffsize = cv2.resize(frame, (400, 400))
cv2.imshow("Lets see", diffsize)