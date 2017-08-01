import random
import scoring
from player import HumanPlayer, RandomPlayer
from playingcards import Deck


class CribbageGame():

    MAX_SCORE = 121

    def __init__(self):
        self.players = [RandomPlayer("Player1"), RandomPlayer("Player2")]
        self.score = {player: 0 for player in self.players}
        self.dealer = random.choice(self.players)

    def score_hand(self):
        pass

    def card_score(self):
        pass

    def start(self):
        while max(self.score.values()) < self.MAX_SCORE:
            round = CribbageRound(self)
            round.play()


class CribbageRound():

    def __init__(self, game):
        # Replenish deck for each round
        self.deck = Deck()
        self.game = game
        self.hands = {player: [] for player in self.game.players}
        self.crib = []

    def deal(self):
        shuffles = 3  # ACC Rule 2.1
        cards_per_player = 6
        for i in range(shuffles):
            self.deck.shuffle()
        for _ in range(cards_per_player):
            for p in self.game.players:
                self.hands[p].append(self.deck.draw())
        print("Cards dealt.")

    def get_crib(self):
        for p in self.game.players:
            cards_to_crib = p.pick_crib_cards(self.hands[p])
            print("Cards cribbed: %s" % cards_to_crib)
            if not set(cards_to_crib).issubset(set(self.hands[p])) or len(cards_to_crib) != 2:
                raise IllegalCardChoiceError
            else:
                self.crib += cards_to_crib
        assert len(self.crib) == 4

    def cut(self):
        cut_point = random.randrange(len(self.deck))
        self.deck.cut(cut_point=cut_point)
        print("Cards cut.")

    def play(self):
        self.deal()
        self.get_crib()
        self.cut()


class IllegalCardChoiceError(Exception):
    pass


def main():
    game = CribbageGame()
    game.start()


if __name__ == '__main__':
    main()