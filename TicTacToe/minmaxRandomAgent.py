import math
import random

from minmaxAgent import MinMaxAgent
from game import convert_index_to_coordinates, get_possible_moves


class MinMaxRandomAgent(MinMaxAgent):
    def __init__(self,  my_token, in_row_to_win, depth=4, default_token=0, rand_threshold=0.5, if_print=True):
        super().__init__(my_token, in_row_to_win, depth, default_token)
        self.rand_threshold = rand_threshold
        self.maps = []
        self.if_print = if_print

    def make_decision(self, map):
        self.size = int(math.sqrt(len(map)))

        rand_value = random.random()
        if self.if_print:
            print(rand_value)
        if rand_value < self.rand_threshold:
            if self.if_print:
                print("rand")
            moves = get_possible_moves(map)
            index = random.randint(0, len(moves) - 1)
            move = moves[index]
            if self.if_print:
                print(move)
            self.save_map(map, move)
            return convert_index_to_coordinates(move, self.size)
        else:
            if self.if_print:
                print("minmax")
            best_move, val = self.minmax(map, depth=self.depth)
            if self.if_print:
                print(best_move)
            self.save_map(map, best_move)
            return convert_index_to_coordinates(best_move, self.size)

    def save_map(self, map, move):
        map[move] = 1
        self.maps.append(map)
