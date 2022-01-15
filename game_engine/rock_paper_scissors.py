""" Rock_Paper_Scissors minigame module for Python Minigames """

# imports
import numpy as np
# to import run.py from parent directory
import sys
sys.path.append('.')
from run import Player


# Rock_Paper_Scissors Player subclass
class Rock_Paper_ScissorsPlayer(Player):
    """ Creates instance of Rock_Paper_ScissorsPlayer """
    def __init__(self, username, score, user_quit, game_choice, score_order, guess):
        super().__init__(username, score, user_quit, game_choice, score_order)
        self.guess = guess

    @classmethod
    def from_current_user(cls, player_instance, guess):
        return cls(**player_instance.__dict__, guess=guess)


# main function calls
def main(user):
    """ main game function calls """


# constants and global vars
OPTIONS = ('rock', 'paper', 'scissors')
