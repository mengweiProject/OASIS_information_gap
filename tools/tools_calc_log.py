# -*- coding: utf-8 -*-
"""
日志工具
"""

# import asyncio
# import logging
#
# def async_log(msg):
#     logging.info(msg)
#
# def log_message(msg):
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     asyncio.run_coroutine_threadsafe(async_log(msg), loop)
#
# log_message("This is an async log message")


# import asyncio
# import logging
# from concurrent.futures import ThreadPoolExecutor
#
# def async_log(msg):
#     logging.info(msg)
#
#
# def setup_logging():
#     log_file = 'log.log'
#     logging.basicConfig(filename=log_file, level=logging.INFO)
#
#
# def log_message(msg):
#     loop = asyncio.get_event_loop()
#     loop.run_in_executor(ThreadPoolExecutor(), async_log, msg)
#
#
# setup_logging()
# for i in range(10000000):
#     log_message("This is an async log message")
# print('end..............')


# import asyncio
# import logging
# from aiologger import Logger
# from aiologger.handlers import StreamHandler, FileHandler
# from concurrent.futures import ProcessPoolExecutor
# from multiprocessing import freeze_support
#
# async def async_log(msg):
#     logger = Logger.with_default_handlers()
#     await logger.info(msg)
#
# def log_message(msg):
#     loop = asyncio.get_event_loop()
#     asyncio.ensure_future(async_log(msg))
#     loop.run_until_complete(asyncio.gather(*asyncio.all_tasks()))
#
# if __name__ == '__main__':
#     freeze_support()
#
#     logging.basicConfig(level=logging.INFO, filename='log.log')
#     file_handler = logging.FileHandler('log.log')
#     formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#     file_handler.setFormatter(formatter)
#     logging.getLogger().addHandler(file_handler)
#
#     log_message("aaaaaaaaasdgasgadsf")


# d = {'a': 1, 'b': 2}
# # d.pop('c')
# # print(d)
# # print(len(d))
# l = [1, 2, 3, 4, 5]
# a, *_, b = l

# import pandas as pd
#
# s = pd.Series(dtype=float)


# def conditional_decorator(condition):
#     print('11111111111')
#     def decorator(func):
#         if condition:
#             # 给目标函数添加装饰器
#             def wrapped_func(*args, **kwargs):
#                 # 在目标函数执行前添加一些额外的功能
#                 print("Before calling the decorated function")
#                 result = func(*args, **kwargs)
#                 # 在目标函数执行后添加一些额外的功能
#                 print("After calling the decorated function")
#                 return result
#             return wrapped_func
#         else:
#             # 不给目标函数添加装饰器，直接返回原函数
#             return func
#     return decorator

# 定义一个条件，用于决定是否给目标函数添加装饰器
# condition = True
#
# @conditional_decorator(condition)
# def target_function():
#     print("This is the target function")
#
# # 调用目标函数
# target_function()

# import pandas as pd
#
# df = pd.DataFrame({'A': [1, 2, 3, 3, 4],
#                    'B': ['a', 'b', 'b', 'c', 'd']})
# print(df)

























