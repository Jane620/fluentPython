# -*- coding:utf-8 -*-
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
