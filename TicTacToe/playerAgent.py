import math


class Player:
    def __init__(self, my_token):
        self.my_token = my_token

    def make_decision(self, map):
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
        return self.my_token
