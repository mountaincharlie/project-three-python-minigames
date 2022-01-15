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
    def __init__(self, username, score, user_quit, game_choice, score_order, guess):
        super().__init__(username, score, user_quit, game_choice, score_order)
        self.guess = guess

    @classmethod
    def from_current_user(cls, player_instance, guess):
        return cls(**player_instance.__dict__, guess=guess)


# random card choosing function
def random_card(deck):
    """
    randomly chooses and removes card from deck
    """

    card = np.random.choice(deck)
    deck.remove(card)

    return card


# ----- PROCESSING USER INPUT -----

def validate_guess(new_card):
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
            guess = input(f"\nEnter 'h' (for higher) or 'l' (for lower) than {new_card}:\n")
            if guess not in options:
                raise ValueError
            else:
                break
        except ValueError:
            print(f"Invalid guess")

    return options[guess]


def score_update(user):
    """
    updates the user's score by 1 when guess is correct
    """
    user.score += 1


# finding the result from the user's guess
def guess_result(user, user_guess, revealed_card_index, new_card_index):
    """
    """
    # finding correct answer
    if new_card_index == revealed_card_index:
        score_update(user)
        correct_answer = 'draw'
        return correct_answer
    elif new_card_index < revealed_card_index:
        correct_answer = 'higher'
    else:
        correct_answer = 'lower'

    # checking if the user's answer is correct
    if user_guess == correct_answer:
        score_update(user)
        return 'correct'
    else:
        return 'wrong'


# checking if the user's guess was correct
def guess_checker(user, user_guess, revealed_card, new_card):
    """
    """
    # getting the values without the suits of the cards
    revealed_card_value = revealed_card.split('_', 1)[0]
    # print(revealed_card_value)
    new_card_value = new_card.split('_', 1)[0]
    # print(new_card_value)

    # getting and comparing the cards' indexes from CARD_ORDER
    revealed_card_index = CARD_ORDER.index(revealed_card_value)
    new_card_index = CARD_ORDER.index(new_card_value)

    # guess_result returns 'draw'/'correct'/'wrong'
    return guess_result(user, user_guess, revealed_card_index, new_card_index)


# main function call
def main(user):
    """ main game function calls """

    # instance of Higher_or_LowerPlayer SubClass (no current guess value)
    higher_or_lower_user = Higher_or_LowerPlayer.from_current_user(user, None)

    # overall while loop for starting the game
    while higher_or_lower_user.quit_status != 'quit':
        # username = higher_or_lower_user.username
        # resetting the user's score everytime they play again
        higher_or_lower_user.score = 0

        # welcome message
        play_or_quit = higher_or_lower_user.welcome_msg()
        if play_or_quit == 'quit':
            break
        print('\nSetting up the game ...\n')

        # ----- SETTING UP THE GAME -----

        # defining the deck list
        deck = ['A_spades', 'K_spades', 'Q_spades', 'J_spades', '10_spades', '9_spades', '8_spades', '7_spades', '6_spades', '5_spades', '4_spades', '3_spades', '2_spades', 'A_diamonds', 'K_diamonds', 'Q_diamonds', 'J_diamonds', '10_diamonds', '9_diamonds', '8_diamonds', '7_diamonds', '6_diamonds', '5_diamonds', '4_diamonds', '3_diamonds', '2_diamonds', 'A_clubs', 'K_clubs', 'Q_clubs', 'J_clubs', '10_clubs', '9_clubs', '8_clubs', '7_clubs', '6_clubs', '5_clubs', '4_clubs', '3_clubs', '2_clubs', 'A_hearts', 'K_hearts', 'Q_hearts', 'J_hearts', '10_hearts', '9_hearts', '8_hearts', '7_hearts', '6_hearts', '5_hearts', '4_hearts', '3_hearts', '2_hearts']
        # deck = ['A_spades', 'A_diamonds', 'A_clubs', 'A_hearts']
        cards_shown = []

        # printing the basic instructions
        print(f'The first card from the deck is displayed below!\n\nChoose whether you think the next card to be revealed\nwill be higher or lower than this card.\nThe cards in order from highest to lowest are:\n{CARD_ORDER}\n')

        # print initial random card
        new_card = random_card(deck)
        print(f'\nThe first card from the deck is:\n{new_card}')

        # while loop for prompting user guesses until they choose to quit
        while True:

            # updates revealed_card
            revealed_card = new_card

            # takes in and validates user guess [in a function]
            higher_or_lower_user.guess = validate_guess(new_card)
            user_guess = higher_or_lower_user.guess

            # prints their guess??
            print(f"\nYou have guessed that the next card will be\n{higher_or_lower_user.guess} than {revealed_card}\n")

            # enter to continue
            input('Hit Enter to reveal the next card:')

            # generates next random card and prints with message
            new_card = random_card(deck)
            print(f'\nThe next card from the deck is:\n{new_card}')

            # checks if the new_card is h/l than new_card
            guess_check = guess_checker(higher_or_lower_user, user_guess, revealed_card, new_card)
            # displaying the results and the user's score
            # print(guess_check)
            # print(higher_or_lower_user.score)

            if guess_check == 'wrong':
                print(f'\nSorry {higher_or_lower_user.username}, the {new_card} is not {user_guess} than the {revealed_card}.\n')
                if len(cards_shown) != 0:
                    print(f'You made correct guesses for the following cards:\n{cards_shown}')
                higher_or_lower_user.game_finish('Your correct guess streak was')
            else:
                # updating number of shown cards if correctly guessed
                cards_shown.append(new_card)
                # prompts guess again or quit
                cont_or_quit = input("\nHit ENTER to guess again or 'quit' to restart the game:\n")
                if cont_or_quit.lower() == 'quit':
                    break

            if len(deck) == 0:
                print(f'\nCongratulations {higher_or_lower_user.username}!\nYou made correct guesses for the following cards:\n{cards_shown}')
                higher_or_lower_user.game_finish('Your correct guess streak was')


# game constants and global vars
CARD_ORDER = ('A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2')
# CARD_ORDER = ('A')
