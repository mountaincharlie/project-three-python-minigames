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


# random card choosing function
def random_card(deck):
    """
    """
    # randomly chooses and removes card from deck
    card = np.random.choice(deck)
    deck.remove(card)

    return card


# ----- PROCESSING USER INPUT -----

def validate_guess():
    """
    Keeps asking the user for a guess of h (higher),
    or l (lower) until a valid entry is given.
    Returns the valid guess.
    """

    options = {
        'h': 'higher',
        'l': 'lower'
        }
    while True:
        try:
            guess = input("\nEnter 'h' (for higher) 'l' (for lower):\n")
            if guess not in options:
                raise ValueError
            else:
                break
        except ValueError:
            print(f"Invalid guess")

    return options[guess]


# main function call
def main(user):
    """ main game function calls """

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
        print('\nSetting up the game ...\n')

        # ----- SETTING UP THE GAME -----

        # build the card_order tuple [make a constant?]
        card_order = ('A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2')
        # build the deck list [make a function call so its reset at game start but not during game]
        deck = ['A_spades', 'K_spades', 'Q_spades', 'J_spades', '10_spades', '9_spades', '8_spades', '7_spades', '6_spades', '5_spades', '4_spades', '3_spades', '2_spades', 'A_diamonds', 'K_diamonds', 'Q_diamonds', 'J_diamonds', '10_diamonds', '9_diamonds', '8_diamonds', '7_diamonds', '6_diamonds', '5_diamonds', '4_diamonds', '3_diamonds', '2_diamonds', 'A_clubs', 'K_clubs', 'Q_clubs', 'J_clubs', '10_clubs', '9_clubs', '8_clubs', '7_clubs', '6_clubs', '5_clubs', '4_clubs', '3_clubs', '2_clubs', 'A_hearts', 'K_hearts', 'Q_hearts', 'J_hearts', '10_hearts', '9_hearts', '8_hearts', '7_hearts', '6_hearts', '5_hearts', '4_hearts', '3_hearts', '2_hearts']
        cards_shown = []  # CHECK at end if we need this

        # printing the basic instructions (just a print)
        print(f'The first card from the deck is displayed below!\n\nChoose whether you think the next card to be revealed\nwill be higher or lower than this card.\nThe cards in order from highest to lowest are:\n{card_order}\n')

        # print initial random card [random card choosing function]
        new_card = random_card(deck)
        print(new_card)
        # adds the new_card to the cards_shown list
        cards_shown.append(new_card)
        # print(deck)
        # print(cards_shown)

        # while loop for prompting user guesses until they choose to quit
        while True:

            # updates revealed_card
            revealed_card = new_card

            # takes in and validates user guess [in a function]
            user_guess = validate_guess()

            # updates higher_or_lower_user.guess
            higher_or_lower_user.guess = user_guess

            # prints their guess??
            print(f"\nYou have guessed that the next card will be\n{higher_or_lower_user.guess} than {revealed_card}\n")

            # enter to continue
            input('Hit Enter to reveal the next card:')

            # generates next random card and prints with message
            new_card = random_card(deck)
            print(f'\nThe next card from the deck is:\n{new_card}')

            # checks if the revealed_card is h/l than new_card
            # updates the user's score [in a function]
            # prompts game_win or game_lost function

            # prompts continue or quit
            # cont_or_quit = input("\nHit ENTER to continue or 'quit' to restart the game:\n")
                # if cont_or_quit.lower() == 'quit':
                    # break


# calling main()
# main()
