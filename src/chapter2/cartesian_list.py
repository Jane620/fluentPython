# -*- coding:utf-8 -*-
'''
@author: jwang
@license: (C) Copyright 2018-2019, Nokia Sbell Tech Corporation Limited.
@contact: jianfeng.2.wang@nokia-sbell.com
@software: Pycharm
@file: cartesian_list.py
@time: 2019/11/19 17:00
@desc:
'''
from typing import Optional


def cartesian_out(size, color) -> Optional[list]:

    if isinstance(size, list) and isinstance(color, list):
        return [(x, y) for x in size for y in color]


if __name__ == '__main__':
    SIZES = ['170', '175', '180']
    COLORS = ['blue', 'red']
    result = cartesian_out(SIZES, COLORS)
    print(result)
