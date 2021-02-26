import requests
from lxml import etree
from ksdemo import KSClient

'''
需求: 爬取
'''

if __name__ == '__main__':
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    page_text = requests.get(url).text
    tree = etree.HTML(page_text)
    src = 'https://so.gushiwen.cn' + tree.xpath('// *[ @ id = "imgCode"]/@src')[0]
    img_data = requests.get(src).content
    with open('yzm.jpg', 'wb') as f:
        f.write(img_data)
    ks = KSClient()
    print('识别结果：' + ks.PostPic('yzm.jpg', 1))