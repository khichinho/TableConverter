# Class of html table

import cv2 as cv

class Table_html:

    def __init__(self, text_part, structure_part):
        struct_binary = cv.adaptiveThreshold(structure_part,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,2)
        inv_struct_binary = ~struct_binary
        _, contours, hierarchy= cv.findContours(struct_binary,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
        
