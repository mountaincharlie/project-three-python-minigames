""" Project 3 - Python Minigames """

# imports (modules and other needed py libraries)

# defining menu dictionary (contains names of game/leaderboard modules)
menu_dict = {
    '1': 'minesweeper',
    '2': 'hangman',
    '3': 'rock_paper_scissors',
    '4': 'leaderboards'
}

# quit variable, used to check if user wants to exit a module/program
# user_quit = None

# creating the Player class
# class Player:

"""
-Asking user if they would like to use an existing username or to choose
from a previously used one. ('y' for yes to an existing username)
-If 'y', the leaderboards worksheets are checked to see if they contain
any usernames already. If they do, they are displayed numbered, for the
user to choose. Else a msg is printed to inform thhe user that there
are no existing usernames yet and they are invited to enter their own.
-If any other key, the user is asked to enter their own username
-Username MUST be less than 15 characters and contain NO spaces.
"""

# creating the current user's instance of the Player class
# current_player = Player(username, 0, None)

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
