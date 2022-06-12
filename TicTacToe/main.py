from game import Game
from playerAgent import Player
from randomAgent import RandomAgent
from minmaxAgent import MinMaxAgent


if __name__ == '__main__':
    map_size = 5
    in_row_to_win = 3

    game = Game(map_size, in_row_to_win, ' ')

    # playerX = Player('X')
    playerX = RandomAgent("X")


    # playerO = Player('O')
    playerO = RandomAgent("O")
    # playerO = MinMaxAgent('O', in_row_to_win)

    game.set_players(playerX, playerO)

    game.main_loop()


