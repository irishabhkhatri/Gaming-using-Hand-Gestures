import cv2
import numpy as np

cap = cv2.VideoCapture(0)
def nothing(x):
    pass

cv2.namedWindow('result')
h,s,v = 100,100,100
#Creating Track Bar
cv2.createTrackbar('h', 'result', 0, 179, nothing)
cv2.createTrackbar('s', 'result', 0, 255, nothing)
cv2.createTrackbar('v', 'result', 0, 255, nothing)

while True:
    _,frame = cap.read()
    blur = cv2.GaussianBlur(frame, (11,11), 0)
    #converting to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    h = cv2.getTrackbarPos('h','result')
    s = cv2.getTrackbarPos('s','result')
    v = cv2.getTrackbarPos('s','result')

    # Normal masking algorithm
    blueLight = np.array([h,s,v])
    blueDark = np.array([180,255,255])

    mask = cv2.inRange(hsv, blueLight, blueDark)

    result = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('result', result)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
