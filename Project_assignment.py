import numpy as np
import sys
import cv2 as cv

#importing image to the program
img = cv.imread('table.jpg')
#dispaying the image with title as Original Image
cv.imshow('Original Image',img)

#converting image to greyscale mode
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#displaying the image with title as greyscale image
cv.imshow('greyscale image',gray)

#converting greyscale image to binary using adaptiveThreshold method
binary = cv.adaptiveThreshold(~gray,255,0,cv.THRESH_BINARY,15,-2)
#displaying the binary image with title as binary
cv.imshow('binary',binary)

#making copies of binary image using .copy function of numpy library and assigning them to horizontal and vertical variables
horizontal = np.copy(binary)
vertical = np.copy(binary)

#calculating columns of horizontal
cols = horizontal.shape[1]
#scaling columns by specific integer to control the display number of horizontal lines
#and equating it to horizontal size as an integer since getStructuringElement requires integer value for horizontal length
horizontalsize = cols//15

#making a image which is a part of original image containing horizontal lines only
horizontalStructure = cv.getStructuringElement(cv.MORPH_RECT,(horizontalsize,1))

#Morphology Operations
#applying erosion method over horizontal and horizontalStructure image
horizontal = cv.erode(horizontal, horizontalStructure)
#applying dilate method over horizontal and horizontalStructure image
horizontal = cv.dilate(horizontal, horizontalStructure)

#displaying horizontal lines as image with title as horizontal
cv.imshow('horizontal',~horizontal)

#calculating rows of vertical
rows = vertical.shape[0]
#scaling columns by specific integer to control the display number of vertical lines
#and equating it to vertical size as an integer since getStructuringElement requires integer value for vertical length
verticalsize = rows // 15

#making a image which is a part of original image containing vertical lines only
verticalStructure = cv.getStructuringElement(cv.MORPH_RECT, (1, verticalsize))

#Morphology Operations
#applying erosion method over vertical and verticalStructure image
vertical = cv.erode(vertical, verticalStructure)
#applying dilation method over vertical and verticalStructure image
vertical = cv.dilate(vertical, verticalStructure)

#displaying vertical lines as image with title as vertical
cv.imshow('vertical',~vertical)

#Adding horizontal and vertical lines to get a complete grid as a mask
complete_grid = horizontal + vertical
#displaying complete grid with the title as complete_grid 
cv.imshow('complete_grid',~complete_grid)

#making xor operation on compleate_grid and binary to get the text part of image only as a image format
text_part = cv.bitwise_xor(complete_grid,binary)
#displaying text part with the title as text_part
cv.imshow('text_part',~text_part)


#waiting for the key press of the keyboard to destroy all the windows which popped up during the runtime simulation
cv.waitKey(0)
cv.destroyAllWindows()



