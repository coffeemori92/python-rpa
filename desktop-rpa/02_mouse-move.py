import pyautogui

# 지정한 위치로 마우스 이동
# pyautogui.moveTo(100 ,100)
# 0.25초 동안 100, 200 으로 위치 이동
# pyautogui.moveTo(100, 200, duration=0.25)

# 상대 좌표로 마우스 이동 (현재 커서가 있는 위치로 부터)
pyautogui.moveTo(100 ,100, duration=0.25)
print(pyautogui.position())
pyautogui.move(100, 100, duration=0.25) # +100, +100 -> 200, 200
print(pyautogui.position())
pyautogui.move(100, 100, duration=0.25) # +200, +200 -> 300, 300
print(pyautogui.position())

p = pyautogui.position()
print(p[0], p[1])
print(p.x, p.y)
