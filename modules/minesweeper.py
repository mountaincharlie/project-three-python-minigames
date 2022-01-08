""" Minesweeper minigame module for Python Minigames """

# imports
import numpy as np


# welcome message function
def welcome_msg():
    print('Welcome to the Minesweeper minigame!')


# function for checking a coordinates surrounding coordinates for bombs
def insert_nums(i, j):
    """ 
    Takes the coordinates of a point in the 2d array.
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
# gerating a 2d array of zeroes from defined rows and cols
rows = 7
cols = 9
hidden_grid = np.zeros((rows, cols), dtype=str)
print('initial grid:\n', hidden_grid)

# generate a number of random coordinates to insert bombs
num_bombs = 6
bomb_coors = set()

# while loop to generate enough unique, random coors
while len(bomb_coors) < num_bombs:

    bomb_rows = np.random.randint(rows)
    bomb_cols = np.random.randint(cols)

    coor = (bomb_rows, bomb_cols)
    bomb_coors.add(coor)
    # print('coor to add: ', coor)
    # print('current set of coors: ', bomb_coors)

print('bomb coors', bomb_coors)

# inserting a bomb 'B' at each coor in hidden_grid
for coor in bomb_coors:
    hidden_grid[coor] = 'B'

print('with bombs:\n', hidden_grid)

# using enumerate instead of range(len())
for i, row in enumerate(hidden_grid):
    for j, col in enumerate(hidden_grid[i]):
        if col != 'B':
            # calling the function to assign the numbers
            insert_nums(i, j)

print('with bomb check number:\n', hidden_grid)
