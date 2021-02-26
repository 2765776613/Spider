import requests
import json

'''
需求: 爬取豆瓣电影排行榜中的电影详情数据
get请求【ajax异步请求】
响应数据是一组json数据
'''
if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list'
    params = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '40'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
    response = requests.get(url=url, params=params, headers=headers)
    list_data = response.json()
    with open('movie.json', 'w', encoding='utf-8') as f:
        json.dump(list_data, f, ensure_ascii=False)
