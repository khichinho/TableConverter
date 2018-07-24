import numpy as np
import sys
import cv2 as cv
import cv2
import imutils
import array
import pytesseract
from PIL import Image

img = cv.imread(sys.argv[1])
cv.imshow('Original Image',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow('greyscale image',gray)
binary = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,15,-2)
binary = cv.adaptiveThreshold(binary,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,15,-2)


horizontal = np.copy(binary)
vertical = np.copy(binary)

cols = horizontal.shape[1]
horizontalsize = cols//35

horizontalStructure = cv.getStructuringElement(cv.MORPH_RECT,(horizontalsize,1))


horizontal = cv.erode(horizontal, horizontalStructure,iterations=23)

horizontal = cv.dilate(horizontal, horizontalStructure,iterations=50)

cv.imshow('horizontal',horizontal)

rows = vertical.shape[0]
verticalsize = rows // 35

verticalStructure = cv.getStructuringElement(cv.MORPH_RECT, (1, verticalsize))

vertical = cv.erode(vertical, verticalStructure,iterations=18)
vertical = cv.dilate(vertical, verticalStructure,iterations=22)

cv.imshow('vertical',vertical)

intersections = cv.bitwise_and(horizontal,vertical)
cv.imshow('intersections',intersections)

#input image and create greyscale simultaneously
img = intersections
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(img,kernel,iterations = 1)
cv2.imshow('dilation',dilation)

#round off corners
blurred = cv2.GaussianBlur(dilation, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
cv2.imshow('thresh',thresh)



#waiting for the Esc key press of the keyboard to destroy all the windows which popped up during the runtime simulation
def close():
	if cv.waitKey(0) == 27:
		cv.destroyAllWindows()
	else:
		close()

close()
