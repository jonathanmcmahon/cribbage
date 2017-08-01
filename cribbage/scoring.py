class ScoreCondition():

    def __init__(self, player):
        self.player = player
        self.condition_met = False

    def set_condition_met(self):
        if not self.condition_met:
            self.condition_met = True
            print("%s, %s to %s" % (self.description, self.points, self.player.name))
            return self.points
        return 0

    def check(self, game):
        raise NotImplementedError


class JackStarter(ScoreCondition):

    description = "his heels"
    points = 2

    def check(self, game):
        if game.starter.rank['name'] == 'jack' and self.player == game.dealer:
            return self.condition_met()
        return 0


class Pair(ScoreCondition):

    description = "pair"
    points = 2

    def check(self, game):
        return False


class Triple(ScoreCondition):

    description = "pair royal"
    points = 6

    def check(self, game):
        return False


class Quadruple(ScoreCondition):

    description = "double pair royal"
    points = 12

    def check(self, game):
        return False
