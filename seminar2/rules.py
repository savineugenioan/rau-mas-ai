# IF () THEN ()
# IF direction = left THEN position = (-1, 0)
class RuleAntecedent:
    def __init__(self, direction=None, world=None):
        self.direction = direction  # up, down, left, right
        self.world = world  # (-1, 0, 0) (-1, 0, 1)


class RuleConsequent:
    def __init__(self, position=None, direction=None):
        self.position = position
        self.direction = direction


class Rule:
    def __init__(self, antecedent, consequent):
        self.antecedent = antecedent
        self.consequent = consequent


M = 30
N = 30

RULES = [
    Rule(
        RuleAntecedent(direction="left", world=(-1, 0, 0)),
        RuleConsequent(position=(-1, 0), direction=None)
    ),
    Rule(
        RuleAntecedent(direction="left", world=(-1, 0, 1)),
        RuleConsequent(position=None, direction="up")
    ),
    Rule(
        RuleAntecedent(direction="up", world=(0, -1, 0)),
        RuleConsequent(position=(0, -1), direction=None)
    ),
    Rule(
        RuleAntecedent(direction="up", world=(0, -1, 1)),
        RuleConsequent(position=None, direction="right")
    ),
    Rule(
        RuleAntecedent(direction="right", world=(1, 0, 0)),
        RuleConsequent(position=(1, 0), direction=None)
    ),
    Rule(
        RuleAntecedent(direction="right", world=(1, 0, 1)),
        RuleConsequent(position=None, direction="down")
    ),
    Rule(
        RuleAntecedent(direction="down", world=(0, 1, 0)),
        RuleConsequent(position=(0, 1), direction=None)
    ),
    Rule(
        RuleAntecedent(direction="down", world=(0, 1, 1)),
        RuleConsequent(position=None, direction="left")
    )
]
