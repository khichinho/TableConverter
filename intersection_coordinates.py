import cv2
import numpy as np
import imutils
import sys
import array
from PIL import Image

img = cv2.imread('intersections.jpg',0)
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(img,kernel,iterations = 1)

cv2.imshow('dilation',dilation)



blurred = cv2.GaussianBlur(dilation, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

# find contours in the thresholded image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]

cols = (len(cnts[1]) - 1)
rows = (len(cnts)//len(cnts[1])) - 1

print(cols)
print(rows)

cXarray=[]
cYarray=[]
# loop over the contours
for c in cnts:
	# compute the center of the contour
	M = cv2.moments(c)
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])
	cXarray.append(cX)
	cYarray.append(cY)
 	
 	
	#draw the contour and center of the shape on the image
	cv2.drawContours(dilation, [c], -1, (255, 0, 0), 2)
	cv2.circle(dilation, (cX, cY), 7, (255, 0, 0), -1)
	cv2.putText(dilation, "*", (cX - 20, cY - 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
 	
	# show the image
	# cv2.imshow("Image", ~dilation)
	# cv2.waitKey(0)

cXarray.reverse()
cYarray.reverse()
print(len(cXarray))

npXarray = np.array(cXarray)
npYarray = np.array(cYarray)

cXarray2d = npXarray.reshape(rows+1,cols+1)
cYarray2d = npYarray.reshape(rows+1,cols+1)

#print(cXarray2d[0][1])
#print(cYarray2d)
# print(matrix)
im = cv2.imread('twc.png')

crop_img = im[cYarray[0]:cYarray[0+6],cXarray[0]:cXarray[1]]
cv2.imshow('cropping',crop_img)

crop_img2 = im[36:68,3:67]
cv2.imshow('crap',crop_img2)

crop_img1 = im[cYarray[64]:cYarray[71],cXarray[64]:cXarray[65]]
cv2.imshow('circle123',crop_img1)
##############################------------------------------------------------------
# mp = 0
# for i in range(0,int(len(cnts) - 1)):
# 	crop_img = im[int(cYarray[i]):int(cYarray[i+cols+2]),int(cXarray[i]):int(cXarray[i+1])]
# 	filename = "element_crop_%d.tiff"%mp
# 	cv2.imwrite(filename,crop_img)
# 	i = i+1
# 	mp = mp+1
mp = 1
i=0
while i < (len(cnts)):
	crop_img = im[int(cYarray[i]):int(cYarray[i+cols+1]),int(cXarray[i]):int(cXarray[i+1])]
	filename = "element_crop_%d.tiff"%mp
	cv2.imwrite(filename,crop_img)
	i = i+1
	mp = mp+1
	if mp%(cols) == 0 :
		i = i+1
print(cXarray[1])
print(cXarray[2])




















# crop_img1 = im[4:36,67:229]
# cv2.imshow('cropping1',crop_img1)

# for i in range(0,cols):
# 	for j in range(0,rows):
# 		crop_img = im[cYarray2d[j][i]:cYarray2d[j+1][i],cXarray2d[i][j]:cXarray2d[i+1][j]]
# 		filename = "lalilao_%d.tiff"%j
# 		cv2.imwrite(filename, crop_img)
# 		i=i+1
# 		j=j+1
# = 0
#  = 0
# for i in range(0,len(cXarray)):
# 	crop_img = im[cYarray[i+p]:cYarray[i+p+cols],cXarray[i]:cXarray[i+1]]
# 	filename = "lalilalo_%d.tiff"%mp
# 	cv2.imwrite(filename, crop_img)
# 	mp = mp + 1
# 	p = p + cols + 1



# mp = 0
# for i in range(0,rows):
# 	for j in range(0,cols):
# 		crop_img = im[i:i+1, j:j+1]
# 		#cv2.imshow("cropped", crop_img)
# 		filename = "lalilalo_%d.tiff"%mp
# 		cv2.imwrite(filename, crop_img)
# 		mp = mp+1

# height, width = rotated.shape[:2]
# j=0
# croparray  = [rotated] * (len(uppers))
# while j< len(uppers):
#     crop1 = rotated[uppers[j]:lowers[j], 0:width]
#     croparray[j] = crop1
#     cv2.imshow("crop" + str(j),croparray[j])
#     j+=1




cv2.waitKey(0)
cv2.destroyAllWindows()
