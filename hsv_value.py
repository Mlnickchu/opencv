import cv2
import sys
import numpy as np


def nothing(x):
    pass


# Creating a window for later use
cv2.namedWindow('hsv_demo',cv2.WINDOW_NORMAL)

# Starting with 100's to prevent error while masking
h, s, v = 100, 100, 100

# Creating track bar
cv2.createTrackbar('hl', 'hsv_demo', 0,   179, nothing)
cv2.createTrackbar('hu', 'hsv_demo', 179, 179, nothing)
cv2.createTrackbar('sl', 'hsv_demo', 0,   255, nothing)
cv2.createTrackbar('su', 'hsv_demo', 255, 255, nothing)
cv2.createTrackbar('vl', 'hsv_demo', 0,   255, nothing)
cv2.createTrackbar('vu', 'hsv_demo', 255, 255, nothing)

try:
    imagePath = sys.argv[1]
    image = cv2.imread(imagePath)
except:
    image = cv2.imread("green.jpg")


while True:

    # get info from track bar and appy to result
    hl = cv2.getTrackbarPos('hl', 'hsv_demo')
    hu = cv2.getTrackbarPos('hu', 'hsv_demo')
    sl = cv2.getTrackbarPos('sl', 'hsv_demo')
    su = cv2.getTrackbarPos('su', 'hsv_demo')
    vl = cv2.getTrackbarPos('vl', 'hsv_demo')
    vu = cv2.getTrackbarPos('vu', 'hsv_demo')

    # Converting to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Normal masking algorithm
    lower = np.array([hl, sl, vl])
    upper = np.array([hu, su, vu])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(image, image, mask=mask)
    #result = cv2.bitwise_not(mask)

    cv2.imshow("hsv_demo", result)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.imwrite("hsv_demo.png", result)
        break

cv2.destroyAllWindows()
