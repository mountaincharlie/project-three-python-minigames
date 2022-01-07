""" Project 3 - Python Minigames """

# imports (modules and other needed py libraries)
import leaderboards as lb
from pprint import pprint

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

    def player_info(self):
        print(f"The user is called: {self.username}, has a current score of: {self.score} and their quit status is: {self.user_quit}")


# test instance of Player class and its player_info method
# username = 'charlie'
# current_user = Player(username, 0, None)
# current_user.player_info()


# quit variable, used to check if user wants to exit a module/program
# user_quit = None


# username selection loop (occurs once per load of program)
username_choice = input("Enter 'y' to reuse a previous username, or anything to choose a new name:\n")
# retrieving the list of usernames from the leaderboards worksheets
if username_choice.lower() == 'y':
    # unpacking the values from manu_dict with * operator
    menu_dict_values = [*menu_dict.values()]
    usernames_dict = lb.unique_usernames(menu_dict_values[:-1])
    while True:
        try:
            pprint(usernames_dict)
            prev_user = int(input("Please enter the number for a previous username:\n"))
            if prev_user in usernames_dict:
                username = usernames_dict[prev_user]
                break
            else:
                raise ValueError
        except ValueError:
            print('Invalid entry. Enter a number from the options below.')

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

print(f"Thank you {username}")

# creating the current user's instance of the Player class
current_user = Player(username, 0, None)
current_user.player_info() # calling method to check attributes


"""
Main while loop for the user to choose from the menu or exit the program.
-Print welcome message
-Print menu_dict
-take menu_choice input from user
-check if menu_choice.lower() != 'quit' and if so, check its a valid menu_dict
key otherwise keep promting input. Upon valid choice, call the approrpiate
module.
-else if menu_choice.lower() = 'quit', then break the while loop and print
thank
you msg
"""
