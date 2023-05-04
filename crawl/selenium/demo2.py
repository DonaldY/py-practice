from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions
import re
import time

option = ChromeOptions()
# option.add_argument('--headless')             # 设置无头模式
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

    print("===============> 行记录")
    for td in ele_tds:
        ele_tt = td.find_elements(By.CSS_SELECTOR, 'img')
        ele_len = len(ele_tt)
        if ele_len == 0:
            print('1: ' + td.text)
        else:
            print('2: ' + ele_tt[0].get_attribute('src'))

    print("===============> 分页信息，提取页数：")
    page_ele = browser.find_element(By.CSS_SELECTOR, '#ID_pagination > td:nth-child(2)')
    print(page_ele.text)
    regex = r"第(\d+)页"
    match = re.search(regex, page_ele.text)
    num = 100000
    if match:
        num = int(match.group(1))
        print(num)  # 输出 1
    else:
        print("未匹配到任何数字")

    print("===============> 点击下一页")
    if num < 1000:
        print("可以点击下一页")
        # input_btn = browser.find_element(By.ID, 'ID_pageNo')
        # input_btn.send_keys("2")
        # script = "document.getElementById('ID_pageNo').value = '2'"
        # browser.execute_script(script)
        next_btn = browser.find_element(By.ID, 'hasNextHref')
        next_btn.click()

        # next_btn = browser.find_element(By.CSS_SELECTOR, '#ID_pagination > td:nth-child(5)')
        # next_btn.click()

    time.sleep(100)

finally:
    browser.close()
