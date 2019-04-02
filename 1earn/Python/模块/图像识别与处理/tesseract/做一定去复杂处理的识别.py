from PIL import Image
from pytesseract import image_to_string

img = Image.open("c.png");
imgry = img.convert("L")
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
out = imgry.point(table, '1')
code = image_to_string(out)


print(code)
