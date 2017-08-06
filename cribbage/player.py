import random


class Player():

    def __init__(self, name):
        self.name = name

    def pick_crib_cards(self, hand):
        raise NotImplementedError

    def play_card(self, hand, table, crib):
        raise NotImplementedError


class RandomPlayer(Player):

    def pick_crib_cards(self, hand):
        return random.sample(hand, 2)

    def play_card(self, hand, table, crib):
        return random.choice(hand)


class HumanPlayer(Player):
    pass