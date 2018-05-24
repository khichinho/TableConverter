import io
from PIL import Image
import pytesseract
import cv2

img = Image.open('element_crop_1.tiff').convert('LA')
# resized_image = cv2.resize(img, (620, 40))
text = pytesseract.image_to_string(img,lang = 'eng')

print(text)
