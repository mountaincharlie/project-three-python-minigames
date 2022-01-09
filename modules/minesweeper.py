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
def gen_mine_coors():
    """
    Uses the number of mines, NUM_MINES as a condition for the
    while loop which generates random coordinates with ROWS
    and COLS and inserts them in the mine_coors set, to
    prevent duplicates.
    Returns the set of coordinates.
    """
    coors = set()
    while len(coors) < NUM_MINES:

        mine_rows = np.random.randint(ROWS)
        mine_cols = np.random.randint(COLS)

        coor = (mine_rows, mine_cols)
        coors.add(coor)

    return coors


# function to insert a mine 'M' at each coor in hidden_grid
def insert_mines(coors, hidden_grid):
    """
    Takes the set of mine coordinates and the hidden_grid
    2d array.
    For each of the coordinates, it inserts a mine,
    represented with a 'M'.
    Returns the updated hidden_grid.
    """
    for coor in coors:
        hidden_grid[coor] = 'M'

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

    # count_nonzero function to find occurances of 'M' in the 2d array
    mines_around = np.count_nonzero(around == 'M')

    # assigning the (i, j) coor with mine number
    hidden_grid[i, j] = mines_around


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
            if col != 'M':
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
                if grid[i, j] == '':
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


def insert_flag(coors, d_grid, h_grid):
    """
    Inserts a flag 'F' at the user's coors in the display_grid.
    If there is a mine at the coors in the hidden_grid, then
    its replaced with a 'F'
    Returns the grid.
    """
    d_grid[coors] = 'F'

    if h_grid[coors] == 'M':
        h_grid[coors] = 'F'

    return d_grid, h_grid



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

    # generating the random and unique mine coors
    mine_coors = gen_mine_coors()
    # print('mine coors', mine_coors)

    # inserting the mines into the grid
    hidden_grid = insert_mines(mine_coors, hidden_grid)
    # print('with mines:\n', hidden_grid)

    # looping through the other coors and inserting their number
    print('completed hidden_grid:\n', examine_coors(hidden_grid))

    # generating the display grid
    display_grid = generate_grid()

    # printing the display_grid
    # print(f'\n{COLS} by {ROWS} Minesweeper grid:\n')
    print_grid(display_grid)

    # MAKE FUNCTION WITH WHILE LOOP (until 'quit') user selection for row and column
    user_row = validate_row_col(ROWS, 'row')
    user_col = validate_row_col(COLS, 'column')
    user_coors = (user_row, user_col)
    print(f"Your chosen coordinate is: {user_coors}")

    # check if user wants to insert a flag or reveal location
    flag_or_reveal = input("Enter 'f' to place a flag or anything else to reveal a location:\n")

    if flag_or_reveal.lower() == 'f':
        # MAKE FUNCTION
        print(f'Flag inserted at {user_coors}\n')
        # function inserts flag into display_grid
        # and checks if there is a mine in hidden_grid
        display_grid, hidden_grid = insert_flag(user_coors, display_grid, hidden_grid)
        print_grid(display_grid)
        print('updated hidden_grid:\n', hidden_grid)
    else:
        # MAKE FUNCTION
        # calling function to check the coors in the hidden_grid
        coor_reveal = hidden_grid[user_coors]
        if coor_reveal == 'M':
            print(f"You hit a mine at {user_coors}!\nGAME OVER")
        else:
            print(f"You avoided the mines!\n'{coor_reveal}' has been inserted at {user_coors}")
            display_grid[user_coors] = coor_reveal
            print_grid(display_grid)


# make into a function for user input (they choose easy/med/hard)?
ROWS = 9
COLS = 9
NUM_MINES = 10

# calling the game
main()
