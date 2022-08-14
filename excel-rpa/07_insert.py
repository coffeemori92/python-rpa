import os
from openpyxl import load_workbook

try:
    if not os.path.exists('out'):
        os.mkdir('out')
except Exception as e:
    print(e)
    
wb = load_workbook('./out/sample.xlsx') # 파일에서 워크북 불러옴
ws = wb.active

# ws.insert_rows(8) # 8번째 줄에 삽입
# ws.insert_rows(8, 5) # 8번째부터 5줄에 삽입

# ws.insert_cols(2) # B번째 열에 열 삽입
ws.insert_cols(2, 3) # B번째 열부터 3열 삽입

wb.save('./out/sample_insert_cols.xlsx')
