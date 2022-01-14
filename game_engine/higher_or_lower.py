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
    print(higher_or_lower_user.username)
    print(higher_or_lower_user.score)
    print(higher_or_lower_user.user_quit)
    print(higher_or_lower_user.game_choice)
    print(higher_or_lower_user.guess)


# calling main()
# main()
