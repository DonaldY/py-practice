from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
try:
    browser.get('file:///Users/yangyf/Documents/Code/python/py-practice/crawl/selenium/demo.html')

finally:
    browser.close()
