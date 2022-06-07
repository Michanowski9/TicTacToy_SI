from player import Player


class Game:
    def __init__(self, size):
        self.size = size
        self.map = [["-" for x in range(size)] for y in range(size)]

        self.player2 = None
        self.player1 = None

    def set_players(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def main_loop(self):
        while True:
            self.print_map()
            self.player1.make_move(self.map)
            self.print_map()
            self.player2.make_move(self.map)

    def draw_horizontal_line(self):
        print("  ", end="")
        for i in range(self.size):
            print("+---", end="")
        print("+")

    # if size is greater than 10 indexes will spoil map
    def print_map(self):
        print()
        print()
        print("  ", end="")
        for i in range(self.size):
            print("  " + str(i), end=" ")
        print()
        for x in range(self.size):
            self.draw_horizontal_line()
            print(str(x) + " | ", end="")
            for y in range(self.size):
                print(self.map[x][y], end=" | ")
            print()
        self.draw_horizontal_line()
