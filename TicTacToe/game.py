from player import Player


class Game:
    def __init__(self, size, in_row_to_win, default_sign):
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

            self.print_map()
            self.player2.make_move(self.map, self.default_sign)
            result = self.check_game_end()
            self.print_result(result)
            if result != self.default_sign:
                break

    def print_result(self, data):
        if data == self.default_sign:
            return
        if data == "Draw":
            print("End of the game. Draw")
            return
        print("End of the game. Player " + str(data) + " won.")

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
