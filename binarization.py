import cv2 as cv

img = cv.imread(r'D:\\Omdena\\image.png', cv.IMREAD_GRAYSCALE)

ret, threshold = cv.threshold(img, 124, 255, cv.THRESH_BINARY)

cv.imwrite('image_binarized.png', threshold)
    