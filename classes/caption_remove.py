
import io
from google.cloud import vision
from google.cloud.vision import types
import sys
import cv2
import numpy as np

def caption_type(words_in_blocks):
	if "Table" in words_in_blocks[0] or "Figure" in words_in_blocks[0]:
		return "up"	
	elif "Table" in words_in_blocks[len(words_in_blocks)-2] or "Figure" in words_in_blocks[len(words_in_blocks)-2]:
		return "down"
	else:
		return "no caption"			

vision_client = vision.ImageAnnotatorClient()
file_name=sys.argv[1]
with io.open(file_name,'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)


response2 = vision_client.document_text_detection(image=image)
texts = response2.text_annotations


li = texts[0].description.split("\n")


print(caption_type(li))


if(caption_type(li) == "up"):
	if "." in li[0]:
		li_0 = li[0].split(".")
		li_0_0 = (" . ".join([li_0[0] , li_0[1]]))
		lil = li_0_0.split(" ")
	elif ":" in li[0]:
		li_0 = li[0].split(":")
		li_0_0 = (" :".join([li_0[0] , li_0[1]]))
		lil = li_0_0.split(" ")		
	else:
		lil = li[0].split(" ")

	x1 = texts[1].bounding_poly.vertices[3].x	
	y1 = texts[1].bounding_poly.vertices[3].y
	x2 = texts[len(lil)].bounding_poly.vertices[2].x
	y2 = texts[len(lil)].bounding_poly.vertices[2].y
	print(x1,y1,x2,y2)
	img = cv2.imread(sys.argv[1])
	h, w = img.shape[:2]
	crop_img = img[y1:h, 0:w]
	cv2.imshow("cropped_up", crop_img)
	cv2.waitKey(0)

elif(caption_type(li) == "down"):
	if "." in li[len(li)-2]:
		li_0 = li[len(li)-2].split(".")
		li_0_0 = (" . ".join([li_0[0] , li_0[1]]))
		lil = li_0_0.split(" ")
	elif ":" in li[len(li)-2]:
		li_0 = li[len(li)-2].split(":")
		li_0_0 = (" :".join([li_0[0] , li_0[1]]))
		lil = li_0_0.split(" ")	
	else:
		lil = li[len(li)-2].split(" ")

	# print(lil)	
	# print(texts[len(texts)-len(lil)])
	x1 = texts[len(texts)-len(lil)].bounding_poly.vertices[0].x	
	y1 = texts[len(texts)-len(lil)].bounding_poly.vertices[0].y
	x2 = texts[len(texts)-1].bounding_poly.vertices[1].x
	y2 = texts[len(texts)-1].bounding_poly.vertices[1].y
	print(x1,y1,x2,y2)
	img = cv2.imread(sys.argv[1])
	h, w = img.shape[:2]
	crop_img = img[0:y1, 0:w]
	cv2.imshow("cropped_down", crop_img)
	cv2.waitKey(0)	

elif(caption_type == "no caption"):
	img = cv2.imread(sys.argv[1])
	cv2.imshow("no caption image", img)
	cv2.waitKey(0)
# for text in texts:
# 	print(text.description)



