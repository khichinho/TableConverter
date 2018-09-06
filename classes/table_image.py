# Class of image table
import sys

import cv2
import classes.text as text


class Table_image:

    def __init__(self, image_file_name):
        original_image = cv2.imread(image_file_name)
        original_binary = Table_image.convert_to_binary(original_image)
        text_from_image = text.Text(image_file_name)
        structure = Table_image.extract_structure(
            original_binary, text_from_image.max_size_bndpoly[0],
            text_from_image.max_size_bndpoly[1])
        # could possible change coefficient_of_margin if some images detected
        # wrongly
        _, _, _ = Table_image.get_intersections(structure[0], structure[1])
        



    def convert_to_binary(image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        binary = cv2.adaptiveThreshold(gray, 255, 0, cv2.THRESH_BINARY, 15, -2)
        return binary


    def extract_structure(image, horizontal, vertical):
        horizontal_line_matrix = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontal, 1))
        vertical_line_matrix = cv2.getStructuringElement(cv2.MORPH_RECT, (1, vertical))
        horizontal_structure = cv2.morphologyEx(image, cv2.MORPH_OPEN, horizontal_line_matrix)
        horizontal_structure = cv2.morphologyEx(horizontal_structure, cv2.MORPH_CLOSE, horizontal_line_matrix)
        vertical_structure = cv2.morphologyEx(image, cv2.MORPH_OPEN, vertical_line_matrix)
        vertical_structure = cv2.morphologyEx(vertical_structure, cv2.MORPH_CLOSE, vertical_line_matrix)
        return horizontal_structure, vertical_structure


    def get_intersections(horizontal_structure, vertical_structure):
        intersections = cv2.bitwise_and(horizontal_structure, vertical_structure)
        intersections_contours = cv2.findContours(intersections, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        row_coordinate_list = []
        column_coordinate_list = []
        for cntr in intersections_contours:
            x, y, w, h = cv2.boundingRect(cntr)
            M = cv2.moments(cntr)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            for i in row_coordinate_list:
                if not cx-(1/2)*w < i < cx+(1/2)*w:
                    row_coordinate_list.append(cx)
            for j in column_coordinate_list:
                if not cy-(1/2)*h < j < cy+(1/2)*h:
                    column_coordinate_list.append(cy)

