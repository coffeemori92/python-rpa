import pyautogui

# pyautogui.mouseInfo()
# pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용

for i in range(5):
    pyautogui.move(100, 100)
    pyautogui.sleep(1)