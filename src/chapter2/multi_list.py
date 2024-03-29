# -*- coding:utf-8 -*-


def multi_same_list(origin_list) -> list:
    """
    this object is not direct to the same address
    :param origin_list:
    :return:
    """
    result = [origin_list * 3] * 3
    result[1][2] = 0
    return result


def multi_diff_list(origin_list) -> list:
    """
    this object is not direct to the diff address
    so its good to change the index value
    why: because each list was created in the different loop
    it looks like this:
        for i in range(3):
            row = origin_list * 3
            result.append(row)
    :param origin_list:
    :return:
    """
    result = [origin_list * 3 for i in range(3)]
    result[1][2] = 0
    return result
