import math
import random

from playerAgent import Player
from game import convert_index_to_coordinates, get_possible_moves


class RandomAgent(Player):
    def __init__(self, my_token):
        super().__init__(my_token)

    def make_decision(self, map):
        mapSize = int(math.sqrt(len(map)))

        moves = get_possible_moves(map)

        index = random.randint(0, len(moves) - 1)
        move = moves[index]

        col, row = convert_index_to_coordinates(move, mapSize)

        print("RandomAgent:")
        print("Col: " + str(col))
        print("Row: " + str(row))

        return col, row
