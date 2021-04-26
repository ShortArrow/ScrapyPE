import scrapy
from scrapy.selector.unified import Selector

class EShisetsuSpider(scrapy.Spider):
    name = 'e_shisetsu'
    allowed_domains = ['www.e-shisetsu.e-aichi.jp']
    start_urls = ['https://www.e-shisetsu.e-aichi.jp/sp/']

    def parse(self, response):
        for a in response.css('a'):
            if "空き状況" in a.css("div::text").get():
                response.follow(a,callback=self.parse2)

    def parse2(self, response):
        for a in response.css('a'):
            print(a.css("div::text").get())
            
