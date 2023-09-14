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


d = {'a': 1, 'b': 2}
# d.pop('c')
# print(d)
# print(len(d))
l = [1, 2, 3, 4, 5]
a, *_, b = l





























