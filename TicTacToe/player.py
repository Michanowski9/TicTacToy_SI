class Player:
    def __init__(self, sign):
        self.sign = sign

    def make_move(self, map, default_sign):
        while True:
            print("Get col:")
            x = int(input())
            print("Get row:")
            y = int(input())
            if map[x][y] == default_sign:
                map[x][y] = self.sign
                break
            print("Field is not empty, please choose another one")

    def get_sign(self):
        return self.sign
