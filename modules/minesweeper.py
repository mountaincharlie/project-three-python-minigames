""" Minesweeper minigame module for Python Minigames """

# imports
import numpy as np
from pprint import pprint


def welcome_msg():
    """ initial user welcome message """
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

    # count_nonzero function to find occurances of 'B' in the 2d array
    bombs_around = np.count_nonzero(around == 'B')

    # assigning the (i, j) coor with bomb number
    hidden_grid[i, j] = bombs_around


# function to loop through each coordinate using enumerate instead of range(len()) and call the insert_nums()
def examine_coors(hidden_grid):
    """
    Takes the hidden_grid 2d array.
    Loops through each coordinate, using enumerate instead of range(len()),
    and calls the insert_nums() function.
    Returns the updated hidden_grid.
    """
    for i, row in enumerate(hidden_grid):
        for j, col in enumerate(row):
            if col != 'B':
                # calling the function to assign the numbers
                insert_nums(i, j, hidden_grid)

    return hidden_grid


# function for displaying the display_grid to the user nicely
def print_grid(grid):
    """
    Takes the display_grid 2d array.
    Inserts a row of numbers to be printed first (when i==0).
    Prints it out by row with the row number then then the row.
    """
    nums = [i for i in range(len(grid[0]))]
    grid = np.insert(grid, 0, nums, axis=0)
    for i, row in enumerate(grid):
        m = i-1
        if i == 0:
            # using str() list slicing to take only
            # the characters within the [ ]
            # CREDIT - "https://www.geeksforgeeks.org/python-remove-square-brackets-from-list/"
            row = str(row)[1:-1]
            print('   ', row)
        else:
            for j, col in enumerate(row):
                grid[i, j] = '#'
                row = str(grid[i])[1:-1]
            print(f"'{m}'", row)


# function for validating user's input for coordinates
def validate_row_col(num, axis):
    """
    Takes the number of ROWS or COLS and 'row' or 'column'.
    Keeps asking the user for a row or column number,
    until a valid entry is given.
    Returns the valid coordinate.
    """

    while True:
        try:
            coor = int(input(f"Enter {axis} number:\n"))
            if coor not in range(num):
                raise ValueError
            else:
                break
        except ValueError:
            print(f"Invalid {axis}")

    return coor


'''
-user interaction
-classes
-access from run.py
'''


def main():
    """ main game function calls """
    # welcome message
    welcome_msg()

    # generating the hidden_grid
    hidden_grid = generate_grid()
    # print('initial grid:\n', hidden_grid)

    # generating the random and unique bomb coors
    bomb_coors = gen_bomb_coors()
    # print('bomb coors', bomb_coors)

    # inserting the bombs into the grid
    hidden_grid = insert_bombs(bomb_coors, hidden_grid)
    # print('with bombs:\n', hidden_grid)

    # looping through the other coors and inserting their number
    print('completed hidden_grid:\n', examine_coors(hidden_grid))

    # generating the display grid
    display_grid = generate_grid()

    # printing the display_grid
    # print(f'\n{COLS} by {ROWS} Minesweeper grid:\n')
    print_grid(display_grid)

    # user interaction (make function)
    user_row = validate_row_col(ROWS, 'row')
    user_col = validate_row_col(COLS, 'column')

    user_coors = (user_row, user_col)
    print(f"Your chosen coordinate is: {user_coors}")

    flag_or_reveal = input("Enter 'f' to place a flag or anything else to reveal a location:\n")
    if flag_or_reveal.lower() == 'f':
        print(flag_or_reveal)
    else:
        # calling function to check the coors in the hidden_grid
        coor_reveal = hidden_grid[user_coors]
        if coor_reveal == 'B':
            print("You hit a mine!\nGAME OVER!")
        else:
            print("You avoided the mines! This location contains: ", coor_reveal)


# make into a function for user input (they choose easy/med/hard)?
ROWS = 9
COLS = 9
NUM_BOMBS = 10

# calling the game
main()
