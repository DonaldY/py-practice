from selenium import webdriver
from selenium.webdriver import ChromeOptions
import time

try:
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option('useAutomationExtension', False)
    # 增加一个参数设置
    option.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(options=option)
    browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
    })

    browser.get('https://bot.sannysoft.com/')
    time.sleep(100) # 等待 100s

finally:
    browser.close()
