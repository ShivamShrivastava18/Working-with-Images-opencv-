import cv2 as cv
import numpy as np

img = cv.imread(r'D:\\Omdena\\image.png', cv.IMREAD_GRAYSCALE)

sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)

sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)

sobel = cv.addWeighted(sobelx, 5, sobely, 5, 0)

cv.imwrite('image_sobel.png', sobel)