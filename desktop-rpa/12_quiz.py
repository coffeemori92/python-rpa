import pyautogui, pyperclip, sys

pyautogui.hotkey('win', 'r')
pyautogui.write('mspaint')
pyautogui.press('enter')

pyautogui.sleep(2)

window = pyautogui.getWindowsWithTitle('제목 없음 - 그림판')[0]
if window.isMaximized == False:
    window.maximize()
    
btn_text = pyautogui.locateOnScreen('./out/btn_text.png')
if btn_text:
    pyautogui.click(btn_text, duration=0.5)
else:
    print('찾기 실패')
    sys.exit()

pyautogui.click(100, 350, duration=0.5)

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    
my_write('안녕')

pyautogui.sleep(5)

# 프로그램 종료
window.close()

pyautogui.sleep(1)

# 저장하지 않음 선택
btn_cancel = pyautogui.locateOnScreen('./out/btn_cancel.png')
pyautogui.click(btn_cancel, duration=0.5)
