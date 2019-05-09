import scrapy

import json
import re


# from tutorial.items import TutorialItem
class AxiomSpider(scrapy.Spider):
    name = "axiom"
    custom_settings = {
        'ITEM_PIPELINES': {
            'tutorial.pipelines.JsonWriterPipelineAxiom': 560
        }
    }
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
    start_urls = [
        "https://ksa.axiomtelecom.com/mobiles/search?page=1"
    ]

    def start_requests(self):

        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        next_page = None

        product_link = "https://ksa.axiomtelecom.com"
        for quote in response.xpath('//div[@class="variant-image"]').xpath('.//a/@href').extract():
            yield {

                'link':product_link + quote
                }
            page = response.xpath('//a[@class="next_page"]').xpath('@href').extract()
            if len(page) > 0:
                next_page = page[0]
            if next_page is not None:
                yield response.follow(next_page,headers=self.headers, callback=self.parse)


class AxiomSpider2(scrapy.Spider):
    name = "axiom2"
    custom_settings = {
        'ITEM_PIPELINES': {
            'tutorial.pipelines.JsonWriterPipelineAxiom2': 570,
            'scrapy.pipelines.images.ImagesPipeline': 1
        },
        'IMAGES_STORE' : '/home/sayone/Desktop/Webscrapping/tutorial/tutorial/images'
    }
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
    start_urls = []

    def __init__(self, *args, **kwargs):
        with open("axiomlink.jl", "r") as f:
            for l in f:
                d = json.loads(l)
                self.start_urls.append(d['link'])

    def extract_information_from_script(self,response):
        script = response.xpath("//script/text()").extract()
        json_full_string = [string for string in script if re.search(r"getProducts",string) is not None][0]
        jsonobj = json.loads(json_full_string[json_full_string.find("[{"):json_full_string.find("}];") + 2],strict=False)
        return jsonobj

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        script_obj = self.extract_information_from_script(response)
        for obj in script_obj:
            attr = []
            value = []
            attr.append('title')
            attr.append('brand')
            attr.append('currency')
            attr.append('price')
            attr.append('color')
            value.append(obj['title'])
            value.append(obj['brand'])
            value.append(obj['currency'])
            value.append(obj['final_price'])
            value.append(obj['catalog_options'][0])
            try:
                value.append(obj['catalog_options'][1])
                attr.append(['RAM'])
            except:
                pass
            func = lambda x: response.xpath(x).extract()
            attr += func("//td[@class='feature_name']/text()")
            value += func("//td[@class='feature_name']/following-sibling::td[1]/text()")
            attr.append("product_link")
            value.append(str(response.url))
            attr.append("thumbnail_url")
            value.append(func("//li[@class='pdp-thumbnail']//img/@src"))
            attr.append("image_url")
            value.append(func("//li[@class='pdp-thumbnail']/a/@data-medium-url"))


            yield {
                "link" : value,
                'image_urls' : func("//li[@class='pdp-thumbnail']/a/@data-medium-url")


            }


# search__container__result__products__single__price
#



