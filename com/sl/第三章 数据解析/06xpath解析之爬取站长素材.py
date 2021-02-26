import requests
from lxml import etree
import os

'''
需求: 下载站长素材中的所有免费简历模板
'''
if __name__ == '__main__':
    if not os.path.exists("./resumes"):
        os.mkdir("./resumes")

    url = 'https://sc.chinaz.com/jianli/free.html'
    page_text = requests.get(url).text
    tree = etree.HTML(page_text)
    a_list = tree.xpath('//div[@id="main"]/div/div/a')
    for a in a_list:
        detail_url = "https:" + a.xpath('./@href')[0]
        detail_page_text = requests.get(detail_url).text
        tree = etree.HTML(detail_page_text)
        down_url = tree.xpath('//div[@id="down"]/div[2]/ul/li[1]/a/@href')[0]
        page_data = requests.get(down_url).content
        title = tree.xpath('//div[@class="ppt_left fl"]/div/div/h1/text()')[0]
        title = title.encode('iso-8859-1').decode('utf-8')  # 解决编码问题
        fileName = './resumes/' + title + '.rar'
        with open(fileName, 'wb') as f:
            f.write(page_data)
        print(fileName, "下载完成")
