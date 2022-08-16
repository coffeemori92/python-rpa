import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('./driver/chromedriver.exe')
browser.maximize_window()

# url 접속
browser.get('https://www.w3schools.com/')

# Learn HTML 클릭
browser.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div[1]/a[1]').click()

# 상단 메뉴 중 HOW TO 클릭
browser.find_element(By.XPATH, '//*[@id="topnav"]/div/div[1]/a[10]').click()

# 좌측 메뉴 중 Contact Form 메뉴 클릭
# browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[118]').click()
# browser.find_element(By.LINK_TEXT, 'Contact Form').click()
browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]').click()
# browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[contains(text(), "Contact")]').click()

# 입력란에 값 입력
first_name = 'hi'
last_name = 'hello'
country = 'Canada'
subject = 'fin'

browser.find_element(By.XPATH, '//*[@id="fname"]').send_keys(first_name)
browser.find_element(By.XPATH, '//*[@id="lname"]').send_keys(last_name)
browser.find_element(By.XPATH, '//*[@id="country"]/option[text()="{}"]'.format(country)).click()
browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/textarea').send_keys(subject)

# 3초 뒤에 submit
time.sleep(3)
browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/a').click()

# 3초 뒤에 모든 브라우저 종료
time.sleep(3)
browser.quit()
