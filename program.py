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


intersections = cv.bitwise_and(horizontal,vertical)
cv.imshow('intersections',~intersections)







#input image and create greyscale simultaneously
img = intersections
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(img,kernel,iterations = 1)
cv2.imshow('dilation',dilation)

#round off corners
blurred = cv2.GaussianBlur(dilation, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
cv2.imshow('thresh',thresh)


# find contours in the thresholded image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]

#rows and cols of image
cols = (len(cnts[1]) - 1)
rows = (len(cnts)//len(cnts[1])) - 1
print(cols)
print(rows)
## (rows+1)*(cols+1) matrix 12*6

cXarray=[]
cYarray=[]

#new image created
height, width = dilation.shape[:2]
newimg = np.zeros((height,width,3), np.uint8)
newimg[:,0*width:width] = (255)

# loop over the contours
for c in cnts:
	# Image moments help you to calculate some features like center of mass of the object
	M = cv2.moments(c)
	#this calculates center(of mass) of individual contours
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])
	cXarray.append(cX)
	cYarray.append(cY)

	cv2.circle(newimg, (cX, cY), 1, (255, 0, 0), -1)

	#draw the contour and center of the shape on the image

#show the image
cv2.imshow("Image", ~dilation)

cv2.imwrite("yolo.jpg",newimg)

cv2.imshow("newimg",newimg)


cXarray.reverse()
cYarray.reverse()
print(len(cXarray))


npXarray = np.array(cXarray)
npYarray = np.array(cYarray)

cXarray2d = npXarray.reshape(rows+1,cols+1)
cYarray2d = npYarray.reshape(rows+1,cols+1)
print((cXarray2d))
print((cYarray2d))


im = text_part

blocks = rows*cols
block = [[text_part]*(cols+1)]*(rows+1)
data = [[""]*(cols)]*(rows+1)

for y in range(0,rows):
    for x in range(0,cols):
        #crop_img = img[y:y+h, x:x+w]
        block[y][x] = im[cYarray2d[y][x]:cYarray2d[y+1][x+1],cXarray2d[y][x]:cXarray2d[y+1][x+1]]
        cv2.imshow("block" +" " + str(y)+ " " +str(x) + ".tiff",block[y][x])
        cv2.imwrite("block" +" " + str(y)+ " " +str(x) + ".tiff",block[y][x])
        text = pytesseract.image_to_string(block[y][x],'eng')
        data[y][x] = text
    print(data[y])

#waiting for the Esc key press of the keyboard to destroy all the windows which popped up during the runtime simulation
def close():
	if cv.waitKey(0) == 27:
		cv.destroyAllWindows()
	else:
		close()

close()