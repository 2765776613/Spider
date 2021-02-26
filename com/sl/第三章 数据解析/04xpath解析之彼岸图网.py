import requests
from lxml import etree
import os

'''
需求: 解析下载图片数据
'''
if __name__ == '__main__':
    if not os.path.exists('./4kImgs'):
        os.mkdir('./4kImgs')
    url = 'http://pic.netbian.com/4kmeinv/'
    response = requests.get(url)
    # 解决中文乱码的第二种方式
    response.encoding = response.apparent_encoding

    tree = etree.HTML(response.text)
    a_list = tree.xpath('//div[@class="slist"]/ul/li/a')
    for li in a_list:
        src = 'http://pic.netbian.com/' + li.xpath('./img/@src')[0]
        alt = li.xpath('./img/@alt')[0]
        # 通用处理中文乱码的解决方案
        # alt = alt.encode('iso-8859-1').decode('gbk')
        img_data = requests.get(src).content
        fileName = './4kImgs/' + alt + '.jpg'
        with open(fileName, 'wb') as f:
            f.write(img_data)
        print(fileName, '爬取完成')
