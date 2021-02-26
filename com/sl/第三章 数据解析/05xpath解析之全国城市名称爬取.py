import requests
from lxml import etree
'''
需求: 爬取全国城市名称
'''
if __name__ == '__main__':
    url = 'https://www.aqistudy.cn/historydata/'
    page_text = requests.get(url).text
    tree = etree.HTML(page_text)
    # 简化写法
    a_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    all_city_names = []
    for a in a_list:
        all_city_names.append(a.xpath('./text()')[0])

    print(all_city_names)
    print(len(all_city_names))

