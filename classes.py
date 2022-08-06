import random

import pandas as pd

from settings import USERS_FILE_ADDRESS, GAME_STRATEGIES, GAME_MODES, ALPHA


class RockPaperScissorsGame:
    """

    """
    def __init__(self, username_information):
        self.user_information = username_information
        self.game_mode = None
        self.score_limit = None
        self.user_score = 0
        self.computer_score = 0
        self.user_strategy = None
        self.computer_strategy = None
        self.number_of_played_strategies = {"Rock": 0, "Paper": 0, "Scissors": 0}
        return

    def update_scores(self):
        """
        update_scores function will update user and computer scores after each round of game.
        :return: None
        """
        if self.user_strategy == self.computer_strategy:
            print("It was a tie!")
        elif self.user_strategy == 1 and self.computer_strategy == 2:
            self.computer_score += 1
            print("Computer won!")
        elif self.user_strategy == 1 and self.computer_strategy == 3:
            self.user_score += 1
            print("You won!")
        elif self.user_strategy == 2 and self.computer_strategy == 1:
            self.user_score += 1
            print("You won!")
        elif self.user_strategy == 2 and self.computer_strategy == 3:
            self.computer_score += 1
            print("Computer won!")
        elif self.user_strategy == 3 and self.computer_strategy == 1:
            self.computer_score += 1
            print("Computer won!")
        elif self.user_strategy == 3 and self.computer_strategy == 2:
            self.user_score += 1
            print("You won!")
        return

    def update_user_stats(self):
        """
        update_user_stats function will update user stats after each game.
        :return: None
        """
        users_dataframe = pd.read_csv(USERS_FILE_ADDRESS)
        users_dataframe.loc[users_dataframe["username"] == self.user_information["username"], "number_of_rocks"] += \
            self.number_of_played_strategies["Rock"]
        users_dataframe.loc[users_dataframe["username"] == self.user_information["username"], "number_of_papers"] += \
            self.number_of_played_strategies["Paper"]
        users_dataframe.loc[users_dataframe["username"] == self.user_information["username"], "number_of_scissors"] += \
            self.number_of_played_strategies["Scissors"]
        users_dataframe.loc[users_dataframe["username"] == self.user_information["username"], "number_of_plays"] += 1
        if self.user_score > self.computer_score:
            print("\n" + 50 * "*")
            print("\nCongratulation, you won the game!")
            users_dataframe.loc[users_dataframe["username"] == self.user_information["username"], "number_of_wins"] += 1
        else:
            print("\n" + 50 * "*")
            print("\nUnfortunately, you lost the game :(")
            users_dataframe.loc[users_dataframe["username"] == self.user_information["username"],
                                "number_of_losses"] += 1
        users_dataframe.loc[users_dataframe["username"] == self.user_information["username"], "win_rate"] = \
            users_dataframe.loc[users_dataframe["username"] == self.user_information["username"], "number_of_wins"] / \
            users_dataframe.loc[users_dataframe["username"] == self.user_information["username"],
                                "number_of_plays"] * 100
        users_dataframe.to_csv(USERS_FILE_ADDRESS, index=False)
        return

    def obtain_computer_strategy(self):
        """
        obtain_computer_strategy will obtain the computer strategy based on the game modes (easy or hard).
        In the easy mode, a random strategy is chosen, while in the hard mode a simple statistical method is
        used to select a strategy based on the user's previous strategies.
        :return: None
        """
        if self.game_mode == 1:
            self.computer_strategy = random.randint(1, 3)
        else:
            random_value = random.random()
            if random_value < ALPHA:
                self.computer_strategy = random.randint(1, 3)
            else:
                users_dataframe = pd.read_csv(USERS_FILE_ADDRESS)
                number_of_rocks = \
                    users_dataframe.loc[users_dataframe["username"] == self.user_information["username"],
                                        "number_of_rocks"].values[0] + self.number_of_played_strategies["Rock"]
                number_of_papers = \
                    users_dataframe.loc[users_dataframe["username"] == self.user_information["username"],
                                        "number_of_papers"].values[0] + self.number_of_played_strategies["Paper"]
                number_of_scissors = \
                    users_dataframe.loc[users_dataframe["username"] == self.user_information["username"],
                                        "number_of_scissors"].values[0] + self.number_of_played_strategies["Scissors"]
                if number_of_rocks >= number_of_papers and number_of_rocks >= number_of_scissors:
                    self.computer_strategy = 2
                elif number_of_papers > number_of_rocks and number_of_papers >= number_of_scissors:
                    self.computer_strategy = 3
                else:
                    self.computer_strategy = 1
        return

    def play(self):
        """
        play function will start and play the game for the user.
        :return: None
        """
        print("\n" + 100 * "-")
        print("\nLet's play rock, paper, scissors!")
        print("\n" + 50 * "*")
        while True:
            score_limit = input(f"\nDear {self.user_information['name']}, enter the score limit: ")
            if score_limit.isdigit() and int(score_limit) > 0:
                self.score_limit = int(score_limit)
                break
            else:
                print("\nPlease enter a valid score limit greater that zero!")
        print("\n" + 50 * "*")
        print("\nGame modes:")
        for game_mode_number, game_mode_name in GAME_MODES.items():
            print(f"{game_mode_number}. {game_mode_name}")
        while True:
            game_mode = input(f"\nDear {self.user_information['name']}, enter the game mode: ")
            if game_mode.isdigit() and int(game_mode) in GAME_MODES.keys():
                self.game_mode = int(game_mode)
                break
            else:
                print("\nPlease enter a valid game mode!")
        round_number = 0
        while self.user_score < self.score_limit and self.computer_score < self.score_limit:
            round_number += 1
            print("\n" + 50 * "*")
            print(f"\nRound {round_number}\n")
            while True:
                for game_strategy, game_strategy_name in GAME_STRATEGIES.items():
                    print(f"{game_strategy}. {game_strategy_name}")
                user_strategy = input("Enter your strategy: ")
                if user_strategy not in ["1", "2", "3"]:
                    print("\nPlease enter a valid strategy!")
                else:
                    self.user_strategy = int(user_strategy)
                    self.number_of_played_strategies[GAME_STRATEGIES[self.user_strategy]] += 1
                    break
            self.obtain_computer_strategy()
            print(f"\nYour strategy was {GAME_STRATEGIES[self.user_strategy]}, "
                  f"the computer strategy was {GAME_STRATEGIES[self.computer_strategy]}!")
            self.update_scores()
            print(f"\nYour score: {self.user_score}")
            print(f"Computer's score: {self.computer_score}")
        self.update_user_stats()
        return
