import time

# # 使用单线程串行方式执行
# start_time = time.time()
#
#
# def get_page(str):
#     print("正在下载:", str)
#     time.sleep(2)
#     print("下载成功:", str)
#
#
# name_list = ['dd', 'aa', 'bb', 'vv']
# for i in range(len(name_list)):
#     get_page(name_list[i])
#
# end_time = time.time()
#
# print("%d second" % (end_time - start_time))

# 使用线程池方式执行
from multiprocessing.dummy import Pool

start_time = time.time()


def get_page(str):
    print("正在下载:", str)
    time.sleep(2)
    print("下载成功:", str)


name_list = ['dd', 'aa', 'bb', 'vv']

# 实例化一个线程池对象
pool = Pool(4)
pool.map(get_page, name_list)

end_time = time.time()
print("%d second" % (end_time - start_time))
