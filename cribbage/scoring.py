from itertools import combinations


class ScoreCondition():

    def __init__(self):
        pass

    def check(self, hand):
        raise NotImplementedError


class HasPairTripleQuad(ScoreCondition):

    def check(self, cards):
        description = None
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
        super()

    def check(self, cards):
        value = sum(i.get_value() for i in cards)
        score = 2 if value == self.n else 0
        description = "%d count" % self.n if score else ""
        return score, description


class HasStraight(ScoreCondition):

    def __is_straight(self, cards):
        rank_set = set([card.rank['rank'] for card in cards])
        return ((max(rank_set) - min(rank_set) + 1) == len(cards) == len(rank_set)) if len(cards) > 2 else False

    def check(self, cards):
        description = ""
        card_set = cards
        while card_set:
            if self.__is_straight(card_set):
                description = "%d-card straight" % len(card_set)
                return len(card_set), description
            card_set.pop(0)
        return 0, description


class CountCombinationsEqualToN(ScoreCondition):

    def __init__(self, n):
        self.n = n
        super()

    def check(self, cards):
        n_counts, score = 0, 0
        cmb_list = []
        card_values = [card.get_value() for card in cards]
        for i in range(len(card_values)):
            cmb_list += list(combinations(card_values, i+1))
        for i in cmb_list:
            n_counts += 1 if sum(i) == self.n else 0;
        description = "%d unique %d-counts" % (n_counts, self.n)
        score = n_counts * 2
        return score, description


class HasFlush(ScoreCondition):

    def check(self, cards):
        n_counts, score = 0, 0
        card_suits = [card.get_suit() for card in cards]
        suit_count = card_suits.count(cards[-1].get_suit())
        score = suit_count if suit_count >= 4 else 0
        assert score < 6, "Flush score exceeded 5"
        description = "" if score < 4 else ("%d-card flush" % score)
        return score, description
