import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['www.c.com']
    start_urls = ['http://www.521609.com/tuku/shz/index.html']
    # 链接提取器
    link = LinkExtractor(allow=r'index_\d+\.html')
    rules = (
        # 规则解析器 follow=True: 可以将链接提取器继续作用到链接提取器提取到的链接所对应的页面中
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response)
