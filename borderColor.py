import numpy as np
import sys
import cv2 as cv
import cv2
import imutils
import array
import pytesseract
from PIL import Image

#importing image to the program
img = cv.imread(sys.argv[1])
#dispaying the image with title as Original Image
cv.imshow('Original Image',img)

#converting image to greyscale mode
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# print(type(gray))
# print(type(img))
#displaying the image with title as greyscale image
cv.imshow('greyscale image',gray)

#converting greyscale image to binary using adaptiveThreshold method
binary = cv.adaptiveThreshold(~gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,15,-2)
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
b = ~complete_grid

#displaying complete grid with the title as complete_grid 
cv.imshow('complete_gridb',b)









img = cv.imread(sys.argv[1])
#dispaying the image with title as Original Image
cv.imshow('Original Image',img)

#converting image to greyscale mode
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray=~gray
# print(type(gray))
# print(type(img))
#displaying the image with title as greyscale image
cv.imshow('greyscale image',gray)

# #converting greyscale image to binary using adaptiveThreshold method
# binary = cv.adaptiveThreshold(~gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,15,-2)
# #displaying the binary image with title as binary
# binary = ~binary
# cv.imshow('binary',binary)

#making copies of binary image using .copy function of numpy library and assigning them to horizontal and vertical variables
horizontal = np.copy(gray)
vertical = np.copy(gray)

#calculating columns of horizontal
cols = horizontal.shape[1]
#scaling columns by specific integer to control the display number of horizontal lines
#and equating it to horizontal size as an integer since getStructuringElement requires integer value for horizontal length
horizontalsize = cols//40

#making a image which is a part of original image containing horizontal lines only
horizontalStructure = cv.getStructuringElement(cv.MORPH_RECT,(horizontalsize,1))
horizontalStructure = ~horizontalStructure
cv.imshow('hS',horizontalStructure)
#Morphology Operations
#applying erosion method over horizontal and horizontalStructure image
horizontal = cv.erode(horizontal, horizontalStructure)
#applying dilate method over horizontal and horizontalStructure image
horizontal = cv.dilate(horizontal, horizontalStructure)

#displaying horizontal lines as image with title as horizontal
cv.imshow('horizontal',horizontal)

binary = cv.adaptiveThreshold(~horizontal,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,15,-2)
#displaying the binary image with title as binary
binary=~binary
cv.imshow('binary',binary)


binary = cv.erode(binary,~horizontalStructure)
binary =cv.dilate(binary,~horizontalStructure)
binary =cv.dilate(binary,~horizontalStructure)

binary =cv.dilate(binary,~horizontalStructure)
binary =cv.dilate(binary,~horizontalStructure)
binary =cv.dilate(binary,~horizontalStructure)
binary =cv.dilate(binary,~horizontalStructure)
binary =cv.dilate(binary,~horizontalStructure)
binary =cv.dilate(binary,~horizontalStructure)

binary =cv.dilate(binary,~horizontalStructure)
binary1 = binary

cv.imshow('new binary',binary1) ######################################   horizontal lines   ######################################






rows = vertical.shape[0]
#scaling columns by specific integer to control the display number of vertical lines
#and equating it to vertical size as an integer since getStructuringElement requires integer value for vertical length
verticalsize = rows //20

#making a image which is a part of original image containing vertical lines only
verticalStructure = cv.getStructuringElement(cv.MORPH_RECT, (1, verticalsize))

#Morphology Operations
#applying erosion method over vertical and verticalStructure image
vertical = cv.erode(vertical, verticalStructure)
#applying dilation method over vertical and verticalStructure image
vertical = cv.dilate(vertical, verticalStructure)

#displaying vertical lines as image with title as vertical
cv.imshow('vertical',~vertical)

binary = cv.adaptiveThreshold(~vertical,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,15,-2)
#displaying the binary image with title as binary
binary=~binary
cv.imshow('binaryv',binary)


binary = cv.erode(binary,~verticalStructure)
binary =cv.dilate(binary,~verticalStructure)
binary =cv.dilate(binary,~verticalStructure)

binary =cv.dilate(binary,~verticalStructure)
binary =cv.dilate(binary,~verticalStructure)
# binary =cv.dilate(binary,~horizontalStructure)
# binary =cv.dilate(binary,~verticalStructure)
# binary =cv.dilate(binary,~verticalStructure)
# binary =cv.dilate(binary,~verticalStructure)
# binary =cv.dilate(binary,~verticalStructure)
binary =cv.dilate(binary,~verticalStructure)
binary =cv.dilate(binary,~verticalStructure)
binary =cv.dilate(binary,~verticalStructure)
binary =cv.dilate(binary,~verticalStructure)
binary =cv.dilate(binary,~verticalStructure)
# binary =cv.dilate(binary,~verticalStructure)
# binary =cv.dilate(binary,~verticalStructure)
# binary =cv.dilate(binary,~verticalStructure)
# binary =cv.dilate(binary,~verticalStructure)
# binary =cv.dilate(binary,~verticalStructure)

# binary =cv.dilate(binary,~horizontalStructure)

binary2 = binary

cv.imshow('new binaryv',binary2)########################## vertical lines ##################################

complete_grid = ~binary1 + ~binary2
a = complete_grid
cv.imshow('complete_grida',a)

text_part = cv.bitwise_xor(~binary1,~binary2)
#displaying text part with the title as text_part
cv.imshow('text_part',~text_part)

intersections = cv.bitwise_and(~binary1,~binary2)
cv.imshow('intersections',~intersections)

print(type(a))
print(type(b))
a = list(a.reshape(-1))
print(a.count(0))
print(a.count(255))
np.savetxt('a.txt',a)

# print(list(a).count(0))

print(b)
b = list(b.reshape(-1))
print(b.count(255))
print(b.count(0))
np.savetxt('b.txt',b)


if((( a.count(0) > a.count(255) ) and ( b.count(0) < b.count(255) ))   and    ((a.count(0)>b.count(255))  ) ):
 print("White Borders")
else:
	print("Black Borders")

def close():
	if cv.waitKey(0) == 27:
		cv.destroyAllWindows()
	else:
		close()

close()