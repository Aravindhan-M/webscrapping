import scrapy

from scrapy_splash import SplashRequest
class priceneSpider(scrapy.Spider):
    name = "pricena"
    custom_settings = {
        'ITEM_PIPELINES': {
            'tutorial.pipelines.JsonWriterPipelineAxiom': 560
        }
    }
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}


    start_urls = ["https://ae.pricena.com/en/product/apple-iphone-6-plus-price-in-dubai-uae"]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, endpoint='render.html')

    def parse(self, response):
        print(response)