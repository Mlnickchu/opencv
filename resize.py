import cv2
import numpy as np

img = cv2.imread("lena256rgb.jpg")
rows, cols = img.shape[:2]
print(img.shape[:2])

resize = cv2.resize(img, (rows, cols), interpolation = cv2.INTER_CUBIC)
cv2.imshow('Resize', resize)
cv2.waitKey(0)

cv2.destroyAllWindows()

