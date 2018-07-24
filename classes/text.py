# Classes for text detected in image
import io

from google.cloud import vision
from google.cloud.vision import types

class Text:

    def __init__(self, image_file_name):
        with io.open(image_file_name, 'rb') as image_file:
            content = image_file.read()
        client = vision.ImageAnnotatorClient()
        image = types.Image(content = content)

        response = client.text_detection(image = image)
        self.texts = response.text_annotations
        self.max_size_bndpoly = Text.max_size_bounding_poly(self.texts)

    @staticmethod
    def max_size_bounding_poly(response_list):
        max_x = 0
        max_y = 0
        # assumed text size is lesser than width and height of table in pixels
        for text_object in response_list:
            bp_x = text_object.bounding_poly.vertices[3].x-text_object.bounding_poly.vertices[0].x
            bp_y = text_object.bounding_poly.vertices[3].y-text_object.bounding_poly.vertices[0].y
            if bp_x>max_x:
                max_x = bp_x
            if bp_y>max_y:
                max_y = bp_y
        
        return (max_x, max_y)
