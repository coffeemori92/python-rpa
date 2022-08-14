import os
from openpyxl import load_workbook

try:
    if not os.path.exists('out'):
        os.mkdir('out')
except Exception as e:
    print(e)
    
wb = load_workbook('./out/sample.xlsx') # 파일에서 워크북 불러옴
ws = wb.active

# ws.delete_rows(8) # 8번째 줄에 있는 줄 삭제
# ws.delete_rows(8, 3) # 8번째 줄부터 총 3 줄 삭제

# wb.save('./out/sample_delete_row.xlsx')

# ws.delete_cols(2) # 2번째 열 삭제
ws.delete_cols(2, 2) # 2번째 열부터 총 2개 열 삭제

wb.save('./out/sample_delete_col.xlsx')
