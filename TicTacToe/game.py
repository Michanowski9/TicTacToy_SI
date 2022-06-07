class Game:
    def __init__(self, size):
        self.size = size
        self.container = [["-" for x in range(size)] for y in range(size)]

    def draw_horizontal_line(self):
        for i in range(self.size):
            print("+---", end="")
        print("+")

    def print_map(self):
        for x in range(self.size):
            self.draw_horizontal_line()
            print("| ",end="")
            for y in range(self.size):
                print(self.container[x][y], end=" | ")
            print()
        self.draw_horizontal_line()
