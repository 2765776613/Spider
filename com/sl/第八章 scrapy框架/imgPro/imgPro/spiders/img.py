import scrapy
from imgPro.items import ImgproItem


class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://sc.chinaz.com/tupian/']

    def parse(self, response):
        # 注意: 使用伪属性
        div_list = response.xpath('//div[@id="container"]/div')
        for div in div_list:
            src = "https:" + div.xpath('./div/a/img/@src2').extract_first()
            # print(src)
            item = ImgproItem()
            item['src'] = src
            yield item
