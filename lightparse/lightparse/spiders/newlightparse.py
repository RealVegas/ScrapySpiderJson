import scrapy

class NewlightparseSpider(scrapy.Spider):
    name = 'newlightparse'
    allowed_domains = ['https://www.divan.ru/ekaterinburg/']
    start_urls = ['https://www.divan.ru/ekaterinburg/category/svet']

    def parse(self, response):
        pass