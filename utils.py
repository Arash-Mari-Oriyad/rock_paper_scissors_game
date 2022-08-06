import os

import pandas as pd
import termtables as tt

from settings import USERS_FILE_ADDRESS, FIRST_MENU_OPTIONS, SECOND_MENU_OPTIONS, PASSWORD_MINIMUM_LENGTH, \
    USERNAME_MAXIMUM_LENGTH, NAME_MAXIMUM_LENGTH, PASSWORD_MAXIMUM_LENGTH, INF


def check_users_file():
    """
    check_users_file function will check if the users file exists. If not, it will create it.
    This function has no input parameters and no return value.
    :return: None
    """
    if os.path.exists(USERS_FILE_ADDRESS):
        pass
    else:
        users_dataframe = pd.DataFrame(columns=["username", "encrypted_password", "name", "number_of_plays",
                                                "number_of_wins", "number_of_losses", "win_rate",
                                                "number_of_rocks", "number_of_papers", "number_of_scissors"])
        users_dataframe.to_csv(USERS_FILE_ADDRESS, index=False)
    return


def display_first_menu():
    """
    display_first_menu function will display the first menu and return the option chosen by the user.
    The available options are:
    1. Sign up
    2. Login
    3. Scoreboard
    4. Exit
    This function has no input parameters.
    :return: user's option as a string
    """
    print("\n" + 100 * "-")
    while True:
        print("\nMenu:")
        for first_menu_option_number, first_menu_option_name in FIRST_MENU_OPTIONS.items():
            print(f"{first_menu_option_number}. {first_menu_option_name}")
        option = input("\nEnter your option: ")
        if option not in FIRST_MENU_OPTIONS.keys():
            print("Invalid option! Pleas try Again.")
        else:
            return FIRST_MENU_OPTIONS[option]


def display_second_menu(user_information):
    """
    display_second_menu function will display the second menu and return the option chosen by the user.
    The available options are:
    1. Play
    2. Stats
    3. Scoreboard
    4. Logout
    5. Exit
    :param user_information: a dictionary containing the user's name and username
    :return: user's option as a string
    """
    print("\n" + 100 * "-")
    while True:
        print("\nMenu:")
        for second_menu_option_number, second_menu_option_name in SECOND_MENU_OPTIONS.items():
            print(f"{second_menu_option_number}. {second_menu_option_name}")
        option = input(f"\nDear {user_information['name']}, enter your option: ")
        if option not in SECOND_MENU_OPTIONS.keys():
            print("Invalid option! Pleas try Again.")
        else:
            return SECOND_MENU_OPTIONS[option]


def encrypt_password(password):
    """
    encrypt_password function will encrypt the password and return the encrypted password.
    The encryption method is simple:
    1. Reverse the password
    2.1. For each alphabetical character in the password, add the password length to its ASCII value and
         change it to its corresponding alphabetical ASCII character.
         Then convert it from lowercase to uppercase or vice versa.
    2.2. For each numerical character in the password,
         calculate the absolute value of the subtraction of that digit from 10.
    :param password: the raw password
    :return: the encrypted password as a string
    """
    password_len = len(password)
    reverse_password = password[::-1]
    encrypted_password = ""
    for character in reverse_password:
        if character.isalpha():
            character_unicode = ord(character) + password_len
            if character.islower():
                if character_unicode > 122:
                    character_unicode -= 26
                encrypted_password += chr(character_unicode).upper()
            else:
                if character_unicode > 90:
                    character_unicode -= 26
                encrypted_password += chr(character_unicode).lower()
        else:
            encrypted_password += str(abs(int(character) - 10))
    return encrypted_password


