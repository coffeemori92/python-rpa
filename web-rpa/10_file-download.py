import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'download.default_directory': os.path.join(os.getcwd(), 'out')
})

browser = webdriver.Chrome('./driver/chromedriver.exe', options=chrome_options)
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')

browser.switch_to.frame('iframeResult')

elem = browser.find_element(By.XPATH, '/html/body/p[2]/a')
elem.click()

time.sleep(3)
browser.close()
