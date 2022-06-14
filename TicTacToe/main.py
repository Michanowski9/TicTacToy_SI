import numpy

from game import Game

from minmaxRandomAgent import MinMaxRandomAgent
from neuronNetworkAgent import NeuronNetworkAgent
from playerAgent import Player
from randomAgent import RandomAgent
from minmaxAgent import MinMaxAgent


if __name__ == '__main__':
    # start game
    map_size = 5
    in_row_to_win = 4

    #       Prepare player 1
    # playerX = Player('X')
    # playerX = MinMaxAgent('X', in_row_to_win, 2)
    # playerX = RandomAgent("X")
    playerX = NeuronNetworkAgent("X")
    # playerX = MinMaxRandomAgent("X", in_row_to_win, 2)

    #      Prepare player 2
    # playerO = Player('O')
    # playerO = MinMaxAgent('O', in_row_to_win, 2)
    # playerO = RandomAgent("O")
    playerO = NeuronNetworkAgent("O")

    game = Game(map_size, in_row_to_win, ' ')
    game.set_players(playerX, playerO)
    game.main_loop()
