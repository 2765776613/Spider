import requests
from lxml import etree
import re
from multiprocessing.dummy import Pool

'''
需求: 爬取梨视频的视频数据
未完成，这个网站的反爬措施太多，没有完全攻破！！！
'''
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',

}
# 原则: 线程池处理的是阻塞且耗时的操作

url = 'https://www.pearvideo.com/category_5'

page_text = requests.get(url, headers).text
tree = etree.HTML(page_text)

li_list = tree.xpath("//li[@class='categoryem']")

session = requests.session()

urls = []
for li in li_list:
    detail_url = "https://www.pearvideo.com/" + li.xpath("./div/a/@href")[0]
    title = li.xpath("./div/a/div[2]/text()")[0] + '.mp4'
    # 对详情页的url发起请求
    detail_page_data = session.get(detail_url, headers=headers).text
    # 从详情页中解析出视频的url  视频是动态加载的
    pattern = 'srcUrl="(.*?)"'
    video_url = re.findall(pattern, detail_page_data)[0]
    dic = {
        'title': title,
        'url': video_url
    }
    urls.append(dic)


def get_video_data(dic):
    url = dic['url']
    print(dic['title'], '正在下载...')
    data = requests.get(url, headers).content
    with open(dic['title'], 'wb') as f:
        f.write(data)
        print(dic['title'], '下载成功!')


# 使用线程池对视频数据进行请求（较为耗时的阻塞操作）
pool = Pool(4)
pool.map(get_video_data, urls)

pool.close()
pool.join()