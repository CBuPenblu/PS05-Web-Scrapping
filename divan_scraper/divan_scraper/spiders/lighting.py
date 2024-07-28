import scrapy


class LightingSpider(scrapy.Spider):
    name = "lighting"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://divan.ru/catalog/svet/"]

    def parse(self, response):
        lights = response.css('div._Ud0k')
        for light in lights:
            yield {
                'name' : light.css('div.lsooF span::text').get(),
                'price': light.css('div.pY3d2 span::text').get(),
                'url': light.css('a').attrib['href']
            }