""" Minesweeper minigame module for Python Minigames """

# imports
import numpy as np


# welcome message function
def welcome_msg():
    print('Welcome to the Minesweeper minigame!')


'''
-create the 2d array hidden_grid
-break into functions each process to build and setup the array
(generate, add bombs, add numbers to other coors)
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

# looping through hidden_grid and inserting the correct numbers
safe_coors = []
'''
for row in range(len(hidden_grid)):
    for col in range(len(hidden_grid[row])):
        if hidden_grid[row, col] == 'B':
            b_coors.append([row, col])
'''
# using enumerate instead of range(len())
for i, row in enumerate(hidden_grid):
    for j, col in enumerate(hidden_grid[i]):
        if col != 'B':
            # safe_coors.append([i, j])
            hidden_grid[i, j] = 1

print('with safe coors numbered:\n', hidden_grid)
# print(f'There are {len(safe_coors)} safe coors and they are: {safe_coors}')
