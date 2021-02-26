import requests
from lxml import etree
from ksdemo import KSClient

'''
这个需求自己未能完成~~~~不知道什么原因~~~自认为代码思路没有问题
编码流程：
1.验证码的识别，获取验证码图片的文字数据
2.对post请求进行发送（处理请求参数）
3.对响应数据进行持久化存储
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
    # 通过抓包工具，找到login的url  一定要勾选 preserve log,才可以看到跳转前的请求
    login_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2021161816327'
    data = {
        'email': '15972945072',
        'icode': code,
        'origURL': 'http://www.renren.com/home',
        'domain': 'renren.com',
        'key_id': '1',
        'captcha_type': 'web_login',
        'password': '3a6c3f29588c0b46a7ebe00211d37c4304696875dec72d5c4c07671806320db7',
        'rkey': 'da25ffa69b1d73a097a822c8b033003e',
        'f': 'http%3A%2F%2Fwww.renren.com%2F973295482'
    }
    response = requests.post(url=login_url, data=data, headers=headers)
    # print(response.status_code)
    login_page_text = response.text
    # 3. 持久化存储
    with open("./renren.html", 'w', encoding='utf-8') as f:
        f.write(login_page_text)
