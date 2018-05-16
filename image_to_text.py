import io
from PIL import Image
import pytesseract
from wand.image import Image as wi 

'''pdf = wi(filename = "b.pdf",resolution = 300)
pdfImage = pdf.convert('jpeg')

imageBlobs = []
for img in pdfImage.sequence:
	imgPage = wi(image = img)
	imageBlobs.append(imgPage.make_blob('jpeg'))

recognised_text = []

for imgBlob in imageBlobs:
	im = Image.open(io.BytesIO(imgBlob))
	text = pytesseract.image_to_string(im,lang = 'eng')
	recognised_text.append(text)

print(recognised_text)'''	
im = Image.open("sample_test.jpg")
text = pytesseract.image_to_string(im,lang = 'eng')

print(text)
