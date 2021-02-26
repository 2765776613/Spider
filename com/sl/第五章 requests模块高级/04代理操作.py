import requests

# 把https换成http就请求成功
# 我也不知道为什么。。。。
url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}

response = requests.get(url, headers, proxies={'http': '59.125.123.129:81'})
response.encoding = 'utf-8'
page_text = response.text

with open('ip.html', 'w', encoding='utf-8') as f:
    f.write(page_text)
