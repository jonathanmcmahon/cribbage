class ScoreCondition():

    def __init__(self):
        pass

    def check(self, hand):
        raise NotImplementedError


class JackStarter(ScoreCondition):

    description = "his heels"
    points = 2

    def check(self, game):
        if game.starter.rank['name'] == 'jack' and self.player == game.dealer:
            return self.condition_met()
        return 0


class PairTripleQuad(ScoreCondition):

    def check(self, table):
        description = None
        same, score = 0, 0
        if len(table) > 1:
            last = table[-4:][::-1]
            while same == 0 and last:
                if all(card.rank['name'] == last[0].rank['name'] for card in last):
                    same = len(last)
                last.pop()
        if same == 2:
            score = 2
            description = "pair"
        elif same == 3:
            score = 6
            description = "pair royal"
        elif same == 4:
            score = 12
            description = "double pair royal"
        return score, description


class FifteenCount(ScoreCondition):

    def check(self, table):
        description = "Fifteen count"
        value = sum(0 + i.value() for i in table)
        score = 2 if value == 15 else 0
        return score, description


class ThirtyOneCount(ScoreCondition):

    def check(self, table):
        description = "Thirty-one count"
        value = sum(0 + i.value() for i in table)
        score = 2 if value == 31 else 0
        return score, description

