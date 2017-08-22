"""Cribbage score conditions used during and after rounds."""
from itertools import combinations
from abc import ABCMeta, abstractmethod
from collections import namedtuple


class ScoreCondition(metaclass=ABCMeta):
    """Abstract Base Class"""

    def __init__(self):
        pass

    @abstractmethod
    def check(self, hand):
        raise NotImplementedError


class HasPairTripleQuad(ScoreCondition):
    def check(self, cards):
        description = None
        pair_rank = ""
        same, score = 0, 0
        if len(cards) > 1:
            last = cards[-4:][::-1]
            while same == 0 and last:
                if all(card.rank['name'] == last[0].rank['name'] for card in last):
                    same = len(last)
                    pair_rank = last[0].rank['symbol']
                last.pop()
            if same == 2:
                score = 2
                description = "Pair (%s)" % pair_rank
            elif same == 3:
                score = 6
                description = "Pair Royal (%s)" % pair_rank
            elif same == 4:
                score = 12
                description = "Double Pair Royal (%s)" % pair_rank
        return score, description


class ExactlyEqualsN(ScoreCondition):

    def __init__(self, n):
        self.n = n
        super().__init__()

    def check(self, cards):
        value = sum(i.get_value() for i in cards)
        score = 2 if value == self.n else 0
        description = "%d count" % self.n if score else ""
        return score, description


class HasStraight_InHand(ScoreCondition):

    @staticmethod
    def _enumerate_straights(cards):
        potential_straights = []
        straights = []
        straights_deduped = []
        if cards:
            for i in range(3,len(cards)+1):
                potential_straights += list(combinations(cards, i))
            for p in potential_straights:
                rank_set = set([card.rank['rank'] for card in p])
                if ((max(rank_set) - min(rank_set) + 1) == len(p) == len(rank_set)):
                    straights.append(set(p))
            for s in straights:
                subset = False
                for o in straights:
                    if s.issubset(o) and s is not o:
                        subset = True
                if not subset:
                    straights_deduped.append(s)
        return straights_deduped

    @classmethod
    def check(cls, cards):
        description = ""
        points = 0
        straights = cls._enumerate_straights(cards)
        for s in straights:
            assert len(s) >= 3, "Straights must be 3 or more cards."
            description += "%d-card straight " % len(s)
            points += len(s)
        return points, description


class HasStraight_DuringPlay(ScoreCondition):

    @staticmethod
    def _is_straight(cards):
        rank_set = set([card.rank['rank'] for card in cards])
        return ((max(rank_set) - min(rank_set) + 1) == len(cards) == len(rank_set)) if len(cards) > 2 else False

    @classmethod
    def check(cls, cards):
        description = ""
        card_set = cards[:]
        while card_set:
            if cls._is_straight(card_set):
                description = "%d-card straight" % len(card_set)
                return len(card_set), description
            card_set.pop(0)
        return 0, description

class CountCombinationsEqualToN(ScoreCondition):
    def __init__(self, n):
        self.n = n
        super().__init__()

    def check(self, cards):
        n_counts, score = 0, 0
        cmb_list = []
        card_values = [card.get_value() for card in cards]
        for i in range(len(card_values)):
            cmb_list += list(combinations(card_values, i + 1))
        for i in cmb_list:
            n_counts += 1 if sum(i) == self.n else 0
        description = "%d unique %d-counts" % (n_counts, self.n) if n_counts else ""
        score = n_counts * 2
        return score, description


class HasFlush(ScoreCondition):
    def check(self, cards):
        card_suits = [card.get_suit() for card in cards]
        suit_count = card_suits.count(cards[-1].get_suit())
        score = suit_count if suit_count >= 4 else 0
        assert score < 6, "Flush score exceeded 5"
        description = "" if score < 4 else ("%d-card flush" % score)
        return score, description
