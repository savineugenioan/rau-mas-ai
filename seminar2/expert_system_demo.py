import numpy as np
from rules import RULES, M, N

class World:
    def __init__(self, n, m):
        self.world = np.zeros((n, m))

    def add_obstacle(self, x, y, dx, dy):
        self.world[x:x+dx, y:y+dy] = 1

class Agent:
    def __init__(self, world, rules=None):
        self.world = world
        self.rules = rules
        self.direction = None
        self.current_position = None
        self.next_position = None
        self.path = []
        self.tried_rules = []

    def set_rules(self, rules):
        self.rules = rules

    def get_input(self):
        user_input = input("Where would you like me to go?\n")
        user_input = list(map(lambda x: int(x), user_input.split(" ")))
        self.navigate(user_input)

    def navigate(self, destination):
        print("..Off I go...")
        while self.current_position != destination:
            self.move()
        print(f"..I'm here: {self.current_position}. I took the following route: {self.path}")

    def move(self):
        while len(self.tried_rules) != len(self.rules):
            for rule_index, rule in enumerate(self.rules):
                fired = self.validate_rule(rule)
                if fired:
                    self.apply_consequent(rule)
                    self.tried_rules.append(rule_index)
                    if rule.consequent.position:
                        print(f"..Moving by {rule.consequent.position} to the {rule.antecedent.direction}")
                    else:
                        print(f"..Changing my direction to {rule.consequent.direction}")
                    self.tried_rules = []
                    break
                else:
                    print("--Bummer! I couldn't do anything... I'm trying a new move...")
                    self.tried_rules.append(rule_index)

    def validate_rule(self, rule):
        antecedent_ok = True
        current_position_x = self.current_position[0]
        current_position_y = self.current_position[1]
        if rule.antecedent.world[0] < 0 and current_position_x + rule.antecedent.world[0] >= 0:
            if self.direction != rule.antecedent.direction or \
                self.world.world[self.current_position[0] + rule.antecedent.world[0], self.current_position[1] + rule.antecedent.world[1]] != rule.antecedent.world[2]:
                    antecedent_ok = False
        elif rule.antecedent.world[0] > 0 and current_position_x + rule.antecedent.world[0] < M:
            if self.direction != rule.antecedent.direction or \
                self.world.world[self.current_position[0] + rule.antecedent.world[0], self.current_position[1] + rule.antecedent.world[1]] != rule.antecedent.world[2]:
                    antecedent_ok = False
        elif rule.antecedent.world[1] < 0 and current_position_y + rule.antecedent.world[1] >= 0:
            if self.direction != rule.antecedent.direction or \
                self.world.world[self.current_position[0] + rule.antecedent.world[0], self.current_position[1] + rule.antecedent.world[1]] != rule.antecedent.world[2]:
                    antecedent_ok = False
        elif rule.antecedent.world[1] > 0 and current_position_y + rule.antecedent.world[1] < N:
            if self.direction != rule.antecedent.direction or \
                self.world.world[self.current_position[0] + rule.antecedent.world[0], self.current_position[1] + rule.antecedent.world[1]] != rule.antecedent.world[2]:
                    antecedent_ok = False
        return antecedent_ok

    def apply_consequent(self, rule):
        if rule.consequent.direction is not None:
            self.direction = rule.consequent.direction
        if rule.consequent.position is not None:
            self.path.append(self.current_position)
            self.current_position = (
                self.current_position[0] + rule.consequent.position[0],
                self.current_position[1] + rule.consequent.position[1]
            )


if __name__ == "__main__":
    world_size = (N, M)
    world = World(*world_size)
    world.add_obstacle(10, 10, 4, 4)
    agent = Agent(world, RULES)
    agent.current_position = (15, 11)
    agent.direction = "left"
    agent.get_input()
