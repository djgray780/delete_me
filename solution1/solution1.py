from typing import List

def create_spiral(N: int) -> List[List[int]]:
    if N < 1:
        return []
    # row/col lower and upper bounds
    col_ub = N 
    row_ub = N 
    col_lb: int = -1
    row_lb: int = -1
    # Indicies for grid (i,j) and values (v) 
    v: int = 0
    i: int = 0
    j: int  = 0
    values = [i+1 for i in range(N**2)]
    grid = [[None]*N for _ in range(N)]
    # Seed initial value
    grid[0][0] = values[v]
    # Perform the algorithm until all the values of v have been placed
    # In the grid.
    while v < len(values) - 1:
        # While able to move rightward, add element to grid
        while j + 1 < col_ub and grid[i][j + 1] == None:
            grid[i][j + 1] = values[v + 1]
            j += 1
            v += 1

        # While able to move southward, add element to grid
        while i + 1 < row_ub and grid[i + 1][j] == None:
            grid[i + 1][j] = values[v + 1]
            i += 1
            v += 1

        # While abole to move westward, add element to grid
        while j - 1 > col_lb and grid[i][j - 1] == None:
            grid[i][j - 1] = values[v + 1]
            j -= 1
            v += 1

        # While able to move northward, add element to grid
        while i - 1 > row_lb  and grid[i - 1][j] == None:
            grid[i - 1][j] = values[v + 1]
            i -= 1
            v += 1
            
    return grid

def main():
    for n in range(0, 6):
        print(f"Printing spiral with N = {n} ...")
        if n == 0:
            print(create_spiral(n))
        
        for j in range(n):
            print(create_spiral(n)[j])
        print("")
        print("")
    
if __name__ == "__main__":
    main()  

