# -*- coding:utf-8 -*-
import pytest
from src.chapter2.bisect_sort import bisect_score, bisect_insort


@pytest.mark.parametrize('score, expect',
                         [
                             (59, "F"),
                             (66, "D"),
                             (78, "C"),
                             (99, "A")
                         ])
def test_bisect_e(score, expect):
    grade = bisect_score(score)
    assert grade == expect


def test_insort():
    result_list = bisect_insort()
    assert result_list == [0, 2, 6, 7, 8, 10, 10]
