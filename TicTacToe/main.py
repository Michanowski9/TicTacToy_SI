from game import Game
from player import Player

if __name__ == '__main__':
    game = Game(10)

    playerX = Player('X')
    playerO = Player('O')
    game.set_players(playerX, playerO)

    game.main_loop()


