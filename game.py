import random
import itertools
import sys

random.seed(5)


class GameBoard:
    def __init__(
        self, color_pool, color_num, final_state,
    ):
        self.color_pool = color_pool
        self.color_num = color_num
        self.guesses = []
        self.feedbacks = []
        self.final_state = final_state or self.random_final_state()

    def __repr__(self):
        return f"""
            final_state: {self.final_state}
            color_pool: {self.color_pool}
            color_num: {self.color_num}
            """

    def random_final_state(self):
        return random.sample(self.color_pool, self.color_num)

    def add_guess(self, guess):
        self.guesses.append(guess)

    def add_feedback(self, feedback):
        self.feedbacks.append(feedback)

    def give_feedback(self, guess):
        full_correct = 0
        half_correct = 0
        for i in range(len(guess)):
            if guess[i] == self.final_state[i]:
                full_correct += 1
            elif guess[i] in self.final_state:
                half_correct += 1
        return full_correct, half_correct


class Player:
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __repr__(self):
        return f"player name: {self.name}"

    def guess(self, color_pool):
        input_ = input("your guess: ").rstrip()
        try:
            input_ = list(map(int, input_.split(" ")))
            for num in input_:
                if num not in color_pool:
                    raise IndexError("not in the color range.")
            return input_
        except ValueError:
            print("Please input correctly.")
            sys.exit()


class Game:
    def __init__(self, gameboard, player):
        self.gameboard = gameboard
        self.player = player

    @property
    def state(self):
        if self.gameboard.final_state == self.player.guess:
            print("You win!")
            print(f"Guesses: {self.gameboard.guesses}")
            print(f"Feedbacks: {self.gameboard.feedbacks}")
            sys.exit()
        else:
            return self.gameboard.feedbacks
