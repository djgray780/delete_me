import pytest

from .solution2 import BaseGrid, ClockwiseSpiralGrid, CounterClockwiseSpiralGrid

@pytest.fixture
def new_BaseGrid():
    return BaseGrid

@pytest.fixture
def new_ClockwiseSpiralGrid():
    return ClockwiseSpiralGrid

@pytest.fixture
def new_CounterClockwiseSpiralGrid():
    return CounterClockwiseSpiralGrid

def test_valid_BaseGrid(new_BaseGrid):
    grid = new_BaseGrid(3)
    assert grid.row_ub == 3
    assert grid.values == [1,2,3,4,5,6,7,8,9]

def test_can_continue_in_direction_N_is_2(new_ClockwiseSpiralGrid):
    # Set Grid State
    g = new_ClockwiseSpiralGrid(2)
    g.i, g.j = 0, 0
    g.grid[0][0] = 1
    assert g.can_continue_rightward() == True

    # True, update (i,j) and add the value.
    g.i, g.j = 0, 1
    g.grid[0][1] = 2
    assert g.can_continue_rightward() == False
    assert g.can_continue_downward() == True
    g.i, g.j = 1, 1
    g.grid[1][1] = 3
    assert g.can_continue_downward() == False
    assert g.can_continue_leftward() == True
    g.i, g.j = 1, 0
    g.grid[1][0] = 4
    assert g.can_continue_leftward() == False
    # Grid is full, next movement up should be False
    assert g.can_continue_upward() == False 

def test_can_continue_up_N_is_2(new_ClockwiseSpiralGrid):
    # The 2x2 grid captures all essential movements except moving up to be true.
    g = new_ClockwiseSpiralGrid(3)
    g.grid[0][0] = 1
    # Set starting point at bottom left corner.
    g.i, g.j = 2, 0
    assert g.can_continue_upward() == True
    g.i, g.j = 1, 0
    g.grid[1][0] = 8
    assert g.can_continue_upward() == False
    # The center element should be null so we can move rightward.
    assert g.can_continue_rightward() == True


def test_advance_in_direction(new_ClockwiseSpiralGrid):
    g = new_ClockwiseSpiralGrid(2)
    g.grid[0][0] = 1
    g.advance_rightward()
    assert g.grid[0][1] == 2
    g.advance_downward()
    assert g.grid[1][1] == 3
    g.advance_leftward()
    assert g.grid[1][0] == 4

def test_create_spiral_N_is_0(new_ClockwiseSpiralGrid):
    g = new_ClockwiseSpiralGrid(0)
    assert g.create_spiral() == []

def test_create_spiral_N_is_1(new_ClockwiseSpiralGrid):
    g = new_ClockwiseSpiralGrid(1)
    assert g.create_spiral() == [[1]]

def test_create_spiral_N_is_2(new_ClockwiseSpiralGrid):
    g = new_ClockwiseSpiralGrid(2)
    assert g.create_spiral() == [[1, 2],
                                 [4, 3]]

def test_create_spiral_N_is_3(new_ClockwiseSpiralGrid):
    g = new_ClockwiseSpiralGrid(3)
    assert g.create_spiral() == [[1, 2, 3],
                                 [8, 9, 4],
                                 [7, 6, 5]]

def test_create_spiral_N_is_4(new_ClockwiseSpiralGrid):
    g = new_ClockwiseSpiralGrid(4)
    assert g.create_spiral() == [[1,  2,  3, 4],
                                [12, 13, 14, 5],
                                [11, 16, 15, 6],
                                [10,  9,  8, 7]]

def test_create_spiral_N_is_5(new_ClockwiseSpiralGrid):
    g = new_ClockwiseSpiralGrid(5)
    assert g.create_spiral() == [[1,  2,  3,  4, 5],
                                [16, 17, 18, 19, 6],
                                [15, 24, 25, 20, 7],
                                [14, 23, 22, 21, 8],
                                [13, 12, 11, 10, 9]]

def test_create_counterclockwise_spiral_N_is_5(new_CounterClockwiseSpiralGrid):
    g = new_CounterClockwiseSpiralGrid(5)
    assert g.create_spiral() == [[1, 16, 15, 14, 13],
                                 [2, 17, 24, 23, 12],
                                 [3, 18, 25, 22, 11],
                                 [4, 19, 20, 21, 10],
                                 [5,  6,  7,  8, 9]]