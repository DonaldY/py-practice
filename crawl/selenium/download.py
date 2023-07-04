# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep


options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': '/Users/yangyf/Downloads'}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(options=options)
driver.get('http://39.108.214.163:8990/monitor/1.104.1.103/20230703/20230703-191050_N000000036725_13826233708_913826233708_1688382648.173319.mp3')
sleep(5)
driver.quit()