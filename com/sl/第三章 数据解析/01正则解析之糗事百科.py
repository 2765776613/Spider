import requests
import re
import os

'''
需求: 爬取糗事百科所有图片
.text (字符串) 
.content (二进制) 
.json() (对象)
'''
if __name__ == '__main__':
    if not os.path.exists('./qiutuImgs'):
        os.mkdir('./qiutuImgs')
    img_src_list = []
    for page in range(1, 10):
        url = 'https://www.qiushibaike.com/imgrank/page/' + str(page)
        page_text = requests.get(url).text

        # 使用聚焦爬虫将页面中所有的图片
        pat = '<div class="thumb">.*?<img src="(.*?)"'
        # 如果不使用re.S参数，则只在每一行内进行匹配
        for src in re.findall(pat, page_text, re.S):
            img_src_list.append(src)
    for src in img_src_list:
        src = 'https:' + src
        img_data = requests.get(src).content
        img_name = src.split('/')[-1]
        img_path = './qiutuImgs/' + img_name
        with open(img_path, 'wb') as f:
            f.write(img_data)
