from player import Player
import numpy as np


class Game:
    def __init__(self, size, in_row_to_win, default_sign):
        """size - size of the map,
        in_row_to_win is number of signs in row to win,
        default_sign is sign of empty field"""
        self.size = size
        self.in_row_to_win = in_row_to_win
        self.default_sign = default_sign
        self.map = [[self.default_sign for x in range(size)] for y in range(size)]

        self.player2 = None
        self.player1 = None

    def set_players(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def main_loop(self):
        while True:
            self.print_map()
            self.player1.make_move(self.map, self.default_sign)
            result = self.check_game_end()
            self.print_result(result)
            if result != self.default_sign:
                break

            # show values for player 1
            print(self.get_map_array(self.player1.get_sign()))

            self.print_map()
            self.player2.make_move(self.map, self.default_sign)
            result = self.check_game_end()
            self.print_result(result)
            if result != self.default_sign:
                break

            # show values for player 2
            print(self.get_map_array(self.player2.get_sign()))


    def print_result(self, data):
        if data == self.default_sign:
            return
        if data == "Draw":
            print("End of the game. Draw")
            return
        print("End of the game. Player " + str(data) + " won.")

    def get_map_array(self, sign):
        """returns map array row by row as a numpy.array"""
        result = []
        for index in range(self.size * self.size):
            value = self.get_value(self.map[index % self.size][index // self.size], sign)
            result.append(value)
        return np.array(result)

    def get_value(self, element, sign):
        """returns 1 if player (sign) is on field, 0 if field is empty, -1 if opponent is on field"""
        if element == sign:
            return 1
        elif element == self.default_sign:
            return 0
        else:
            return -1

    # checking game status
    def check_game_end(self):
        """ returns sign of the player who won, or returns default sign if no one won """
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
                if self.map[x][y] == self.default_sign:
                    return self.default_sign
        return "Draw"

    def check_horizontal(self, x, y):
        """returns true if for this point founded full set in horizontal"""
        temp = self.map[x][y]
        if temp == self.default_sign:
            return False
        for i in range(self.in_row_to_win):
            if temp != self.map[x + i][y]:
                return False
        return True

    def check_vertical(self, x, y):
        """returns true if for this point founded full set in vertical"""
        temp = self.map[x][y]
        if temp == self.default_sign:
            return False
        for i in range(self.in_row_to_win):
            if temp != self.map[x][y + i]:
                return False
        return True

    def check_slant(self, x, y):
        """returns true if for this point founded full set in slant"""
        temp = self.map[x][y]
        if temp == self.default_sign:
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
