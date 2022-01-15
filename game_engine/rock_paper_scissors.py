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
    def __init__(self, username, score, user_quit, game_choice, score_order, choice):
        super().__init__(username, score, user_quit, game_choice, score_order)
        self.choice = choice

    @classmethod
    def from_current_user(cls, player_instance, choice):
        return cls(**player_instance.__dict__, choice=choice)


def validate_choice():
    """
    Keeps asking the user for a choice of r (rock),
    p (paper) or s (scissors) until a valid entry
    is given.
    Returns the valid choice.
    """

    while True:
        try:
            choice = input("\nEnter 'r' (rock), 'p' (paper) or 's' (scissors):\n")
            if choice not in OPTIONS:
                raise ValueError
            else:
                break
        except ValueError:
            print("Invalid choice")

    return OPTIONS[choice]


def rand_rps_choice():
    """
    Generates a random value from the OPTIONS
    dict as the cpu's choice.
    Returns the cpu's choice.
    """
    choice = np.random.choice(list(OPTIONS))

    return choice


# main function call
def main(user):
    """ main game function calls """

    # instance of Rock_Paper_ScissorsPlayer SubClass (no current guess value)
    rock_paper_scissors_user = Rock_Paper_ScissorsPlayer.from_current_user(user, None)

    # overall while loop for starting the game
    while rock_paper_scissors_user.quit_status != 'quit':
        # resetting the user's score everytime they play again
        rock_paper_scissors_user.score = 0

        # welcome message
        play_or_quit = rock_paper_scissors_user.welcome_msg()
        if play_or_quit == 'quit':
            break
        print('\nSetting up the game ...\n')

        # defining/resetting counter for number of rounds
        rounds_played = 0

        # printing the basic instructions
        print(f"Choose whether you want to play one of: {OPTIONS}\nThe computer will also make a choice\nand the winner will be displayed.\nThe game is out of 15 rounds.\n")

        # while loop for prompting user choices until they choose to quit
        while True:
            rounds_played += 1
            print(f'Round {rounds_played}')

            # takes in and validates user choice
            rock_paper_scissors_user.choice = validate_choice

            # generates random cpu choice
            cpu_choice = rand_rps_choice()

            # compares the two guesses
            # winner = 

            # prints the result
            print(f"\nYou chose {rock_paper_scissors_user.choice}\nThe CPU chose {cpu_choice}\n{winner} won this round.")

            # ending the game
            # if rounds_played == 15: game_finish()

            # prompts play next round or quit
            cont_or_quit = input("\nHit ENTER to guess again or 'quit' to restart the game:\n")
            if cont_or_quit.lower() == 'quit':
                break


# constants and global vars
OPTIONS = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissors'
    }
