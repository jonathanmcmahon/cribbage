import random
import scoring
from player import HumanPlayer, RandomPlayer
from playingcards import Deck


class CribbageGame():

    MAX_SCORE = 121
    CRIB_SIZE = 4
    N_GO = 31

    def __init__(self):
        self.players = [RandomPlayer("Player1"), RandomPlayer("Player2")]
        self.score = {player: 0 for player in self.players}
        self.dealer = random.choice(self.players)
        self.board = CribbageBoard(self.players, self.MAX_SCORE)

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
        self.table = []

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
            if not set(cards_to_crib).issubset(set(self.hands[p])):
                raise IllegalCardChoiceError("Crib cards selected are not part of player's hand.")
            elif len(cards_to_crib) != 2:
                raise IllegalCardChoiceError("Wrong number of cards sent to crib.")
            else:
                self.crib += cards_to_crib
        assert len(self.crib) == self.game.CRIB_SIZE, "Crib size is not %s" % self.game.CRIB_SIZE

    def cut(self):
        cut_point = random.randrange(len(self.deck))
        self.deck.cut(cut_point=cut_point)
        print("Cards cut.")

    def play(self):
        round_done = False
        self.deal()
        self.get_crib()
        self.cut()
        while not round_done:
            for p in self.game.players:
                card = p.play_card(hand=self.hands[p], table=self.table, crib=self.crib)
                self.table.append(card)
                score, round_done = self.update_score()
                self.game.board.peg(p, score)


    def update_score(self, table):
        pass


class CribbageBoard():

    def __init__(self, players, max_score):
        self.max_score = max_score
        self.pegs = {p: {'front': 0, 'rear': 0} for p in players}

    def peg(self, player, points):
        self.pegs[player]['rear'] = self.pegs[player]['front']
        self.pegs[player]['front'] += points

    def get_score(self, player):
        return self.pegs[player]['front']




class IllegalCardChoiceError(Exception):
    pass



def main():
    game = CribbageGame()
    game.start()


if __name__ == '__main__':
    main()