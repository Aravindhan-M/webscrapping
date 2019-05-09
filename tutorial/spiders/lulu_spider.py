import scrapy
import logging
from scrapy.utils.log import configure_logging
import json
import re
import math
configure_logging(install_root_handler=False)
logging.basicConfig(
    filename='log.txt',
    format='%(levelname)s: %(message)s',
    level=logging.INFO
)


# class LuluSpider(scrapy.Spider):
#     name = "lulu_spider"
#     custom_settings = {
#         'ITEM_PIPELINES': {
#             'tutorial.pipelines.JsonWriterPipelineLULU': 560
#         }
#     }
#     headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
#     start_urls = [
#         "https://www.luluhypermarket.com/en-sa/mobiles-mobiles-%26-gadgets/c/HY00214728?q=%3Arelevance%3Acategory%3AHY00214730&text="
#     ]
#     next_pg = 'https://www.luluhypermarket.com/en-sa/mobiles-mobiles-&-gadgets/c/HY00214728/loadMoreProducts?q=:relevance:category:HY00214730&text=&page={pageno}&plpColumnNumber=0'
#     next_page_no = 1
#     total_page = 0
#     first_run = True
#
#     def start_requests(self):
#
#         for url in self.start_urls:
#             yield scrapy.Request(url, headers=self.headers)
#
#     def parse(self, response):
#         self.logger.info('request URL %s', response.url)
#         product_link = "https://www.luluhypermarket.com"
#         for quote in response.xpath('//div[@class="product-tile-main"]').xpath('.//a/@href').extract():
#             self.logger.info('quote is %s',quote)
#             yield {
#
#                 'link': product_link + quote
#                 }
#         if self.first_run:
#             items_per_page = int(response.xpath('//span[@class="plpShowingResultsLabel"]/text()')[0].extract())
#             total_items_raw = response.xpath('//div[@class="showing-prod-count top"]/text()')[1].extract()
#             total_items = int(re.findall(r'\d+', total_items_raw)[0])
#             self.total_page = math.floor(total_items/items_per_page)
#             self.logger.info('total pageno %s',self.total_page)
#             self.first_run = False
#         next_page = self.next_pg.format(pageno=self.next_page_no)
#         self.logger.info('next page is %s',next_page)
#         if self.next_page_no > self.total_page:
#             next_page = None
#         if next_page is not None:
#             yield response.follow(next_page,headers=self.headers, callback=self.parse)
#         self.next_page_no = self.next_page_no + 1


class LuluSpider2(scrapy.Spider):
    name = "lulu_spider2"
    custom_settings = {
        'ITEM_PIPELINES': {
            'tutorial.pipelines.JsonWriterPipelineLULU2': 570,
            'scrapy.pipelines.images.ImagesPipeline': 1
        },
        'IMAGES_STORE' : '/home/sayone/Desktop/Webscrapping/tutorial/tutorial/images/lulu'
    }
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
    start_urls = []
    img_url = 'https://www.luluhypermarket.com'

    def __init__(self, *args, **kwargs):
        with open("items.jl", "r") as f:
            for l in f:
                d = json.loads(l)
                self.start_urls.append(d['link'])
    #
    # def extract_information_from_script(self,response):
    #     script = response.xpath("//script/text()").extract()
    #     json_full_string = [string for string in script if re.search(r"getProducts",string) is not None][0]
    #     jsonobj = json.loads(json_full_string[json_full_string.find("[{"):json_full_string.find("}];") + 2],strict=False)
    #     return jsonobj

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        name = response.xpath('//h1[@class="pdp-productname"]/text()').extract()[0]
        #price = response.xpath('//div[@class="prod-price"]').xpath('.//span/text()').extract()[0]
        price = response.xpath('//div[@class="prod-price"]').xpath('.//li[last()]/span/text()').extract()[0]
        currency = "SAR"
        data = response.xpath('//div[@class="features-ul"]').xpath('.//p/text()').extract()   # list contains attr followed by value
        data.append("name")
        data.append(name)
        data.append("price")
        data.append(price)
        data.append("currency")
        data.append(currency)
        data.append("product_url")
        data.append(response.url)
        self.logger.info('data is')
        self.logger.info(data)
        yield {
            "link": [d.strip() for d in data],
            'image_urls': [self.img_url + i for i in response.xpath('//div[@class="carousel-inner"]').xpath('.//div//div//img/@src').extract()]

        }

# search__container__result__products__single__price
#



