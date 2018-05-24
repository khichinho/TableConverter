import cv2
import numpy as np
import sys

# read img
img = cv2.imread(sys.argv[1])

# convert image to greyscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#convert grayscale to binary, otsu  removes noise
th, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

########     CODE FOR ROTATION 
# minAreaRect on the nozeros
pts = cv2.findNonZero(threshed)
# Finds a rotated rectangle of the minimum area enclosing the input 2D point set. //Similar to minEnclosingCircle and minEnclosingTriangle
ret = cv2.minAreaRect(pts)

(cx,cy), (w,h), ang = ret 
if w>h:
    w,h = h,w
    ang += 0

#Find rotated matrix, do rotation to threshed image
M = cv2.getRotationMatrix2D((cx,cy), 0, 1)  #print(M)
rotated = cv2.warpAffine(threshed, M, (img.shape[1], img.shape[0]))
#######
####### FINDS DIFFERENT ROWS
#converts 2d array to vector
hist = cv2.reduce(rotated,1, cv2.REDUCE_AVG).reshape(-1)
th = 1
#finds height and width of image
H,W = img.shape[:2]
# finds lines of words in  complete image
uppers = [y for y in range(H-1) if hist[y]<=th and hist[y+1]>th]
lowers = [y+2 for y in range(H-1) if hist[y]>th and hist[y+1]<=th]
######

#noise removal
i=0
while i < len(uppers):
    if(lowers[i] - uppers[i] < 3):
        del lowers[i]
        del uppers[i]
    i +=1

rotated = cv2.cvtColor(rotated, cv2.COLOR_GRAY2BGR)

# for y in uppers:
#     cv2.line(rotated, (0,y), (W, y), (255,0,0), 1)

# for y in lowers:
#     cv2.line(rotated, (0,y), (W, y), (0,255,0), 1)

cv2.imshow("result.png", rotated)

#differentiate different lines
height, width = rotated.shape[:2]
j=0
croparray  = [rotated] * (len(uppers))
while j< len(uppers):
    crop1 = rotated[uppers[j]:lowers[j], 0:width]
    croparray[j] = crop1
    cv2.imshow("crop" + str(j),croparray[j])
    j+=1

#saves tiff files
# j=0
# while j<len(uppers):
# 	crop1 = rotated[uppers[j]:lowers[j],0:width]
# 	filename = "crop_%d.tiff"%j
# 	cv2.imwrite(filename, crop1)
# 	j=j+1
#cv2.waitKey(0)

def close():
	if cv2.waitKey(0) == 27:
		cv2.destroyAllWindows()
	else:
		close()

close()
