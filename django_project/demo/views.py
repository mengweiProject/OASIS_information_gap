# import multiprocessing
# import json
# from django.http import JsonResponse
#
#
#
#
# def calc_sum(a, b):
#     import time
#     # time.sleep(1)
#     return a + b
#
# # 在顶层模块中创建进程池
# process_pool = None
# def create_process_pool():
#     global process_pool
#     if process_pool is None:
#         process_pool = multiprocessing.Pool(processes=8)
#
# def get_multi_res(request):
#     global process_pool
#     if process_pool is None:
#         create_process_pool()
#
#     paramList = [(1,2),(3,4),(5,6)]
#     result = []
#     for a, b in paramList:
#         res = process_pool.apply_async(calc_sum, args=(a, b))
#         result.append(res)
#     data = {}
#     for res in result:
#         data[f'{res.get()}'] = res.get()
#     print(data)
#     return JsonResponse(data)

from multiprocessing import Pool
from time import sleep

from django.http import HttpResponse

from util.db_pool import Database
from threading import Thread

db1 = Database()
db1.connect()
conn1 = db1.get_connection()
cursor1 = conn1.cursor()


# 每个进程都应该有自己的连接池对象
def get_connection():
    db = Database()
    db.connect()
    conn = db.get_connection()
    cursor = conn.cursor()
    return conn,  cursor


def shifangziyuan(conn,  cursor):
    cursor.close()
    conn.close()
    print('释放资源成功')


def task_function(arg):
    conn, cursor = get_connection()
    sql = f'select * from users'
    cursor.execute(sql)

    # 获取查询结果
    results = cursor.fetchall()
    print(arg)
    # sleep(1)
    # 另起一个线程去释放连接
    thread = Thread(target=shifangziyuan, args=(conn,  cursor))
    thread.start()
    return results


def your_view(request):
    # 创建进程池，设置最大进程数
    pool = Pool(processes=8)

    # 执行任务函数，并传递参数（如果有需要）
    results = pool.map(task_function, [(111,)] * 8)


    # 处理结果并返回响应
    # ...
    return HttpResponse(str(results))


if __name__ == '__main__':
    conn, cursor = get_connection()
    sql = f'select * from users'
    cursor.execute(sql)

    # 获取查询结果
    results = cursor.fetchall()
    print(results)
    shifangziyuan(conn, cursor)