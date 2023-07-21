import cv2 as cv
import numpy as np

img = cv.imread(r'D:\\Omdena\\noise.png')

img_blur = cv.GaussianBlur(img, (3, 3), 1.3)

cv.imwrite('noise_filtered1.png', img_blur)