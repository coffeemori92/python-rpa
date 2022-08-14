import pyautogui

# img = pyautogui.screenshot()
# img.save('./out/screenshot.png') # 파일로 저장

# pyautogui.mouseInfo()
# 983,12 52,132,187 #3484BB

pixel = pyautogui.pixel(983, 12)
print(pixel)

print(pyautogui.pixelMatchesColor(983, 12, (52,132,187)))
print(pyautogui.pixelMatchesColor(983, 12, pixel))