def signup():
    """
    signup function will create a user in users.csv file using the following information:
    1. name
    2. username
    3. password
    This function has no input parameters.
    :return: user information as a dictionary
    :return:
    """
    print("\n" + 100 * "-")
    users_dataframe = pd.read_csv(USERS_FILE_ADDRESS)
    while True:
        print("\nTo signup, please enter your details below.")
        name = input("Name: ")
        username = input("Username: ")
        password = input("Password: ")
        if len(name) > NAME_MAXIMUM_LENGTH:
            print(f"The name must be less than {NAME_MAXIMUM_LENGTH} characters! Please try again.")
        if username == "":
            print("\nThe username cannot be empty! Please try again.")
        elif len(username) > USERNAME_MAXIMUM_LENGTH:
            print(f"\nThe username cannot be longer than {USERNAME_MAXIMUM_LENGTH} characters! Please try again.")
        elif username in users_dataframe["username"].values:
            print("\nThe username already exists! Please try again.")
        elif len(password) < PASSWORD_MINIMUM_LENGTH:
            print(f"\nThe password must be at least {PASSWORD_MINIMUM_LENGTH} characters long! Please try again.")
        elif len(password) > PASSWORD_MAXIMUM_LENGTH:
            print(f"\nThe password cannot be longer than {PASSWORD_MAXIMUM_LENGTH} characters! Please try again.")
        elif not password.isalnum():
            print("\nThe password must only contain letters and numbers! Please try again.")
        elif username == password:
            print("\nThe username and password cannot be the same! Please try again.")
        else:
            break
    encrypted_password = encrypt_password(password=password)
    users_dataframe = users_dataframe.append({"username": username, "encrypted_password": encrypted_password,
                                              "name": name, "number_of_plays": 0,
                                              "number_of_wins": 0, "number_of_losses": 0, "win_rate": 0,
                                              "number_of_rocks": 0, "number_of_papers": 0, "number_of_scissors": 0},
                                             ignore_index=True)
    users_dataframe.to_csv(USERS_FILE_ADDRESS, index=False)
    print("\nYou signed up successfully. you are now logged in :)")
    return {"name": name, "username": username}


def login():
    """
    login function will return the user information if the given username and password are correct.
    This function has no input parameters.
    :return: user information as a dictionary
    """
    print("\n" + 100 * "-")
    users_dataframe = pd.read_csv(USERS_FILE_ADDRESS)
    while True:
        print("\nTo login, please enter your details below.")
        username = input("Username: ")
        password = input("Password: ")
        if username in users_dataframe["username"].values:
            if encrypt_password(password) == \
                    str(users_dataframe.loc[users_dataframe["username"] == username, "encrypted_password"].values[0]):
                print("You logged in successfully :)")
                break
            else:
                print("\nThe password was wrong! Please try again.")
        else:
            print("\nThe username was not found! Please try again.")
    name = users_dataframe.loc[users_dataframe["username"] == username, "name"].values[0]
    return {"name": name, "username": username}


def logout():
    """
    logout function will just print a message.
    This function has no input parameters and return values.
    :return: None
    """
    print("You logged out successfully :)")
    return


def display_scoreboard():
    """
    display_dashboard function will draw a table that contains information about users.
    Users in the dashboard are ranked based on their win rate amount.
    This function has no input parameters and return values.
    :return: None
    """
    print("\n" + 100 * "-")
    users_dataframe = pd.read_csv(USERS_FILE_ADDRESS)
    if users_dataframe.empty:
        print("\nThe scoreboard is empty.")
        return
    print("Scoreboard (based on win rate):")
    users_dataframe = users_dataframe.sort_values(by=["win_rate"], ascending=False)
    columns = ["Rank", "Name", "Username", "Win Rate", "Number of Plays", "Number of Wins", "Number of Losses"]
    rows = []
    rank = 0
    previous_win_rate = INF
    for index, row in users_dataframe.iterrows():
        if previous_win_rate > row["win_rate"]:
            rank += 1
            previous_win_rate = row["win_rate"]
        rows.append([rank, row["name"], row["username"],
                     str(row["win_rate"])+"%" if row["number_of_plays"] > 0 else "N/A",
                     row["number_of_plays"], row["number_of_wins"], row["number_of_losses"]])
    table = tt.to_string(rows, columns)
    print(table)
    return


def display_stats(user_information):
    """
    display_stats function will show the user's stats in terms of win rate,
    number of plays, number of wins, and number of losses.
    :param user_information: a dictionary contains name and username of the user
    :return: None
    """
    print("\n" + 100 * "-")
    users_dataframe = pd.read_csv(USERS_FILE_ADDRESS)
    user_row = users_dataframe.loc[users_dataframe["username"] == user_information["username"]]
    print(f"\nDear {user_information['name']}, your stats are as follows:")
    number_of_plays = user_row["number_of_plays"].values[0]
    number_of_wins = user_row["number_of_wins"].values[0]
    number_of_losses = user_row["number_of_losses"].values[0]
    win_rate = user_row["win_rate"].values[0] if number_of_plays > 0 else "N/A"
    columns = ["Measure", "Value"]
    rows = [["Number of Plays", number_of_plays], ["Number of Wins", number_of_wins],
            ["Number of Losses", number_of_losses], ["Win Rate", win_rate]]
    table = tt.to_string(rows, columns)
    print(table)
    return
