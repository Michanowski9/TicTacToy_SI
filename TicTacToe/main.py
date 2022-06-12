from game import Game
from playerAgent import Player
from randomAgent import RandomAgent
from minmaxAgent import MinMaxAgent


if __name__ == '__main__':
    # start game
    map_size = 3
    in_row_to_win = 3

    # Prepare player 1
    # playerX = Player('X')
    playerX = MinMaxAgent('O', in_row_to_win)

    # Prepare player 2
    # playerO = Player('O')
    playerO = RandomAgent("X")

    game = Game(map_size, in_row_to_win, ' ')
    game.set_players(playerX, playerO)
    game.main_loop()


