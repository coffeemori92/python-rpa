import pyautogui

# fw = pyautogui.getActiveWindow() # 현재 활성화된 창
# print(fw.title) # 창의 제목 정보
# print(fw.size) # 창의 크기 정보
# print(fw.left, fw.top, fw.right, fw.bottom) # 창의 좌표 정보

# pyautogui.click(fw.left + 25, fw.top + 20)

# for window in pyautogui.getAllWindows():
#     print(window)

# for window in pyautogui.getWindowsWithTitle('제목 없음'):
#     print(window)

w = pyautogui.getWindowsWithTitle('제목 없음')[0]
print(w)

if w.isActive == False:   
    w.activate() # 활성화 (맨 앞으로 가져오기)
    
if w.isMaximized == False:
    w.maximize()

pyautogui.sleep(1)    
w.restore()

pyautogui.sleep(1)  
w.close() # 윈도우 닫기

# if w.isMinimized == False:
#     w.minimize()
