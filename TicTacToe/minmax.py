from player import Player
from heuristic import simple_score


class MinMaxAgent(Player):
    def __init__(self, token, depth=3, heuristic_fun=simple_score):
        super().__init__(token)
        self.depth = depth
        self.heuristic_fun = heuristic_fun

    def make_decision(self, map):
        raise NotImplementedError


