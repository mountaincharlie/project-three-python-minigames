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
rows = 9
cols = 9
hidden_grid = np.zeros((rows, cols), dtype=int)
print(hidden_grid)

# generate a number of random coordinates to insert bombs
