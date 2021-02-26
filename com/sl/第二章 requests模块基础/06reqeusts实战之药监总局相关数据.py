import requests
import json

'''
需求: 爬取国家药品监督管理总局中基于中华人民共和国化妆品生产许可证相关数据
http://scxk.nmpa.gov.cn:81/xk/
'''

if __name__ == '__main__':
    # 批量获取不同企业的id值
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
    id_list = []  # 存储企业的id
    all_data_list = []  # 存储所有的企业详情数据

    for page in range(1, 6):
        data = {
            'on': 'true',
            'page': str(page),
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': ''
        }

        json_ids = requests.post(url=url, data=data, headers=headers).json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])
    # 获取企业详情数据
    detail_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data = {
            'id': id
        }
        detail_json = requests.post(url=detail_url, data=data, headers=headers).json()
        all_data_list.append(detail_json)
    # 持久化存储
    with open("hzp.json", 'w', encoding='utf-8') as f:
        json.dump(all_data_list, f, ensure_ascii=False)
