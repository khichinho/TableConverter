import numpy as np
import sys
import cv2 as cv

img = cv.imread('table.jpg')
cv.imshow('Original Image',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('greyscale image',gray)

binary = cv.adaptiveThreshold(~gray,255,0,cv.THRESH_BINARY,15,-2)
cv.imshow('binary',binary)

horizontal = np.copy(binary)
vertical = np.copy(binary)

cols = horizontal.shape[1]
horizontalsize = cols//15

horizontalStructure = cv.getStructuringElement(cv.MORPH_RECT,(horizontalsize,1))

horizontal = cv.erode(horizontal, horizontalStructure)
horizontal = cv.dilate(horizontal, horizontalStructure)

cv.imshow('horizontal',~horizontal)

rows = vertical.shape[0]
verticalsize = rows // 15

verticalStructure = cv.getStructuringElement(cv.MORPH_RECT, (1, verticalsize))

vertical = cv.erode(vertical, verticalStructure)
vertical = cv.dilate(vertical, verticalStructure)

cv.imshow('vertical',~vertical)

complete_grid = horizontal + vertical
cv.imshow('complete_grid',~complete_grid)

text_part = cv.bitwise_xor(complete_grid,binary)
cv.imshow('text_part',~text_part)



cv.waitKey(0)
cv.destroyAllWindows()



