""" Higher_or_Lower minigame module for Python Minigames """

# imports
import numpy as np
# to import run.py from parent directory
import sys
sys.path.append('.')
from run import Player


# Higher_or_Lower Player subclass
class Higher_or_LowerPlayer(Player):
    """ Creates instance of Higher_or_LowerPlayer """
    def __init__(self, username, score, user_quit, game_choice, guess):
        super().__init__(username, score, user_quit, game_choice)
        self.guess = guess

    @classmethod
    def from_current_user(cls, player_instance, guess):
        return cls(**player_instance.__dict__, guess=guess)


# main function call
def main(user):
    """ main game function calls """
    print('hello')

    # instance of Higher_or_LowerPlayer SubClass (no current guess value)
    higher_or_lower_user = Higher_or_LowerPlayer.from_current_user(user, None)

    # overall while loop for starting the game
    while higher_or_lower_user.quit_status != 'quit':
        username = higher_or_lower_user.username
        # resetting the user's score everytime they play again
        higher_or_lower_user.score = 0

        # welcome message
        play_or_quit = higher_or_lower_user.welcome_msg()
        if play_or_quit == 'quit':
            break
        print('\nBuilding the ... ...\n')

        # build the game lists/tuples [function call]

        # printing the basic instructions (just a print)

        # print initial random card [random card choosing function]

        # while loop for prompting user guesses until they choose to quit
        # while True:

        # takes in and validates user guess [in a function]

        # updates higher_or_lower_user.guess

        # prints their guess??
        # print(f"\nYou have guessed that the next card will be: {higher_or_lower_user.guess} than {current_card}\n")

        # checks/updates the user's score [in a function]

        # prompts continue or quit
        # cont_or_quit = input("\nHit ENTER to continue or 'quit' to restart the game:\n")
            # if cont_or_quit.lower() == 'quit':
                # break


# calling main()
# main()
