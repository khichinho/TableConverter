# Class of image table
import sys

import cv2 as cv
import text


class Table_image:
    
    def __init__(self, image_file_name):
        original_image = cv.imread(image_file_name)
        original_binary = Table_image.convert_to_binary(original_image)
        text_from_image = text.Text(image_file_name)
        structure = Table_image.extract_structure(
            original_binary, text_from_image.max_size_bndpoly[0],
            text_of_image.max_size_bndpoly[1])
        # could possible change coefficient_of_margin if some images detected
        # wrongly
        _, _, _ = Table_image.get_intersections(structure[0], structure[1])
        


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
        return (horizontal_structure, vertical_structure)

    @staticmethod
    def get_intersections(
            horizontal_structure, vertical_structure):
        intersections = cv.bitwise_and(
            horizontal_structure, vertical_structure)
        intersections_contours = cv.findContours(
            intersections, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        row_cordinate_list = []
        column_cordinate_list = []
        for cntr in intersections_contours:
            x, y, w, h = cv.boundingRect(cntr)
            M = cv.moments(cntr)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            for i in row_cordinate_list:
                if not cx-(1/2)*w < i < cx+(1/2)*w:
                    row_cordinate_list.append(cx)
            for j in column_cordinate_list:
                if not cy-(1/2)*h < i < cy+(1/2)*h:
                    column_cordinate_list.append(cy)

