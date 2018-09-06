# Classes for text detected in image
import io
import os

from google.cloud import vision
from google.cloud.vision import types


class Text:

    def __init__(self, image_file_name, api_key_path=None):
        # if api key not provided search in evirnment variable
        if api_key_path is None:
            try:
                self.api_key_path = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
            except KeyError:
                print("Please provide Google Cloud Vision API Key as sys.argv or "
                      "set GOOGLE_APPLICATION_CREDENTIALS environment variable.")
        else:
            self.api_key_path = api_key_path

        try:
            with io.open(image_file_name, 'rb') as image_file:
                content = image_file.read()
        except FileNotFoundError:
            print("Please provide correct path to image od table.")

        client = vision.ImageAnnotatorClient(self.api_key_path)
        image = types.Image(content=content)

        response = client.text_detection(image=image)
        self.texts = response.text_annotations
        self.max_size_bndpoly, self.avg_size_bndpoly = Text.get_bounding_poly_attributes(self.texts)


    def get_bounding_poly_attributes(self):
        sum_x = 0
        sum_y = 0
        max_x = 0
        max_y = 0
        # assumed text size is lesser than width and height of table in pixels
        for text_object in self.texts:
            bp_x = text_object.bounding_poly.vertices[3].x - text_object.bounding_poly.vertices[0].x
            bp_y = text_object.bounding_poly.vertices[3].y - text_object.bounding_poly.vertices[0].y
            if bp_x > max_x:
                max_x = bp_x
            if bp_y > max_y:
                max_y = bp_y
            sum_x += bp_x
            sum_y += bp_y
        return (max_x, max_y), (sum_x/len(self.texts), sum_y/len(self.texts))
