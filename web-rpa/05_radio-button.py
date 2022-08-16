import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('./driver/chromedriver.exe')
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

# 프레임 전환
browser.switch_to.frame('iframeResult')

elem = browser.find_element(By.XPATH, '//*[@id="html"]')

if elem.is_selected() == False:
    elem.click()
else:
    print('선택되어 있음')
    
time.sleep(3)    

browser.close()
