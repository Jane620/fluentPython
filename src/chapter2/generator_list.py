# -*- coding:utf-8 -*-
'''
@author: jwang
@license: (C) Copyright 2018-2019, Nokia Sbell Tech Corporation Limited.
@contact: jianfeng.2.wang@nokia-sbell.com
@software: Pycharm
@file: generator_list.py
@time: 2019/11/19 17:44
@desc:
'''

def generator_list(group):
    return tuple(single for single in group)


if __name__ == '__main__':
    SIZES = ['S', 'M', 'L']
    print(list(x for x in generator_list(SIZES)))
