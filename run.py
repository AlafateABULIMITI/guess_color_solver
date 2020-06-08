from game import GameBoard, Player, Game

gameboard = GameBoard(final_state=None, color_pool=[1, 2, 3, 4, 5, 6], color_num=4)
print(gameboard)

p1 = Player("felix")
print(p1)

game = Game(gameboard, p1)

guess = p1.guess(gameboard.color_pool)
print(guess)
gameboard.add_guess(guess)
full_correct, half_correct = gameboard.give_feedback(guess)
gameboard.add_feedback([full_correct, half_correct])
print(full_correct, half_correct)
game.state
