import copy
import math
import random

from playerAgent import Player
from game import convert_index_to_coordinates, get_possible_moves


class NeuronNetworkAgent(Player):
    def __init__(self, my_token):
        super().__init__(my_token)

    def make_decision(self, map):
        mapSize = int(math.sqrt(len(map)))

        moves = get_possible_moves(map)

        best_move = moves[0]
        best_value = 0

        for move in moves:
            # wejscie do sieci neuronowej
            moved_map = self.get_moved_map(copy.deepcopy(map), move)

            # TODO

            # zamiast 0 zamienic na wynik sieci neuronowej
            result = 0  # function(moved_map)

            if result > best_value:
                best_value = result
                best_move = move

        return convert_index_to_coordinates(best_move, mapSize)

    @staticmethod
    def get_moved_map(map, move):
        map[move] = 1
        return map
