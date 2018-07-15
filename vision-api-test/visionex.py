

import io
from google.cloud import vision
from google.cloud.vision import types


vision_client = vision.ImageAnnotatorClient()
file_name='abc.jpg'
with io.open(file_name,'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)
response1 = vision_client.label_detection(image=image)
labels = response1.label_annotations

response2 = vision_client.text_detection(image=image)
texts = response2.text_annotations

#web_detection_params = vision.types.WebDetectionParams(include_geo_results=True)
#image_context = vision.types.ImageContext(web_detection_params=web_detection_params)

#response3 = client.web_detection(image=image, image_context=image_context)

li_inner = []
li_outer = []

for label in labels:
    print (label.description)



print("-------------------------------------------------------")

for text in texts:
    li_inner.append(text.bounding_poly.vertices[0].x)
    li_inner.append(text.bounding_poly.vertices[1].x)
    li_inner.append(text.bounding_poly.vertices[2].x)
    li_inner.append(text.bounding_poly.vertices[3].x)
li_outer.append(li_inner)

print(li_outer)

print("-------------------------------------------------------------")

#for entity in response3.web_detection.web_entities:
#   print(u'\tDescription: {}'.format(entity.description))

print("---------------------------------------------------------")
