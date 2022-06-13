import math
import random

from minmaxAgent import MinMaxAgent
from game import convert_index_to_coordinates, get_possible_moves


class MinMaxRandomAgent(MinMaxAgent):
    def __init__(self,  my_token, in_row_to_win, depth=4, default_token=0, rand_threshold=0.5):
        super().__init__(my_token, in_row_to_win, depth, default_token)
        self.rand_threshold = rand_threshold

    def make_decision(self, map):
        self.size = int(math.sqrt(len(map)))

        rand_value = random.random()
        print(rand_value)
        if rand_value < self.rand_threshold:
            print("rand")
            moves = get_possible_moves(map)
            index = random.randint(0, len(moves) - 1)
            return convert_index_to_coordinates(moves[index], self.size)
        else:
            print("minmax")
            best_move, val = self.minmax(map, depth=self.depth)
            return convert_index_to_coordinates(best_move, self.size)

        print("error")
        return 0, 0

