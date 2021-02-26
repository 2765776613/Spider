import scrapy


class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.521609.com/tuku/shz/index.html']

    # 生成一个通用的url模板
    url = 'http://www.521609.com/tuku/shz/index_%d.html'
    page_num = 2

    def parse(self, response):
        titles = response.xpath('//ul[@class="pbl "]/li/a/p/text()').extract()
        print(titles)
        if self.page_num <= 5:
            new_url = self.url % self.page_num
            self.page_num += 1
            # 手动请求发送: callback回调函数是专门用于数据解析的
            yield scrapy.Request(url=new_url, callback=self.parse)
