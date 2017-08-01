import unittest
from cribbage.playingcards import Card, Deck

class TestCardClass(unittest.TestCase):

    def setUp(self):
        self.card = Card(rank=Deck.RANKS[0], suit=Deck.SUITS[0])

    def test_to_str(self):
        self.assertEqual(str(self.card), 'A♥')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

class TestDeckClass(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_deck_size(self):
        self.assertEqual(len(self.deck.cards), 52)

    def test_to_str(self):
        self.assertEqual(str(self.deck), 'A♥ 2♥ 3♥ 4♥ 5♥ 6♥ 7♥ 8♥ 9♥ 10♥ J♥ Q♥ K♥ A♦ 2♦ 3♦ 4♦ 5♦ 6♦ 7♦ 8♦ 9♦ 10♦ J♦ Q♦ K♦ A♣ 2♣ 3♣ 4♣ 5♣ 6♣ 7♣ 8♣ 9♣ 10♣ J♣ Q♣ K♣ A♠ 2♠ 3♠ 4♠ 5♠ 6♠ 7♠ 8♠ 9♠ 10♠ J♠ Q♠ K♠ ')

    def test_shuffle(self):
        preshuffle = str(self.deck.cards)
        self.assertEqual(preshuffle, str(self.deck.cards))
        self.deck.shuffle()
        self.assertNotEqual(preshuffle, str(self.deck.cards))



if __name__ == '__main__':
    unittest.main()