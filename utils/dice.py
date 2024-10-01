import random


class Dice:

    def __init__(self, max_score=6):
        self.max_score = max_score


    # method to throw the dice
    def throw(self):
        # generate the possible scores
        possible_scores = range(1, self.max_score + 1)

        # select a score
        score = random.choice(possible_scores)

        return score