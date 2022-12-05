import re

import scrapy


class GetLinksSpider(scrapy.Spider):
    name = 'get_links'
    allowed_domains = ['index.minfin.com.ua']
    start_urls = ['https://index.minfin.com.ua/ua/russian-invading/casualties']

    def parse(self, response):
        for link in response.xpath('//div/h4/a'):

            yield {
                "link": "/month.php?month=" + re.search(r"\d{4}-\d{2}", link.xpath('.//@href').get()).group()
            }
