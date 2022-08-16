import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

browser = webdriver.Chrome('./driver/chromedriver.exe')
browser.maximize_window()
browser.get('https://flight.naver.com/')

browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]').click()
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[1]/div/input')
elem.click()
elem.send_keys('제주')

time.sleep(3)

browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/section').click()
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()

# 가는날
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[3]/button').click()

# 오는날
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[2]/button').click()

# 검색
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/button').click()

# 첫번째 결과 출력
try:
    elem = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[5]/div/div[2]/div[2]/div/div[2]')))
    print(elem.text)
except Exception as e:
    print(e)
    
# 첫번째 결과 출력
# elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[5]/div/div[2]/div[2]/div/div[2]')
# print(elem.text)

time.sleep(5)

browser.close()
