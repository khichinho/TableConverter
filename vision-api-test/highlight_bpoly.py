import cv2
import io
import os
import sys

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    sys.argv[1])

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.document_text_detection(image=image)
text = response.text_annotations

# text_out = response.document_text_detection(image)
# print(text_out)

img = cv2.imread(sys.argv[1])
for t in text:
    x0 = t.bounding_poly.vertices[0].x
    x1 = t.bounding_poly.vertices[1].x
    x2 = t.bounding_poly.vertices[2].x
    x3 = t.bounding_poly.vertices[3].x
    y0 = t.bounding_poly.vertices[0].y
    y1 = t.bounding_poly.vertices[1].y
    y2 = t.bounding_poly.vertices[2].y
    y3 = t.bounding_poly.vertices[3].y
    cv2.rectangle(img, (min([x0, x1, x2, x3]), max([y0, y1, y2, y3])), (max([x0, x1, x2, x3]), min([y0, y1, y2, y3])), (255, 255, 0), 1)

cv2.imwrite("highlighted_"+sys.argv[1], img)