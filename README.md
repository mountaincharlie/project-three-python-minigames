# Python Minigames [to finish]

Python Minigames are a collection of ___ well known games, built in Python, including; Minesweeper, __, __ ... The option to set or reuse a username enables the user to personalise their experience and the ability to save and view scores in the leaderboard feature, allows for the games to be played casually, to track progress, or competatively, against others.

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
* Repsonse by Kevin on Stack Overflow: <a href = "https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response">Implementing Your Own Validation Rules</a>] for using if/else statements to trigger my own validation rules.

## Program Expansion Ideas [to finish]

Features that could be added to expand and improve the program in the future.

to do:
* menu option to change user name without exiting the program
* other games to include ...
