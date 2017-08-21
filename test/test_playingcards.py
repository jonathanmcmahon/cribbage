import unittest
from playingcards import Card, Deck


class TestCardClass(unittest.TestCase):
    def setUp(self):
        rank_ace = Deck.RANKS['ace']
        rank_two = Deck.RANKS['two']
        self.card = Card(rank=Deck.RANKS['ace'], suit=Deck.SUITS['hearts'])
        self.acecard = Card(rank=rank_ace, suit=Deck.SUITS['hearts'])
        self.twocard = Card(rank=rank_two, suit=Deck.SUITS['hearts'])

    def test_to_str(self):
        self.assertEqual(str(self.card), 'A♥')

    def test_lt(self):
        self.assertEqual(self.twocard < self.acecard, False)
        self.assertEqual(self.acecard < self.twocard, True)
        self.assertEqual(self.acecard < self.acecard, False)
        self.assertEqual(self.twocard < 3, True)
        self.assertEqual(self.twocard < 2, False)
        self.assertEqual(self.twocard < -2, False)

    def test_gt(self):
        self.assertEqual(self.twocard > self.acecard, True)
        self.assertEqual(self.acecard > self.twocard, False)
        self.assertEqual(self.acecard > self.acecard, False)
        self.assertEqual(self.twocard > 3, False)
        self.assertEqual(self.twocard > 2, False)
        self.assertEqual(self.twocard > -2, True)

    def test_eq(self):
        self.assertEqual(self.twocard == self.acecard, False)
        self.assertEqual(self.acecard == self.twocard, False)
        self.assertEqual(self.acecard == self.acecard, True)
        self.assertEqual(self.twocard == 3, False)
        self.assertEqual(self.twocard == 2, True)
        self.assertEqual(self.twocard == -2, False)

    def test_add(self):
        self.assertEqual(self.twocard + self.acecard, 3)
        self.assertEqual(self.acecard + self.twocard, 3)
        self.assertEqual(self.acecard + self.acecard, 2)
        self.assertEqual(self.twocard + self.twocard, 4)
        self.assertEqual(self.twocard + 3, 5)


class TestDeckClass(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_deck_size(self):
        self.assertEqual(len(self.deck.cards), 52)

    def test_to_str(self):
        self.assertEqual(str(self.deck),
                         'A♥ 2♥ 3♥ 4♥ 5♥ 6♥ 7♥ 8♥ 9♥ 10♥ J♥ Q♥ K♥ ' +
                         'A♦ 2♦ 3♦ 4♦ 5♦ 6♦ 7♦ 8♦ 9♦ 10♦ J♦ Q♦ K♦ ' +
                         'A♣ 2♣ 3♣ 4♣ 5♣ 6♣ 7♣ 8♣ 9♣ 10♣ J♣ Q♣ K♣ ' +
                         'A♠ 2♠ 3♠ 4♠ 5♠ 6♠ 7♠ 8♠ 9♠ 10♠ J♠ Q♠ K♠ ')

    def test_shuffle(self):
        preshuffle = str(self.deck.cards)
        self.assertEqual(preshuffle, str(self.deck.cards))
        self.deck.shuffle()
        self.assertNotEqual(preshuffle, str(self.deck.cards))


if __name__ == '__main__':
    unittest.main()
