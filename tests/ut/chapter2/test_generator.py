# -*- coding:utf-8 -*-
import pytest
from src.chapter2.generator_list import generator_list, file_path_output


@pytest.mark.parametrize('sizes', ['S', 'M', 'L'])
def test_generator(sizes):
    result = generator_list(sizes)
    i = 0  # loop test generator
    for size in result:
        assert sizes[i] == size
        i += 1


@pytest.mark.parametrize('fullfile', ['/home/tester/local/x.py'])
def test_file_path_filename(fullfile):
    path, filename = file_path_output(fullfile)
    assert path.endswith('local')   # /home/tester/local
    assert filename.endswith('py')  # x.py
