import cv2
import numpy as np
import imutils
import sys

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

print(len(cnts[1]))
print(len(cnts)/len(cnts[1]))

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
	cv2.imshow("Image", ~dilation)
	cv2.waitKey(0)

# print(cXarray)
# print(cYarray)



cv2.waitKey(0)
cv2.destroyAllWindows()