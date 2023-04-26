from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions

option = ChromeOptions()
option.add_argument('--headless')             # 设置无头模式
browser = webdriver.Chrome(options=option)
try:
    browser.get('file:///Users/yangyf/Downloads/demo.html')
    element = browser.find_element(By.ID, 'tableDate').text
    elements = browser.find_elements(By.CSS_SELECTOR, '#tableDate > tbody > tr')
    print(len(elements))    # 长度
    print(elements[0].text)  # 文本
    s_element = elements[0]
    print(s_element.get_attribute('ondblclick'))  # 拿取标签中的元素

    ele_tds = s_element.find_elements(By.CSS_SELECTOR, 'td')
    print(len(ele_tds))

    for td in ele_tds:
        ele_tt = td.find_elements(By.CSS_SELECTOR, 'img')
        ele_len = len(ele_tt)
        if ele_len == 0:
            print('1: ' + td.text)
        else:
            print('2: ' + ele_tt[0].get_attribute('src'))

finally:
    browser.close()
