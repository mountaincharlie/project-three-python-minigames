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
    def __init__(self, username, score, user_quit, game_choice, coors):
        super().__init__(username, score, user_quit, game_choice)
        self.coors = coors

    @classmethod
    def from_current_user(cls, player_instance, coors):
        return cls(**player_instance.__dict__, coors=coors)

