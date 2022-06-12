import math


class Player:
    def __init__(self, token):
        self.token = token

    def make_move(self, map):
        print("Current move: " + self.token)
        mapSize = math.sqrt(len(map))
        while True:
            print("Get col:")
            col = int(input())
            print("Get row:")
            row = int(input())

            if map[int(row * mapSize + col)] == 0:
                return col, row
            print("Field is not empty, please choose another one")

    def get_token(self):
        return self.token
