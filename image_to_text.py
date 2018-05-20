import io
from PIL import Image
import pytesseract
from wand.image import Image as wi 

	
im = Image.open("a.jpg")
text = pytesseract.image_to_string(im,lang = 'eng')

print(text)
