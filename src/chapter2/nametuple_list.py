# -*- coding:utf-8 -*-
from collections import namedtuple


class Location:
    """
        module main 我是模块说明
    """
    def __init__(self):
        """
            function main 我是函数说明
        """
        self.name = "HZ"
        self.country = "ZJ"
        self.popu = 100
        self.cord = ('100', '200')


def exec_city_info():
    """
        定义nametuple时需要按照一串字符的形式送入, 元组的构造函数只支持一种单一的可迭代对象
    """
    loca = Location()
    City = namedtuple("City", "name country population cordinations")
    return City(loca.name, loca.country, loca.popu, loca.cord)
