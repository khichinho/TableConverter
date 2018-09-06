	
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


def split_to_list(wordblock):
	if "(" in wordblock:
		l = wordblock.split("(")
		wordblock = ("( ".join([l[0] , l[1]]))
	

	if ")" in wordblock:
		l = wordblock.split(")")
		wordblock = (" )".join([l[0] , l[1]]))		

	if "." in wordblock:
		l = wordblock.split(".")
		wordblock = (" . ".join([l[0] , l[1]]))	

	if ":" in wordblock:
		l = wordblock.split(":")
		wordblock = (" :".join([l[0] , l[1]]))	
	# li = l1.split(" ")
				
	return 	wordblock.split(" ")


def list_of_lists(api_op_list):
	l = []
	for i in range(0,len(api_op_list)-1):
		l.append(split_to_list(api_op_list[i]))
	return l	


def join_to_list(wordblock_listformat):
	s = " ".join(wordblock_listformat)
	return s 	





vision_client = vision.ImageAnnotatorClient()
file_name=sys.argv[1]
with io.open(file_name,'rb') as image_file:
	content = image_file.read()

image = types.Image(content=content)


response2 = vision_client.document_text_detection(image=image)
texts = response2.text_annotations

li = (texts[0].description.split("\n"))

# print(li)




# print(split_to_list("Table 2.3 Some naturally occuring acids"))
 
# li = [ "Natural source","Vinegar","Orange","Tamarind","Tomato","Acid","Acetic acid","Citric acid","Tartaric acid","Oxalic acid","Natural source","Sour milk (Curd)","Lemon","Ant sting","Nettle sting","Acid","Lactic acid","Citric acid","Methanoic acid","Methanoic acid"]

# print(list_of_lists(li))

lil = list_of_lists(li)

tuple_list = []
for i in range(1,len(lil)+1):
	x1 = texts[i].bounding_poly.vertices[0].x 
	y1 = texts[i].bounding_poly.vertices[0].y 

	x2 = texts[i].bounding_poly.vertices[3].x 
	y2 = texts[i].bounding_poly.vertices[3].y 

	x3 = texts[len(lil[i-1])].bounding_poly.vertices[1].x 
	y3 = texts[len(lil[i-1])].bounding_poly.vertices[1].y 

	x4 = texts[len(lil[i-1])].bounding_poly.vertices[2].x 
	y4 = texts[len(lil[i-1])].bounding_poly.vertices[2].y 

	tuple_list.append( (li[i-1],(x1,y1),(x2,y2),(x3,y3),(x4,y4)) )




# print(texts[len(lil[0])])

for tuples in tuple_list:
	print(tuples)






