from playerAgent import Player
from heuristic import simple_score
from game import convert_index_to_coordinates


class MinMaxAgent(Player):
    def __init__(self, my_token, in_row_to_win, depth=4, heuristic_fun=simple_score):
        super().__init__(my_token)
        self.in_row_to_win = in_row_to_win
        self.depth = depth
        self.heuristic_fun = heuristic_fun

    def make_decision(self, map):
        best_move, _ = self.minmax(map, depth=self.depth)

        col, row = convert_index_to_coordinates(best_move)

        return col, row

    def minmax(self, map, depth=4, maximizing=True):
        """returns index in map array"""
        raise NotImplementedError
