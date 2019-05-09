# "https://yaoota.com/en-sa/category/mobiles-and-tablets/mobiles/"
# #"/en-sa/product/huawei-mate-20-pro-128gb-4g-dual-sim-black-price-from-axiomtelecom-saudi-arabia
# search__container__result__products__single__image media-left
# t = response.css("ul.pagination")
# t.css('a[aria-label*=Next]::attr(href)').extract()

# itemLink sk-clr2 sPrimaryLink
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "mobiles"
    start_urls = [
        "https://saudi.souq.com/sa-en/mobile-phone/l/?ref=nav&section=2&page=1"
    ]

    def parse(self, response):
        # response.css("div.search__container__result__products__single__image a::attr(href)")[20].extract()
        product_link = "https://saudi.souq.com/"
        for quote in response.css('div.search__container__result__products__single__image'):
            self.start_urls.append(product_link + quote.css('a::attr(href)').extract_first())
            yield {

                'text': product_link + quote.css('a::attr(href)').extract_first(),
                }
            next_page = response.css('li.next a::attr(href)').extract_first()
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)