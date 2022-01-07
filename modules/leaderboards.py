""" Leaderboards module for Python Minigames """

# imports
import gspread
from oauth2client.service_account import ServiceAccountCredentials
# remove at end of project (unless using for project)
from pprint import pprint

# setting up the constant variabels for the API
SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]
CREDS = ServiceAccountCredentials.from_json_keyfile_name("creds.json", SCOPE)
CLIENT = gspread.authorize(CREDS)
SHEET = CLIENT.open("leaderboards")

# checking it works
# first_leaderboard = SHEET.worksheet('minesweeper')
# data = first_leaderboard.get_all_values()
# pprint(data)

# accessing rows/columns/cells (delete)
# row = first_leaderboard.row_values(2)
# col = first_leaderboard.col_values(2)
# cell = first_leaderboard.cell(2,2).value

# DEFINE 'sheets' in run.py
# sheets = ['minesweeper', 'hangman']

# finding all unique usernames using a set and | operator
def unique_usernames(sheets):
    usernames = set()
    # looping through each worksheet in the 'sheets' list
    for sheet in sheets:
        worksheet = SHEET.worksheet(sheet) # getting the worksheet
        data = worksheet.col_values(2) # getting the value sin the username col
        usernames |= set(data[1:]) # creating a union of both sets

    # converting the set into dictionary weith number keys
    usernames_dict = {}
    for i, name in enumerate(usernames):
        usernames_dict[i] = name
    return usernames_dict


# test calling functions
# unique_usernames(sheets)
