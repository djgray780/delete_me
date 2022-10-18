from typing import Counter, List

class BaseGrid:
    i: int = 0
    j: int = 0
    v: int = 0
    row_lb: int = -1
    col_lb: int = -1
    def __init__(self, N: int):
        self.N = N
        self.row_ub = N
        self.col_ub = N
        self.grid: List[List[None]] = [ [None]*N for _ in range(N) ]
        self.values: List[List[None]] = [i + 1 for i in range(N**2)]
        self.max_values_index: int = len(self.values) - 1

    def set_grid_value(self):
        return self.values[self.v + 1]

    def can_continue_rightward(self) -> bool:
        return self.j + 1 < self.col_ub and self.grid[self.i][self.j + 1] == None    
            
    def can_continue_downward(self) -> bool:
        return self.i + 1 < self.row_ub and self.grid[self.i + 1][self.j] == None

    def can_continue_leftward(self) -> bool:
        return self.j - 1 > self.col_lb and self.grid[self.i][self.j - 1] == None

    def can_continue_upward(self) -> bool:
        return self.i - 1 > self.col_lb and self.grid[self.i - 1][self.j] == None

    def advance_rightward(self):
        self.grid[self.i][self.j + 1] = self.set_grid_value()
        self.j += 1
        self.v += 1      

    def advance_leftward(self):
        self.grid[self.i][self.j - 1] = self.set_grid_value()
        self.j -= 1
        self.v += 1

    def advance_downward(self):
        self.grid[self.i + 1][self.j] = self.set_grid_value()
        self.i += 1
        self.v += 1        

    def advance_upward(self):
        self.grid[self.i - 1][self.j] = self.set_grid_value()
        self.i -= 1
        self.v += 1


class ClockwiseSpiralGrid(BaseGrid):
    def __init__(self, N: int):
        super(ClockwiseSpiralGrid, self).__init__(N)

    def create_spiral(self) -> List[List[int]]:
        if self.N < 1:
            return []

        self.grid[self.i][self.j] = self.values[self.v]
        while self.v < self.max_values_index:
            while self.can_continue_rightward():
                self.advance_rightward()

            while self.can_continue_downward():
                self.advance_downward()

            while self.can_continue_leftward():
                self.advance_leftward()

            while self.can_continue_upward():
                self.advance_upward()

        return self.grid

class CounterClockwiseSpiralGrid(BaseGrid):
    def __init__(self, N: int):
        super(CounterClockwiseSpiralGrid, self).__init__(N)

    def create_spiral(self) -> List[List[int]]:
        if self.N < 1:
            return []

        self.grid[self.i][self.j] = self.values[self.v]
        while self.v < self.max_values_index:

            while self.can_continue_downward():
                self.advance_downward()

            while self.can_continue_rightward():
                self.advance_rightward()

            while self.can_continue_upward():
                self.advance_upward()

            while self.can_continue_leftward():
                self.advance_leftward()

        return self.grid

def main():
    # Another benefit of this approach is that if we wanted to display output to the user
    # we could create a method to extend the class such as display_spiral() 
    for n in range(0, 6):
        print(f"Printing clockwise spiral with N = {n} ...")
        spiral_grid = ClockwiseSpiralGrid(n).create_spiral()
        if n == 0:
            print(spiral_grid)
        for j in range(n):
            print(spiral_grid[j])
        print("")
        print("") 

        if n == 5:
            print(f"Just for fun here is a counter clockwise grid with N = 5")
            ccw_spiral_grid = CounterClockwiseSpiralGrid(5).create_spiral()
            for j in range(n):
                print(ccw_spiral_grid[j])


if __name__ == '__main__':
    main()