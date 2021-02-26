import requests
from lxml import etree

'''
需求: 爬取58同城中二手房的房源信息
'''
if __name__ == '__main__':
    url = 'https://cq.58.com/ershoufang/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
    page_text = requests.get(url, headers).text
    tree = etree.HTML(page_text)
    with open("58.txt", 'w', encoding='utf-8') as f:
        for title in tree.xpath('//section[@class="list"][1]//h3/text()'):
            f.write(title + '\n')
