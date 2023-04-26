from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
try:
    browser.get('file:///Users/yangyf/Downloads/demo.html')
    print(browser.current_url)    # 打印 url
    print(browser.get_cookies())  # 打印 cookies
    print(browser.page_source)    # 打印 页面源码
finally:
    browser.close()
