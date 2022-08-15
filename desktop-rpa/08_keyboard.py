import pyautogui
import pyperclip

w = pyautogui.getWindowsWithTitle('제목 없음')[0]
print(w)

w.activate()

# pyautogui.write('12345')
# pyautogui.write('hello world!', interval=0.25)

# pyautogui.write(
#     ['t', 'e', 's', 't', 'left', 'left', 'right', 'l', 'a', 'enter'], 
#     interval=0.25
# )

# 특수 문자
# shift 4 -> $
# pyautogui.keyDown('shift')
# pyautogui.press('4')
# pyautogui.keyUp('shift')

# 조합키
# pyautogui.keyDown('ctrl')
# pyautogui.keyDown('a')
# pyautogui.keyUp('a')
# pyautogui.keyUp('ctrl')

# 간편한 조합키
# pyautogui.hotkey('ctrl', 'a')

# pyperclip.copy('안녕') # '안녕' 글자를 클립보드에 저장
# pyautogui.hotkey('ctrl', 'v') # 클립보드에 있는 글자 붙여넣기

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    
my_write('안녕')

# 자동화 프로그램 종료
# win : ctrl + alt + del
# mac : cmd + shift + option + q