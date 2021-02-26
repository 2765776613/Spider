import requests
import json

'''
需求: 破解百度翻译
post请求 【ajax异步请求】
响应数据是一组json数据
'''
if __name__ == '__main__':
    # step1 指定url
    post_url = 'https://fanyi.baidu.com/sug'
    # step2 进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
    # step3 post请求参数处理
    word = input('enter a word:\n')
    data = {
        'kw': word
    }
    # step4 请求发送
    response = requests.post(url=post_url, data=data, headers=headers)
    # step5 获取响应数据 json()返回的是obj (如果确认响应数据是json类型的，才可以使用json()方法)
    dic_obj = response.json()
    # step6 持久化存储
    fileName = word + '.json'
    with open(fileName, 'w', encoding='utf-8') as f:
        json.dump(dic_obj, f, ensure_ascii=False)
