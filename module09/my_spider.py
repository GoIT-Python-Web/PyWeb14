import scrapy
from scrapyscript import Job, Processor

processor = Processor(settings=None)


class PythonSpider(scrapy.spiders.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):  # noqa
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('span small::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)


def baz() -> str:
    yield 'Hello'


if __name__ == '__main__':
    job = Job(PythonSpider)
    results = processor.run(job)

    print(results)
