import random


class Deck:
    """Deck of cards."""
    SUITS = {
        'hearts': {'name': 'hearts', 'symbol': '♥', 'unicode_flag': 'B'},
        'diamonds': {'name': 'diamonds', 'symbol': '♦', 'unicode_flag': 'C'},
        'clubs': {'name': 'clubs', 'symbol': '♣', 'unicode_flag': 'D'},
        'spades': {'name': 'spades', 'symbol': '♠', 'unicode_flag': 'A'}
    }

    RANKS = {
        'ace': {'name': 'ace', 'symbol': 'A', 'value': 1, 'rank': 1, 'unicode_flag': '1'},
        'two': {'name': 'two', 'symbol': '2', 'value': 2, 'rank': 2, 'unicode_flag': '2'},
        'three': {'name': 'three', 'symbol': '3', 'value': 3, 'rank': 3, 'unicode_flag': '3'},
        'four': {'name': 'four', 'symbol': '4', 'value': 4, 'rank': 4, 'unicode_flag': '4'},
        'five': {'name': 'five', 'symbol': '5', 'value': 5, 'rank': 5, 'unicode_flag': '5'},
        'six': {'name': 'six', 'symbol': '6', 'value': 6, 'rank': 6, 'unicode_flag': '6'},
        'seven': {'name': 'seven', 'symbol': '7', 'value': 7, 'rank': 7, 'unicode_flag': '7'},
        'eight': {'name': 'eight', 'symbol': '8', 'value': 8, 'rank': 8, 'unicode_flag': '8'},
        'nine': {'name': 'nine', 'symbol': '9', 'value': 9, 'rank': 9, 'unicode_flag': '9'},
        'ten': {'name': 'ten', 'symbol': '10', 'value': 10, 'rank': 10, 'unicode_flag': 'A'},
        'jack': {'name': 'jack', 'symbol': 'J', 'value': 10, 'rank': 11, 'unicode_flag': 'B'},
        'queen': {'name': 'queen', 'symbol': 'Q', 'value': 10, 'rank': 12, 'unicode_flag': 'D'},
        'king': {'name': 'king', 'symbol': 'K', 'value': 10, 'rank': 13, 'unicode_flag': 'E'}
    }

    def __init__(self):
        self.cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.cards.append(Card(rank=self.RANKS[rank], suit=self.SUITS[suit]))
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
        len_precut = len(self.cards)
        if cut_point is None:
            cut_point = random.randrange(len(self.cards))
        self.cards = self.cards[cut_point:] + self.cards[:cut_point]
        assert len(self.cards) == len_precut, "Cards lost in cut."


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.tupl = (str(rank['symbol']), str(suit['symbol']))

    def __str__(self):
        return str(self.rank['symbol'] + self.suit['symbol'])

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        if type(other) == Card:
            return self.rank['value'] < other.rank['value']
        elif type(other) == int:
            return self.rank['value'] < other
        else:
            raise NotImplementedError

    def __gt__(self, other):
        if type(other) == Card:
            return self.rank['value'] > other.rank['value']
        elif type(other) == int:
            return self.rank['value'] > other
        else:
            raise NotImplementedError

    def __eq__(self, other):
        if type(other) == Card:
            return self.rank['value'] == other.rank['value']
        elif type(other) == int:
            return self.rank['value'] == other
        else:
            raise NotImplementedError

    def __add__(self, other):
        if type(other) == Card:
            return self.rank['value'] + other.rank['value']
        elif type(other) == int:
            return self.rank['value'] + other
        else:
            raise NotImplementedError

    def get_value(self):
        return self.rank['value']

    def get_suit(self):
        return self.suit['name']

    def get_rank(self):
        return self.rank['name']

    def __hash__(self):
        return hash(self.tupl)
