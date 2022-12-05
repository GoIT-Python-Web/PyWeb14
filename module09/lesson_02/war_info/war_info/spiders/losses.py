import json
import re
from datetime import datetime

import scrapy


class LossesSpider(scrapy.Spider):
    name = 'losses'
    allowed_domains = ['index.minfin.com.ua']
    start_urls = ['https://index.minfin.com.ua/ua/russian-invading/casualties']

    def get_next_links(self):
        with open('links.json') as f:
            r = json.load(f)
        return [el.get("link") for el in r]

    def parse(self, response):
        result = {}
        for element in response.css('ul[class=see-also] li[class=gold]'):
            date = element.xpath('span/text()').get()
            try:
                date = datetime.strptime(date, "%d.%m.%Y").isoformat()
                print(date)
            except ValueError:
                print(f'Error for {date}')
                continue

            result.update({"date": date})
            losses = element.xpath('div[@class="casualties"]/div/ul/li')
            for l in losses:
                print(' '.join(l.css('*::text').extract()).split("—"))
                title, quantity = ' '.join(l.css('*::text').extract()).split("—")
                title = title.strip()
                quantity = re.search(r"\d+", quantity).group()
                result.update({title: int(quantity)})
            yield result

        for next_link in self.get_next_links():
            yield scrapy.Request(url=self.start_urls[0] + next_link)
