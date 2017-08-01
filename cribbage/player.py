import random

class Player():

    def __init__(self, name):
        self.name = name

    def pick_crib_cards(self, hand):
        raise NotImplementedError

    def get_move(self, game):
        raise NotImplementedError


class RandomPlayer(Player):

    def pick_crib_cards(self, hand):
        return random.sample(hand, 2)

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    pass