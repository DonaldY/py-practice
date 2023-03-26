from selenium import webdriver
from selenium.webdriver import ChromeOptions

option = ChromeOptions()
option.add_argument('--headless')             # 设置无头模式
browser = webdriver.Chrome(options=option)
browser.set_window_size(1366, 768)            # 设置窗口大小
browser.get('https://www.baidu.com')
browser.get_screenshot_as_file('preview.png') # 截图，并生成在当前目录下