import unittest
import scoring
import playingcards as pc


class TestPairScoring(unittest.TestCase):
    def setUp(self):
        pass

    def test_pair_pair(self):
        s = scoring.HasPairTripleQuad()
        hand = []
        for i in pc.Deck.RANKS.keys():
            hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS[i]))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        score, _ = s.check(hand)
        self.assertEqual(score, 2)

    def test_pair_triple(self):
        s = scoring.HasPairTripleQuad()
        hand = []
        for i in pc.Deck.RANKS.keys():
            hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS[i]))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']))
        score, _ = s.check(hand)
        self.assertEqual(score, 6)

    def test_pair_quadruple(self):
        s = scoring.HasPairTripleQuad()
        hand = []
        for i in range(6):
            hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['two']))
        score, _ = s.check(hand)
        self.assertEqual(score, 12)

    def test_pair_nothing(self):
        s = scoring.HasPairTripleQuad()
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
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['eight'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 0)
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 0)

    def test_pair_minimumcards(self):
        s = scoring.HasPairTripleQuad()
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 2)
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 6)
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 12)


class TestExactlyEqualsN(unittest.TestCase):
    def setUp(self):
        pass

    def test_ExactlyEqualsN15_count_is_equal(self):
        s = scoring.ExactlyEqualsN(n=15)
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['ace']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['five'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 2)

    def test_ExactlyEqualsN15_count_is_less_than(self):
        s = scoring.ExactlyEqualsN(n=15)
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['five'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 0)

    def test_ExactlyEqualsN15_count_is_greater_than(self):
        s = scoring.ExactlyEqualsN(n=15)
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['ace']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['five'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 0)

    def test_ExactlyEqualsN15_one_card(self):
        s = scoring.ExactlyEqualsN(n=15)
        hand = [pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['ace'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 0)

    def test_ExactlyEqualsN31_count_is_equal(self):
        s = scoring.ExactlyEqualsN(n=31)
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['ace']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['jack']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['queen']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['ace'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 2)

    def test_ExactlyEqualsN31_count_is_less_than(self):
        s = scoring.ExactlyEqualsN(n=31)
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['ace']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['jack']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['queen'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 0)

    def test_ExactlyEqualsN31_count_is_greater_than(self):
        s = scoring.ExactlyEqualsN(n=31)
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['ace']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['jack']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['queen']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['two'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 0)


class TestHasStraight_DuringPlay(unittest.TestCase):

    def setUp(self):
        self.s = scoring.HasStraight_DuringPlay()

    def test_HasStraight_DuringPlay_2card(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['five'])]
        score, _ = self.s.check(hand)
        self.assertEqual(score, 0)

    def test_HasStraight_DuringPlay_3card(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['six'])]
        score, _ = self.s.check(hand)
        self.assertEqual(score, 3)

    def test_HasStraight_DuringPlay_4card(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['two']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['six']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['seven'])]
        score, _ = self.s.check(hand)
        self.assertEqual(score, 4)

    def test_HasStraight_DuringPlay_3card_after_broken(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['two']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['six']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['seven']),
                pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['five'])]
        score, _ = self.s.check(hand)
        self.assertEqual(score, 3)

    def test_HasStraight_DuringPlay_6card_outoforder(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['two']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['six']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['seven']),
                pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['three'])]
        score, _ = self.s.check(hand)
        self.assertEqual(score, 6)

    def test_HasStraight_DuringPlay_4card_broken(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['six']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['seven']),
                pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['two'])]
        score, _ = self.s.check(hand)
        self.assertEqual(score, 0)

    def test_HasStraight_DuringPlay_12card(self):
        hand = []
        for rank in pc.Deck.RANKS:
            hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS[rank]))
        score, _ = self.s.check(hand)
        self.assertEqual(score, 13)


