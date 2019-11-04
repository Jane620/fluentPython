# -*- coding:utf-8 -*-
# everything need test
import pytest
from src.chapter1.poker import Pokers


@pytest.fixture
def poker():
    return Pokers()


def test_len(poker):
    assert len(poker) == 52


def test_first_card(poker):
    card_1 = poker[0]
    assert card_1 == ("2","Spades")

def test_last_card(poker):
    card_last = poker[-1]
    assert card_last == ('A', 'hearts')

