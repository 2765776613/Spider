# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.http import HtmlResponse
from time import sleep


class WangyiproDownloaderMiddleware:

    def process_request(self, request, spider):

        return None

    # 该方法拦截五大板块对应的响应对象，进行篡改
    def process_response(self, request, response, spider):
        bro = spider.bro  # 获取在爬虫类中定义的浏览器对象
        # spider爬虫对象
        # 判断请求的url是否属于五大板块对应的url
        if (request.url in spider.models_urls):
            bro.get(request.url)  # 进行请求发送
            sleep(2)
            page_text = bro.page_source  # 页面源码数据（包含动态加载新闻数据）

            # 五大板块对应的响应对象
            # 针对定位到的这些response进行篡改
            # 实例化一个新的响应对象（符合要求：包含动态加载出的新闻数据），替代原来的响应对象
            # 如何获取动态加载出来的新闻数据？？
            # 基于selenium便捷的获取动态加载数据
            new_response = HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)
            return new_response
        else:
            return response  # 其他请求对应的响应对象

    def process_exception(self, request, exception, spider):

        pass
