from utils.game import Game
from utils.dice import Dice

# get the inputs
input_max_turn = int(input("How many turns?:\n"))


# initiate a dice block
my_dice = Dice()

# initate a game
my_game = Game("Game 1", input_max_turn, my_dice)

# take a turn
while len(my_game.scores) < my_game.max_turns:
    input("➡️ Press Enter for the next turn:\n")
    my_game.take_turn()

    # show the current score
    my_game.get_total_score()

# show total score
print("🏁 Game finished")
my_game.get_total_score()

input("Game finshed. Press any key to exit")

pass