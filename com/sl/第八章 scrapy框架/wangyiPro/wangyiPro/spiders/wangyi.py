import scrapy
from selenium import webdriver
from wangyiPro.items import WangyiproItem


class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com/']
    models_urls = []  # 存储五个板块对应详情页的url

    # 实例化一个浏览器对象
    def __init__(self):
        self.bro = webdriver.Chrome()

    # 解析五大板块对应详情页的url
    def parse(self, response):
        li_list = response.xpath('//*[@id="js_festival_wrap"]/div[3]/div[2]/div[2]/div[2]/div/ul/li')
        alist = [3, 4, 6, 7, 8]  # 对应板块的li的索引
        for index in alist:
            model_url = li_list[index].xpath('./a/@href').extract_first()
            self.models_urls.append(model_url)

        # 依次对每一个板块对应的页面进行请求
        for url in self.models_urls:
            yield scrapy.Request(url, callback=self.parse_model)

    # 解析出每一个板块页面中对应新闻的标题和新闻详情页的url
    def parse_model(self, response):
        # 由于板块页面信息都是动态加载的，直接解析是解析不到的
        div_list = response.xpath('/html/body/div/div[3]/div[4]/div[1]/div/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            new_detail_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()

            item = WangyiproItem()
            item['title'] = title
            # 对新闻详情页的url发起请求
            yield scrapy.Request(new_detail_url, callback=self.parse_detail, meta={'item': item})

    # 解析新闻内容
    def parse_detail(self, response):
        content = response.xpath('//*[@id="content"]/div[2]//text()').extract()
        content = "".join(content)
        item = response.meta['item']
        item['content'] = content
        yield item

    def closed(self, spider):
        self.bro.quit()
