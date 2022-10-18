import pytest

from .solution1 import create_spiral

@pytest.fixture
def new_create_spiral():
    return create_spiral

def test_create_spiral_N_is_0(new_create_spiral):
    assert new_create_spiral(0) == []

def test_create_spiral_N_is_1(new_create_spiral):
    assert new_create_spiral(1) == [[1]]

def test_create_spiral_N_is_2(new_create_spiral):
    assert new_create_spiral(2) == [[1, 2],
                                    [4, 3]]

def test_create_spiral_N_is_3(new_create_spiral):
    assert new_create_spiral(3) == [[1, 2, 3],
                                    [8, 9, 4],
                                    [7, 6, 5]]

def test_create_spiral_N_is_4(new_create_spiral):
    assert new_create_spiral(4) == [[ 1,  2,  3, 4],
                                    [12, 13, 14, 5],
                                    [11, 16, 15, 6],
                                    [10,  9,  8, 7]]

def test_create_spiral_N_is_5(new_create_spiral):
    assert new_create_spiral(5) == [[ 1,  2,  3,  4, 5],
                                    [16, 17, 18, 19, 6],
                                    [15, 24, 25, 20, 7],
                                    [14, 23, 22, 21, 8],
                                    [13, 12, 11, 10, 9]]