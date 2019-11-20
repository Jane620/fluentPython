# -*- coding:utf-8 -*-
from collections import namedtuple

City = namedtuple("City", "name country population cordinations")


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
        nametuple
    """
    loca = Location()
    return City(loca.name, loca.country, loca.popu, loca.cord)


def make_city_info(info_list: list):

    print(f" fileds : {City._fields}")
    return City._make(info_list)
