from PIL import Image
from pytesseract import image_to_string

img = Image.open("a.png");
code = image_to_string(img,lang='chi_sim')
print(code)
