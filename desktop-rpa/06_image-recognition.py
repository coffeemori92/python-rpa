import time, sys
import pyautogui

# menu = pyautogui.locateOnScreen('./out/menu.png')
# print(menu)

# pyautogui.click(menu)

# checkboxes = pyautogui.locateAllOnScreen('./out/checkbox.png')

# for checkbox in checkboxes:
#     print(checkbox)
#     pyautogui.click(checkbox, duration=0.25)
    
# plus_icon = pyautogui.locateOnScreen('./out/plus.png')

# start = time.time()
# pyautogui.moveTo(plus_icon)
# print('time : ', time.time() - start)

# 속도 개선
# 1. GrayScale
# plus_icon = pyautogui.locateOnScreen('./out/plus.png', grayscale=True)
# start = time.time()
# pyautogui.moveTo(plus_icon)
# print('time : ', time.time() - start)

# 2. 범위지정
# 1741,649
# 1905,735
# plus_icon = pyautogui.locateOnScreen('./out/plus.png', region=(1741, 649, 1905 - 1741, 735 - 649))
# pyautogui.moveTo(plus_icon)

# 3. 정확도 조정
# 90 퍼센트
# run_icon = pyautogui.locateOnScreen('./out/run.png', confidence=0.9)
# pyautogui.moveTo(run_icon)

# 자동화 대상이 바로 보여지지 않는 경우
# 1. 계속 기다리기
# file_menu_notepad = pyautogui.locateOnScreen('./out/file_menu_notepad.png')
# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)
# else:
#     print('발견 실패')

# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen('./out/file_menu_notepad.png')

# pyautogui.click(file_menu_notepad)

# 2. 일정시간 기다리기
# timeout = 10
# start = time.time() # 시작시간 설정

# file_menu_notepad = None

# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen('./out/file_menu_notepad.png')
#     end = time.time()
#     if end - start > timeout: 
#         print('시간종료')
#         sys.exit()

# pyautogui.click(file_menu_notepad)

def find_target(img_file, timeout):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout: break
    return target

def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f'[Timeout {timeout}s] Target not found ({img_file}). Terminate program.')
        sys.exit()
        
my_click('./out/file_menu_notepad.png', 10)
