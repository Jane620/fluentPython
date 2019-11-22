# -*- coding:utf-8 -*-
import os
from array import array
from src.chapter2.array_base import arrary_to_file, array_from_file, FLOATS



FILENAME = os.path.abspath(os.path.join(os.getcwd(), r"..\..\..\static\floats.bin"))


def test_array():
    read_array = array('d')
    arrary_to_file(FILENAME)
    read_array = array_from_file(FILENAME, read_array, 10**7)
    assert FLOATS[-1] == read_array[-1]
