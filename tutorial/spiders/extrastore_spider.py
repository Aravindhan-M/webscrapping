import scrapy
from selenium import webdriver
import json
import selenium
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.crawler import CrawlerProcess
# https://saudi.souq.com/sa-en/mobile-phone/l/?ref=nav&page=32


class SouqSpider(scrapy.Spider):
    name = "extrastore"
    custom_settings = {
        'ITEM_PIPELINES': {
            'tutorial.pipelines.JsonWriterPipelineextra': 550
        }
    }
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
    start_urls = [
        "http://www.extrastores.com//en-sa/Products/mobiles-9950024"
    ]

    def start_requests(self):

        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        next_page = None
        # response.css("div.search__container__result__products__single__image a::attr(href)")[20].extract()
        product_link = "https://saudi.souq.com/"
        for quote in response.css('a.itemLink.sk-clr2.sPrimaryLink'):
            yield {

                'link':product_link + quote.css('a::attr(href)').extract()[0]
                }
            page = response.css('li.pagination-next.goToPage a::attr(href)').extract_first()
            if page is not None:
                page = page.split("&")
                page.insert(1,"section=2")
                next_page = "&".join(page)
            if next_page is not None:
                yield response.follow(next_page,headers=self.headers, callback=self.parse)
