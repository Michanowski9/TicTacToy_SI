from player import Player
import numpy as np


class Game:
    def __init__(self, size, in_row_to_win, default_token):
        """size - size of the map,
        in_row_to_win is number of tokens in row to win,
        default_token is token of empty field"""
        self.size = size
        self.in_row_to_win = in_row_to_win
        self.default_token = default_token
        self.map = [[self.default_token for x in range(size)] for y in range(size)]

        self.player2 = None
        self.player1 = None

    def set_players(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def main_loop(self):
        while True:
            if self.make_round(self.player1):
                break

            if self.make_round(self.player2):
                break

    def make_round(self, player):
        self.print_map()

        col, row = player.make_move(self.get_map_array(player.get_token()))
        self.map[col][row] = player.get_token()

        result = self.check_game_end()
        self.print_result_if_end(result)
        if result != self.default_token:
            return 'END'

    def print_result_if_end(self, data):
        if data == self.default_token:
            return
        if data == "Draw":
            print("End of the game. Draw")
            return
        self.print_map()
        print("End of the game. Player " + str(data) + " won.")

    def get_map_array(self, token):
        """returns map array row by row as a numpy.array"""
        result = []
        for index in range(self.size * self.size):
            value = self.get_value(self.map[index % self.size][index // self.size], token)
            result.append(value)
        return np.array(result)

    def get_value(self, element, token):
        """returns 1 if player (token) is on field, 0 if field is empty, -1 if opponent is on field"""
        if element == token:
            return 1
        elif element == self.default_token:
            return 0
        else:
            return -1

    # checking game status
    def check_game_end(self):
        """ returns token of the player who won, or returns default token if no one won """
        for x in range(self.size - self.in_row_to_win + 1):
            for y in range(self.size):
                if self.check_horizontal(x, y):
                    return self.map[x][y]
        for x in range(self.size):
            for y in range(self.size - self.in_row_to_win + 1):
                if self.check_vertical(x, y):
                    return self.map[x][y]
        for x in range(self.size - self.in_row_to_win + 1):
            for y in range(self.size - self.in_row_to_win + 1):
                if self.check_slant(x, y):
                    return self.map[x][y]
        for x in range(self.size):
            for y in range(self.size):
                if self.map[x][y] == self.default_token:
                    return self.default_token
        return "Draw"

    def check_horizontal(self, x, y):
        """returns true if for this point founded full set in horizontal"""
        temp = self.map[x][y]
        if temp == self.default_token:
            return False
        for i in range(self.in_row_to_win):
            if temp != self.map[x + i][y]:
                return False
        return True

    def check_vertical(self, x, y):
        """returns true if for this point founded full set in vertical"""
        temp = self.map[x][y]
        if temp == self.default_token:
            return False
        for i in range(self.in_row_to_win):
            if temp != self.map[x][y + i]:
                return False
        return True

    def check_slant(self, x, y):
        """returns true if for this point founded full set in slant"""
        temp = self.map[x][y]
        if temp == self.default_token:
            return False
        for i in range(self.in_row_to_win):
            if temp != self.map[x + i][y + i]:
                return False
        return True

    # drawing map
    def print_map(self):
        """if size is greater than 10 indexes will spoil map"""
        print()
        print()
        print("  ", end="")
        for i in range(self.size):
            print("  " + str(i), end=" ")
        print()
        for y in range(self.size):
            self.draw_horizontal_line()
            print(str(y) + " | ", end="")
            for x in range(self.size):
                print(self.map[x][y], end=" | ")
            print()
        self.draw_horizontal_line()

    def draw_horizontal_line(self):
        print("  ", end="")
        for i in range(self.size):
            print("+---", end="")
        print("+")
