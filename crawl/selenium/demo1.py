from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ChromeOptions
import time


option = ChromeOptions()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
browser = webdriver.Chrome(options=option)
try:
    browser.get('https://www.baidu.com')      # 直接访问 百度
    input = browser.find_element(By.ID, 'kw') # 按照 ID 定位：id=kw
    input.send_keys('Python')                 # 文本框输入 python
    input.send_keys(Keys.ENTER)               # 按下按钮
    wait = WebDriverWait(browser, 10)         # 隐式等待：等待 10 秒
    wait.until(EC.presence_of_element_located((By.ID, 'content_left'))) # 显式等待：等到某个元素加载完成：id=content_left
    print(browser.current_url)    # 打印 url
    print(browser.get_cookies())  # 打印 cookies
    print(browser.page_source)    # 打印 页面源码

    time.sleep(10)
finally:
    browser.close()
