import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('./driver/chromedriver.exe')
browser.maximize_window()
browser.get('https://www.w3schools.com/tags/att_input_type_radio.asp')

curr_handle = browser.current_window_handle
print(curr_handle) # 현재 윈도우 핸들 정보

# Try it yourself
browser.find_element(By.XPATH, '//*[@id="main"]/div[2]/a').click()

handles = browser.window_handles # 모든 핸들 정보

for handle in handles:
    print(handle) # 각 핸들 정보
    browser.switch_to.window(handle) # 각 핸들로 이동
    print(browser.title) # 핸들 (브라우저)의 타이틀

# 현재 핸들 닫기
browser.close()

browser.switch_to.window(curr_handle)
print(browser.title) # HTML input type="radio"

time.sleep(3)
browser.get('http://daum.net')

time.sleep(3)

browser.quit()


