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

    def update_leaderboard(self):
        """
        Updates the leaderboard after a game is complete.
        Sets the leaderboard as the worksheet from the leaderboard
        module's SHEET constant, using the player's game_choice
        attribute to access the correct worksheet.
        Gets the scores column from the worksheet and uses this in
        the leaderboard module's function 'row_to_insert_at()'
        along with the user's score, to find the row the user
        should be inserted at.
        Uses the leaderboard module's function 'rank_generator()'
        with (insert_at_row - 1) since the 'Rank' heading is at row
        1 and 1st place is at row 2 etc.
        Creates the user's row data and inserts it at the correct
        row.
        Calls the the leaderboard module's function 'rank_refresh()'
        on the worksheet inorder to correct the rest of the user's
        ranks.
        Gives user feedback before opening and after updating the
        worksheet.
        """

        print(f"\nUpdating the {self.game_choice} leaderboard ...\n")
        leaderboard = lb.SHEET.worksheet(self.game_choice)

        score_list = leaderboard.col_values(3)
        insert_at_row = lb.row_to_insert_at(score_list, self.score)

        rank = lb.rank_generator((insert_at_row - 1))

        user_list = [rank, self.username, self.score]
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


# setting the username
def setting_username():
    """
    Prompts the user for a username until a valid option
    is chosen.
    If the user wants to choose a previous username, the
    names of the worksheets are unpacked from the menu_dict{}
    with * the operator and by removing the first 5 characters
    of the name with index slicing (e.g. removes 'play_').
    The worksheet names are passed in the leaderboard module's
    function 'unique_usernames()' to create a dictionary of
    unique usernames.
    A try/except is used to get a valid option from the dict
    of previous usernames.
    If the user wants to choose a new username, a try/except is
    used to ensure the new username is 15 characters or less and
    doesn't contain any spaces.
    Returns the username back into main().
    """

    username_choice = input("Enter 'y' to reuse a previous username, or anything to choose a new name:\n")

    if username_choice.lower() == 'y':
        print('\nFinding previous usernames from the Leaderboards...')
        menu_dict_values = [*menu_dict.values()]

        lb_sheet_names = []
        for value in menu_dict_values:
            sheet_name = value[5:]
            lb_sheet_names.append(sheet_name)

        # slicing the last Main Menu item which is 'leaderboards'
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

    else:
        while True:
            try:
                username = input("Enter a username (without spaces & less than 15 characters):\n")
                if (len(username) > 15) or (' ' in username):
                    raise ValueError
                else:
                    break
            except ValueError:
                print("\nInvalid username\n")

    return username


# function for prompting the user to choose from Main Menu
def main_menu_choice(current_user):
    """
    Uses a try/except to prompt the user for an option from
    Main Menu until a valid option is chosen or the user enters
    'quit' to exit the program.
    The loop is broken out from if the user enters 'quit'.
    When a valid option is made (option exists in menu_dict):
    - the option is extracted into menu_choice
    - specific user feedback is given
    - the user's game_choice attribute is updated with the option
    name (the option with the frist 5 characters sliced off)
    - the string of the module's full name/path is created
    - the module is importeed with importlib's 'import_module()'
    function
    - the module's 'main()' function is called, passing the user
    as a param
    """

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

                current_user.user_game_choice = menu_choice[5:]

                module_str = 'game_engine.' + menu_choice[5:]

                module = il.import_module(module_str)

                module.main(current_user)
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid entry. Enter a number from the options below.\n Or 'quit' to exit")


def main():
    """
    Main game function.
    Prints welcome message to the user.
    Calls 'setting_username()' function to set the user's username.
    Print's specific welcome with the username.
    Creates an instance of the Player Class, 'current_user' with:
    - username = username
    - score = 0
    - user_quit = None
    - game_choice = None
    While loop calls 'main_menu_choice()' function to prompt valid
    menu options from the user until their quit_status == 'quit'.
    Prints exit message.
    """

    print("Welcome to Python Minigames!\n\nLet's start by setting your username.")
    username = setting_username()
    print(f"\nWelcome to Python Minigames {username}!\n")

    current_user = Player(username, 0, None, None)

    while current_user.quit_status != 'quit':
        main_menu_choice(current_user)

    print(f'Thank you {username} for playing Python Minigames!')


# calling the main() only when run.py is called not imported
if __name__ == "__main__":
    main()
