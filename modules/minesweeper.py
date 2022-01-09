""" Minesweeper minigame module for Python Minigames """

# imports
import numpy as np


# welcome message function
def welcome_msg():
    print('Welcome to the Minesweeper minigame!')


def generate_grid():
    """
    Uses the number of ROWS and COLS to generatea 2d array of
    zeroes with type String.
    Returns the grid.
    """
    grid = np.zeros((ROWS, COLS), dtype=str)

    return grid


# func with while loop to generate enough unique, random coors
def gen_bomb_coors():
    """
    Uses the number of bombs, NUM_BOMBS as a condition for the
    while loop which generates random coordinates with ROWS
    and COLS and inserts them in the bomb_coors set, to
    prevent duplicates.
    Returns the set of coordinates.
    """
    coors = set()
    while len(coors) < NUM_BOMBS:

        bomb_rows = np.random.randint(ROWS)
        bomb_cols = np.random.randint(COLS)

        coor = (bomb_rows, bomb_cols)
        coors.add(coor)

    return coors


# function to insert a bomb 'B' at each coor in hidden_grid
def insert_bombs(coors, hidden_grid):
    """
    Takes the set of bomb coordinates and the hidden_grid
    2d array.
    For each of the coordinates, it inserts a bomb,
    represented with a 'B'.
    Returns the updated hidden_grid.
    """
    for coor in coors:
        hidden_grid[coor] = 'B'

    return hidden_grid


# function to loop through each coordinate using enumerate instead of range(len()) and call the insert_nums()
def examine_coors(hidden_grid):
    """
    Takes the hidden_grid 2d array.
    Loops through each coordinate, using enumerate instead of range(len()),
    and calls the insert_nums() function.
    Returns the updated hidden_grid. 
    """
    for i, row in enumerate(hidden_grid):
        for j, col in enumerate(hidden_grid[i]):
            if col != 'B':
                # calling the function to assign the numbers
                insert_nums(i, j, hidden_grid)

    return hidden_grid


def insert_nums(i, j, hidden_grid):
    """
    Called inside the examine_coors() function's for loop.
    Takes the coordinates of a point in hidden_grid and the 2d array
    itself.
    Creates a 2d array of the point and the coordinates around it, using
    index slicing and max() inorder to prevent including negative
    indexes which would access the list from the opposite end.
    """

    # CREDIT - finding matrix of surrounding coors from MSeifert's solution on stackoverflow "https://stackoverflow.com/questions/36964875/sum-of-8-neighbors-in-2d-array/37026344#37026344"
    around = hidden_grid[max(0, i-1): i+2, max(0, j-1): j+2]
    # print(around)
    # count_nonzero function to find occurances of 'B' in the 2d array
    bombs_around = np.count_nonzero(around == 'B')
    # assigning the (i, j) coor with bomb number
    hidden_grid[i, j] = bombs_around


'''
-break code into functions for setting up hidden_grid
(generate, add bombs, add numbers to other coors)
-create display_grid
-user interaction
-classes
-access from run.py
'''
# make into a function for user input (they choose easy/med/hard)
ROWS = 7
COLS = 9
NUM_BOMBS = 6

# generating the hidden_grid
hidden_grid = generate_grid()
print('initial grid:\n', hidden_grid)

# generating the random and unique bomb coors
bomb_coors = gen_bomb_coors()
print('bomb coors', bomb_coors)

# inserting the bombs into the grid
print('with bombs:\n', insert_bombs(bomb_coors, hidden_grid))

# looping through the other coors and inserting their number
print('with bomb check number:\n', examine_coors(hidden_grid))
