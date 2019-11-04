import pytest
from src.chapter1.vector import Vector


@pytest.fixture
def vector():
    def spawn(x, y):
        return Vector(x, y)
    return spawn


def test_vector(vector):
    vector_1 = vector(1, 2)
    vector_2 = vector(2, 3)
    vector_3 = vector(3, 5)
    print(vector_1 + vector_2)
    print(vector_3)
    assert type(vector_1) == Vector
    assert vector_1 + vector_2 == vector_3
