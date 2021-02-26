import requests
from lxml import etree

url = 'https://github.com/session'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}
data = {
    'commit': 'Sign in',
    'login': '2765776613',
    'password': 'xxxxxx',
    'webauthn-support': 'supported',
    'webauthn-iuvpaa-support': 'unsupported',
    'authenticity_token': '30oYLtQXHH5hncKwCP6VlKWXdTRUu0yOA86vVrWbTZif8DyzEfwSEu2gqhvlPGmuFvjR40uilXlNrq6ib90BfQ=='
}
session = requests.Session()
page_text = session.post(url=url, headers=headers, data=data).text

# with open('./git.html', 'w', encoding='utf-8') as fp:
#     fp.write(page_text)

user_url = 'https://github.com/2765776613'
user_page_text = session.get(user_url, headers=headers).text
# with open('./gitUser.html', 'w', encoding='utf-8') as fp:
#     fp.write(user_page_text)

# 解析出仓库的描述信息
tree = etree.HTML(user_page_text)
li_list = tree.xpath("//div[@class='mt-4']/div/ol/li")
for li in li_list:
    title = li.xpath('div/div/p[1]/text()')[0]
    print(title.strip())
