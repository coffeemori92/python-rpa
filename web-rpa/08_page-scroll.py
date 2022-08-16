import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('./driver/chromedriver.exe')
browser.get('https://shopping.naver.com/home/p/index.naver')

elem = browser.find_element(By.XPATH, '//*[@id="_verticalGnbModule"]/div/div[2]/div/div[2]/div/div[2]/form/fieldset/div/input')
elem.send_keys('무선마우스')
elem.send_keys(Keys.ENTER)

# 스크롤
# 지정한 위치로 스크롤 내리기
# 모니터 (해상도) 높이인 1080 위치로 스크롤 내리기
# browser.execute_script('window.scrollTo(0, 1080)')
# browser.execute_script('window.scrollTo(0, 2080)')

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

# 동적 페이지에 대해서 마지막까지 스크롤 반복 수행
interval = 2 # 2초에 한번씩 스크롤 내리기

prev_height = browser.execute_script('return document.body.scrollHeight')

while True:
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    
    # 페이지 로딩 대기
    time.sleep(interval)
    
    # 현재 문서 높이 가져와서 저장
    curr_height = browser.execute_script('return document.body.scrollHeight')
    if curr_height == prev_height: # 직전 높이와 같으면, 높이 변화가 없으면
        break # 반복문 탈출
    
    prev_height = curr_height

# 맨 위로 올리기
browser.execute_script('window.scrollTo(0, 0)')

time.sleep(3)

browser.close()
