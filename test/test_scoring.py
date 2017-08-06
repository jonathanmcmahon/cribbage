import unittest
import scoring
import playingcards as pc


class TestPairScoring(unittest.TestCase):

    def setUp(self):
        pass

    def test_pair_pair(self):
        s = scoring.PairTripleQuad()
        hand = []
        for i in pc.Deck.RANKS.keys():
            hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS[i]))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        score, _ = s.check(hand)
        self.assertEqual(score, 2)

    def test_pair_triple(self):
        s = scoring.PairTripleQuad()
        hand = []
        for i in pc.Deck.RANKS.keys():
            hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS[i]))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        score, _ = s.check(hand)
        self.assertEqual(score, 6)

    def test_pair_quadruple(self):
        s = scoring.PairTripleQuad()
        hand = []
        for i in range(6):
            hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['two']))
        score, _ = s.check(hand)
        self.assertEqual(score, 12)

    def test_pair_nothing(self):
        s = scoring.PairTripleQuad()
        hand = []
        for i in pc.Deck.RANKS.keys():
            hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS[i]))
        score, _ = s.check(hand)
        self.assertEqual(score, 0)
        hand = []
        for i in pc.Deck.RANKS.keys():
            hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS[i]))
        score, _ = s.check(hand)
        self.assertEqual(score, 0)
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['eight']))
        score, _ = s.check(hand)
        self.assertEqual(score, 0)
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        score, _ = s.check(hand)
        self.assertEqual(score, 0)

    def test_pair_minimumcards(self):
        s = scoring.PairTripleQuad()
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        score, _ = s.check(hand)
        self.assertEqual(score, 2)
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        score, _ = s.check(hand)
        self.assertEqual(score, 6)
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        score, _ = s.check(hand)
        self.assertEqual(score, 12)


class TestFifteenCount(unittest.TestCase):

    def setUp(self):
        pass

    def test_fifteencount_true(self):
        s = scoring.FifteenCount()
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['ace']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['five']))
        score, _ = s.check(hand)
        self.assertEqual(score, 2)

    def test_fifteencount_lessthan(self):
        s = scoring.FifteenCount()
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['five']))
        score, _ = s.check(hand)
        self.assertEqual(score, 0)

    def test_fifteencount_greaterthan(self):
        s = scoring.FifteenCount()
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['ace']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['five']))
        score, _ = s.check(hand)
        self.assertEqual(score, 0)

    def test_fifteencount_singlecard(self):
        s = scoring.FifteenCount()
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['ace']))
        score, _ = s.check(hand)
        self.assertEqual(score, 0)


class TestThirtyOneCount(unittest.TestCase):

    def setUp(self):
        pass

    def test_thirtyonecount_true(self):
        s = scoring.ThirtyOneCount()
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['ace']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['jack']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['queen']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['ace']))
        score, _ = s.check(hand)
        self.assertEqual(score, 2)

    def test_thirtyonecount_lessthan(self):
        s = scoring.ThirtyOneCount()
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['ace']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['jack']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['queen']))
        score, _ = s.check(hand)
        self.assertEqual(score, 0)

    def test_thirtyonecount_greaterthan(self):
        s = scoring.ThirtyOneCount()
        hand = []
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['ace']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['jack']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['queen']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['two']))
        score, _ = s.check(hand)
        self.assertEqual(score, 0)


if __name__ == '__main__':
    unittest.main()