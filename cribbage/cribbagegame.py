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
        self.dealer = random.choice(self.players)
        self.board = CribbageBoard(self.players, self.MAX_SCORE)

    def start(self):
        winner = random.choice(self.players)
        game_score = [0 for p in self.players]
        while max(game_score) < self.MAX_SCORE:
            round = CribbageRound(self, dealer=winner)
            winner = round.play()
            game_score = [self.board.get_score(p) for p in self.players]
            print(self.board)


class CribbageRound():

    def __init__(self, game, dealer):
        # Replenish deck for each round
        self.deck = Deck()
        self.game = game
        self.hands = {player: [] for player in self.game.players}
        self.crib = []
        self.table = []
        self.starter = None
        self.dealer=dealer

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
                for card in cards_to_crib:
                    self.hands[p].remove(card)
        assert len(self.crib) == self.game.CRIB_SIZE, "Crib size is not %s" % self.game.CRIB_SIZE

    def cut(self):
        cut_point = random.randrange(len(self.deck))
        self.deck.cut(cut_point=cut_point)
        print("Cards cut.")

    def play(self):
        loser = None
        self.cut()
        self.deal()
        self.get_crib()
        self.cut()
        self.starter = self.deck.draw()
        if self.starter.get_rank() == 'jack':
            self.game.board.peg(self.dealer, 1)
            print("2 points to %s for his heels." % str(self.dealer))
        active_players = self.game.players[:]
        while active_players:
            for p in self.game.players:
                if p in active_players:
                    card = p.play_card(hand=self.hands[p], table=self.table, crib=self.crib)
                    table_value = sum(i['card'].get_value() for i in self.table) if self.table else 0
                    if card.get_value() + table_value > 31 or card is None:
                        print("Player %s chooses go." % str(p))
                        loser = loser if loser else p
                        active_players.remove(p)
                        # If no one can play any more cards, give point to last player to play a card
                        if len(active_players) == 0:
                            player_of_last_card = self.table[-1]['player']
                            self.game.board.peg(player_of_last_card, 1)
                    else:
                        self.table.append({'player': p, 'card': card })
                        print("Player %s plays %s" % (str(p), str(card)))
                        # Consider cards played by both players when scoring during play
                        assert table_value <= 31, "Value of cards on table must be <= 31 to be eligible for scoring."
                        score = self.update_score(cards=[move['card'] for move in self.table])
                        if score:
                            self.game.board.peg(p, score)
        return loser

    def update_score(self, cards):
        score = 0
        score_scenarios = [scoring.ExactlyEqualsN(n=15), scoring.ExactlyEqualsN(n=31),
                           scoring.HasPairTripleQuad(), scoring.HasStraight()]
        for scenario in score_scenarios:
            s, desc = scenario.check(cards)
            score += s
            print(desc) if desc else None
        return score


class CribbageBoard():

    def __init__(self, players, max_score):
        self.max_score = max_score
        self.pegs = {p: {'front': 0, 'rear': 0} for p in players}

    def __str__(self):
        return str(self.pegs)

    def __repr__(self):
        return str(self)

    def peg(self, player, points):
        assert points > 0, "You must peg 1 or more points."
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