import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome('./driver/chromedriver.exe')
browser.get('https://www.w3schools.com/html/')

elem = browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[62]')

# 방법 1 : ActionChain
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()

# 방법 2 : 좌표 정보 이용
xy = elem.location_once_scrolled_into_view
print('type : ', type(xy))
print('value : ', xy)

time.sleep(3)

browser.close()
