import cv2
import numpy as np
# -*- coding: utf-8 -*-

# 綠葉圖像
img_leaf = cv2.imread('green.jpg')
img = cv2.imread("lena256rgb.jpg")

# 導入原始圖像，SHOW圖
cv2.imshow("Original jpg",img_leaf)

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
green_hsv = cv2.cvtColor(img_leaf,cv2.COLOR_BGR2HSV)
lower_green = np.array([78,43,46])
upper_green = np.array([99,255,255])
binary_green = cv2.inRange(green_hsv,lower_green,upper_green)
cv2.imshow('binary',binary_green)

# 再透過反向，將人物選起來，(人物變為白色)
bitwise_not = cv2.bitwise_not(binary_green)
cv2.imshow('bitwise_not: binary',bitwise_not)

bitwise_not2 = cv2.bitwise_not(img_leaf,mask=binary_green)
cv2.imshow('Bitwise_not2: binary',bitwise_not2)

bitwise_and = cv2.bitwise_and(img_leaf,img_leaf,mask=bitwise_not)
cv2.imshow('Bitwise_and',bitwise_and)

cv2.waitKey(0)
cv2.destroyAllWindows() #洗掉建立的全部視窗，釋放資源
