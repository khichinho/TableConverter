# Class of image table
import sys

import cv2 as cv
import text


class Table_image:
    
    def __init__(self, image_file_name):
        original_image = cv.imread(image_file_name)
        original_binary = Table_image.convert_to_binary(original_image)
        text_of_image = text.Text(image_file_name)
        structure = Table_image.extract_structure(
            original_binary, text_of_image.max_size_bndpoly[0],
            text_of_image.max_size_bndpoly[1])


    @staticmethod
    def convert_to_binary(image):
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        binary = cv.adaptiveThreshold(
            gray, 255, 0, cv.THRESH_BINARY, 15, -2)
        return binary

        

    @staticmethod 
    def extract_structure(image, horizontal, vertical):
        horizontal_line_matrix = cv.getStructuringElement(
            cv.MORPH_RECT, (horizontal, 1))
        vertical_line_matrix = cv.getStructuringElement(
            cv.MORPH_RECT, (1, vertical))
        horizontal_structure = cv.morphologyEx(
            image, cv.MORPH_OPEN, horizontal_line_matrix)
        horizontal_structure = cv2.morphologyEx(
            horizontal_structure, cv.MORPH_CLOSE, horizontal_line_matrix)
        vertical_structure = cv.morphologyEx(
            image, cv.MORPH_OPEN, vertical_line_matrix)
        vertical_structure = cv.morphologyEx(
            vertical_structure, cv.MORPH_CLOSE, vertical_line_matrix)
        
