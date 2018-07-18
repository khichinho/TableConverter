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
        texts = response.text_annotations

        text_list = texts[0].split('\n')
        

class Phrase:

    def __init__(self, text, bnd_poly):
        self.text = text
        self.bnd_poly = bnd_poly