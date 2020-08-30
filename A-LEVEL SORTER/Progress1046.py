circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.9, 500)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(output, (x, y), r, (0, 200, 0), 2)
            cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
            img = np.hstack([output])
            cv2.imshow('output', img)
    if cv2.waitKey(3) == 27:
        break
cv2.destroyAllWindows()
