import requests

# 以下网站已经被封了，所以这个模拟需要更换url才能完成
urls = [
    'http://xmdx.sc.chinaz.net/Files/DownLoad/jianli/201904/jianli10231.rar',
    'http://zjlt.sc.chinaz.net/Files/DownLoad/jianli/201904/jianli10229.rar',
    'http://xmdx.sc.chinaz.net/Files/DownLoad/jianli/201904/jianli10231.rar'
]


def get_content(url):
    print("正在爬取", url)
    response = requests.get(url)
    if (response.status_code == 200):
        return response.content


def parse_content(content):
    print("响应数据的长度为:", len(content))


for url in urls:
    content = get_content(url)
    parse_content(content)
