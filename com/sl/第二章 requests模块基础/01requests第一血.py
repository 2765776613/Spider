import requests

'''
需求: 爬取搜狗首页的页面数据
'''

if __name__ == '__main__':
    # step1: 指定url
    url = "https://www.sogou.com/"

    # step2: 发起请求
    # get方法会返回一个响应对象
    response = requests.get(url=url)

    # step3: 获取响应数据
    page_text = response.text

    # step4: 持久化存储
    with open('sogou.html', 'w', encoding='utf-8') as f:
        f.write(page_text)

