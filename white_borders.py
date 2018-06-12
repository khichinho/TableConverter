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

# binary =cv.dilate(binary,~horizontalStructure)
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
# binary =cv.dilate(binary,~verticalStructure)
# binary =cv.dilate(binary,~verticalStructure)
# binary =cv.dilate(binary,~verticalStructure)
# binary =cv.dilate(binary,~verticalStructure)

# binary =cv.dilate(binary,~horizontalStructure)

binary2 = binary

cv.imshow('new binaryv',binary2)########################## vertical lines ##################################

complete_grid = ~binary1 + ~binary2
cv.imshow('complete_grid',complete_grid)

text_part = cv.bitwise_xor(~binary1,~binary2)
#displaying text part with the title as text_part
cv.imshow('text_part',~text_part)

intersections = cv.bitwise_and(~binary1,~binary2)
cv.imshow('intersections',~intersections)



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


print(len(cnts[0]))
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




im = gray

blocks = rows*cols
block = [[gray]*(cols+1)]*(rows+1)
data = [[""]*(cols)]*(rows+1)


a = im[cYarray2d[0][0]:cYarray2d[1][0],cXarray2d[0][0]:cXarray2d[0][1]]
b = im[cYarray2d[0][1]:cYarray2d[1][1],cXarray2d[0][1]:cXarray2d[0][2]]
j = im[cYarray2d[1][0]:cYarray2d[2][0],cXarray2d[1][0]:cXarray2d[1][1]]



cv.imshow('b',j)


#######################################################################################
								# MAKE THIS LOOP CORRECT TO GIVE ALL IMAGES #
#######################################################################################
for y in range(0,rows):
    for x in range(0,cols):
        #crop_img = img[y:y+h, x:x+w]
        block[y][x] = im[cYarray2d[y][x]:cYarray2d[y+1][x],cXarray2d[y][x]:cXarray2d[y][x+1]]
        text = pytesseract.image_to_string(block[y][x],lang = 'eng')
        cv2.imwrite("block" +"_" + str(y)+ "_" +str(x) + ".tiff",block[y][x])
        data[y][x] = text
    print(data[y])






#waiting for the Esc key press of the keyboard to destroy all the windows which popped up during the runtime simulation
def close():
	if cv.waitKey(0) == 27:
		cv.destroyAllWindows()
	else:
		close()

close()
