import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('./driver/chromedriver.exe')
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox')

# 프레임 전환
browser.switch_to.frame('iframeResult')

elem = browser.find_element(By.XPATH, '//*[@id="vehicle1"]')

if elem.is_selected() == False:
    elem.click()

time.sleep(3)    

browser.close()
