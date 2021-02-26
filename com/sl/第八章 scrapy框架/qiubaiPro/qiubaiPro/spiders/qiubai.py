import scrapy
from qiubaiPro.items import QiubaiproItem

'''
需求: 爬取糗事百科
'''


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    # 基于终端指令的持久化存储
    # def parse(self, response):
    #     # 解析：作者的名称+段子内容
    #     div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
    #     all_data = []  # 存储所有解析到的数据
    #     for div in div_list:
    #         # xpath返回的是列表，但是列表元素一定是Selector类型的对象
    #         # author = div.xpath('./div/a[2]/h2/text()')[0].extract()
    #         author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()  # 替代上面一句
    #         content = div.xpath('./a[1]/div/span//text()').extract()
    #         # 列表转为字符串
    #         content = "".join(content).strip()
    #         dic = {
    #             'author': author,
    #             'content': content
    #         }
    #         all_data.append(dic)
    #         # print(author, content)
    #     return all_data

    # 基于管道的持久化存储
    def parse(self, response):
        # 解析：作者的名称+段子内容
        div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
        for div in div_list:
            # xpath返回的是列表，但是列表元素一定是Selector类型的对象
            # author = div.xpath('./div/a[2]/h2/text()')[0].extract()
            author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()  # 替代上面一句
            content = div.xpath('./a[1]/div/span//text()').extract()
            # 列表转为字符串
            content = "".join(content).strip()

            item = QiubaiproItem()
            item['author'] = author
            item['content'] = content
            # 将item提交给了管道
            yield item