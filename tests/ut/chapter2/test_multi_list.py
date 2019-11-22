# -*- coding:utf-8 -*-
from src.chapter2.multi_list import multi_same_list, multi_diff_list


def test_multi_same(nothing_list):
    """

    :param nothing_list: 
    :return: 
    """
    result = multi_same_list(nothing_list)
    assert result[1][2] == 0
    assert result[0][2] == 0


def test_multi_diff(nothing_list):
    """

    :param nothing_list:
    :return:
    """
    result = multi_diff_list(nothing_list)
    assert result[1][2] == 0
    assert result[0][2] == "_"
