from selenium import webdriver
from lxml import etree
from time import sleep

# 实例化一个浏览器对象
driver = webdriver.Chrome()
# 让浏览器发起一个指定url对应请求
driver.get('http://scxk.nmpa.gov.cn:81/xk/')
# 获取浏览器当前页面的页面源码数据
page_text = driver.page_source

# 解析企业名称
tree = etree.HTML(page_text)
title_list = tree.xpath('//*[@id="gzlist"]/li/dl/a/text()')
print(title_list)

sleep(5)
driver.quit()