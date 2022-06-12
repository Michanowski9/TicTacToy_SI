class Player:
    def __init__(self, token):
        self.token = token

    def make_move(self, map, default_token):
        while True:
            print("Get col:")
            x = int(input())
            print("Get row:")
            y = int(input())
            if map[x][y] == default_token:
                map[x][y] = self.token
                break
            print("Field is not empty, please choose another one")

    def get_token(self):
        return self.token