class TestHasStraight_InHand(unittest.TestCase):

    def setUp(self):
        self.s = scoring.HasStraight_InHand()

    def test_HasStraight_InHand_2card(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['five'])]
        score, _ = self.s.check(hand)
        self.assertEqual(score, 0)

    def test_HasStraight_InHand_3card(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['six'])]
        score, _ = self.s.check(hand)
        self.assertEqual(score, 3)

    def test_HasStraight_InHand_4card(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['two']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['six']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['seven'])]
        score, _ = self.s.check(hand)
        self.assertEqual(score, 4)

    def test_HasStraight_InHand_Double_4_Straight(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['two']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['six']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['seven']),
                pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['five'])]
        score, _ = self.s.check(hand)
        self.assertEqual(score, 8)

    def test_HasStraight_InHand_6card_outoforder(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['two']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['six']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['seven']),
                pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['three'])]
        score, _ = self.s.check(hand)
        self.assertEqual(score, 6)

    def test_HasStraight_InHand_4card_broken(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['six']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['seven']),
                pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['two'])]
        score, _ = self.s.check(hand)
        self.assertEqual(score, 4)

    def test_HasStraight_InHand_ThreePairs(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['four']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['four']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['six']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['six']),
                pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['two'])]
        score, _ = self.s.check(hand)
        self.assertEqual(score, 24)

    def test_HasStraight_InHand_NoStraight(self):
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['two']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['four']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['six']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['eight']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['ten']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['queen'])]
        score, _ = self.s.check(hand)
        self.assertEqual(score, 0)

    def test_HasStraight_InHand_EmptyHand(self):
        hand = []
        score, _ = self.s.check(hand)
        self.assertEqual(score, 0)

    def test_HasStraight_InHand_12card(self):
        hand = []
        for rank in pc.Deck.RANKS:
            hand.append(pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS[rank]))
        score, _ = self.s.check(hand)
        self.assertEqual(score, 13)



class TestCountCombinationsEqualToN(unittest.TestCase):
    def setUp(self):
        pass

    def test_CountCombinationsEqualToN_one(self):
        s = scoring.CountCombinationsEqualToN(n=15)
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['ace']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['five'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 2)

    def test_CountCombinationsEqualToN_two_overlapping(self):
        s = scoring.CountCombinationsEqualToN(n=15)
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['ace']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['five'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 4)

    def test_CountCombinationsEqualToN_two_nonoverlapping(self):
        s = scoring.CountCombinationsEqualToN(n=15)
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['spades'], rank=pc.Deck.RANKS['ace']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['seven']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['eight'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 4)


class TestHasFlush(unittest.TestCase):
    def setUp(self):
        pass

    def test_HasFlush_four_card_flush(self):
        s = scoring.HasFlush()
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['ace']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['jack'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 4)

    def test_HasFlush_five_card_flush(self):
        s = scoring.HasFlush()
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['ace']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['jack']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['two'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 5)

    def test_HasFlush_three_card_non_flush(self):
        s = scoring.HasFlush()
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['jack']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['two'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 0)

    def test_HasFlush_four_card_old_flush(self):
        """Tests to make sure latest card must be part of flush"""
        s = scoring.HasFlush()
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['ace']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['jack']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['two'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 0)

    def test_HasFlush_four_card_split_flush(self):
        s = scoring.HasFlush()
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['ace']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['two']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['jack'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 4)

    def test_HasFlush_five_card_split_flush(self):
        s = scoring.HasFlush()
        hand = [pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['nine']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['ace']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['king']),
                pc.Card(suit=pc.Deck.SUITS['clubs'], rank=pc.Deck.RANKS['ace']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['five']),
                pc.Card(suit=pc.Deck.SUITS['diamonds'], rank=pc.Deck.RANKS['two']),
                pc.Card(suit=pc.Deck.SUITS['hearts'], rank=pc.Deck.RANKS['jack'])]
        score, _ = s.check(hand)
        self.assertEqual(score, 5)


if __name__ == '__main__':
    unittest.main()
