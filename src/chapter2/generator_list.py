# -*- coding:utf-8 -*-
import os


# 生成器
def generator_list(group: list):
    return tuple(single for single in group)


# 元组拆包实例1
def file_path_output(path: str) -> tuple:
    path, filename = os.path.split(path)
    return path, filename
