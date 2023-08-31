import multiprocessing
import json
from django.http import JsonResponse

def calc_sum(a, b):
    import time
    time.sleep(1)
    return a + b

# 在顶层模块中创建进程池
process_pool = None
def create_process_pool():
    global process_pool
    if process_pool is None:
        process_pool = multiprocessing.Pool(processes=8)

def get_multi_res(request):
    global process_pool
    if process_pool is None:
        create_process_pool()

    paramList = [(1,2),(3,4),(5,6)]
    result = []
    for a, b in paramList:
        res = process_pool.apply_async(calc_sum, args=(a, b))
        result.append(res)
    data = {}
    for res in result:
        data[f'{res.get()}'] = res.get()
    print(data)
    return JsonResponse(data)