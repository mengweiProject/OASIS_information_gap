# # -*- coding: utf-8 -*-
#
# """
# 演示代码
# """
#
# import pandas as pd
#
# from data_stracture import basic
#
# # def moslems_detector(complete_s):
# #     is_detector = True
# #     temp_deque = basic.Deque()
# #     for s in complete_s:
# #         temp_deque.addRear(s)
# #
# #     while temp_deque.size() > 1 and is_detector:
# #         first = temp_deque.removeRear()
# #         last = temp_deque.removeFront()
# #         if first != last:
# #             is_detector = False
# #
# #     return is_detector
# #
# #
# # if __name__ == '__main__':
# #     s = 'asdfasdfasdfasdffdsafdsafdsafdsa'
# #     print(moslems_detector(s))
#
# # def calc_sum(l):
# #     if len(l) == 1:
# #         return l[0]
# #     return l[0] + calc_sum(l[1:])
# #
# # l = [i for i in range(1, 101)]
# # print(calc_sum(l))
# import re
#
# s = 'asdkjfa;ioguwpoiuit9gwbwr4309g09348g9348'
# reg = f'\d+'
# print(re.findall(reg, s))
#

from multiprocessing import Pool


d = {'a': 111, 'b': 222}

def calc_f1(n):
    res = d.get('a')
    print(res)
    return res ** n


def calc_f2(n):
    res = d.get('a')
    print(res)
    return res ** n


def calc_f3(n):
    res = d.get('a')
    print(res)
    return res ** n


def calc_f(n):
    res = d.get('a')
    print(res)
    return res ** n


if __name__ == '__main__':
    pool = Pool(processes=6)
    res = pool.map(calc_f, [i for i in range(100)])
    pool.close()
    pool.join()
    print(res)

