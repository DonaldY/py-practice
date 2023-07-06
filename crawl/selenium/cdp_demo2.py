from selenium import webdriver
from selenium.webdriver import ChromeOptions
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

option = ChromeOptions()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
browser = webdriver.Chrome(options=option)

wait = WebDriverWait(browser, 10)         # 隐式等待：等待 10 秒
browser.get('http://www.customs.gov.cn/customs/302249/zfxxgk/2799825/302274/302277/4899681/index.html')

# elements = browser.find_element(By.CSS_SELECTOR, '#tableDate > tbody')
# print('all : '.format(elements))

# element = browser.find_element(By.XPATH, '#tableDate > tbody')
# print('all : '.format(element))



time.sleep(100) # 等待 100s
