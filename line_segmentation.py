import cv2
import numpy as np
import sys
from PIL import Image

# read img
img = cv2.imread('twc.png')

# convert image to greyscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#convert grayscale to binary
th, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
## (3) minAreaRect on the nozeros
pts = cv2.findNonZero(threshed)
ret = cv2.minAreaRect(pts)


(cx,cy), (w,h), ang = ret 
if w>h:
    w,h = h,w
    ang += 0

## (4) Find rotated matrix, do rotation
M = cv2.getRotationMatrix2D((cx,cy), 0, 1)
print(M)
rotated = cv2.warpAffine(threshed, M, (img.shape[1], img.shape[0]))

## (5) find and draw the upper and lower boundary of each lines
hist = cv2.reduce(rotated,1, cv2.REDUCE_AVG).reshape(-1)

th = 2
H,W = img.shape[:2]
uppers = [y for y in range(H-1) if hist[y]<=th and hist[y+1]>th]
lowers = [y for y in range(H-1) if hist[y]>th and hist[y+1]<=th]

i=0
while i < len(uppers):
    if(lowers[i] - uppers[i] < 3):
        del lowers[i]
        del uppers[i]
    i +=1

print(uppers)
print(lowers)

rotated = cv2.cvtColor(rotated, cv2.COLOR_GRAY2BGR)
for y in uppers:
    cv2.line(rotated, (0,y), (W, y), (255,0,0), 1)

for y in lowers:
    cv2.line(rotated, (0,y), (W, y), (0,255,0), 1)

cv2.imshow("result.png", rotated)

height, width = rotated.shape[:2]
print(height)
print(width)



j=0
while j<len(uppers):
	crop1 = rotated[uppers[j]:lowers[j],0:width]
	filename = "crop_%d.jpg"%j
	cv2.imwrite(filename, crop1)
	j=j+1
#cv2.waitKey(0)

cv2.waitKey(0)
cv2.destroyAllWindows()
