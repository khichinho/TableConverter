import sys
import numpy as np
import cv2
import scipy.misc as sp
from sys import argv
import os
from array import *
import csv

# To store bounding box of each cell in table

# Give index of value in list of contents around 2 values from exect position

def give_index(list_l,value):
	for i in range(len(list_l)):
		if value == list_l[i] or value+1 == list_l[i] or value+2 == list_l[i] or value-1 == list_l[i] or value-2 == list_l[i]:
			return i

	return -1		

# Find cells in table image store bounding boxes and position of row and coloums in image

def Find_Table_Cells_Using_Contoures(image):

	attributes = []
	im = cv2.imread(str(image) + ".png") #A png image is provided as input.
	imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) #Convert colour image to gray scale.
	ret,imgbinary = cv2.threshold(imgray, 180, 255, 0) #Threshold of binarization = 180
	imgbinary = 255 - imgbinary # The image is binarised to an absolute black and white image.
	contours, hierarchy = cv2.findContours(imgbinary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #contours of the image are found and hierachical information is stored #cv2.RETR_TREE contour retrieval mode (https://docs.opencv.org/3.4.0/d9/d8b/tutorial_py_contours_hierarchy.html) #cv2.CHAIN_APPROX_SIMPLE returen minimum parameters for a shape
	count = 0

    # To detect positions of row and coloum boundries two lists
	row_set = set([])
	coloum_set = set([])
	# Add positions of contour boundries as suspected row or coloum lines with having margin of
	# 2 points while matching on both side
	for i in range(len(contours)):
		if hierarchy[0][i][3] != -1:
			mask = np.zeros(imgray.shape, np.uint8)
			x, y, w, h = cv2.boundingRect(contours[i])
			tempImage = im[y:y+h, x:x+w]
			sp.imsave("./rough/" +str(count)+".png", tempImage)	#save the symbol image.
			count = count + 1
			if x not in row_set and x+1 not in row_set and x-1 not in row_set and x+2 not in row_set and x-2 not in row_set:
				row_set.add(x)
			if x+w not in row_set and x+w+1 not in row_set and x+w-1 not in row_set and x+w+2 not in row_set and x+w-2 not in row_set:
				row_set.add(x+w)
			if y not in coloum_set and y+1 not in coloum_set and y-1 not in coloum_set and y+2 not in coloum_set and y-2 not in coloum_set:
				coloum_set.add(y)
			if y+h not in coloum_set and y+h+1 not in coloum_set and y+h-1 not in coloum_set and y+h+2 not in coloum_set and y+h-2 not in coloum_set:
				coloum_set.add(y+h)
					
	# Sort both of the array's		
			
	row_set = sorted(row_set)
	coloum_set = sorted(coloum_set)

	# Probable table size in ideal case

	print "TABLE in page " + " : ", len(coloum_set)-1, "*", len(row_set)-1 

	# For each coutour find in how many rows and colums it is spanned and store it in attributes.

	for i in range(len(contours)):
		if hierarchy[0][i][3] != -1:
			mask = np.zeros(imgray.shape, np.uint8)
			x, y, w, h = cv2.boundingRect(contours[i])
			row1 = give_index(coloum_set,y)
			row2 = give_index(coloum_set,y+h)
			col1 = give_index(row_set,x)
			col2 = give_index(row_set,x+w)
			attributes.append((row1,row2-1,col1,col2-1,x,x+w,y,y+h))

	# To store row and coloum boundries.

	row_coloums = []
	row_coloums.append((row_set))
	row_coloums.append((coloum_set))
			
	# print attributes
	myFile = open("./rough/" + "row_coloums.csv", 'w')
	with myFile:
	    writer = csv.writer(myFile)
	    writer.writerows(row_coloums)
	    writer.writerows(attributes)


image = sys.argv[1]
Find_Table_Cells_Using_Contoures(image)
