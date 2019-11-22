# -*- coding:utf-8 -*-
import bisect
import sys
import random


HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:2d}'


def bisect_insert(bisect_fn):
    """
    bisect method return the needle postion
    :param bisect_fn:
    :return:
    """
    for needle in reversed(NEEDLES):
        postion = bisect_fn(HAYSTACK, needle)
        offset = postion * '  |'
        print(ROW_FMT.format(needle, postion, offset))


def bisect_insort():
    SIZE= 7
    random.seed(1729) # give the random seed than let each random get the same value
    my_list = []
    for i in range(SIZE):
        new_item = random.randrange(SIZE*2)
        bisect.insort(my_list, new_item)
        # print(f"{new_item} -> {my_list}")
    return my_list


def bisect_score(score, breakpoint=[60, 70, 80, 90], grades="FDCBA"):

    i = bisect.bisect(breakpoint, score)
    return grades[i]


if __name__ == '__main__':
    if sys.argv[-1] == "left":
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print(f"Demo: {bisect_fn.__name__}")
    print("haystack ->", " ".join("%2d" % i for i in HAYSTACK))
    bisect_insert(bisect_fn)

    print("--------------------")
    bisect_insort()
