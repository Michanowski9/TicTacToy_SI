import copy
import math

import numpy as np

from model_definition import build_model, get_hyperparams
from playerAgent import Player
from game import convert_index_to_coordinates, get_possible_moves


class NeuronNetworkAgent(Player):
    def __init__(self, my_token):
        super().__init__(my_token)

        hp = get_hyperparams()

        self.model = build_model(hp)
        self.model.load_weights("output/model_best_weights")
        self.model.set_verbose = False

    def make_decision(self, my_map):
        moves = get_possible_moves(my_map)

        best_move = moves[0]
        best_value = 0

        for move in moves:
            moved_map = self.get_moved_map(copy.deepcopy(my_map), move)

            result = self.predict(moved_map)
            # print(moved_map)
            print(result)

            if result > best_value:
                best_value = result
                best_move = move

        map_size = int(math.sqrt(len(my_map)))
        print(best_move)
        print(best_value)
        return convert_index_to_coordinates(best_move, map_size)

    @staticmethod
    def get_moved_map(my_map, move):
        my_map[move] = 1
        return my_map

    def predict(self, data):
        return self.model.predict(np.array(data).reshape(-1, 25))[0][0]
