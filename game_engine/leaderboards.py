""" Leaderboards module for Python Minigames """

# imports
import gspread
from oauth2client.service_account import ServiceAccountCredentials
# to import run.py from parent directory
import sys
sys.path.append('.')
import run

# setting up the constant variables for the API
SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]
CREDS = ServiceAccountCredentials.from_json_keyfile_name("creds.json", SCOPE)
CLIENT = gspread.authorize(CREDS)
# catching error if the spreadsheet cannot be found
try:
    SHEET = CLIENT.open("leaderboards")
except gspread.exceptions.SpreadsheetNotFound:
    print('[NOTE: Sorry, the leaderboards spreadsheets could not be found.\nIt will not be possible to update or view any leaderboards at this time.]\n')

# defining the leaderboards_menu outside main()
leaderboards_menu = run.menu_dict
# removing the final key/value which is 'view_leaderboards'
leaderboards_menu.pop(str(len(leaderboards_menu)))


def unique_usernames(sheets):
    """
    Finds all the different usernames previously saved to the
    leaderboards worksheets.
    Defines an empty set to add the usernames to, which prevents
    duplicates.
    Loops through the list of 'sheet' names passed into the function.
    For each sheet, the data from the second column (contains usernames)
    is put into a set and sliced to remove the 'Usernames' heading and
    the union between the data and pre-defined set is created using the
    | operator.
    A for loop and enumerates function is used to turn the set of usernames
    into a dictionary with number keys.
    Returns the usernames_dict.
    """
    usernames = set()
    # catching errors if the spreadsheet or the worksheets cannot be found
    try:
        for sheet in sheets:
            worksheet = SHEET.worksheet(sheet)
            data = worksheet.col_values(2)
            usernames |= set(data[1:])
    except gspread.exceptions.WorksheetNotFound:
        print(f'\nSorry, one of the leaderboards could not be found.\nUnable to access previous usernames at this time.\n')
        return  'new_username_req'
    except NameError:
        print('\nSorry, since the leaderboards spreadsheets could not be found,\nit will not be possible to access previous usernames at this time.\n')
        return  'new_username_req'

    usernames_dict = {}
    for i, name in enumerate(usernames):
        usernames_dict[i] = name

    return usernames_dict


def row_to_insert_at(score_list, user_score, score_order):
    """
    Finds which row in the leaderboard the user's data
    should be inserted at.
    For the length of the list of scores, and ignoring the
    first value which is the heading, checks if the user's
    score is less than or equal to (a better or equal score).
    insert_at_row = i+1 since the sheet starts at row = 1 and
    has a heading in the frist row.
    If the user's score isnt better than any in the list, the
    insert row will be the last one.
    Returns the insert_at_row.
    """
    # if they game has reverse score (lower is better)
    if score_order == 'high_to_low':
        for i in range(1, len(score_list)):
            if user_score <= int(score_list[i]):
                insert_at_row = i+1
                break
            insert_at_row = len(score_list)
    else:  # for regular scoring (higher is better)
        for i in range(1, len(score_list)):
            if user_score >= int(score_list[i]):
                insert_at_row = i+1
                break
            insert_at_row = len(score_list)+1

    return insert_at_row


def rank_converter(num):
    """
    Converts a number into a rank (1st/2nd etc...)
    If the number is one of the special cases (11-13)
    they're assigned a place of 'th'.
    Numbers ending in 1 are assigned 'st'
    Numbers ending in 2 are assigned 'nd'
    Numbers ending in 3 are assigned 'rd'
    And the rest are also assigned 'th'
    The rank is the string of the number and its place.
    Returns the rank.
    """
    if num in range(11, 14):
        place = 'th'
    elif str(num)[-1] == '1':
        place = 'st'
    elif str(num)[-1] == '2':
        place = 'nd'
    elif str(num)[-1] == '3':
        place = 'rd'
    else:
        place = 'th'

    rank = str(num) + place

    return rank


