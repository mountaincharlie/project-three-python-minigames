# Python Minigames [to finish]

Python Minigames are a collection of ___ mini version of classic logic games and mini games of skill/chance, built in Python, including; Minesweeper, __, __ ... The option to set or reuse a username enables the user to personalise their experience and the ability to save and view scores in the leaderboard feature, allows for the games to be played casually, to track progress, or competatively, against others.

This app provides a fun and quick way to play a few small, popular games, with easy to follow instructions and user feedback allowing all kinds of user's to get started straight away. 

![Viewing my website on the Am I Responsive site](##IMAGE LOCATION## "Python Minigames website on the Am I Responsive site")

[Image made using <a href = "http://ami.responsivedesign.is/">Am I Responsive Website</a>]

## Contents [to finish]
---

* [Technologies Used](https://github.com/mountaincharlie/project-three-python-minigames#technologies-used)

## Technologies Used 
---

* Python

## Features [to finish]
---

To do:
* descriptions/user value/screenshots 
* menu/navigation
* the games [Player Class model!] (link to instructions section)
* the leaderboard (link to API section)

## The Games [to finish]
---

To do:
* instructions and screenshots
* Minesweeper
* ...

## Google Drive and Sheets APIs [to finish]
---

To do:
* explain steps/purpose and screenshots 
* setup?
* interacting with the leaderboards
* each leaderboard and read/writing from/to it

## Python Libraries [to finish]
---

To do:
* uses and credit for
* Numpy?
* PyDictionary?

## User Experience Design [to finish]
---

To do:
* interactivity
* navigation
* user feedback
* CI template for console style layout in the browser

## Accessability [to finish]
---

* ?

## Testing [to finish]
---

To do:
### PEP8 Python Validator
* SHOULD BE: No errors or warnings
* <a href = ##LINK##>Link to validator results</a>

### Bugs and Fixes
* **Bug:** when checking if the user's input was a key in the menu_dict dictionary, the if statement was never being triggered even by input I thought was correct.
    * **Solution:** the number entered as 'input' was being assigned to its variable as a string when it needed to be an integer, so I added an 'int()' around the input.
* **Bug:** trying to find a way to update the user_quit attribute from outside the current_user instance.
    * **Solution:** adding the Property Decorator to the Player class to include Getter and Setter methods, for getting the attribute and for settings its value. [CREDIT - help from Corey Schafer's video: <a href = "https://www.youtube.com/watch?v=jCzT9XFZ5bw">Python OOP Tutorial 6: Property Decorators - Getters, Setters, and Deleters</a>]
* **Bug:** trying to find a way to set a try/except validation for my own specific cases where the user's input needed to be a certain length or a number which was a key in the menu_dict.
    * **Solution:** using an if/else statement to test the conditions and either bresk out of the while loop or raise an error which was then handled in the 'except'. [CREDIT - help from repsonse by Kevin on Stack Overflow: <a href = "https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response">Implementing Your Own Validation Rules</a>]
* **Bug:** trying to work out how to import the games and leaderboard modules from my seperate 'game_engine' directory, to the run.py file.
    * **Solution:** add an empty '__ init __.py' file into the directory, which tells python to treat it as a package, and to then import each module like: 'from modules import leaderboards' etc. [CREDIT - help from Chris' post on finxter: <a href = "https://blog.finxter.com/python-how-to-import-modules-from-another-folder/#:~:text=The%20most%20Pythonic%20way%20to,import%20module%20.">Method 3: Dot Notation with __ init __.py</a>]
* **Bug:** trying to call one of the game/leaderboard modules from the user choosing a dictionary key whose value was the name of the module as a string. The AttributeError kept occuring since the string of the module's name wasn't the same thing as the actual module, so didnt have any attributes, which meant when I was trying to call a function from the module this way, i kept recieving the error message. 
    * **Solution:** importing 'importlib' and then using its import_module() method to import the chosen module, with its full name as a string. For example, to call the minesweeper module: module_str = 'game_engine.minesweeper', module = importlib.import_module(module_str), module.welcome_msg() (to call the welcome_msg function from the chosen module). [CREDIT - help from NanoDano's post on Dev_DUNGEON: <a href = "https://www.devdungeon.com/content/import-python-module-string-name">Import Python Module by String Name</a>]
* **Bug:** while generating random coordinates for mines, in Minesweeper.py, there were cases where duplicate coordinates were generated, which would've meant there wouldn't be the correct number of mines in the hidden_grid.
    * **Solution:** I wrapped the random coordinate generation in a while loop which ran while the number of items in the set (coors) was less than the defined number of mines (NUM_MINES). Because it is a set, 'coors' doesn't allow duplicate values and so if a coordinate was generated in the loop that was already in the set, it would not be added to the set and so the loop would have to run an additional time inorder to generate a different unique coordinate. 
* **Bug:** when trying to import the Player class from run.py into my game modules, the code in run.py was being triggered in the import.
    * **Solution:** I wrapped all of my non-function/class code in run.py into a function called main() and called it at the end of the script. I also put the function call in an if statement that if __ name __ == __ main() __ inorder to prevent the function being called when run.py was imported. [CREDIT - help from Jeremy's answer on Stack Overflow: <a href = "https://stackoverflow.com/questions/6523791/why-is-python-running-my-module-when-i-import-it-and-how-do-i-stop-it/6523855#6523855">prevent code in the module from being executed when imported</a>]
* **Bug:** popping the final value from leaderboards_menu dictionary inside the leaderboards module's main() function meant that everytime game_engine.leaderboards.main(current_user) was called from run.py, another value was removed from leaderboards_menu dictionary.
    * **Solution:** defining leaderboards_menu outside of its main() function so that the last value is removed from its call of run.menu_dict instead of previous stored version of leaderboards_menu.
* **Bug:**
    * **Solution:**

### Unfixed Bugs
* SHOULD BE: No unfixed bugs

## Deployment [to finish]
---

To do:
* fully describe process to deploy to Heroku

## Credits [to finish]
---

To do:
* other credits

### Help With Bug Fixes
* Corey Schafer's video: <a href = "https://www.youtube.com/watch?v=jCzT9XFZ5bw">Python OOP Tutorial 6: Property Decorators - Getters, Setters, and Deleters</a> for creating a getter and setter in my Player Class.
* Repsonse by Kevin on Stack Overflow: <a href = "https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response">Implementing Your Own Validation Rules</a> for using if/else statements to trigger my own validation rules.
* Chris' post on finxter: <a href = "https://blog.finxter.com/python-how-to-import-modules-from-another-folder/#:~:text=The%20most%20Pythonic%20way%20to,import%20module%20.">Method 3: Dot Notation with __ init __.py</a> for how to import modules from a sperate directory.
* NanoDano's post on Dev_DUNGEON: <a href = "https://www.devdungeon.com/content/import-python-module-string-name">Import Python Module by String Name</a> for how to import a module using its name as a string.
* Jeremy's answer on Stack Overflow: <a href = "https://stackoverflow.com/questions/6523791/why-is-python-running-my-module-when-i-import-it-and-how-do-i-stop-it/6523855#6523855">prevent code in the module from being executed when imported</a> for how to prevent a module's code being exectuted when its imported into another module.
* Kite's post: <a href = "https://www.kite.com/python/answers/how-to-iterate-through-a-decreasing-range-with-a-for-loop-in-python">How to iterate through a decreasing range with a for-loop in Python</a> for how to iterate through a decreasing range with a for-loop.

### Code Snippets Borrowed From/Inspired By
* GeeksforGeeks's post: <a href = "https://www.geeksforgeeks.org/python-remove-square-brackets-from-list/">Python | Remove square brackets from list</a> for how to remove the square brackets from a list, using the str() method and list slicing, which i used in minesweeer.py for displaying the display_grid to the user.
* Part of MSeifert's answer on Stack Overflow: <a href = "https://stackoverflow.com/questions/36964875/sum-of-8-neighbors-in-2d-array/37026344#37026344">calculate the sum of a particular region</a> for how to create 2 array of the region (8 surrounding coordinates) around a coordinate, including the corrdinate, which I used in minesweeper.py to find the number of mines surrounding a coordinate.
* Help from peterz's answer on Stack Overflow: <a href = "https://stackoverflow.com/questions/63117963/how-to-instantiate-a-subclass-type-variable-from-an-existing-superclass-type-obj/63173689#63173689">instantiate a subclass type variable from an existing superclass type object in Python</a> for how to create an instance of a SubClass which used the attribute values from an instance of a SuperClass, which I used inorder to create an instance of the SubClass in each game module, from the Player SuperClass in run.py, using the attribute values from the current_user instance of Player in run.py. 
* Using Sepero's answer on Stack Overflow: <a href = "https://stackoverflow.com/questions/1054271/how-to-import-a-python-class-that-is-in-a-directory-above/11096846#11096846">How to import a Python class that is in a directory above?</a> for how to import a class from a directory above the one it was being imported into, which I used to import my Player Class from run.py into my game modules.

## Program Expansion Ideas [to finish]
---

Features that could be added to expand and improve the program in the future.

to do:
* menu option to change user name without exiting the program
* other games to include ...
* easy/med/hard version of the games (change some params of the game e.g. bigger grid and more mines in minesweeper) and seperate leaderboards for each mode OR a multiplier so that hard modes yeild better scores 
