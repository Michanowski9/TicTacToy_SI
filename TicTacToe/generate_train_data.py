import sys

from game import Game

from minmaxRandomAgent import MinMaxRandomAgent


if __name__ == '__main__':
    # save terminal output
    original_stdout = sys.stdout

    number_of_games_to_generate = 200

    with open('train_data.txt', 'w') as f:
        for i in range(number_of_games_to_generate):
            sys.stdout = original_stdout    # get terminal output
            print("game nr: " + str(i + 1))

            map_size = 5
            in_row_to_win = 4

            playerX = MinMaxRandomAgent("X", in_row_to_win, 2, 0, 0.6, False)
            playerO = MinMaxRandomAgent("O", in_row_to_win, 2, 0, 0.6, False)

            game = Game(map_size, in_row_to_win, ' ', False)

            game.set_players(playerX, playerO)
            game.main_loop()

            sys.stdout = f                  # get file output

            # printing to file
            result = 1 if (game.result == playerX.get_token()) else 0
            for map in playerX.maps:

                print(map, end="")
                print(":" + str(result))

            result = 1 if (game.result == playerO.get_token()) else 0
            for map in playerO.maps:
                print(map, end="")
                print(":" + str(result))

        sys.stdout = original_stdout        # get terminal output
