import scrapy
from scrapy.crawler import CrawlerProcess


class NewlightparseSpider(scrapy.Spider):

    name = 'newlightparse'
    allowed_domains = ['https://www.divan.ru']
    start_urls = ['https://www.divan.ru/ekaterinburg/category/svet']

    def parse(self, response, **kwargs):
        lumins = response.css('div._Ud0k')

        for lum in lumins:
            yield {
                'name': lum.css('div.lsooF span::text').get(),
                'price': lum.css('div.pY3d2 span::text').get(),
                'url': 'https://www.divan.ru' + lum.css('a::attr(href)').get()
            }


# Создание экземпляра CrawlerProcess с нужными настройками
process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',  # Формат
        'FEED_URI': 'luminaries.json',  # Имя файла
        'FEED_EXPORT_ENCODING': 'utf-8'  # Кодировка
    })

# Запуск паука
process.crawl(NewlightparseSpider)
process.start()