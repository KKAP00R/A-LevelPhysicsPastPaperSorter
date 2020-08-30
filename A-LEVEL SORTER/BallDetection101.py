import cv2
import numpy as np
import imutils

image = cv2.imread('frame10.jpg') 
cv2.waitKey(0) 
output = image.copy()
blur = cv2.GaussianBlur(image, (11, 11), 0)
gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY) 
kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
im = cv2.addWeighted(image, 4, cv2.blur(image, (30, 30)), -4, 128)
cv2.imshow("IM", im)
cv2.waitKey(0)

edged = cv2.Canny(im, 30, 200) 
cv2.waitKey(0) 


cv2.imshow('Canny Edges After Contouring', edged) 
cv2.waitKey(0) 

print("Number of Contours found = ") 


circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.9, 200)

if circles is not None:
	circles = np.round(circles[0, :]).astype("int")
	for (x, y, r) in circles:
		cv2.circle(output, (x, y), r, (0, 255, 0), 4)
		cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
	cv2.imshow("output", np.hstack([output]))
else:
    cv2.imshow("output", output)

cv2.waitKey(0)
cv2.destroyAllWindows() 