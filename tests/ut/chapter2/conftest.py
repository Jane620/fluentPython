# -*- coding:utf-8 -*-
import pytest


@pytest.fixture
def basic_list():
    return ["a", "b", "c", "d"]


@pytest.fixture()
def nothing_list():
    return ["_"]
