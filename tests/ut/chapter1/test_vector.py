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
    vector_4 = vector(2, 4)
    vector_5 = vector(3, 4)
    assert type(vector_1) == Vector
    assert str(vector_1) == "Vector((1, 2))"
    assert vector_1 + vector_2 == vector_3
    assert vector_1 * 2 == vector_4
    assert abs(vector_5) == 5
    assert bool(vector_5) == True
