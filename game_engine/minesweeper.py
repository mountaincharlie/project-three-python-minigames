""" Minesweeper minigame module for Python Minigames """

# imports
import numpy as np
# to import run.py from parent directory
import sys
sys.path.append('.')
from run import Player


# minesweeper Player subclass
class MinesweeperPlayer(Player):
    """ Creates instance of MinesweeperPlayer """
    def __init__(self, username, score, user_quit, game_choice, coors):
        super().__init__(username, score, user_quit, game_choice)
        self.coors = coors

    @classmethod
    def from_current_user(cls, player_instance, coors):
        return cls(**player_instance.__dict__, coors=coors)


# ----- GRID GENERATING -----


def generate_grid():
    """
    Uses the number of ROWS and COLS to generatea 2d array of
    zeroes with type String.
    Returns the grid.
    """
    grid = np.zeros((ROWS, COLS), dtype=str)

    return grid


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


# ----- PROCESSING USER INPUT -----

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
    Takes the coors, display_grid and hidden_grid.
    Checks if the user has placed their maximum number of
    flags already.
    If not, then it inserts a flag 'F' at the user's coors
    in the display_grid.
    If there is a mine at the coors in the hidden_grid, then
    its replaced with a 'F'
    Returns the grids.
    """
    # count_nonzero finding occurances of 'F' in d_grid
    placed_flags = np.count_nonzero(d_grid == 'F')
    if int(placed_flags) == NUM_MINES:
        print(f"You have placed {NUM_MINES}. Please remove a flag first.")
    else:
        d_grid[coors] = 'F'
        print(f'Flag inserted at {coors}\n')

        if h_grid[coors] == 'M':
            h_grid[coors] = 'F'

    return d_grid, h_grid


def remove_flag(coors, d_grid, h_grid):
    """
    Takes the coors, display_grid and hidden_grid.
    If theres a flag in hidden_grid it replaces back the
    mine 'M'.
    If theres a flag in display_grid it replaces it with a
    '#', else it tells the user that there isnt a flag
    there to remove.
    Returns the potentially updated d_grid and h_grid
    """
    if h_grid[coors] == 'F':
        h_grid[coors] = 'M'

    if d_grid[coors] == 'F':
        d_grid[coors] = '#'
        print(f"Flag removed at {coors}")
    else:
        print(f"There is no flag to remove at {coors}")

    return d_grid, h_grid


def flag_check(coors, d_grid, h_grid):
    """
    Takes the coors, display_grid and hidden_grid.
    Calls function to insert or to remove a flag
    depending on the user's input.
    Returns the grids.
    """
    insert_or_remove = input("Hit ENTER to insert a flag or enter 'r' to remove a flag:\n")

    if insert_or_remove.lower() == 'r':
        d_grid, h_grid = remove_flag(coors, d_grid, h_grid)
    else:
        d_grid, h_grid = insert_flag(coors, d_grid, h_grid)

    return d_grid, h_grid


def mine_count(user, h_grid):
    """
    Takes the hidden_grid.
    Counts the occurances of 'M' in the grid.
    If there are no mines remaining (they're all flagged)
    then the game_won() function is called.
    Returns the return of game_won() (which is 'quit')
    """
    mines_remaining = np.count_nonzero(h_grid == 'M')

    if int(mines_remaining) == 0:
        win_message = 'reveals'
        return user.game_won(win_message)


def coor_reveal(user, user_coors, h_grid, d_grid):
    """
    Takes minesweeper_user, minesweeper_user.coors, hidden_grid, display_grid.
    Checks the contents of the coordinate from in hidden_grid.
    If the coordinate contains a mine, the game is over, otherwise, a
    message to the user is displayed and the contents are written into the
    coordinates in display_grid.
    """
    # finding the 'M' or number at user_coors in hidden_grid
    coor_content = h_grid[user_coors]

    # adds one to the user's score (tracks number of reveals)
    user.score += 1

    if coor_content == 'M':
        lose_message = f'there was a mine at {user_coors}'
        return user.game_lost(lose_message)
    else:
        print(f"You avoided the mines!\n'{coor_content}' has been revealed at {user_coors}\n")
        # inserting the revealed number and displaying the grid
        d_grid[user_coors] = coor_content
        print_grid(d_grid)


# function for checking flag or reveal
def flag_or_reveal(user, display_grid, hidden_grid):
    """  """
    user_choice = input("Hit ENTER to reveal the location or enter 'f' to insert/remove a flag:\n")

    user_coors = user.coors

    if user_choice.lower() == 'f':
        # call flag check for deciding insert/remove flag
        display_grid, hidden_grid = flag_check(user_coors, display_grid, hidden_grid)

        # displaying display_grid
        print_grid(display_grid)

        # check number of mines
        game_complete_check = mine_count(user, hidden_grid)
        if game_complete_check == 'quit':
            return game_complete_check

        # REMOVE AFTER TESTING
        # print('updated hidden_grid:\n', hidden_grid)
    else:
        # calling function to check the content of the coor in the hidden_grid
        return coor_reveal(user, user_coors, hidden_grid, display_grid)


def main(user):
    """ main game function calls """

    # instance of MinesweeperPlayer SubClass (no current coors value)
    minesweeper_user = MinesweeperPlayer.from_current_user(user, None)

    # overall while loop for starting the game
    while minesweeper_user.quit_status != 'quit':
        username = minesweeper_user.username
        # resetting the user's score everytime they play again
        minesweeper_user.score = 0

        # welcome message
        # play_or_quit = welcome_msg(minesweeper_user)
        play_or_quit = minesweeper_user.welcome_msg()
        if play_or_quit == 'quit':
            break
        print('\nBuilding the minesweeper grid ...\n')

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
        # print('completed hidden_grid:\n', hidden_grid)
        examine_coors(hidden_grid)

        # generating the display grid
        display_grid = generate_grid()

        # printing the basic instructions and display_grid
        print(f'Your grid is displayed below!\n\nChoose coordinates to either reveal or\nto place/remove a flag at.\nAttempt to flag each of the {NUM_MINES} mines\nusing the fewest number of reveals.\n(Remember you have only {NUM_MINES} flags)\n')

        print_grid(display_grid)

        # user selection for row and column until 'quit'
        while True:
            user_row = validate_row_col(ROWS, 'ROW')
            user_col = validate_row_col(COLS, 'COLUMN')
            # user_coors = (user_row, user_col)
            minesweeper_user.coors = (user_row, user_col)
            print(f"\nYour chosen coordinate is: {minesweeper_user.coors}\n")

            # checks if user wants to insert a flag or reveal location
            f_or_r = flag_or_reveal(minesweeper_user, display_grid, hidden_grid)
            if f_or_r == 'quit':
                # minesweeper_user.quit_status = f_or_r
                break
            cont_or_quit = input("\nHit ENTER to continue or 'quit' to restart the game:\n")
            if cont_or_quit.lower() == 'quit':
                # minesweeper_user.quit_status = cont_or_quit
                break

    # game exit message
    print(f'\nThank you {username} for playing the Minesweeper minigame!\n')


# game constants
ROWS = 8
COLS = 8
NUM_MINES = 10

# calling the game (should be done in run.py)
# main()
