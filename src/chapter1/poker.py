# -*- coding:utf-8 -*-
'''
@author: jwang
@license: (C) Copyright 2018-2019, Nokia Sbell Tech Corporation Limited.
@contact: jianfeng.2.wang@nokia-sbell.com
@software: Pycharm
@file: poker.py
@time: 2019/10/16 10:08
@desc:
'''
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class Pokers:

    ranks = [str(x) for x in range(2, 11)] + list('JQKA')
    suits = 'Spades diamonds clubs hearts'.split()

    def __init__(self):
        self._card = [Card(rank, suit) for rank in self.ranks
                      for suit in self.suits]

    def __len__(self):
        return len(self._card)

    def __getitem__(self, position):
        return self._card[position]
