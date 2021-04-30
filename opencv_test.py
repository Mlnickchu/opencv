import cv2
import numpy as np
import sys
# -*- coding: utf-8 -*-


def nothing(x):
    pass

# Creating a window for later use
cv2.namedWindow('hsv_demo',0)

# Starting with 100's to prevent error while masking
h,s,v = 100,100,100

# Creating track bar
cv2.createTrackbar('hl', 'hsv_demo', 0,   179, nothing)
cv2.createTrackbar('hu', 'hsv_demo', 179, 179, nothing)
cv2.createTrackbar('sl', 'hsv_demo', 0,   255, nothing)
cv2.createTrackbar('su', 'hsv_demo', 255, 255, nothing)
cv2.createTrackbar('vl', 'hsv_demo', 0,   255, nothing)
cv2.createTrackbar('vu', 'hsv_demo', 255, 255, nothing)

# 綠葉圖像
image = "green.jpg"
img ="lena256rgb.jpg"

try:
    imagePath = sys.argv[1]
    image = cv2.imread(imagePath)
except:
    image = cv2.imread(image)



# 導入原始圖像，SHOW圖
cv2.imshow("Original jpg",image)

#將圖片做灰階
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray",gray)
#
# # 二值化有兩種方式: 1. 設定Threshold
# #將圖片設定Threshoold 二值化
# ret,towvalue= cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
# cv2.imshow('towvalue',towvalue)
#
# # 2. 從HSV的圖像進行二值化
# hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) # step1 先轉成HSV
# cv2.imshow("hsv",hsv)
# lower = np.array([91,0,0])
# upper = np.array([161,145,255])
# binary = cv2.inRange(hsv,lower,upper)
# cv2.imshow("Binary",binary)


# 測試RGB顏色對應到HSV
# green = np.array([[[148,0,211]]],dtype='uint8')
# hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
# print('HSV: ',hsv_green)


# 綠色葉子的圖，透過RGB先轉HSV後，直接二值化，選出綠色的部分(非人物)，白色部分是我們的取的葉子(green)的範圍
# 白色是我們要的部分
# green_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# lower_green = np.array([78,43,46])
# upper_green = np.array([99,255,255])
# binary_green = cv2.inRange(green_hsv,lower_green,upper_green)
# cv2.imshow('binary',binary_green)
#
# # 再透過反向，將人物選起來，(人物變為白色)
# bitwise_not = cv2.bitwise_not(binary_green)
# cv2.imshow('bitwise_not: binary',bitwise_not)
#
# bitwise_not2 = cv2.bitwise_not(image, mask=binary_green)
# cv2.imshow('Bitwise_not2: binary',bitwise_not2)
#
# bitwise_and = cv2.bitwise_and(image, image, mask=bitwise_not)
# cv2.imshow('Bitwise_and',bitwise_and)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows() #洗掉建立的全部視窗，釋放資源

#TODO 另一個範例
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
        cv2.imwrite("hsv_demo.png", result) #將調好的圖片HSV儲存
        break
cv2.destroyAllWindows()