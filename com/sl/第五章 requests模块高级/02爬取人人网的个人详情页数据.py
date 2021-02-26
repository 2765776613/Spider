import requests
from lxml import etree
from ksdemo import KSClient

'''
由于前面的需求没能完成，这个需求也无法完成
'''

if __name__ == '__main__':
    url = 'http://www.renren.com/SysHome.do'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
    page_text = requests.get(url).text
    tree = etree.HTML(page_text)
    code_img_src = tree.xpath('//*[@id="verifyPic_login"]/@src')[0]
    code_img_data = requests.get(code_img_src).content
    with open('./yzm.jpg', 'wb') as f:
        f.write(code_img_data)
    # 1. 识别验证码
    ks = KSClient()
    code = ks.PostPic('./yzm.jpg', 1)
    print("识别结果:", code)
    # 2. 发起post请求   （分析url非常重要）
    # 通过抓包工具，找到login的url
    login_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2021161147455'
    data = {
        'email': '15972945072',
        'icode': '',
        'origURL': 'http://www.renren.com/home',
        'domain': 'renren.com',
        'key_id': '1',
        'captcha_type': 'web_login',
        'password': '3a6c3f29588c0b46a7ebe00211d37c4304696875dec72d5c4c07671806320db7',
        'rkey': 'da25ffa69b1d73a097a822c8b033003e',
        'f': ''
    }
    session = requests.Session()
    response = session.post(url=login_url, data=data, headers=headers)
    print(response.status_code)

    detail_url = 'http://www.renren.com/973295482/profile'
    detail_page_text = session.get(url=url, headers=headers).text
    with open('bobo.html', 'w', encoding='utf-8') as f:
        f.write(detail_page_text)
