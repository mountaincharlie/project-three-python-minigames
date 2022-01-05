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
first_leaderboard = SHEET.worksheet('minesweeper')
data = first_leaderboard.get_all_values()
pprint(data)

# accessing rows/columns/cells (delete)
# row = first_leaderboard.row_value(2)
# col = first_leaderboard.col_value(2)
# cell = first_leaderboard.cell(2,2).value
