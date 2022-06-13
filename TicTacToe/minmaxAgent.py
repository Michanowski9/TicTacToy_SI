import copy
import math

from playerAgent import Player
from game import convert_index_to_coordinates, get_possible_moves, convert_coordinates_to_index


class MinMaxAgent(Player):
    def __init__(self, my_token, in_row_to_win, depth=4, default_token=0):
        super().__init__(my_token)
        self.in_row_to_win = in_row_to_win
        self.depth = depth

        self.default_token = default_token
        self.size = 0

    def make_decision(self, map):
        self.size = int(math.sqrt(len(map)))

        best_move, val = self.minmax(map, depth=self.depth)

        # for tests
        # print("val: " + str(val))

        return convert_index_to_coordinates(best_move, self.size)

    def minmax(self, map, depth=4, maximizing=True):
        moves = get_possible_moves(map)
        if depth == 0 or len(moves) == 0:
            return None, self.get_heuristic(map)
        if self.check_win(map) == 1:
            return None, depth * self.get_heuristic(map)

        best_move = moves[0]

        # for tests
        # if depth == 4:
        #     print(moves)

        if maximizing:
            value = -math.inf
            for move in moves:
                new_map = copy.deepcopy(map)
                new_map[move] = 1
                temp_move, temp_value = self.minmax(new_map, depth-1, False)

                # for tests
                # if depth == 4:
                #     print("move: " + str(move) + " " + str(temp_value))

                if temp_value > value:
                    best_move = move
                    value = temp_value
            return best_move, value
        else:
            value = math.inf
            for move in moves:
                new_map = copy.deepcopy(map)
                new_map[move] = -1
                temp_move, temp_value = self.minmax(new_map, depth-1, True)
                if temp_value < value:
                    best_move = move
                    value = temp_value
            return best_move, value

    def get_heuristic(self, map):
        score = 0
        win_result = self.check_win(map)
        if win_result == -1:
            return -1000
        elif win_result == 1:
            return 1000
        elif win_result == "Draw":
            return 0

        score += self.get_score(map)
        return score

    def check_win(self, map):

        result = self.check_horizontal_loop(map)
        if result != self.default_token:
            return result

        result = self.check_vertical_loop(map)
        if result != self.default_token:
            return result

        result = self.check_slant_right_loop(map)
        if result != self.default_token:
            return result

        result = self.check_slant_left_loop(map)
        if result != self.default_token:
            return result

        if self.check_for_draw(map):
            return "Draw"

        return 0

    def check_horizontal_loop(self, map):
        for col in range(self.size - self.in_row_to_win + 1):
            for row in range(self.size):
                temp = self.count_horizontal(map, row, col)
                if temp == self.in_row_to_win or temp == -self.in_row_to_win:
                    return map[convert_coordinates_to_index(col, row, self.size)]
        return 0

    def check_vertical_loop(self, map):
        for col in range(self.size):
            for row in range(self.size - self.in_row_to_win + 1):
                temp = self.count_vertical(map, row, col)
                if temp == self.in_row_to_win or temp == -self.in_row_to_win:
                    return map[convert_coordinates_to_index(col, row, self.size)]
        return 0

    def check_slant_right_loop(self, map):
        for col in range(self.size - self.in_row_to_win + 1):
            for row in range(self.size - self.in_row_to_win + 1):
                temp = self.count_slant_right(map, row, col)
                if temp == self.in_row_to_win or temp == -self.in_row_to_win:
                    return map[convert_coordinates_to_index(col, row, self.size)]
        return 0

    def check_slant_left_loop(self, map):
        for col in range(self.in_row_to_win - 1, self.size):
            for row in range(self.size - self.in_row_to_win + 1):
                temp = self.count_slant_left(map, row, col)
                if temp == self.in_row_to_win or temp == -self.in_row_to_win:
                    return map[convert_coordinates_to_index(col, row, self.size)]
        return 0

    def check_for_draw(self, map):
        for elem in map:
            if elem == self.default_token:
                return False
        return True

    def get_score(self, map):
        temp = [self.find_max_horizontal(map),
                self.find_max_vertical(map),
                self.find_max_slant_right(map),
                self.find_max_slant_left(map)]
        result = 0
        for elem in temp:
            result += elem
        return result

    def find_max_horizontal(self, map):
        result = 0
        for col in range(self.size - self.in_row_to_win + 1):
            for row in range(self.size):
                temp = self.count_horizontal(map, row, col)
                if temp > result:
                    result = temp
        return result

    def find_max_vertical(self, map):
        result = 0
        for col in range(self.size):
            for row in range(self.size - self.in_row_to_win + 1):
                temp = self.count_vertical(map, row, col)
                if temp > result:
                    result = temp
        return result

    def find_max_slant_right(self, map):
        result = 0
        for col in range(self.size - self.in_row_to_win + 1):
            for row in range(self.size - self.in_row_to_win + 1):
                temp = self.count_slant_right(map, row, col)
                if temp > result:
                    result = temp
        return result

    def find_max_slant_left(self, map):
        result = 0
        for col in range(self.in_row_to_win, self.size):
            for row in range(self.size - self.in_row_to_win + 1):
                temp = self.count_slant_left(map, row, col)
                if temp > result:
                    result = temp
        return result

    def count_horizontal(self, map, row, col):
        result = 0
        for i in range(self.in_row_to_win):
            result += map[convert_coordinates_to_index(col + i, row, self.size)]
        return result

    def count_vertical(self, map, row, col):
        result = 0
        for i in range(self.in_row_to_win):
            result += map[convert_coordinates_to_index(col, row + i, self.size)]
        return result

    def count_slant_right(self, map, row, col):
        result = 0
        for i in range(self.in_row_to_win):
            result += map[convert_coordinates_to_index(col + i, row + i, self.size)]
        return result

    def count_slant_left(self, map, row, col):
        result = 0
        for i in range(self.in_row_to_win):
            result += map[convert_coordinates_to_index(col - i, row + i, self.size)]
        return result
