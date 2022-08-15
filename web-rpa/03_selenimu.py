from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('./driver/chromedriver.exe')
browser.get('http://naver.net')

elem = browser.find_element(By.LINK_TEXT, '카페')
print(elem)
print(elem.get_attribute('href'))
print(elem.get_attribute('class'))

# elem.click()
# browser.back()
# browser.forward()
# browser.refresh()

elem = browser.find_element(By.ID, 'query')
# print(elem)
elem.send_keys('hi')
elem.send_keys(Keys.ENTER)

# elem = browser.find_element(By.TAG_NAME, 'a')
# print(elem)
# print(elem.get_attribute('href'))

elems = browser.find_elements(By.TAG_NAME, 'a')

for elem in elems:
    print(elem.get_attribute('href'))