def rank_refresh(leaderboard):
    """
    Adjusts the ranks column after the current user's
    data has been inserted.
    Takes the worksheet the user is being added to.
    The initial rank column values are inserted to a list
    and the heading is popped.
    The new rank column list is defined.
    For loop starting at 1 since the sheet doesnt have a 0th
    row and for the length of the rank column + 1 inorder to
    cover all of the rows with data, calls rank_converter()
    and appending to the new rank column list in order to create
    a list as long as the rows of ranks from 1st to nth and inserts
    the rank heading back at index 0.
    Uses a for loop with enumerates() to update the worksheet cell
    at each row, in the rank columns (1) with the value of rank.
    """
    rank_col = leaderboard.col_values(1)
    rank_heading = rank_col.pop(0)
    new_rank_col = []

    for i in range(1, len(rank_col)+1):
        rank = rank_converter(i)
        new_rank_col.append(rank)
    new_rank_col.insert(0, rank_heading)

    for i, rank in enumerate(new_rank_col):
        row = i+1
        leaderboard.update_cell(row, 1, rank)


def print_leaderboard_dict(menu):
    """
    Prints the leaderboard menu in a more readable way for the user.
    Each game name is the value in the dictionary minus the 'play_'
    string at the start, which is removed using index slicing.
    The numbered key and the gaem name are printed, seperated by a
    '-'.
    """
    for key in menu:
        game_name = menu[key][5:]
        print(key, '-', game_name)


def leaderboard_choice(user, menu):
    """
    Prompts the user for an option from the menu until a valid 
    option is chosen.
    Calls the print_leaderboard_dict() to display the menu for
    the user and requests an input for an option or 'quit.
    If the user chooses to quit, the user.quit_status is set to
    'quit'.
    Otherwise, it checks if the input exists as one of the menu
    dict's keys.
    If its not a valid key, ValueError is raised, with a message
    to the user.
    If the user make a valid choice, that game's leaderboard
    worksheet is retrived and for each row of its data, the first
    (rank), second (username) and third (score) values are printed
    with '--' between them to make it more readable for the user.
    The user is given the option to return to the Leaderboards Menu
    or quit to the Main Menu.
    """
    while True:
        try:
            print('Leaderboards Menu:')
            print_leaderboard_dict(menu)

            leaderboard = input("\nEnter a number to select an option (or 'quit' to exit):\n")

            if leaderboard == 'quit':
                user.quit_status = leaderboard
                break
            elif leaderboard in menu:
                leaderboard_name = menu[leaderboard][5:]

                print(f'\n --- Opening the {leaderboard_name} leaderboard ...\n')

                # catching errors if the spreadsheet or the worksheets cannot be found
                try:
                    leaderboard_worksheet = SHEET.worksheet(leaderboard_name)
                    data = leaderboard_worksheet.get_all_values()
                    print(f'{leaderboard_name.upper()} LEADERBOARD:')
                    for row in data:
                        print(row[0], '--', row[1], '--', row[2])
                except gspread.exceptions.WorksheetNotFound:
                    print(f'\nSorry, the {leaderboard_name} leaderboard could not be found.\nUnable to view the {leaderboard_name} leaderboard at this time.\n')
                except NameError:
                    print('\nSorry, since the leaderboards spreadsheets could not be found,\nit will not be possible to view any leaderboards at this time.\n')

                choice = input("\nHit ENTER to return to the Leaderboards Menu or 'quit' to return to the Main Menu:\n")

                if choice == 'quit':
                    user.quit_status = choice
                break
            else:
                raise ValueError

        except ValueError:
            print("\nInvalid entry. Enter a number from the options below.\nOr 'quit' to exit\n")


def main(user):
    """
    Main leaderboard function.
    Creates the leaderboard_user instance of the Player class from run.py.
    Personally welcomes the user.
    While the user doesn't want to quit, leaderboard_choice() is called with
    the user and the Leaderboards Menu as params.
    A final thank you message is printed before the user returns to Main Menu. 
    """
    username = user.username
    leaderboard_user = run.Player(username, 0, None, None, 'low_to_high')
    print(f' ----- Welcome to the Python Minigames Leaderboards {leaderboard_user.username}! ----- \n')

    while leaderboard_user.quit_status != 'quit':
        leaderboard_choice(leaderboard_user, leaderboards_menu)

    print(f'\nThank you for using the Python Minigame Leaderboards {username}!\n')
