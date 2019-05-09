# "https://yaoota.com/en-sa/category/mobiles-and-tablets/mobiles/"
# #"/en-sa/product/huawei-mate-20-pro-128gb-4g-dual-sim-black-price-from-axiomtelecom-saudi-arabia
# search__container__result__products__single__image media-left
# t = response.css("ul.pagination")
# t.css('a[aria-label*=Next]::attr(href)').extract()
# itemLink sk-clr2 sPrimaryLink
# "https://saudi.souq.com/sa-en/mobile-phone/l/?ref=nav&page=2"
# "https://saudi.souq.com/sa-en/mobile-phone/l/?ref=nav"
# scrapy shell -s USER_AGENT='Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'

# scrapy crawl quotes -o quotes.jl
import scrapy
import logging
from scrapy.utils.log import configure_logging
import json
configure_logging(install_root_handler=False)
logging.basicConfig(
    filename='log.txt',
    format='%(levelname)s: %(message)s',
    level=logging.INFO
)


# import selenium
# from twisted.internet import reactor, defer
# from scrapy.crawler import CrawlerRunner
# from scrapy.utils.log import configure_logging
# from scrapy.crawler import CrawlerProcess
# https://saudi.souq.com/sa-en/mobile-phone/l/?ref=nav&page=32


class SouqSpider(scrapy.Spider):
    name = "souq"
    custom_settings = {
        'ITEM_PIPELINES': {
            'tutorial.pipelines.JsonWriterPipeline': 400
        }
    }
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
    start_urls = [
        "https://saudi.souq.com/sa-en/mobile-phone/l/?ref=nav&section=2&page=1"
    ]

    def start_requests(self):

        for url in self.start_urls:

            yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        print("response is")
        print(response)


        for quote in response.css('a.itemLink.sk-clr2.sPrimaryLink'):
            yield {

                'link': quote.css('a::attr(href)').extract()[0],
                }
            next_page = None
            page = response.css('li.pagination-next.goToPage a::attr(href)').extract_first()
            if page is not None:
                page = page.split("&")
                page.insert(1,"section=2")
                next_page = "&".join(page)
            print(next_page)
            if next_page is not None:
                yield response.follow(next_page,headers=self.headers, callback=self.parse,meta = {'dont_redirect': True,'handle_httpstatus_list': [302,307]})


class SouqSpider2(scrapy.Spider):
    current_url = None
    name = "souq2"
    custom_settings = {
        'ITEM_PIPELINES': {
            'tutorial.pipelines.JsonWriterPipeline2': 500,
            'scrapy.pipelines.images.ImagesPipeline': 1
        },
        'IMAGES_STORE': '/home/sayone/Desktop/Webscrapping/tutorial/tutorial/images/souq'
    }

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
    start_urls = []

    def __init__(self, *args, **kwargs):
        with open("itemsar.jl", "r",encoding = 'utf-8') as f:
            for l in f:
                d = json.loads(l)

                self.start_urls.append(d['link'])

    def start_requests(self):
        for url in self.start_urls:
            self.current_url = url
            yield scrapy.Request(url, headers=self.headers)


    def parse(self, response):
        for res in response.xpath('//div[@id="specs-full"]'):


            dt= res.xpath('.//dt/text()').extract()
            dd = []
            value_element = res.xpath('.//dd')
            for value in value_element:
                if len(value.xpath('.//i'))==0:
                    val = value.xpath('text()').extract()
                    dd.append(val[0] if len(val) > 0 else "")
                else:
                    dd.append(False if value.xpath('.//i/@class').extract()[0] == 'fi-x' else True)
            dt.append("name")
            dd.append(response.xpath('//div[contains(@class,"product-title")]//h1/text()').extract()[0])
            dt.append("price")
            price_val = response.xpath('//h3[@class="price is sk-clr1"]/text()').extract()[1]
            price_string = (price_val.encode('ascii', 'ignore')).decode("utf-8")
            dd.append(price_string.strip())
            dt.append("currency-code")
            dd.append(response.xpath('//span[@class="currency-text sk-clr1"]/text()').extract()[0])
            dt.append("product_link")
            dd.append(response.url)

            print(dt)
            print(dd)
            res = dict(zip(dt, dd))
            print(res)
            list3 = []
            for x, y in zip(dt, dd):
                list3.append(x)
                list3.append(y)

        yield {
            "link" : list3,
            'image_urls':response.xpath('//div[@class="img-bucket "]')[0].xpath(".//img/@src").extract()

        }
        next_pages = response.css('a.value.size-value::attr(data-url)').extract()
        for page in next_pages:
            next_page = page
            if next_page is not None:
                self.current_url = next_page
                yield response.follow(next_page,headers=self.headers, callback=self.parse)




# configure_logging()
# runner = CrawlerRunner()
#
#
# @defer.inlineCallbacks
# def crawl():
#     yield runner.crawl(SouqSpider)
#     yield runner.crawl(SouqSpider2)
#     reactor.stop()
#
#
# crawl()
# reactor.run()
