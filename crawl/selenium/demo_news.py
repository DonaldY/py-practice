
import scrapy
from scrapy.http import Request
from selenium import webdriver
from selenium.webdriver.common.by import By


class SinaSpiderSpider(scrapy.Spider):
    name = 'sina_spider'


    def __init__(self):
        self.start_urls = ['https://news.sina.com.cn/china/']
        self.option = webdriver.ChromeOptions()
        self.option.add_argument('no=sandbox')
        self.option.add_argument('--blink-setting=imagesEnable=false')

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        driver = webdriver.Chrome(chrome_options=self.option)
        driver.set_page_load_timeout(30)
        driver.get(response.url)

        title = driver.find_element(By.XPATH, "//h2[@class='undefined']/a[@target='_blank']")
        time = driver.find_element(By.XPATH, "//h2[@class='undefined']/../div[@class='feed-card-a "
                                             "feed-card-clearfix']/div[@class='feed-card-time']")

        for i in range(len(title)):
            print(title[i].text)
            print(time[i].text)