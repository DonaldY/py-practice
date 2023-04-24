from selenium import webdriver
from selenium.webdriver import ChromeOptions
import time
from selenium.webdriver.common.by import By

option = ChromeOptions()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

browser = webdriver.Chrome(options=option)

browser.get('http://credit.customs.gov.cn/ccppwebserver/pages/ccpp/html/declCompany.html')


#
# elements = browser.find_element(By.CSS_SELECTOR, '#tableDate > tbody')
# print('all : '.format(elements))

element = browser.find_element(By.XPATH, '#tableDate > tbody')
print('all : '.format(element))



time.sleep(100) # 等待 100s
