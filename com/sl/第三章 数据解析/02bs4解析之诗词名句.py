import requests
from bs4 import BeautifulSoup

'''
需求: 爬取三国演义小说所有的章节标题和章节内容
text/get_text() 可以获取某一标签中所有的文本内容
string 只可以获取该标签下面直系的文本内容
'''
if __name__ == '__main__':
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
    response = requests.get(url, headers)
    # 解决中文乱码的第一种方式
    # 在检查源码中 Content-Type: text/html; 而没有charset 就需要下面的代码
    # 至于utf-8，需要查看源代码
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    li_list = soup.select('.book-mulu > ul > li')
    f = open("./sanguo.txt", 'w', encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url = 'https://www.shicimingju.com' + li.a['href']
        # 对详情页发起请求，解析出章节内容
        detail_response = requests.get(detail_url, headers)
        detail_response.encoding = 'utf-8'
        # 解析出详情页中相关的章节内容
        soup = BeautifulSoup(detail_response.text, 'lxml')
        content = soup.find('div', class_='chapter_content').text
        f.write(title + ':' + content + '\n')
        print(title, '爬取成功')
