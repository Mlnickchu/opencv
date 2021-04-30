import cv2
import sys
import numpy as np

cap = cv2.VideoCapture(0)
# Capture frame-by-frame
# ret看抓到與否

def nothing(x):
    pass

cv2.namedWindow('Gaussian_Blur')

# Starting with 100's to prevent error while masking
h,s,v = 100,100,100

# Creating track bar
cv2.createTrackbar('hl', 'Gaussian_Blur', 0,   50, nothing)
cv2.createTrackbar('hu', 'Gaussian_Blur', 179, 179, nothing)
cv2.createTrackbar('sl', 'Gaussian_Blur', 0,   255, nothing)
cv2.createTrackbar('su', 'Gaussian_Blur', 255, 255, nothing)
cv2.createTrackbar('vl', 'Gaussian_Blur', 0,   255, nothing)
cv2.createTrackbar('vu', 'Gaussian_Blur', 255, 255, nothing)
# 高斯的調整
cv2.createTrackbar('ksize', 'Gaussian_Blur', 0, 10, nothing)

while True:
    ret,frame = cap.read()

    # get info from track bar and appy to result
    hl = cv2.getTrackbarPos('hl', 'Gaussian_Blur')
    hu = cv2.getTrackbarPos('hu', 'Gaussian_Blur')
    sl = cv2.getTrackbarPos('sl', 'Gaussian_Blur')
    su = cv2.getTrackbarPos('su', 'Gaussian_Blur')
    vl = cv2.getTrackbarPos('vl', 'Gaussian_Blur')
    vu = cv2.getTrackbarPos('vu', 'Gaussian_Blur')

    # Converting to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('hsv',hsv)
    # Normal masking algorithm
    lower = np.array([hl, sl, vl])
    upper = np.array([hu, su, vu])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("hsv_demo", result)

    bitwise_not = cv2.bitwise_not(mask)
    cv2.imshow('bitwise_not',bitwise_not)

    kernel = np.ones((3,3), np.uint8)
    erode  = cv2.erode(mask, kernel, iterations=1)
    dilate = cv2.dilate(erode, kernel, iterations=1)

    ksize  = cv2.getTrackbarPos('ksize', 'Gaussian_Blur')
    binary = cv2.GaussianBlur(dilate, (2*ksize+1, 2*ksize+1), 0)
    cv2.imshow("Gaussian_Blur", binary)

    bitwise_and_blur = cv2.bitwise_and(frame, frame, mask=binary)
    cv2.imshow("Bitwise_and_blur", bitwise_and_blur)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()