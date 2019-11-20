# -*- coding:utf-8 -*-
from src.chapter2.nametuple_list import exec_city_info, make_city_info


def test_city():
    """
        function main 我是函数说明
    """
    detail = exec_city_info()
    assert detail.name == "HZ"

def test_make():
    """
    nametuple._make(iterator) == nametuple(*iterator)
    :return:
    """
    city_info = ("HZ", "ZJ", 100, (101,200))
    details = make_city_info(city_info)
    assert details.name == "HZ"
