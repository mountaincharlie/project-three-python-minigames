""" Project 3 - Python Minigames """

# imports (modules and other needed py libraries)
from pprint import pprint
import importlib as il
from game_engine import leaderboards as lb


# dictionary of menu options
menu_dict = {
    '1': 'play_minesweeper',
    '2': 'play_higher_or_lower',
    '3': 'play_rock_paper_scissors',
    '4': 'view_leaderboards'
}


class Player:
    """ Creates an instance of Player """
    def __init__(self, username, score, user_quit, game_choice, score_order):
        self.username = username
        self.score = score
        self.user_quit = user_quit
        self.game_choice = game_choice
        self.score_order = score_order

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
        Uses the leaderboard module's function 'rank_converter()'
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

        print(f"\n --- Updating the {self.game_choice} leaderboard ...\n")
        leaderboard = lb.SHEET.worksheet(self.game_choice)

        score_list = leaderboard.col_values(3)
        insert_at_row = lb.row_to_insert_at(score_list, self.score, self.score_order)

        rank = lb.rank_converter((insert_at_row - 1))

        user_list = [rank, self.username, self.score]
        leaderboard.insert_row(user_list, insert_at_row)

        lb.rank_refresh(leaderboard)

        print(f"You've been added to the {self.game_choice} leaderboard at {rank} place.\n(You can view the Leaderboards module from the Main Menu)\n")

    def welcome_msg(self):
        """
        Initial user welcome message for each game.
        Uses the user's username and game choice to write a personal welcome
        message.
        Prompts the user to begin the game (hit ENTER) or view the game
        instructions (enter 'i') or to quit to Main Menu (enter 'quit').
        If the user wants to view the instructions, the read_instructions()
        function is called to display them.
        The user is then prompted to continue to the game (hit ENTER) or to
        quit to Main Menu (enter 'quit').
        Returns the user's quit_status.
        """
        print(f'\n ----- Welcome to the {self.game_choice.capitalize()} minigame {self.username}! ----- \n')

        user_choice = input("Hit ENTER to begin or 'i' to see the Minigame instructions, or 'quit' to return to the Main Menu:\n")

        if user_choice == 'i':
            print(f'\n --- Opening the {self.game_choice.capitalize()} minigame instructions ...\n')
            self.read_instructions()
            user_choice = input("\nHit ENTER to start the game or 'quit' to return to the Main Menu:\n")

        return user_choice

    def read_instructions(self):
        """
        Reads a game's instruction txt file and prints it line by line to the
        user.
        Creates the string name of the path to the txt file.
        Uses a try/except to open and read the file and then print each line,
        after stripping the '\n'.
        If the txt file cannot be found, the FileNotFoundError is caught and
        an informative message is displayed to the user.
        """
        file = 'game_engine/' + str(self.game_choice) + '.txt'

        try:
            with open(file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    line.strip('\n')
                    print(line)
        except FileNotFoundError:
            print(f'Sorry, the {self.game_choice.capitalize()} instructions file could not be found.')

    def play_again(self):
        """
        Prompts the user to enter anything to play the game again or 'quit'
        to return to the Main Menu.
        Returns 'quit'.
        """
        choice = input("Hit ENTER to play again or 'quit' to return to the Main Menu:\n")

        if choice == 'quit':
            self.quit_status = 'quit'

        return 'quit'

    def game_finish(self):
        """
        """
        self.update_leaderboard()

        return self.play_again()

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


def print_dict(dictionary):
    """
    Takes a dictionary and for each of its keys it
    prints the key, a dash and then the dictionary's
    value at the key.
    """
    for key in dictionary:
        print(key, '-', dictionary[key])


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
        print('\n --- Finding previous usernames from the Leaderboards...')
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
                print_dict(usernames_dict)

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
                username = input("\nEnter a username (without spaces & less than 15 characters):\n")
                if (len(username) > 15) or (' ' in username):
                    raise ValueError
                else:
                    break
            except ValueError:
                print("\nInvalid username\n")

    return username


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
            print('\nMain Menu:')
            print_dict(menu_dict)

            menu_choice = input("\nEnter a number to select an option (or 'quit' to exit):\n")

            if menu_choice == 'quit':
                current_user.quit_status = menu_choice
                break
            elif menu_choice in menu_dict:
                menu_choice = menu_dict[menu_choice]

                choice_name = menu_choice[5:]

                print(f'\n --- Opening {choice_name} ... \n')

                current_user.user_game_choice = choice_name

                module_str = 'game_engine.' + choice_name

                module = il.import_module(module_str)

                module.main(current_user)
                break
            else:
                raise ValueError
        except ValueError:
            print("\nInvalid entry. Enter a number from the options below.\nOr 'quit' to exit\n")


def main():
    """
    Main program function.
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
    print(f"\n ----- Welcome to Python Minigames {username}! ----- ")

    current_user = Player(username, 0, None, None, 'low_to_high')

    while current_user.quit_status != 'quit':
        main_menu_choice(current_user)

    print(f'\nThank you for playing Python Minigames {username}!')


# calling the main() only when run.py is called not imported
if __name__ == "__main__":
    main()
