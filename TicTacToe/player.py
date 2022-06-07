class Player:
    def __init__(self, sign):
        self.sign = sign

    def make_move(self, map):
        while True:
            print("Get row:")
            x = int(input())
            print("Get col:")
            y = int(input())
            if map[x][y] == '-':
                map[x][y] = self.sign
                break
            print("Field is not empty, please choose another one")
