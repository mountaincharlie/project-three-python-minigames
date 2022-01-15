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

    return OPTIONS[choice]


# compares the choices
def choice_compare(user_choice, cpu_choice):
    """
    """

    if user_choice == cpu_choice:
        winner = 'It was a draw. No one'
    elif user_choice == 'rock' and cpu_choice == 'paper':
        winner = 'The CPU'
    elif user_choice == 'rock' and cpu_choice == 'scissors':
        winner = 'You'
    elif user_choice == 'paper' and cpu_choice == 'scissors':
        winner = 'The CPU'
    elif user_choice == 'paper' and cpu_choice == 'rock':
        winner = 'You'
    elif user_choice == 'scissors' and cpu_choice == 'rock':
        winner = 'The CPU'
    elif user_choice == 'scissors' and cpu_choice == 'paper':
        winner = 'You'

    return winner


# main function call
def main(user):
    """ main game function calls """

    # instance of Rock_Paper_ScissorsPlayer SubClass (no current guess value)
    rock_paper_scissors_user = Rock_Paper_ScissorsPlayer.from_current_user(user, None)

    # overall while loop for starting the game
    while rock_paper_scissors_user.quit_status != 'quit':

        # resetting the user's score everytime they play again
        rock_paper_scissors_user.score = 0
        # resetting cpu score
        cpu_score = 0

        # welcome message
        play_or_quit = rock_paper_scissors_user.welcome_msg()
        if play_or_quit == 'quit':
            break
        print('\nSetting up the game ...\n')

        # defining/resetting counter for number of rounds
        rounds_played = 0

        # printing the basic instructions
        print(f"Choose to play: rock, paper or scissor.\nThe computer will also make a choice\nand the winner will be displayed.\nThe game is out of 15 rounds.\n")

        # while loop for prompting user choices until they choose to quit
        while True:
            rounds_played += 1
            print(f'Round {rounds_played}')

            # takes in and validates user choice
            rock_paper_scissors_user.choice = validate_choice()

            # generates random cpu choice
            cpu_choice = rand_rps_choice()

            # compares the two guesses
            round_winner = choice_compare(rock_paper_scissors_user.choice, cpu_choice)

            # tracking the user's score (+1 for wins only)
            if round_winner == 'You':
                rock_paper_scissors_user.score += 1
            elif round_winner == 'The CPU':
                cpu_score += 1
            # ADD LATER? compares cpu and user wins for winner

            # prints the result
            print(f"\nYou chose {rock_paper_scissors_user.choice}\nThe CPU chose {cpu_choice}\n{round_winner} won this round.\n{rock_paper_scissors_user.username}: {rock_paper_scissors_user.score}\nCPU: {cpu_score}")

            # ending the game
            if rounds_played == 15:
                rock_paper_scissors_user.game_finish('Your total number of winning rounds was')
                break

            # prompts play next round or quit
            cont_or_quit = input(f"\nHit ENTER for round {rounds_played+1} or 'quit' to restart the game:\n")
            if cont_or_quit.lower() == 'quit':
                break


# constants and global vars
OPTIONS = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissors'
    }
