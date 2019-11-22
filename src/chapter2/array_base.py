# -*- coding:utf-8 -*-
from array import array
from random import random


FLOATS = array('d', (random() for i in range(10**7)))


def arrary_to_file(filename):

    with open(filename, 'wb') as f:
        FLOATS.tofile(f)


def array_from_file(filename, arrays, precision):

    with open(filename, 'rb') as f:
        arrays.fromfile(f, precision)
    return arrays
