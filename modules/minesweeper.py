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

# 
