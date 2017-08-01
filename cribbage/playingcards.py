import random


class Deck():

    SUITS = [
        {'name': 'hearts', 'symbol': '♥', 'unicode_flag': 'B'},
        {'name': 'diamonds', 'symbol': '♦', 'unicode_flag': 'C'},
        {'name': 'clubs', 'symbol': '♣', 'unicode_flag': 'D'},
        {'name': 'diamonds', 'symbol': '♠', 'unicode_flag': 'A'}
    ]

    RANKS = [
        {'name': 'ace', 'symbol': 'A', 'value': 14, 'unicode_flag': '1' },
        {'name': 'two', 'symbol': '2', 'value': 2, 'unicode_flag': '2'},
        {'name': 'three', 'symbol': '3', 'value': 3, 'unicode_flag': '3'},
        {'name': 'four', 'symbol': '4', 'value': 4, 'unicode_flag': '4'},
        {'name': 'five', 'symbol': '5', 'value': 5, 'unicode_flag': '5'},
        {'name': 'six', 'symbol': '6', 'value': 6, 'unicode_flag': '6'},
        {'name': 'seven', 'symbol': '7', 'value': 7, 'unicode_flag': '7'},
        {'name': 'eight', 'symbol': '8', 'value': 8, 'unicode_flag': '8'},
        {'name': 'nine', 'symbol': '9', 'value': 9, 'unicode_flag': '9'},
        {'name': 'ten', 'symbol': '10', 'value': 10, 'unicode_flag': 'A'},
        {'name': 'jack', 'symbol': 'J', 'value': 11, 'unicode_flag': 'B'},
        {'name': 'queen', 'symbol': 'Q', 'value': 12, 'unicode_flag': 'D'},
        {'name': 'king', 'symbol': 'K', 'value': 13, 'unicode_flag': 'E'}
    ]

    def __init__(self):
        self.cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.cards.append(Card(rank=rank, suit=suit))
        assert len(self.cards) == 52, "Deck has %i cards" % len(self.cards)

    def __str__(self):
        s = ''
        for card in self.cards:
            s += (str(card) + " ")
        return s

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def cut(self, cut_point):
        if cut_point is None:
            cut_point = random.randrange(len(self.cards))
        self.cards = self.cards[cut_point:] + self.cards[:cut_point]


class Card():

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return str(self.rank['symbol'] + self.suit['symbol'])

    def __repr__(self):
        return str(self)