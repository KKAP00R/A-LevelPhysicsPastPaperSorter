import cv2

print(cv2.__version__)
vidcap = cv2.VideoCapture('testing02.mp4')
success,image = vidcap.read()
count = 0
while (count<=100):
  cv2.imwrite("frame%d.jpg" % count, image)
  success,image = vidcap.read()
  print ('Read a new frame: ', success)
  count += 1
i = 0
