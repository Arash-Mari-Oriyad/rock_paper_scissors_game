from classes import RockPaperScissorsGame
from utils import check_users_file, signup, login, logout,\
    display_first_menu, display_second_menu, display_scoreboard, display_stats


def main():
    """
    main function will be called when the program starts.
    It first checks if the users file exists. If not, it will create it.
    Then it will display the first menu and call the appropriate functions based on the user's option.
    This process will continue until the user chooses to exit.
    This function has no input parameters and no return value.
    :return: None
    """
    check_users_file()
    is_logged_in = False
    user_information = None
    print("Welcome to Rock, Paper, and Scissors Game :)")
    while True:
        if not is_logged_in:
            option = display_first_menu()
            if option == "Sign up":
                user_information = signup()
                if user_information is not None:
                    is_logged_in = True
            elif option == "Login":
                user_information = login()
                if user_information is not None:
                    is_logged_in = True
            elif option == "Scoreboard":
                display_scoreboard()
            elif option == "Exit":
                print("See you soon, bye :)")
                break
        else:
            option = display_second_menu(user_information=user_information)
            if option == "Play":
                game = RockPaperScissorsGame(user_information)
                game.play()
            elif option == "Stats":
                display_stats(user_information=user_information)
            elif option == "Scoreboard":
                display_scoreboard()
            elif option == "Logout":
                logout()
                is_logged_in = False
            elif option == "Exit":
                print("See you soon, bye :)")
                break
    return


if __name__ == "__main__":
    main()
