import unittest
from player import RandomPlayer
import cribbagegame


class TestCribbageBoard(unittest.TestCase):

    def setUp(self):
        self.players = [RandomPlayer("Player1"), RandomPlayer("Player2")]
        self.board = cribbagegame.CribbageBoard(players=self.players, max_score=121)

    def test_peg(self):
        self.board.peg(self.players[0], 100)
        self.assertEqual(self.board.pegs[self.players[0]]['front'], 100)
        self.assertEqual(self.board.pegs[self.players[0]]['rear'], 0)

    def test_peg_leapfrog(self):
        self.board.peg(self.players[0], 100)
        self.board.peg(self.players[0], 5)
        self.assertEqual(self.board.pegs[self.players[0]]['front'], 105)
        self.assertEqual(self.board.pegs[self.players[0]]['rear'], 100)


class TestCribbageRound(unittest.TestCase):

    def setUp(self):
        self.game = cribbagegame.CribbageGame()
        self.round = cribbagegame.CribbageRound(self.game)

    def test_get_crib(self):
        self.round.deal()
        self.round.get_crib()

    def test_cut(self):
        self.round.cut()


if __name__ == '__main__':
    unittest.main()