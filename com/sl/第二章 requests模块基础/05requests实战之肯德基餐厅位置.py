import requests
import json

'''
需求: 爬取肯德基餐厅查询中指定地点的餐厅数据  
首先判断输入查询位置后，页面的url是否改变，若不变，则是ajax请求
'''
if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    data = {
        'cname': '',
        'pid': '',
        'keyword': '上海',
        'pageIndex': '1',
        'pageSize': '10'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
    response = requests.post(url=url, data=data, headers=headers)
    kfc_obj = response.json()
    with open('kfc.json', 'w', encoding='utf-8') as f:
        json.dump(kfc_obj, f, ensure_ascii=False)
