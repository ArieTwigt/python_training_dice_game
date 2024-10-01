from utils.dice import Dice

class Game:

    # constructor
    def __init__(self, 
                 name: str, 
                 max_turns: int, 
                 selected_dice: Dice):
        self.name = name
        self.max_turns = max_turns
        self.selected_dice = selected_dice
        self.scores = []

    # method to get a score
    def take_turn(self):
        # check if there are turns left
        if len(self.scores) >= self.max_turns:
            print("🏁 The game is already over.")
        else:
            # throw the dice
            score = self.selected_dice.throw()
            print(f"You threw: 🎲 {score}")

            # add to the list of scores
            self.scores.append(score)


    # method to get the total score
    def get_total_score(self):
        total_score = sum(self.scores)
        print(f"Total score: {total_score}")





    pass