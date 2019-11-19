# -*- coding:utf-8 -*-
'''
@author: jwang
@license: (C) Copyright 2018-2019, Nokia Sbell Tech Corporation Limited.
@contact: jianfeng.2.wang@nokia-sbell.com
@software: Pycharm
@file: test_cartesian.py
@time: 2019/11/19 17:08
@desc:
'''
import pytest
from src.chapter2.cartesian_list import cartesian_out


@pytest.mark.parametrize('sizes', [['170', '175', '180']])
@pytest.mark.parametrize('colors', [['blue', 'red']])
def test_cartesian(sizes, colors):
    result = cartesian_out(sizes, colors)
    assert isinstance(result, list)


@pytest.mark.parametrize('sizes', ['170'])
@pytest.mark.parametrize('colors', [['blue', 'red']])
def test_cartesian_with_str(sizes, colors):
    result = cartesian_out(sizes, colors)
    if result is None:
        assert True
    else:
        assert False
