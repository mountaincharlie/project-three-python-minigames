""" Project 3 - Python Minigames """

# imports (modules and other needed py libraries)
from pprint import pprint
import importlib as il
from game_engine import leaderboards as lb


# defining menu dictionary (contains names of game/leaderboard modules)
menu_dict = {
    '1': 'play_minesweeper',
    '2': 'play_hangman',
    '3': 'play_rock_paper_scissors',
    '4': 'view_leaderboards'
}


# creating the Player class
class Player:
    """ Creates an instance of Player """
    def __init__(self, username, score, user_quit, game_choice):
        self.username = username
        self.score = score
        self.user_quit = user_quit
        self.game_choice = game_choice

    # function for updating the leaderboard after a game is complete
    def update_leaderboard(self):
        """
        """

        # getting the worksheet
        print(f"\nUpdating the {self.game_choice} leaderboard ...\n")
        leaderboard = lb.SHEET.worksheet(self.game_choice)
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
        print(f"You've been added to the {self.game_choice} leaderboard at {rank} place.\n(You can view the Leaderboards module from the Main Menu)\n")

    # property decorator for quit_status getter/setter methods
    @property
    def quit_status(self):
        return self.user_quit

    @quit_status.setter
    def quit_status(self, value):
        self.user_quit = value

    # property decorator for game_choice getter/setter methods
    @property
    def user_game_choice(self):
        return self.game_choice

    @user_game_choice.setter
    def user_game_choice(self, value):
        self.game_choice = value


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
        lb_sheet_names = []
        for value in menu_dict_values:
            sheet_name = value[5:]
            lb_sheet_names.append(sheet_name)
        usernames_dict = lb.unique_usernames(lb_sheet_names[:-1])
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
    current_user = Player(username, 0, None, None)

    # while loop to prompt input from menu_dict options until 'quit'
    while current_user.quit_status != 'quit':
        # while loop to catch value errors and prompt input until 'quit'
        while True:
            try:
                print('Main Menu:')
                pprint(menu_dict)
                menu_choice = input("\nEnter a number to select an option (or 'quit' to exit):\n")
                if menu_choice == 'quit':
                    current_user.quit_status = menu_choice
                    break
                elif menu_choice in menu_dict:
                    menu_choice = menu_dict[menu_choice]
                    print(f'\nOpening {menu_choice} ... \n')
                    # updating user's game_choice
                    current_user.user_game_choice = menu_choice[5:]
                    # building the string 'package_name.module_name'
                    module_str = 'game_engine.' + menu_choice[5:]
                    # importing the module from the string with importlib
                    module = il.import_module(module_str)
                    # calling the chosen module with the current_user instance of Player
                    module.main(current_user)
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid entry. Enter a number from the options below.\n Or 'quit' to exit")

    # exit thank you message
    print(f'Thank you {username} for playing Python Minigames!')


# calling the main() only when run.py is called not imported
if __name__ == "__main__":
    main()
