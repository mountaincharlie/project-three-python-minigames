""" Project 3 - Python Minigames """

# imports (modules and other needed py libraries)
from pprint import pprint
import importlib as il
# from game_engine import minesweeper
# from game_engine import hangman
# from game_engine import rock_paper_scissors
from game_engine import leaderboards as lb


# defining menu dictionary (contains names of game/leaderboard modules)
menu_dict = {
    '1': 'minesweeper',
    '2': 'hangman',
    '3': 'rock_paper_scissors',
    '4': 'leaderboards'
}


# creating the Player class
class Player:
    """ Creates an instance of Player """
    def __init__(self, username, score, user_quit):
        self.username = username
        self.score = score
        self.user_quit = user_quit

    # REMOVE when not needed for testing
    def player_info(self):
        print(f"The user is called: {self.username}, has a current score of: {self.score} and their quit status is: {self.user_quit}")

    # function for updating the leaderboard after a game is complete
    def update_leaderboard(self, sheet):
        """
        """

        # getting the worksheet
        print(f"Updating the {sheet} leaderboard ...")
        leaderboard = lb.SHEET.worksheet(sheet)
        # getting score values to compare user's score too
        score_list = leaderboard.col_values(3)
        # finding the row number to insert the user's data
        insert_at_row = lb.row_to_insert_at(score_list, self.score)
        # calculate the user's rank
        rank = lb.rank_generator((insert_at_row - 1))
        # generating the user's list of data
        user_list = [rank, self.username, self.score]

        # inserting the data to the row refeshing the rank column
        leaderboard.insert_row(user_list, insert_at_row)
        lb.rank_refresh(leaderboard)
        print(f"You've been added to the {sheet} leaderboard at {rank} place.\n(You can view the Leaderboards module from the Games Menu)")

    # property decorator for getter/setter methods
    @property
    def quit_status(self):
        return self.user_quit

    @quit_status.setter
    def quit_status(self, value):
        self.user_quit = value


# wrapping the run.py code in a main() function called at the bottom
def main():
    # initial welcome message
    print("Welcome to Python Minigames!\n\nLet's start by setting your username.")
    # username selection loop (occurs once per load of program)
    username_choice = input("Enter 'y' to reuse a previous username, or anything to choose a new name:\n")

    # retrieving the list of usernames from the leaderboards worksheets
    if username_choice.lower() == 'y':
        print('\nFinding previous usernames from the Leaderboards...')
        # unpacking the values from manu_dict with * operator
        menu_dict_values = [*menu_dict.values()]
        usernames_dict = lb.unique_usernames(menu_dict_values[:-1])
        while True:
            try:
                print('\nPrevious usernames:')
                pprint(usernames_dict)
                prev_user = int(input("\nPlease enter the number for a previous username:\n"))
                if prev_user in usernames_dict:
                    username = usernames_dict[prev_user]
                    break
                else:
                    raise ValueError
            except ValueError:
                print('\nInvalid entry. Enter a number from the options below.')

    # while loop for requesting a valid username from the user
    else:
        while True:
            try:
                username = input("Enter a username (without spaces & less than 15 characters):\n")
                if (len(username) > 15) or (' ' in username):
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Invalid username")

    print(f"\nWelcome to Python Minigames {username}!\n")

    # creating the current user's instance of the Player class
    current_user = Player(username, 0, None)

    # while loop to prompt input from menu_dict options until 'quit'
    while current_user.quit_status != 'quit':
        # while loop to catch value errors and prompt input until 'quit'
        while True:
            try:
                print('Games Menu:')
                pprint(menu_dict)
                menu_choice = input("\nEnter a number to select an option (or 'quit' to exit):\n")
                if menu_choice == 'quit':
                    current_user.quit_status = menu_choice
                    break
                elif menu_choice in menu_dict:
                    menu_choice = menu_dict[menu_choice]
                    print(f'\nOpening {menu_choice} ... \n')
                    # building the string 'package_name.module_name'
                    module_str = 'game_engine.' + menu_choice
                    # importing the module from the string with importlib
                    module = il.import_module(module_str)
                    # calling the chosen module with the current_user instance of Player
                    module.main(current_user)
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid entry. Enter a number from the options below.\n Or 'quit' to exit")

        # feedback for choice being applied
        # print(f'\nSuccessfully applying: {menu_choice}\n')

    # exit thank you message
    print(f'Thank you {username} for playing Python Minigames!')


# calling the main() only when run.py is called not imported
if __name__ == "__main__":
    main()
