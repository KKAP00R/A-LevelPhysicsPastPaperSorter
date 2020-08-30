import cv2
import imutils
import numpy as np

img = cv2.imread("frame4.jpg")
img_sized = imutils.resize(img, width = 800) #Resizing the Image for Faster Processing
img_blur = cv2.GaussianBlur(img_sized, (11, 11), 0)  #Blur the image for softening for edge detection
img_hsv = cv2.cvtColor(img_blur, cv2.COLOR_BGR2HSV)
img_hsvwblur = cv2.cvtColor(img_sized, cv2.COLOR_BGR2HSV)
img_blurhsv = cv2.GaussianBlur(img_hsvwblur, (11, 11), 0)

cv2.imshow("HSV with BLUR", img_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("HSV without BLUR", img_blurhsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

RedLower = np.array([0, 50, 50])
RedUpper = np.array([127, 255, 255])
mask_1 = cv2.inRange(img_hsv, RedLower, RedUpper)

RedLower = np.array([130, 50, 50])
RedUpper = np.array([180, 255, 255])
mask_2 = cv2.inRange(img_hsv, RedLower, RedUpper)

mask = mask_1 + mask_2

output_img = img_sized.copy()
output_img[np.where(mask == 0)] = 0

output_hsv = img_hsv.copy()
output_hsv[np.where(mask==0)] = 0

cv2.imshow("Operation1", output_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Operation2", output_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
center = None
	
if len(cnts) > 0:
	c = max(cnts, key=cv2.contourArea)
	((x, y), radius) = cv2.minEnclosingCircle(c)
	M = cv2.moments(c)
	center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

gray = cv2.cvtColor(output_img, cv2.COLOR_BGR2GRAY)
output = img_sized.copy()

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 2.5, 400)
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