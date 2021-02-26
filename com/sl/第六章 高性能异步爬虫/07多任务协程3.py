import requests
import asyncio
import time
import aiohttp

start = time.time()
urls = ['http://127.0.0.1:5000/sl', 'http://127.0.0.1:5000/jack', 'http://127.0.0.1:5000/tom']


async def get_page(url):
    print("正在下载", url)
    # with 前面必须有async修饰
    async with aiohttp.ClientSession() as session:
        # get()   post()
        # headers, params/data, proxy=''
        async with await session.get(url) as response:
            # text()返回字符串形式的响应数据
            # read()返回的二进制形式的响应数据
            # json()返回的就是json对象
            # 注意：在获取响应数据操作之前一定要使用await进行手动挂起
            page_text = await response.text()
            print(page_text)
    print("下载完成", url)


tasks = []
for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print(end - start)
