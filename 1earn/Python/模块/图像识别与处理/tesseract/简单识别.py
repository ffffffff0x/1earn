from PIL import Image
from pytesseract import image_to_string

img = Image.open("c.png");
code = image_to_string(img)
print(code)
