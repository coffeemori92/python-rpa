import os
from openpyxl import Workbook

try:
    if not os.path.exists('out'):
        os.mkdir('out')
except Exception as e:
    print(e)
    
wb = Workbook() # 새 워크북 생성

ws = wb.active  # 현재 활성화된 sheet 가져옴

ws.title = 'sample1' # 시트의 이름 변경

wb.save('./out/sample.xlsx')

wb.close()
 