from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class articlespider(CrawlSpider):
    name = 'example2'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/index.html']
    rules = [Rule(LinkExtractor(allow='catalogue',deny='index.html')),
            Rule(LinkExtractor(allow='index.html'), callback='parse_items',follow=True)]
    def parse_items(self,response):
        yield{
            'name' :response.xpath('//div[@class="row"]').xpath('.//h1/text()').extract()[0]
        }