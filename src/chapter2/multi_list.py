# -*- coding:utf-8 -*-


def multi_same_list(origin_list):
    """
    this object is not direct to the same address
    :param origin_list:
    :return:
    """
    result = [origin_list * 3] * 3
    result[1][2] = 0
    return result


def multi_diff_list(origin_list):
    """
    this object is not direct to the diff address
    so its good to change the index value
    :param origin_list:
    :return:
    """
    result = [origin_list * 3 for i in range(3)]
    result[1][2] = 0
    return result
