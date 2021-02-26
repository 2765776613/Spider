import requests

'''
需求: 爬取搜狗指定词条对应的搜索结果页面(简易网页采集器)
'''
'''
UA: User-Agent(请求载体的身份标识)
UA检测: 门户网站的服务器会检测对应请求的载体身份标识，如果检测到请求的载体身份标识为某一款浏览器，
那么说明该请求是一个正常的请求。但是，如果检测到请求的载体身份标识不是基于某一款浏览器的，则表示
该请求为不正常的请求(爬虫)，则服务器端就很有可能拒绝该次请求。
UA伪装：让爬虫对应的请求载体身份标识伪装成某一款浏览器
'''

if __name__ == '__main__':
    url = 'https://www.sogou.com/web'
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
    keyword = input("enter a word:\n")
    # 处理url携带的参数: 封装到字典中
    param = {
        'query': keyword
    }
    response = requests.get(url=url, params=param, headers=headers)
    page_text = response.text
    fileName = keyword + '.html'
    with open(fileName, 'w', encoding='utf-8') as f:
        f.write(page_text)
