from selenium import webdriver
from selenium.webdriver import ChromeOptions
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

option = ChromeOptions()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
browser = webdriver.Chrome(options=option)

browser.get('http://credit.customs.gov.cn/ccppwebserver/pages/ccpp/html/declCompany.html')
browser.delete_all_cookies()

time.sleep(10)

# 不顶用
# 还是会报：没有符合条件的数据
next_btn = browser.find_element(By.ID, 'hasNextHref')
# next_btn.click()

webdriver.ActionChains(browser).move_to_element(next_btn).perform()

print("已经移动到：" + str(next_btn))

time.sleep(1)

webdriver.ActionChains(browser).move_to_element(next_btn).click(next_btn).perform()


print("click next page")

time.sleep(100)
