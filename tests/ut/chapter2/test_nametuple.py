# -*- coding:utf-8 -*-
from src.chapter2.nametuple_list import exec_city_info


def test_city():
    """
        function main 我是函数说明
    """
    detail = exec_city_info()
    assert detail.name == "HZ"
