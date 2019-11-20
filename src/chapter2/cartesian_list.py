# -*- coding:utf-8 -*-
from typing import Optional


# 笛卡尔积
def cartesian_out(size, color) -> Optional[list]:

    if isinstance(size, list) and isinstance(color, list):
        return [(x, y) for x in size for y in color]

