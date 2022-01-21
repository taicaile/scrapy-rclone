import scrapy
from example.items import ExampleItem


class GoodreadSpider(scrapy.Spider):
    name = "goodread"
    start_urls = ["https://www.goodreads.com/quotes"]

    def parse(self, response):
        """parse"""
        image_urls = response.css(".quoteDetails img ::attr(src)").getall()
        yield ExampleItem(image_urls=image_urls)
