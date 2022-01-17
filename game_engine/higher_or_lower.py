""" Higher_or_Lower minigame module for Python Minigames """

from run import Player
import numpy as np
# to import run.py from parent directory
import sys
sys.path.append('.')


# Higher_or_Lower Player subclass
class Higher_or_LowerPlayer(Player):
    """ Creates instance of Higher_or_LowerPlayer """
    def __init__(self, username, score, user_quit, game_choice, score_order, guess):
        super().__init__(username, score, user_quit, game_choice, score_order)
        self.guess = guess

    @classmethod
    def from_current_user(cls, player_instance, guess):
        return cls(**player_instance.__dict__, guess=guess)


def random_card(deck):
    """
    Uses numpy's random.choice() functino to randomly
    chooses and remove a card from deck.
    Returns the card.
    """

    card = np.random.choice(deck)
    deck.remove(card)

    return card


def validate_guess(new_card):
    """
    Defines a dictionary of the user's allowed options.
    Keeps asking the user for a guess of h (higher),
    or l (lower) until a valid entry is given.
    Returns the valid guess from the options dict.
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
    Called when a guess is correct
    Updates the user's score by 1
    """
    user.score += 1


def guess_result(user, user_guess, revealed_card_index, new_card_index):
    """
    Called in return from guess_checker().
    Finds the result from the user's guess.
    Finds what the correct answer should be and exits the function
    with 'draw' if its a draw.
    Checks if the user got the correct answer and returns 'correct'
    or 'wrong'.
    """

    if new_card_index == revealed_card_index:
        score_update(user)
        correct_answer = 'draw'
        return correct_answer
    elif new_card_index < revealed_card_index:
        correct_answer = 'higher'
    else:
        correct_answer = 'lower'

    if user_guess == correct_answer:
        score_update(user)
        return 'correct'
    else:
        return 'wrong'


def guess_checker(user, user_guess, revealed_card, new_card):
    """
    Checks if the user's guess is correct.
    Gets the values without the suits of the cards.
    Gets and compares the cards' indexes from CARD_ORDER.
    Returns guess_result() which returns 'draw'/'correct'/'wrong'.
    """
    revealed_card_value = revealed_card.split('_', 1)[0]
    new_card_value = new_card.split('_', 1)[0]

    revealed_card_index = CARD_ORDER.index(revealed_card_value)
    new_card_index = CARD_ORDER.index(new_card_value)

    return guess_result(user, user_guess, revealed_card_index, new_card_index)


def main(user):
    """ main game function calls """

    # instance of Higher_or_LowerPlayer SubClass (no current guess value)
    higher_or_lower_user = Higher_or_LowerPlayer.from_current_user(user, None)

    # overall while loop for starting the game
    while higher_or_lower_user.quit_status != 'quit':
        higher_or_lower_user.score = 0

        # welcome message
        play_or_quit = higher_or_lower_user.welcome_msg()
        if play_or_quit == 'quit':
            break
        print('\n --- Setting up the game ...\n')

        # defining the deck list
        deck = ['A_spades', 'K_spades', 'Q_spades', 'J_spades', '10_spades', '9_spades', '8_spades', '7_spades', '6_spades', '5_spades', '4_spades', '3_spades', '2_spades', 'A_diamonds', 'K_diamonds', 'Q_diamonds', 'J_diamonds', '10_diamonds', '9_diamonds', '8_diamonds', '7_diamonds', '6_diamonds', '5_diamonds', '4_diamonds', '3_diamonds', '2_diamonds', 'A_clubs', 'K_clubs', 'Q_clubs', 'J_clubs', '10_clubs', '9_clubs', '8_clubs', '7_clubs', '6_clubs', '5_clubs', '4_clubs', '3_clubs', '2_clubs', 'A_hearts', 'K_hearts', 'Q_hearts', 'J_hearts', '10_hearts', '9_hearts', '8_hearts', '7_hearts', '6_hearts', '5_hearts', '4_hearts', '3_hearts', '2_hearts']
        cards_shown = []

        # printing the basic instructions
        print(f'The first card from the deck is displayed below!\n\nChoose whether you think the next card to be revealed\nwill be higher or lower than this card.\nThe cards in order from highest to lowest are:\n{CARD_ORDER}\n')

        # print initial random card
        new_card = random_card(deck)
        print(f'\nThe first card from the deck is:\n{new_card}')

        # while loop for prompting user guesses until they choose to quit
        while True:

            # updating revealed_card
            revealed_card = new_card

            higher_or_lower_user.guess = validate_guess(new_card)
            user_guess = higher_or_lower_user.guess

            print(f"\nYou have guessed that the next card will be\n{higher_or_lower_user.guess} than {revealed_card}\n")

            input('Hit Enter to reveal the next card:')

            # generates next random card
            new_card = random_card(deck)
            print(f'\nThe next card from the deck is:\n{new_card}')

            # checks if the new_card is h/l than new_card
            guess_check = guess_checker(higher_or_lower_user, user_guess, revealed_card, new_card)

            if guess_check == 'wrong':
                print(f'\nSorry {higher_or_lower_user.username}, the {new_card} is not {user_guess} than the {revealed_card}.\n')
                if len(cards_shown) != 0:
                    print(f'You made correct guesses for the following cards:\n{cards_shown}')
                print(f'Your correct guess streak was: {higher_or_lower_user.score}')
                higher_or_lower_user.game_finish()
                break
            else:
                if guess_check == 'draw':
                    print(f'\nYou passed!\n{new_card} is neither higher or lower than {revealed_card}')
                else:
                    print(f'\nYou were correct!\n{new_card} is {higher_or_lower_user.guess} than {revealed_card}')
                # updating number of shown cards
                cards_shown.append(new_card)

                cont_or_quit = input("\nHit ENTER to guess again or 'quit' to restart the game:\n")
                if cont_or_quit.lower() == 'quit':
                    break

            if len(deck) == 0:
                print(f'\nCongratulations {higher_or_lower_user.username}!\nYou made correct guesses for the following cards:\n{cards_shown}\nYour correct guess streak was: {higher_or_lower_user.score}')
                higher_or_lower_user.game_finish()
                break


# game constant
CARD_ORDER = ('A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2')
