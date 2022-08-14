import os
from openpyxl import Workbook
from openpyxl.drawing.image import Image

try:
    if not os.path.exists('out'):
        os.mkdir('out')
except Exception as e:
    print(e)

wb = Workbook()
ws = wb.active

img = Image('./assets/image.png')

# C3 위치에 img.png 파일의 이미지를 삽입
ws.add_image(img, 'C3')

wb.save('./out/sample_image.xlsx')
