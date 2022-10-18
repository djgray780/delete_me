# Introduction

The problem asks to create a function that takes in an integer value greater than 1 and returns a two dimensional array such that the entries create a clockwise spiral. I felt there given the time available there were two approaches to developing the same solution. Given that the OA was sent on Friday I could not clarify the exact requirements in time, so I have submitted two solutions that I detail below.

The first solution, `solution1.py`, meets the requirements as specified: a single function that passes the given test cases and some extra that I have added. However, the internal function logic is not easily reached which makes it hard to confidently test the function. A single function approach also does not scale well. If the stakeholders came back and requested that we do a counter clockwise spiral then large chunks of the code would need to be duplicated. 

I address some of the short comings in `solution1.py` in `solution2.py` by building a `BaseGrid` class that enables testing modular function logic. This approach provides greater flexibility and code reusability, and I demonstrate this by creating two subclasses called `ClockwiseSpiralGrid` and `CounterClockwiseSpiralGrid`. Each subclass implements `create_spiral()` but the `CounterClockwiseSpiralGrid` demonstrates that new functionality can be easily achieved with the same code without additional bloat.

But most importantly, it was just a lot of fun to build it out both ways to demonstrate two views of the same problem.

## Set Up

To get started, make sure that you have Python `V3.8.xx` installed on your system and unzip the files into a top level directory of your choice, for example, `dennis-oa`. Execute the following commands to create a virtual environment in `dennis-oa`. 
```python
python3 -m venv venv
```

To activate the virtual environment on your system run the following command after the colon:
```
Unix/MacOS: . venv/bin/activate
Windows: c:\>c:\Python38\python -m venv c:\path\to\myenv
```

Install dependencies into the virtual environment: 
```
pip install -r requirements.txt
```

To run the tests simply `cd` into the solution folder of your choice and run the following command with the verbose flag to see test names:
```
pytest -v  
```

Alternatively, each solution contains a `main()` file that prints the results of the test cases to `stout`. To run these, `cd` into the solution folder and run:
```python
python3 <solution>.py
```  

## Solution Approach

My solution involves creating an array of values with the input `N` and traversing a grid in four cardinal directions. The pseudo code solution below will run in O(N ** 2) time and use O(N ** 2) memory.  

1. Take the input `N` and create an array of values `V` from `1 ... N` 
2. Create an `N x N` grid `G` to populate with the values from Step 1.
3. Start by seeding `G[0][0]` with `V[0]` 
4. Handle edge case when `N < 1` 
5. Until each value of `V` has been visited do:
	1 While `G[i][j+1]` is empty and in the grid, move eastward and place a value in the cell.
		- If the condition is `False` then we are at an eastern edge and can go south
	2. While `G[i+1][j]` is empty and in the grid, move southward and place a value in the cell
		- If the condition is `False` then we are at a southern edge and can go west.
	3. While `G[i][j-1]` is empty and in the grid, move westward and place a value in the cell.
		- If the condition is False then we are at a western edge and can go north.
	4. While `G[i-1][j]` is empty and in the grid, move northward and place a value in the cell
		= If the condition is False then we are at a northern edge and can revisit Step 1 to move eastward. 
6. When all of 4 is complete, return the newly populated grid. 

# Improvement Opportunities
- The current solutions start in the top-left corner of the grid, but some flexibility could be introduced to allow the user to begin at any of the four corners of the grid.
- Could write doc tests in Python in addition to the unit tests so that users of the code have an additional layer of documentation they can refer to.
- Refactor the test suite so that it is more extensible.
- Refactor the code by packaging it and separating the source code from the test code. 
- Extend the behaviour of the code by requesting an input from the user.  # delete_me
