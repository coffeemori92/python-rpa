import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('./driver/chromedriver.exe')
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select')

# 프레임 전환
browser.switch_to.frame('iframeResult')

# elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[3]')
# elem.click()

# 옵션 중에서 텍스트가 Opel인 항목을 선택
# elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[text()="Opel"]')
# elem.click()

# 텍스트값 부분일치
elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[contains(text(), "pel")]')
elem.click()

time.sleep(3)    

browser.close()
