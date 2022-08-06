# Rock, Paper, and Scissors Game

This project which is implemented using the 
python programming language provides an
interactive environment through console (terminal)
to play the *Rock, Paper, and Scissors* game.


## Quick Start

All required packages are listed in the 
*requirement.txt* file. To install all 
necessary packages in one step, you can 
easily execute the following command:
```angular2html
pip install -r requirements.txt
```

To start the program, one should simply execute the *main.py*
file using the following command:
```
python main.py
```

This will display a menu with some options to select.
Other instructions are given through your journey 
into the game.


## Project Structure

This project contains 6 files, except the README file,
as follows:
1. *requirements.txt*
2. *settings.py*
3. *main.py*
4. *utils.py*
5. *classes.py*
6. *users.csv*

Each file is described in details.

### - requirements.txt
This file contains the required python package
to execute the program.
The mose important external packages used in the
project are as follows:
- *pandas*: to work with dataframes
- *termtables*: to draw simple tables in console

### - settings.py
This file contains some global variables used in different files
as follows:
- USER_FILE_ADDRESS
- FIRST_MENU_OPTIONS
- SECOND_MENU_OPTIONS
- GAME_STRATEGIES
- GAME_MODES
- PASSWORD_MINIMUM_LENGTH
- NAME_MAXIMUM_LENGTH
- USERNAME_MAXIMUM_LENGTH
- PASSWORD_MAXIMUM_LENGTH
- ALPHA: a real-valued number between 0 and 1, used as a threshold
  for the random process of choosing strategy for
  the computer in the *hard* mode.
- INF: a very large number.

### - main.py
This file contains the *main* function which starts the game
by displaying a menu and navigate the user between different options.
The *main* function itself calls the functions in 
*utils.py* and *classes.py* files.

### - utils.py
This file contains multiple small functions which are called
by the *main* function in the *main.py* file repeatedly.
A short description of each function is available as bellow:
- *check_users_file*: to check if the users file exists. If not, it will create it.
  The *users.csv* file contains information about users.
- *display_first_menu*: to display the first menu with options: 
  *Sign up*, *Login*, *Scoreboard*, and *Exit*.   
- *display_second_menu*: to display the second menu with options: 
  *Play*, *Stats*, *Scoreboard*, *Logout*, and *Exit*. The
  second menu will appear after a user login to the system successfully.
- *encrypt_password*: to encrypt a raw password using a simple encryption
  method based on the password length.
- *signup*: to signup using *name*, *username*, and *password*
- *login*: to signup using *username* and *password*
- *logout*: to logout from the program
- *display_scoreboard*: to display a scoreboard of ranked users
- *display_stats*: to show the user's stats in terms of win rate,
    number of plays, number of wins, and number of losses. 
  
## - classes.py
This file contains one class called *RockPaperScissorsGame*.
This class has following attributes:
- user_information
- game_mode
- score_limit
- user_score
- computer_score
- user_strategy
- computer_strategy
- number_of_played_strategies

And following methods:
- update_scores: to update user and computer scores after
  each round of game
- update_user_stats: to update user stats after each game
- obtain_computer_strategy: to obtain the computer strategy based on the game modes (easy or hard).
  In the easy mode, a random strategy is chosen, while in the hard mode a simple statistical method is
  used to select a strategy based on the user's previous strategies.
- play: to start and play the game for the user.


## - users.csv
This file contains information about users as follows:
- name
- username
- encrypted_password
- number_of_plays
- number_of_wins
- number_of_losses
- win_rate
- number_of_rocks
- number_of_papers
- number_of_scissors